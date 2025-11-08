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

def get_dna_complement(dna):
    #return the reverse complement of a DNA string

    # mapping
    comp_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    complement = ""
    i = 0
    while i < len(dna):
        base = dna[i].upper()
        if base not in comp_map:
            raise ValueError(f"Invalid DNA base: {base}")
        complement += comp_map[base]
        j += 1

    return complement[::-1]