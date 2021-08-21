import random
import sys


def main():
    bases = ['A', 'T', 'G', 'C']
    seq = "".join(random.choices(bases, k=100))  # Good!
    print("Given sequence =", seq)
    print("Length of sequence =", len(seq))

    kmer1_file = open("kmer1.txt", "w")
    for k in range(3, 4):
        kmer1_file.write("k =" + str(k) + "\n" + "%s %17s" % (f'{k}-mer', 'count') + "\n" + '-' * 25 + "\n")

        for value in range(len(seq) - k + 1):
            val_k = seq[value: value + k]
            kmer_count = seq.count(val_k)
            kmer1_file.write("%s %16s" % (val_k, kmer_count) + "\n")
        kmer1_file.write("=" * 25)
        kmer1_file.close()

    kmer2_file = open("kmer2.txt", "w")
    for k in range(4, 5):
        kmer2_file.write("k =" + str(k) + "\n" + "%s %17s" % (f'{k}-mer', 'count') + "\n" + '-' * 25 + "\n")

        for value in range(len(seq) - k + 1):
            val_k = seq[value: value + k]
            kmer_count = seq.count(val_k)
            kmer2_file.write("%s %16s" % (val_k, kmer_count) + "\n")
        kmer2_file.write("=" * 25)
        kmer2_file.close()

    kmer3_file = open("kmer3.txt", "w")
    for k in range(5, 6):
        kmer3_file.write("k =" + str(k) + "\n" + "%s %17s" % (f'{k}-mer', 'count') + "\n" + '-' * 25 + "\n")
        for value in range(len(seq) - k + 1):
            val_k = seq[value: value + k]
            kmer_count = seq.count(val_k)
            kmer3_file.write("%s %16s" % (val_k, kmer_count) + "\n")
        kmer3_file.write("=" * 25)
        kmer3_file.close()

    kmer4_file = open("kmer4.txt", "w")
    for k in range(6, 7):
        kmer4_file.write("k =" + str(k) + "\n" + "%s %17s" % (f'{k}-mer', 'count') + "\n" + '-' * 25 + "\n")
        for value in range(len(seq) - k + 1):
            val_k = seq[value: value + k]
            kmer_count = seq.count(val_k)
            kmer4_file.write("%s %16s" % (val_k, kmer_count) + "\n")
        kmer4_file.write("=" * 25)
        kmer4_file.close()

    kmer5_file = open("kmer5.txt", "w")
    for k in range(7, 8):
        kmer5_file.write("k =" + str(k) + "\n" + "%s %17s" % (f'{k}-mer', 'count') + "\n" + '-' * 25 + "\n")
        for value in range(len(seq) - k + 1):
            val_k = seq[value: value + k]
            kmer_count = seq.count(val_k)
            kmer5_file.write("%s %16s" % (val_k, kmer_count) + "\n")
        kmer5_file.write("=" * 25)
        kmer5_file.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
