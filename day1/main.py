def part_one(file):
    f = open(file, "r").read()

    list1, list2 = map(sorted, map(list, zip(*(map(int, line.split()) for line in f.strip().split("\n")))))

    result = 0

    for a, b in zip(list1, list2):
        result += abs(a - b)

    print(result)


def part_two(file):
    f = open(file, "r").read()

    list1, list2 = map(sorted, map(list, zip(*(map(int, line.split()) for line in f.strip().split("\n")))))

    result = 0

    for a in list1:
        result += a * list2.count(a)

    print(result)


part_one("data/data.txt")
part_two("data/data.txt")
