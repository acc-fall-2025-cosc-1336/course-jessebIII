#!/usr/bin/env python3
"""Compute the p-distance matrix for DNA strings in FASTA format.

Usage:
  python src/rosalind_pdistance.py input.fasta

If no filename is provided the script reads FASTA from standard input.

Outputs a matrix where entry i,j is the proportion of differing
symbols between string i and string j (formatted to 3 decimal places).
"""
import sys
from typing import Dict, List, Tuple


def parse_fasta(lines: List[str]) -> List[Tuple[str, str]]:
    """Parse FASTA lines into a list of (id, sequence) tuples.
    Keeps the original order.
    """
    records: List[Tuple[str, str]] = []
    current_id = None
    current_seq_parts: List[str] = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if current_id is not None:
                records.append((current_id, "".join(current_seq_parts)))
            current_id = line[1:].strip()
            current_seq_parts = []
        else:
            current_seq_parts.append(line)

    if current_id is not None:
        records.append((current_id, "".join(current_seq_parts)))

    return records


def p_distance(s1: str, s2: str) -> float:
    """Return p-distance between equal-length strings s1 and s2."""
    if len(s1) != len(s2):
        raise ValueError("Sequences must have equal length")
    if len(s1) == 0:
        return 0.0
    diffs = 0
    for a, b in zip(s1, s2):
        if a != b:
            diffs += 1
    return diffs / len(s1)


def distance_matrix(seqs: List[str]) -> List[List[float]]:
    n = len(seqs)
    mat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                mat[i][j] = 0.0
            else:
                mat[i][j] = p_distance(seqs[i], seqs[j])
    return mat


def main(argv: List[str]):
    if len(argv) >= 2:
        path = argv[1]
        with open(path, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
    else:
        lines = sys.stdin.read().splitlines()

    records = parse_fasta(lines)
    if not records:
        print("No FASTA records found", file=sys.stderr)
        return 1

    ids = [rid for (rid, seq) in records]
    seqs = [seq for (rid, seq) in records]

    # validate equal lengths
    L = len(seqs[0])
    for s in seqs:
        if len(s) != L:
            print("Error: sequences are not all the same length", file=sys.stderr)
            return 1

    mat = distance_matrix(seqs)

    # print matrix rows with 3 decimal places
    for row in mat:
        print(" ".join(f"{x:.3f}" for x in row))

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
