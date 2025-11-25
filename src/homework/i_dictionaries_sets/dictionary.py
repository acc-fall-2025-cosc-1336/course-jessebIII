def add_inventory(inventory, widget, quantity):
	if inventory is None or not isinstance(inventory, dict):
		raise ValueError("inventory must be a dict")
	if not isinstance(widget, str) or widget == "":
		raise ValueError("widget must be a non-empty string")
	if not isinstance(quantity, int):
		raise ValueError("quantity must be an integer")

	if widget in inventory:
		inventory[widget] = inventory[widget] + quantity
	else:
		inventory[widget] = quantity


def remove_inventory_widget(inventory, widget):
	if inventory is None or not isinstance(inventory, dict):
		raise ValueError("inventory must be a dict")
	if not isinstance(widget, str) or widget == "":
		raise ValueError("widget must be a non-empty string")

	return inventory.pop(widget, 0)
