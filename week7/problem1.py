import sys


def main():
    with open("war_and_peace.txt", "r", encoding="utf-8") as f:
        text_readiness = f.readlines()
        print(text_readiness)
        text_tell = f.tell()
        print(text_tell)
        text_seek = f.seek(10)
        print(text_seek)
        print(f.tell())
        print(len(text_readiness))
        print(len(f.read()))

    return 0


if __name__ == "__main__":
    sys.exit(main())
