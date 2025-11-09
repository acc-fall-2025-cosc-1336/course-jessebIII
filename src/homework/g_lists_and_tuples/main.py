"""Small program to collect numbers into a list (step 1 of 3).

Step 1: read a series of numbers from the user, store them in a list and
print the list. Subsequent steps will compute the minimum and maximum.
"""

def main():
	nums = []
	print("Enter numbers one at a time. Press Enter on a blank line to finish.")
	while True:
		s = input("Number (blank to finish): ").strip()
		if s == "":
			break
		try:
			# allow integers or floats
			if '.' in s:
				n = float(s)
			else:
				n = int(s)
		except ValueError:
			print("Invalid number, please try again.")
			continue
		nums.append(n)

	print(f"Numbers entered: {nums}")

	# Step 2: compute and display the lowest number
	if len(nums) == 0:
		print("No numbers were entered.")
		return

	# find minimum using a loop
	minimum = nums[0]
	i = 1
	while i < len(nums):
		if nums[i] < minimum:
			minimum = nums[i]
		i += 1

	print(f"Lowest number: {minimum}")

	# Step 3: compute and display the highest number
	maximum = nums[0]
	j = 1
	while j < len(nums):
		if nums[j] > maximum:
			maximum = nums[j]
		j += 1

	print(f"Highest number: {maximum}")


if __name__ == "__main__":
	main()
