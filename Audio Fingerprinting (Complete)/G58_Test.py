import os
import sys
import logging
import sqlite3
from datetime import datetime
import M3.G58_Table as G58_Table
import M3.G58_Database as G58_Database
import M3.G58_API as G58_API
import threading
import librosa


def main():
    logging.info("Logging - Main")
    check_same_file()

def check_same_file():
    db = G58_Database.Database()
    db.connect_to_all()

    if not db.database_initialized():
        logging.warning("Database not properly initialized.")

    filepath = "D:\\00 Documents\School\Capstone\Repo\Sound Samples\Chairs - Leather\LeatherChairStandUp_BW.26481.wav"
    existing_file_id = db.get_file_id(filepath)

    x, fs = librosa.load(filepath)
    features = G58_API.get_features(x, fs)

    file_matches = db.get_all_hash_matches(features)

    for file_id, count in file_matches.items():
        logging.info("file_id: %s, count: %s" % (file_id, count))

    print(existing_file_id)
    print(str(existing_file_id) in file_matches)



    db.disconnect_from_all()

def add_all_files_to_db():
    G58_API.initialize_db(force=False)
    G58_API.add_files_to_database("D:\\00 Documents\\School\\Capstone\\Repo\\Sound Samples\\Chairs - Leather")
    G58_API.add_files_to_database("D:\\00 Documents\\School\\Capstone\\Repo\\Sound Samples\\Guns - Machine")
    G58_API.add_files_to_database("D:\\00 Documents\\School\\Capstone\\Repo\\Sound Samples\\car_door_hard")

def search_db():
    G58_API.query_database_with_file("D:\\00 Documents\\School\\Capstone\\Repo\\Sound Samples\\Guns - Machine\\GunshotMachineGun_BW.56148.wav")

def test_table():
    table = G58_Table.Table("./DB/test_table.db", "test_table", [["new", "text"]])

    if table.exists():
        logging.info("Table already exists, not creating - checking columns")
        if not table.table_matches_file():
            logging.error("Table does NOT match what is already saved - code is outdated or something went wrong")

        next_index = table.next_id
    else:
        logging.info("Table does not exist - create the table")
        table.create_table()
        if not table.table_matches_file():
            logging.error("Table does NOT match what is already saved - code is outdated or something went wrong")

    c_names = table.column_names()
    c_all = table.columns()

    logging.info("c_names:")
    logging.info(c_names)

    logging.info("c_all:")
    logging.info(c_all)

    if "new" not in c_names:
        logging.error("Added column is not in name list")

    for column in c_all:
        c_0 = column[0]
        c_1 = column[1]

        if c_0 == "new" and c_1 != "text":
            logging.error("Added column has wrong type")

    c_map = {"new": "my value"}
    returned_id = table.add_row(c_map)
    logging.info("Returned id: " + str(returned_id))
    if returned_id != next_index:
        logging.error("Returned id is incorrect")
    if table.next_id != next_index + 1:
        logging.error("next id is incorrect")

    c_map = {"new": "my value2"}
    returned_id = table.add_row(c_map)
    logging.info("Returned id: " + str(returned_id))
    if returned_id != next_index + 1:
        logging.error("Returned id is incorrect")
    if table.next_id != next_index + 2:
        logging.error("next id is incorrect")

    # wrong column name
    c_map = {"bad test": "my value3"}
    returned_id = table.add_row(c_map)
    logging.info("Returned id: " + str(returned_id))
    if returned_id != -1:
        logging.error("Returned id is incorrect")
    if table.next_id != next_index + 2:
        logging.error("next id is incorrect")

    # bad id override
    c_map = {"new": "my value4", "id": 0}
    returned_id = table.add_row(c_map)
    logging.info("Returned id: " + str(returned_id))
    if returned_id != -1:
        logging.error("Returned id is incorrect")
    if table.next_id != next_index + 2:
        logging.error("next id is incorrect")

    # inentionally set next id to be incorrect
    table.update_next_id(1)
    c_map = {"new": "my value4"}
    returned_id = table.add_row(c_map)
    logging.info("Returned id: " + str(returned_id))
    if returned_id != -1:
        logging.error("Returned id is incorrect")
    if table.next_id < 1:
        logging.error("next id is incorrect")

    test_table_multi_thread(4)
    test_table_multi_thread(50)


def test_table_multi_thread(num_threads):
    num_iterations = 10

    table = G58_Table.Table("./DB/test_table2.db", "test_table2", [["value", "text"]])
    if table.exists():
        table.drop_table()

    table.create_table()

    threads = []
    results = []
    for i in range(0, num_threads):
        results.append([])

    def test_table_one_thread(thread_num, number_inserts):
        for count in range(0, number_inserts):
            c_map = {"value": str(thread_num) + "_" + str(count)}
            added_id = table.add_row(c_map)
            results[thread_num].append(added_id)

    for i in range(0, num_threads):
        x = threading.Thread(target=test_table_one_thread, args=(i, num_iterations))
        threads.append(x)
        x.start()

    for i in range(num_threads):
        threads[i].join()

    all_results = list()

    for one_thread_result in results:
        for returned_id in one_thread_result:
            all_results.append(returned_id)

    all_results.sort()
    if len(all_results) != num_threads * num_iterations:
        logging.error("Wrong number of results for multi-threading")
    if all_results[0] != 0 and all_results[(num_threads * num_iterations) - 1] != (num_threads * num_iterations) - 1:
        logging.error("Wrong results for multi-threading")

    logging.info("Returned IDs while multi-threading: ")
    logging.info(all_results)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout,
                        # filename='logfile.log',
                        level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s: %(message)s",
                        )
    main()
