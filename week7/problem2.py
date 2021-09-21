import sys


def main():
    with open("input_matrices.txt", 'r') as f:
        f_read = f.readlines()
        # print(len(f_read))
        for line in f_read:
            mat_line = line.split()
            # mat_a[mat_line] = []
            # print(mat_line)

        for i in range(0, len(f_read), 3):
            mat_format = mat_line[:3]
            print(mat_format)

        # struggling in this
        # steps:
        # 1) Remove /t and separate into commas
        # 2) Make it into list
        # 3) do a for loop? make a def? which would separate it into [[a1,a2,a3],[a4,a5,a6],[a7,a8,a9]],[[b1,b2,b3],[b4,b5,b6],[b7,b8,b9]],[c1...] and so on...

        # print(i)

    return 0


if __name__ == "__main__":
    sys.exit(main())
