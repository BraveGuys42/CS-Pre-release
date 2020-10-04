Category = ["Case", "Case", "RAM", "RAM", "RAM", "Main Hard Disk Drive", "Main Hard Disk Drive", "Main Hard Disk Drive", "Solid State Drive", "Solid State Drive", "Second Hard Disk Drive", "Second Hard Disk Drive", "Second Hard Disk Drive", "Optical Drive", "Optical Drive", "Operating System", "Operating System"]
ItemCode = ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "E1", "E2", "E3", "F1", "F2", "G1", "G2"]
Description = ["Compact", "Tower", "8 GB", "16 GB", "32GB", "1 TB HDD", "2 TB HDD", "4 TB HDD", "240 GB SSD", "480 GB SSD", "1 TB HDD", "2 TB HDD", "4 TB HDD", "DVD/Blu-Ray Player", "DVD/Blu-Ray Re-writer", "Standard Version", "Professional Version"]
Price = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99,89.99,129.99,59.99,119.99,49.99,89.99,129.99,50.00,100.00,100.00,175.00]


Cart = ""
Total_Price = 0

Items = ["Case","RAM","HDD"]

Letter = ["A", "B", "C"]

for i in range(3):
	while True:
		order = input(f"Enter item code for {Items[i]}: ")
		if Letter[i] in order and order in ItemCode:
			Code = ItemCode.index(order)
			Cart += Description[Code] + " " + Category[Code] + ", "
			Total_Price += Price[Code]
			break
		else:
			print("Wrong item code")
Total_Price = round(Total_Price,2)
print("You have ordered a " + Cart + "and at a total price of $" + str(Total_Price))

Counter = 0
AddCart = ""
Items = ["Solid State Drive","Second Hard Disk Drive","Optical Drive", "Operating System"]
Letter = ["D", "E", "F", "G"]
while True:
	More = input("Would you like more items? (Y/N): ")
	if More == "Y":
		Counter += 1
		while True:
			select = input("What item would you like? " + str(Items) + "\n: ")
			if select in Items:
				i = Items.index(select)
				break
			else:
				print("Please enter item from list")
		while True:
			order = input(f"Enter item code for {select}: ")
			if Letter[i] in order and order in ItemCode:
				Code = ItemCode.index(order)
				AddCart += Description[Code] + " " + Category[Code] + ", "
				Total_Price += Price[Code]
				break
	elif More == "N":
		break

	else:
		print("Please enter either Y or N")
if Counter > 0:
	if Counter == 1:
		Total_Price *= 0.95
	elif Counter > 1:
		Total_Price *= 0.90
	Total_Price = round(Total_Price,2)
	print("You have ordered a " + AddCart + "and discounted total price of $" + str(Total_Price))
print("Have a good day")