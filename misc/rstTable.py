import sys


def main():
    tabLen = 4
    with open(sys.argv[1], "r", encoding="utf-8") as fh:
        content = fh.read()
    results = []
    for line in content.split("\n"):
        tmp = line.split(" ", tabLen-1)
        if len(tmp) == 1:
            continue
        if len(tmp) < tabLen:
            print(tmp)
            # sys.exit()
        results.append(tmp)
    # tabLen = len(results[0])
    maxLen = []
    for idx in range(tabLen):
        maxLen.append(max(map(lambda line: len(line[idx]), results)))
    for line in results:
        print("| ", end="")
        for idx in range(tabLen):
            print(" " + line[idx].ljust(maxLen[idx], " "), end="")
            print(" |", end="")
        print()


if __name__ == '__main__':
    main()
