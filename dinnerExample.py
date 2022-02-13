# theme for the dinner
theme = "Mexican"
print("%s Style Dinner" % (theme))

# gets # of people
people = input("How many people:")
print(people, "people are coming to dinner")

numPeople = int(people)

# if more than 10 people, we need to buy more food.
if numPeople > 10:
    print("Buy more food.")
else:
    print("We have enough food.")

# get guest names
guests = []
numPeople = int(people)
for i in range(numPeople):
    name = input("Enter the guests name:")
    guests.append(name)

print("The " + people + " guests for our " +
      theme + " Thanksgiving dinner are:")
print(guests)
