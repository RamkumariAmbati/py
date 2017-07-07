# Print CRUD Operations in python.
import csv
FileName = "More.dat"
def print_menu():
	print(5 * "-", "Menu", 5 * "-")
	print("1. CreateItem")
	print("2. Display Items List")
	print("3. Update Item")
	print("4. Delete Item")
	print("5. Exit")
	print(10 * "-")
def CreateItem():
	ItemDetails = []
	with open(FileName, "a") as FileObject:
		ItemDetails.append(input("Enter Item Id: "))
		ItemDetails.append(input("Enter Item Name: "))
		ItemDetails.append(input("Enter Item Price: "))
		ItemDetails.append("1")
		writer = csv.writer(FileObject)
		writer.writerow(ItemDetails)
	FileObject.close()
def DisplayItemsList():
	FileObject = open(FileName, "r")
	ItemDetails = FileObject.readlines()
	for values in ItemDetails:
		print(ItemDetails)
		print(values.split(",")[3])
	ArrayItemDetails = ItemDetails
	for Counter, values in enumerate(ArrayItemDetails):
		Array = values.split(",")
		for Field in Array:
			print(Field)
		if Field[3] == "1":
			print(Field)
	FileObject.close()
def UpdateItem():
	TempId = input("Enter the Item Identication Number: ")
	div = ','
	with open(FileName, "r") as FileObject:
		ArrayItemDetails = FileObject.readlines()
		Counter = 0
		for Counter, Item in enumerate(ArrayItemDetails):
			FieldArray = Item.split(div)
			if FieldArray[0] == TempId:
					print("1. Update Name \n2. Update Price \n3. Update Status \n4. Exit")
					choice = int(input("Enter your choice(1-4): "))
					if choice == 1:
						FieldArray[1] = input('Enter New Item name: ')
					if choice == 2:
						FieldArray[2] = input('Enter New Item Price: ')
					if choice == 3:
						FieldArray[3] = input('Enter New Status: ')
					if choice == 4:
						exit
			TempItem = div.join(FieldArray)
			ArrayItemDetails[Counter] = TempItem
			with open(FileName, "w") as FileObject:
				FileObject.writelines(ArrayItemDetails)
	FileObject.close()
def DeleteItem():
	print("Item Deleted.")
variable = True
while variable:
	print_menu()
	choice = int(input("Enter the choice: "))
	if choice == 1:     
		CreateItem()
	elif choice == 2:
		DisplayItemsList()
	elif choice == 3:
		UpdateItem()
	elif choice == 4:
		DeleteItem()
	elif choice == 5:
		break
	else:
		print("You have entered a wrong choice.")

