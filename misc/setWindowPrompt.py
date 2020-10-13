import os


def color(message, params):
    # params = list(params)[:2]
    params[0] += 30
    params[1] += 40
    params = map(str, params)
    csi = '\x1b['
    reset = '\x1b[0m'
    ret = ""
    ret += csi + ";".join(params) + "m"
    ret += message
    ret += reset
    return ret


def test():
    for x in range(0, 10):
        for y in range(0, 10):
            for z in range(0, 8):
                r = color("(%s, %s, %s)" % (x, y, z), [x, y, z])
                print(r, end=" ")
            print()
    return


def main():
    params = []
    style = "╭──"
    style += color("$P", [3, 9, 1])
    style += "$S$_╰─$$$S"
    # style = color("╭─$P$S$_╰─$$$S", [3, 9, 1])
    print("setx PROMPT " + style)
    # os.system("prompt "+ style)
    os.system("setx PROMPT " + style)


if __name__ == '__main__':
    # test()
    main()
