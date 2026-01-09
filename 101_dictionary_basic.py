# print the keys and value separately and together as data for a person
person = {
    "name: ": "Rukun",
    "job: ": "Train operator",
    "country: ": "UK"
}
marks = {
    "math": 85,
    "english": 78,
    "physics": 90
}
# print(marks["math"])     # 85
# #print(marks["biology"]) #program crashes because of no biology subject in the marks sets
# print(marks.get("biology","not found"))
# print(person["name"])
# print(person["job"])
# marks["history"] = 89   #add a new key
# marks["math"] = 99      #update an existing key
# print(marks["math"])
# print(marks["history"])
for subject in marks:
    print(subject)
for key in person:
    print(key, person[key])
for subject, value in marks.items():
    print(subject, value)