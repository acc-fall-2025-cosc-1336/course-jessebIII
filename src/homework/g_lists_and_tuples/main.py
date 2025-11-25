"""Menu to compute p-distance matrix for sequences.

Menu:
1-Get p distance matrix
2-Exit
"""

def _import_pdistance():
	"""Import get_p_distance_matrix from the lists helper with a few fallbacks."""
	try:
		from src.homework.g_lists_and_tuples.lists import get_p_distance_matrix

		return get_p_distance_matrix
	except Exception:
		try:
			from lists import get_p_distance_matrix

			return get_p_distance_matrix
		except Exception:
			from .lists import get_p_distance_matrix

			return get_p_distance_matrix


def _read_sequence(prompt="Enter a sequence"):
	"""Read a non-empty sequence from input and return it as a list of characters."""
	while True:
		s = input(prompt + "\n").strip()
		if s == "":
			print("Empty sequence not allowed, please try again.")
			continue
		# return as list of characters (works for DNA strings)
		return list(s)


def main():
	while True:
		print()
		print("1-Get p distance matrix")
		print("2-Exit")
		choice = input("Enter an option: ").strip()

		if choice == "2":
			print("Exiting.")
			break

		if choice != "1":
			print("Invalid option, please choose 1 or 2.")
			continue

		# collect sequences
		seqs = []
		while True:
			seq = _read_sequence("Enter a sequence")
			seqs.append(seq)

			# after at least 2 sequences allow stopping
			if len(seqs) >= 2:
				ans = input("Do you want to enter another sequence? ").strip().lower()
				if ans in ("n", "no"):
					break

		try:
			get_matrix = _import_pdistance()
			mat = get_matrix(seqs)
			# print matrix with 3 decimal places
			for row in mat:
				print(" ".join(f"{x:.3f}" for x in row))
		except Exception as e:
			print("Error computing p-distance matrix:", e)


if __name__ == "__main__":
	main()