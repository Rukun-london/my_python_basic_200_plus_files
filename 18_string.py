dictionary= {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [22, 23, 21, 24],
    "city": ["Physics", "Math", "CS", "Biology"],
    "country": ["uk", "usa","bolivia","hongkong"]
}
#header
print("{:^10}|{:^10}|{:^10}|{:^10}".format("name", "age","city","country"))
print('---' *25)
#body
#for name, age,city, country in dictionary:     #(there is a mistake in next two lines)
 #   print(f"{:^10}|{:^10}|{:^10}|{:^10}".format(dictionary["name"],dictionary[ "age"],dictionary["city"],dictionary["country"]))
        #or next two line
#for name, age, city, country in zip(dictionary["name"], dictionary["age"], dictionary["city"], dictionary["country"]):
 #   print("{:^10}|{:^10}|{:^10}|{:^10}".format(name, age, city, country))


for i in range(len(dictionary["name"])):
    print("{:^10}|{:^10}|{:^10}|{:^10}".format(
  dictionary["name"][i],
        dictionary["age"][i],
        dictionary["city"][i],
        dictionary["country"][i]
    ))

                 #   or which i havent learnt yet
# determine column widths
#columns = list(dictionary.keys())
#widths = {col: max(len(col), max(len(str(x)) for x in dictionary[col])) + 2 for col in columns}

# header
#print(" | ".join(f"{col:^{widths[col]}}" for col in columns))
#print("-" * (sum(widths.values()) + 3 * (len(columns) - 1)))

# body
#for row in zip(*dictionary.values()):
 #   print(" | ".join(f"{str(val):^{widths[col]}}" for val, col in zip(row, columns)))

