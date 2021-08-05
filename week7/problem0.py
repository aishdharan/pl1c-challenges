import sys


def main():
    with open("exotic.txt", 'r') as f:
        text = f.read()
        print(f)
    with open("new_exotic.txt", 'w', encoding='utf-8') as p:
        p.write(text)
        print(p)
    f.close()
    p.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
