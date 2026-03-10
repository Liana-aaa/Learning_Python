import csv

with open("example.csv", "r") as f:
    data = csv.DictReader(f)
    avg = 0
    count = 0
    max_grade = 0

    for line in data:
        grade = int(line["grade"])
        avg += grade
        count += 1
        if grade > max_grade:
            max_grade = grade

    avg /= count
    print(avg)
    print(max_grade)

with open("example.csv", "r") as f:
    data = csv.DictReader(f)
    for line in data:
        grade = int(line["grade"])
        if grade > avg:
            print(line["name"])