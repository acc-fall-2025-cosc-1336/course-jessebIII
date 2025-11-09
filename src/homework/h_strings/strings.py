"""String utilities for DNA homework (loops only).

Functions:
- get_hamming_distance(dna1, dna2): return integer Hamming distance for equal-length strings
- get_dna_complement(dna): return the reverse complement of the dna string (A<->T, C<->G)

Restrictions: use loops only; avoid string slicing.
"""

def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("Sequences must be of equal length.")

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
    """Return the reverse complement of a DNA string using loops only.

    Raises ValueError for invalid nucleotides. Output is uppercase.
    """
    comp_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # build complement (in forward order)
    comp = ""
    i = 0
    while i < len(dna):
        base = dna[i].upper()
        if base not in comp_map:
            raise ValueError(f"Invalid nucleotide: {dna[i]}")
        comp += comp_map[base]
        i += 1

    # build reverse of comp without using slicing
    rev_comp = ""
    k = len(comp) - 1
    while k >= 0:
        rev_comp += comp[k]
        k -= 1

    return rev_comp

