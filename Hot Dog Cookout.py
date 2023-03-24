#!/usr/bin/env python3
import math
franks = 10
hotdogBuns = 8
people = int(input("How many people are attending the cookout? :"))
dogsperPerson = int(input("\nHow many hot dogs will each person eat? :"))


franks_required = (people * dogsperPerson)/franks
franks_needed = math.ceil(franks_required)

buns_required =(people * dogsperPerson)/hotdogBuns
buns_needed = math.ceil(buns_required)

leftover_buns = (buns_needed * hotdogBuns) - (people * dogsperPerson)

leftover_franks = (franks_needed * franks) - (people * dogsperPerson)

print("\nThe minimum number of packages of hot dogs required: ",franks_needed)


print()
print("The minimum number of packages of hot dog buns required:", buns_needed)


print()
print("The number of hot dogs that will be left over: ", leftover_franks)


print()
print("The number of hot dogs buns that will be left over: ",leftover_buns)