import numpy as np
import cProfile
import pstats
import io
from pstats import SortKey

pr = cProfile.Profile()
pr.enable()


def hash_func(vecs, projections):
    bools = np.dot(vecs, projections.T) > 0

    arr = []
    for bool_vec in bools:
        arr.append(np.packbits(np.flip(bool_vec))[0])

    return arr


HashList = []
for index in range(1000):
    projections1 = np.random.randn(8, 2)
    vecs = np.random.randint(0, 200, (50, 2))

    HashList.append(hash_func(vecs, projections1))
HashList = np.array(HashList)

SearchIndex = np.random.randint(0, 49)
SearchParam = HashList[0][SearchIndex:SearchIndex + 2]
NumMatches = []
MaxMatches = 30

for Hash in HashList:
    Matches = 0
    for index in range(len(Hash) - len(SearchParam)):
        if np.array_equal(Hash[index:index+len(SearchParam)], SearchParam):
            Matches += 1
        if Matches == MaxMatches:
            break
    NumMatches.append(Matches)

print(sum(NumMatches))

SearchParam = ' ' + ' '.join([str(element) for element in HashList[0][SearchIndex:SearchIndex + 2]]) + ' '
StringMatches = []

for Hash in HashList:
    Matches = 0
    HashString = ' '.join([str(element) for element in Hash])
    if SearchParam in HashString:
        Matches = min([HashString.count(SearchParam), MaxMatches])
    StringMatches.append(Matches)

print()
print(sum(StringMatches))

for index in range(len(NumMatches)):
    if NumMatches[index] != StringMatches[index]:
        print(index)
        print(NumMatches[index])
        print(StringMatches[index])
        print(SearchParam)
        print(' '.join([str(element) for element in HashList[index]]))
        input()

print(SearchParam)

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
