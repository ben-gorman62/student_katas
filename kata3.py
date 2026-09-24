

# A3: In this DNA sequence, which is the letter that first occurs 4 times in a
# row?
# 
# AAACTTTGGGCCAACCGGGAGGGTTTGCATTTAAATTTGGACCGCCAAACCTGGAAAGGGCCGATTTGGCCCTTAGGTAAATTGCCGGTTTCCCTCCTTTAATTCCGGTGGCCTTGGGGATTCAACCCAAGGACCCAAGGGATTTGCCAATTTCCAGGAAACCCAAACCCAAAGGAAATTTAAATTTCATTTCCCTTTAAACTTAAAATTGTAA

dna = "AAACTTTGGGCCAACCGGGAGGGTTTGCATTTAAATTTGGACCGCCAAACCTGGAAAGGGCCGATTTGGCCCTTAGGTAAATTGCCGGTTTCCCTCCTTTAATTCCGGTGGCCTTGGGGATTCAACCCAAGGACCCAAGGGATTTGCCAATTTCCAGGAAACCCAAACCCAAAGGAAATTTAAATTTCATTTCCCTTTAAACTTAAAATTGTAA"

#create counter that tracks number of appearances
# A appears first - count 1
# A appears second - count 2
# A appears third - count 3
# C appears fourth - count 1
# etc.
# print letter that triggers count 4

def repeating_letter(string):
    count = 1
    for pos in range(1, len(string)):
        if string[pos] == string[pos - 1]:
            count += 1
            if count == 4:
                return print(string[pos])
        else:
            count = 1
#        print(string[pos])
#        print(count)

repeating_letter(dna)

# sort()
# return 
