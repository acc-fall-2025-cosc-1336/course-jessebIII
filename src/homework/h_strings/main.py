1from strings import get_hamming_distance, get_dna_complement


def main():
	while True:
		print("\n1-Hamming Distance")
		print("2-Dna Complement")
		print("3-Exit")
		choice = input("Enter your choice (1-3): ").strip()

		if choice == '1':
			seq1 = input("Enter first DNA string: ").strip()
			seq2 = input("Enter second DNA string: ").strip()
			try:
				dist = get_hamming_distance(seq1, seq2)
				print(f"Hamming distance: {dist}")
			except ValueError as e:
				print(f"Error: {e}")

		elif choice == '2':
			seq = input("Enter DNA string: ").strip()
			try:
				comp = get_dna_complement(seq)
				print(f"DNA complement: {comp}")
			except ValueError as e:
				print(f"Error: {e}")

		elif choice == '3':
			print("Exiting.")
			break

		else:
			print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
	main()