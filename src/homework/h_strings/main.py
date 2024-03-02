
#01jaimesg

def get_hamming_distance(dna1, dna2):
    distance = 0

    dna1 = "GAGCCTACTAACGGGAT"
    dna2 = "CATCGTAATGACGGCCT"
    s = len(dna1)
    for i in range(s):
         if dna1[i] != dna2[i]:
              distance += 1

    return distance

example_dist = get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
#print(example_dist)


def get_dna_complement(strand):

    complementary_strand = ""
    for symbol in strand:
        if symbol == 'A':
            complementary_strand += 'T'
            continue
        if symbol == 'T':
            complementary_strand += 'A'
            continue
        if symbol == 'C':
            complementary_strand += 'G'
            continue
        if symbol == 'G':
            complementary_strand += 'C'
            continue
    return complementary_strand


#print(get_dna_complement("AAAACCCGGT" [::-1]))


num = int(input("Enter (1) for Hamming Distance, (2) for DNA Complement, (0) to Exit:  "))

while num > 0 < 3:
    if num == 1:
        print(example_dist)     
    elif num == 2:
        print(get_dna_complement("AAAACCCGGT" [::-1]))
    else:
        print("wrong number")

    num = int(input("Enter (1) for Hamming Distance, (2) for DNA Complement, (0) to Exit:  "))
else:
    print("Thank you for using this code")



