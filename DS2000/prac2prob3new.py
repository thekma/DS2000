seconds = int(input("How many seconds?"))
years = seconds // (86400*365)
leftOverSeconds = seconds%(86400*365)
days = leftOverSeconds // 86400
leftOverSeconds2 = leftOverSeconds%86400
print("There are",years," years ",days," days ",leftOverSeconds2," seconds in ",seconds,"Seconds")
