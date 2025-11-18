"""Menu-driven program to collect numbers and show lowest/highest values.

Menu:
1-Show the list low /high values
2-Exit

def _import_list_funcs():
	"""Import helper that tries a few import styles so this file can be
	executed both as a script and as a package module during tests.
	"""
	try:
		from src.homework.g_lists_and_tuples.lists import (
			get_lowest_list_value,
			get_highest_list_value,
		)
		return get_lowest_list_value, get_highest_list_value
	except Exception:
		try:
			# When running this file directly from its directory
			from lists import get_lowest_list_value, get_highest_list_value

			return get_lowest_list_value, get_highest_list_value
		except Exception:
			# When imported as a package
			from .lists import get_lowest_list_value, get_highest_list_value

			return get_lowest_list_value, get_highest_list_value


def _read_number(prompt="Enter a list value"): 
	"""Read a number from input, return int or float. Repeat until valid."""
	while True:
		s = input(prompt + "\n").strip()
		try:
			if "." in s:
				return float(s)
			return int(s)
		except ValueError:
			print("Invalid number, please try again.")


def main():
	while True:
		print()
		print("1-Show the list low /high values")
		print("2-Exit")
		choice = input("Enter an option: ").strip()

		if choice == "2":
			print("Exiting.")
			break

		if choice != "1":
			print("Invalid option, please choose 1 or 2.")
			continue

		# Option 1: collect list values
		values = []
		while True:
			n = _read_number("Enter a list value")
			values.append(n)

			# Only after at least 3 values do we display the continue prompt
			if len(values) >= 3:
				ans = input("Do you want to enter another value? ").strip().lower()
				if ans in ("n", "no"):
					break
				# any other answer continues the loop

		# compute and display low/high using helpers
		try:
			low_fn, high_fn = _import_list_funcs()
			low = low_fn(values)
			high = high_fn(values)
			print(f"Lowest value: {low}")
			print(f"Highest value: {high}")
		except Exception as e:
			print("Error computing low/high:", e)


if __name__ == "__main__":
	main()