import sys
# import os
import re
matrix = []


def init():
    # path = ""
    try:
        # try:
        #     if os.path.isfile(sys.argv[1]):
        #         path = os.path.split(sys.argv[1])[1]
        # except Exception as e:
        #     print(str(e))
        result = re.split(r"/", sys.argv[1])
        path = result[-1]
        f = open(path)
        for line in f:
            wordsList = line.split()
            for w in wordsList:
                v = w.split(',')
                lineList = [str(v[0]), str(v[1]), str(v[2])]
                matrix.append(lineList)
        f.close()
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    column_name = sys.argv[2]
    init()
    find_column = False
    duplicate = True
    for i in range(0, len(matrix[0])):
        index = matrix[0][i]
        for j in range(i + 1, len(matrix[0])):
            if index == matrix[0][j]:
                duplicate = False
    if not duplicate:
        exit("Are duplicates in column")
    for i in range(0, len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            exit("Line %d is longer then first line" % i)
    for i in range(0, len(matrix[0])):
        if column_name.lower() == matrix[0][i].lower():
            find_column = True
    if not find_column:
        exit("Column not found")
    list_cuv = []
    for i in range(0, len(matrix[0])):
        if column_name.lower() == matrix[0][i].lower():
            for j in range(1, len(matrix)):
                list_cuv.append(matrix[j][i].lower())
    print("[OK]")
    counts = dict()
    for word in list_cuv:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    # print(counts)
    sorted_counts = sorted(counts.items(), key=lambda cuv: cuv[1], reverse=True)
    for i in range(0, len(sorted_counts)):
        print(sorted_counts[i][0])
