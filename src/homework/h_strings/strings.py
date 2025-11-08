# use loops only; avoid string slicing
def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("Sequences must be of equal length")

    distance = 0
    i = 0
    while i < len(dna1):
        a = dna1[i].upper()
        b = dna2[i].upper()
        if a != b:
            distance += 1
        i += 1
    return distance