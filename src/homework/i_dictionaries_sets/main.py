def _import_helpers():
	try:
		from src.homework.i_dictionaries_sets import add_inventory, remove_inventory_widget
		return add_inventory, remove_inventory_widget
	except Exception:
		try:
			from .dictionary import add_inventory, remove_inventory_widget
			return add_inventory, remove_inventory_widget
		except Exception:
			from dictionary import add_inventory, remove_inventory_widget
			return add_inventory, remove_inventory_widget


def _read_widget_name(prompt="Enter widget name"):
	while True:
		name = input(prompt + "\n").strip()
		if name == "":
			print("Widget name cannot be empty.")
			continue
		return name


def _read_quantity(prompt="Enter quantity (integer)"):
	while True:
		s = input(prompt + "\n").strip()
		try:
			q = int(s)
			return q
		except ValueError:
			print("Please enter a valid integer quantity.")


def main():
	add_inventory, remove_inventory_widget = _import_helpers()
	inventory = {}

	while True:
		print()
		print("Inventory Menu")
		print("1-Add or Update Item")
		print("2-Delete Item")
		print("3-Exit")
		choice = input("Enter an option: ").strip()

		if choice == "3":
			print("Exiting.")
			break

		if choice == "1":
			name = _read_widget_name()
			qty = _read_quantity()
			try:
				add_inventory(inventory, name, qty)
				print(f"{name} => {inventory.get(name, 0)}")
			except Exception as e:
				print("Error adding/updating item:", e)
			continue

		if choice == "2":
			name = _read_widget_name("Enter widget name to delete")
			try:
				removed = remove_inventory_widget(inventory, name)
				if removed:
					print(f"Removed {name} (quantity {removed}).")
				else:
					print(f"{name} not found in inventory.")
			except Exception as e:
				print("Error deleting item:", e)
			continue

		print("Invalid option, please choose 1, 2 or 3.")


if __name__ == "__main__":
	main()
