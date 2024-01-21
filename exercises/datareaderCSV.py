import csv


f = "C:\\Users\\Vflor\Downloads\\sample CSV\\Product_v5.csv"

with open(f , newline='' , encoding="utf8") as csvfile:
    csvReader = csv.DictReader(csvfile )
    prices = []
    for column in csvReader:
        prices.append(column["value"])
    pr = list(map(float , prices))
    print(sum(pr))

#convert a list with strings to float
#floatPrices = [float(p) for p in prices] #varianta 1
#floatPrices = list(map(float , prices))  # varianta 2