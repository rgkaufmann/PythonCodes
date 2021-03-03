import librosa
import librosa.display
import logging
from numpy import matlib
import FileIO
import SQL
import sys
import numpy
import matplotlib.pyplot as plt
import config
import GUI

setup = False


class LSH:
    def __init__(self, dim):
        self.num_tables = 2
        self.hash_size = 8

        if setup:
            for i in range(self.num_tables):
                projections = matlib.randn(self.hash_size, dim)
                SQL.insert_table_data(db_conn, i, projections.tostring(), self.hash_size)

    def add(self, vecs, label):
        for table_id in range(self.num_tables):
            projection_string, hash_size = SQL.get_table_data(db_conn, table_id)
            projections = numpy.frombuffer(projection_string).reshape((int(hash_size), int(config.FV_SIZE)))
            hashes = hash_func(vecs, projections)
            hashes_no_dups = list(dict.fromkeys(hashes))

            for h in hashes_no_dups:
                count = hashes.count(h)
                SQL.insert_file_hash(db_conn, label, h, count, table_id)

    def query(self, vecs):
        all_hashes = list()
        for table_id in range(self.num_tables):
            table_hashes = list()

            projection_string, hash_size = SQL.get_table_data(db_conn, table_id)
            projections = numpy.frombuffer(projection_string).reshape((int(hash_size), int(config.FV_SIZE)))

            hashes = hash_func(vecs, projections)
            hashes_no_dups = list(dict.fromkeys(hashes))

            for h in hashes_no_dups:
                db_matches = SQL.get_file_hash(db_conn, h, table_id)
                for db_match in db_matches:
                    file_path, count = db_match[0], db_match[1]
                    table_hashes.extend([file_path]*(int(count)*hashes.count(h)))

            all_hashes.extend(table_hashes)

        return all_hashes


def main():
    FileIO.iterate_over_files("./Sound Samples/", fingerprint_file)
    results = query("./Sound Samples/Explosions/EXPL Source Forest Medium WhiteLight 2x MKH8040ST.wav")
    for r in sorted(results, key=results.get, reverse=True):
        print(r, results[r])

    results = query("./Sound Samples/00 Hmitch Test/High Voltage Lab - Jacob Ladder - 0.2 Meters. Electricity,Arc,50Hz,"
                    "Large,Aggressive,Overdrive,Spark_03.wav")
    for r in sorted(results, key=results.get, reverse=True):
        print(r, results[r])

    SQL.disconnect_from_db(db_conn)
    return 0


def init():
    SQL.initialize_db(config.DB_FILEPATH).close()


def query1(filepath):
    x, fs = librosa.load(filepath)
    features = librosa.feature.melspectrogram(y=x, sr=fs, n_mels=128, fmax=8000)
    features_dB = librosa.power_to_db(features, ref=numpy.max)
    librosa.display.specshow(features_dB, x_axis='time', y_axis='mel', sr=fs, fmax=8000)

    plt.figure(figsize=(10, 4))
    #plt.colorbar(format='%+2.0f dB')
    plt.show()


def query(filepath):
    x, fs = librosa.load(filepath)
    features = get_features(x, fs)
    results = lsh.query(features)

    print('num results', len(results))
    print('num features', len(features))

    counts = dict()
    for similar_file in results:
        similar_filepath = similar_file

        if similar_filepath in counts:
            counts[similar_filepath] += 1
        else:
            counts[similar_filepath] = 1

    for similar_filepath in counts:
        num_features = SQL.get_file_features(db_conn, similar_filepath)
        counts[similar_filepath] = float(counts[similar_filepath]) / num_features

    return counts


def fingerprint_file(filepath):
    GUI.create_fig(filepath)

    if SQL.get_file_features(db_conn, filepath):
        logging.warning("File already fingerprinted: %s", filepath)
        return

    x, fs = librosa.load(filepath)
    features = get_features(x, fs)
    lsh.add(features, filepath)

    if not SQL.insert_file_features(db_conn, filepath, len(features)):
        num_features = SQL.get_file_features(db_conn, filepath)
        SQL.update_file_features(db_conn, filepath, num_features + len(features))

def new_fingerprint_file(database, filepath):
    GUI.create_fig(filepath)

    # ToDo: Check if file already fingerprinted (get id)


    x, fs = librosa.load(filepath)
    features = get_features(x, fs)
    lsh.add(features, filepath)

    # ToDo: Add file features to table if not already present
    if not SQL.insert_file_features(db_conn, filepath, len(features)):
        num_features = SQL.get_file_features(db_conn, filepath)
        SQL.update_file_features(db_conn, filepath, num_features + len(features))


def hash_func(vecs, projections):
    bools = numpy.dot(vecs, projections.T) > 0

    arr = []
    for bool_vec in bools:
        arr.append(bool2int(bool_vec))

    return arr


def bool2int(x):
    y = 0
    for i, j in numpy.ndenumerate(x):
        if j:
            y += 1 << i[0]
    return y


def get_features(x, fs):
    return librosa.feature.melspectrogram(y=x, sr=fs, n_mels=128, fmax=8000).T


if setup:
    init()

db_conn = SQL.connect_to_db(config.DB_FILEPATH)
lsh = LSH(config.FV_SIZE)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout,
                        # filename='logfile.log',
                        level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s: %(message)s",
                        )
    main()
