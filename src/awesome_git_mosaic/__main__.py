import sys

from . import write


def main():
    if len(sys.argv) > 1:
        write(sys.argv[1], 45, 1, True, True)
    else:
        print("You need to give something to write")


if __name__ == "__main__":
    main()
