import sys

"""
Notes:
- If the file has been saved with a particular encoding, what should we do when reading it?
"""


def main():
    with open("exotic.txt", 'r') as f:
        text = f.read()
        print(f)
    with open("new_exotic.txt", 'w', encoding='utf-8') as p:
        p.write(text)
        print(p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
