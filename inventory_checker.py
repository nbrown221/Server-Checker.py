import csv

inv_file = open("inventory.csv", "r")
reader = csv.reader(inv_file)

request = input("What would you like to see: ")
cleaned_request = request.lower()
for item in reader:
    if cleaned_request in item[0].lower():
        print(item)
    elif cleaned_request in item[1].lower():
        print(item)
    elif cleaned_request in item[2].lower():
        print(item)

