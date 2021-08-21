import sys


def main():
    with open("Ictalurus_puntatus.fasta", 'r') as f:
        fa = {}
        for line in f:
            if line[0] == '>':
                fasta_format = line[1:].rstrip()
                # print(fasta_format)
                fa[fasta_format] = []
                # print(fa)
            else:
                fa[fasta_format].append(line.rstrip())
            # print(fa)
        for name, nuc_list in fa.items():
            fa[name] = ''.join(nuc_list)
        print(fa)

        for fasta_name, seq in fa.items():
            rna = seq.replace('T', 'U')
            print("RNA Sequence = ", rna)

            translated_sequence = []
            for k in rna:
                if k == "A":
                    translated_sequence.append("U")
                elif k == "U":
                    translated_sequence.append("A")
                elif k == "C":
                    translated_sequence.append("G")
                elif k == "G":
                    translated_sequence.append("C")

            translated_joined = ''.join(translated_sequence)
            print(f"Transcribed sequence = {translated_joined}")
            genetic_code = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
                            "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
                            "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
                            "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
                            "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
                            "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                            "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                            "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                            "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
                            "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                            "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
                            "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
                            "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
                            "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                            "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
                            "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
                            }
            protein = ''
            for i in range(0, len(translated_joined) - (3 + len(translated_joined) % 3), 3):
                if genetic_code[translated_joined[i:i + 3]] == "STOP":
                    break
                protein += genetic_code[translated_joined[i:i + 3]]
            print(f"Translated Protein = {protein}")

            rna_file = open("rna_seq.fasta", "w")
            for seq_name, dna_seq in fa.items():
                rna_convert = dna_seq.replace("T", "U")
                rna_file.write(">" + seq_name + "\n" + rna_convert + "\n")
            rna_file.close()

            translated_file = open("translated_seq.fasta", "w")
            for seq_name, dna_seq in fa.items():
                rna_convert = dna_seq.replace("T", "U")
                translated_sequence = []
                # translated_sequence = rna.replace("A", "U").replace("U", "A").replace("C", "G").replace("G", "C")
                for k in rna_convert:
                    if k == "A":
                        translated_sequence.append("U")
                    elif k == "U":
                        translated_sequence.append("A")
                    elif k == "C":
                        translated_sequence.append("G")
                    elif k == "G":
                        translated_sequence.append("C")

                # print(trans_seq)
                translated_joined = ''.join(translated_sequence)
                # print(f"Transcribed sequence = {translated_joined}")
                # print(rna_seq)
                genetic_code = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
                                "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
                                "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
                                "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
                                "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
                                "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                                "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                                "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                                "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
                                "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                                "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
                                "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
                                "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
                                "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                                "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
                                "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
                                }
                protein = ''
                for i in range(0, len(translated_joined) - (3 + len(translated_joined) % 3), 3):
                    if genetic_code[translated_joined[i:i + 3]] == "STOP":
                        break
                    protein += genetic_code[translated_joined[i:i + 3]]
                # print(f"Translated Protein = {protein}")
                translated_file.write(">" + seq_name + "\n" + protein + "\n")
            translated_file.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
