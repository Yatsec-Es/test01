import csv

# Create an empty set
testSet = set()
# This will be an array of tests that will be later
# saved as CSV
testArr = []


with open('249.csv', newline='') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i != 0:
            # Add the test ID to the set
            testSet.add(row[3])
            # Add a new element to the list of tests
            testArr.append([row[3], row[1], row[5], row[6]]) # test ID, EVVNC, coverage, status
            print(i, row[3])
            print(testArr[i-1])
        i += 1
print(sorted(testSet))





outCsv = list()

i = 0
for test in sorted(testSet):
    outCsv.append(list())
    outCsv[i].append(test)
    i += 1

# Corrupt the data in the input CSV so we could see missing entries
testArr[10][0] = 'hhhhhhh'
testArr[100][0] = 'hhhhhhh'


emptyRow = ['', '', '', '']

i = 0
for test in outCsv:
    print(test[0])
    testFound = False
    for row in testArr:
        if row[0] == test[0]:
            # Found matching test ID
            for item in row[1:]: outCsv[i].append(item)
            testFound = True
            break

    if testFound == False:
        for item in emptyRow[1:]: outCsv[i].append(item)
    print(i, ' ', outCsv[i])
    i += 1



# Pretend there is another input file and append more info to every row of the output CSV
testArr[180][0] = 'hhhhhhh'
testArr[181][0] = 'hhhhhhh'
i = 0
for test in outCsv:
    print(test[0])
    testFound = False
    for row in testArr:
        if row[0] == test[0]:
            # Found matching test ID
            for item in row[1:]: outCsv[i].append(item)
            testFound = True
            break

    if testFound == False:
        for item in emptyRow[1:]: outCsv[i].append(item)
    print(i, ' ', outCsv[i])
    i += 1



# OUTPUT
with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(outCsv)
