country= input("where is your country: ")
age = input("how old r you: ")
age = int(age)
if country == "Taiwan":
	if age >= 18 :
		print("You can apply for a driver license")
	else :
		print("You still can not get a driver license ")
elif country == "America":
	if age >= 16 :
		print("You can apply for a driver license")
	else :
		print("You still can not get a driver license ")
else :
	print("you could only enter Taiwan/America")