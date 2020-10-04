listOfItems= 		["Case", "RAM", "Main HDD", "SSD", "Second HDD", "Optical Drive", "Operating System"]

cases_ItemCode= 	["A1", "A2"]
cases_Desc= 		["Compact", "Tower"]
cases_Price= 		[75.0, 150.0]

RAM_ItemCode= 		["B1", "B2", "B3"]
RAM_Desc= 			["8 GB", "16 GB", "32 GB"]
RAM_Price= 			[79.99, 149.99, 299.99]

mainhdd_ItemCode= 	["C1", "C2", "C3"]
mainhdd_Desc= 		["1TB HDD", "2TB HDD", "4TB HDD"]
mainhdd_Price= 		[49.99, 89.99, 129.99]

ssd_ItemCode= 		["D1", "D2"]
ssd_Desc= 			["240GB SSD", "480GB SSD"]
ssd_Price= 			[59.99, 119.99]

sechdd_ItemCode= 	["E1", "E2", "E3"]
sechdd_Desc= 		["1TB HDD", "2TB HDD", "4TB HDD"]
sechdd_Price= 		[49.99, 89.99, 129.99]

optdrive_ItemCode= 	["F1", "F2"]
optdrive_Desc= 		["DVD Player", "DVD Re-Writer"]
optdrive_Price= 	[50.0, 100.0]

opersys_ItemCode= 	["G1", "G2"]
opersys_Desc= 		["Standard", "Professional"]
opersys_Price= 		[100.0, 175.0]

###############################################################
Cart = ""
Total_Price = 0
while True:
	print("Case Codes: ", cases_ItemCode)
	print("Case Description: ", cases_Desc)
	print("Case Prices", cases_Price)
	order = input("Please enter item code for desired case: ")
	if order in cases_ItemCode:
		index = cases_ItemCode.index(order)
		Cart += cases_Desc[index] + " Case, "
		Total_Price += cases_Price[index]
		break
	else:
		print("*Please enter correct code*")
while True:
	print("RAM codes: ", RAM_ItemCode)
	print("RAM Description: ", RAM_Desc)
	print("RAM Prices: ", RAM_Price)
	order = input("Please enter item code for desired RAM size: ")
	if order in RAM_ItemCode:
		index = RAM_ItemCode.index(order)
		Cart += RAM_Desc[index] + " RAM, "
		Total_Price += RAM_Price[index]
		break
	else:
		print("*Please enter correct code*")

while True:
	print("Main HDD codes: ", mainhdd_ItemCode)
	print("Main HDD Description: ", mainhdd_Desc)
	print("Main HDD Prices: ", mainhdd_Price)
	order = input("Please enter item code for desired Main HDD size: ")
	if order in mainhdd_ItemCode:
		index = mainhdd_ItemCode.index(order)
		Cart += mainhdd_Desc[index] + " Main HDD, "
		Total_Price += mainhdd_Price[index]
		break
	else:
		print("*Please enter correct code*")
Total_Price = round(Total_Price,2)
print("You have ordered " + Cart + "at a price of $" + str(Total_Price))
########################################################################
Add = ""
Count = 0
while True:
	More = input("Would you like additional items? (Y/N): ")
	if More == "Y":
		Count +=1
		print("What item would you like? " + str(listOfItems[3:]))
		order = input(": ")
		if order == "SSD":		
			while True:
				print("SSD codes: ", ssd_ItemCode)
				print("SSD Description: ", ssd_Desc)
				print("SSD Prices: ", ssd_Price)
				order = input("Please enter item code for desired SSD size: ")
				if order in ssd_ItemCode:
					index = ssd_ItemCode.index(order)
					Add += ssd_Desc[index] + ", "
					Total_Price += ssd_Price[index]
					break
				else:
					print("*Please enter correct code*")

		elif order == "Second HDD":		
			while True:
				print("Secondary HDD codes: ",sechdd_ItemCode)
				print("Secondary HDD Description: ", sechdd_Desc)
				print("Secondary HDD Prices: ", sechdd_Price)
				order = input("Please enter item code for desired Secondary HDD size: ")
				if order in sechdd_ItemCode:
					index = sechdd_ItemCode.index(order)
					Add += sechdd_Desc[index] + " Secondary HDD, "
					Total_Price += sechdd_Price[index]
					break
				else:
					print("*Please enter correct code*")

		elif order == "Optical Drive":		
			while True:
				print("Optical Drive codes: ", optdrive_ItemCode)
				print("Optical Drive Description: ", optdrive_Desc)
				print("Optical Drive Prices: ", optdrive_Price)
				order = input("Please enter item code for desired Optical Drive size: ")
				if order in optdrive_ItemCode:
					index = optdrive_ItemCode.index(order)
					Add += optdrive_Desc[index] + " Optical Drive, "
					Total_Price += optdrive_Price[index]
					break
				else:
					print("*Please enter correct code*")

		elif order == "Operating System":		
			while True:
				print("Operating System codes: ", opersys_ItemCode)
				print("Operating System Description: ", opersys_Desc)
				print("Operating System Prices: ", opersys_Price)
				order = input("Please enter item code for desired Operating System size: ")
				if order in opersys_ItemCode:
					index = opersys_ItemCode.index(order)
					Add += opersys_Desc[index] + " Operating System, "
					Total_Price += ssd_Price[index]
					break
				else:
					print("*Please enter correct code*")
	elif More == "N":
		break

	else:
		print("Please enter either Y or N")

if Count > 0:
	if Count == 1:
		Total_Price *= 0.95
		Total_Price = round(Total_Price,2)
	elif Count > 1:
		Total_Price *= 0.90
		Total_Price = round(Total_Price,2)
	print("You have ordered addtion items " + Add + "at a discounted price of $" + str(Total_Price))
print("Have a nice")
