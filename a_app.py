# ---- Session on Clean Coding, Data types, Functions, TDD ----
HORIZONTAL_RULE = "-" * 40    # by pressing F2, you can rename a variable and all its instances; making the varibale all uppercase shows that it is a constant variable

# Refactor the following

# Assigning Lists
list_sample = [1, 2, 3, "Four", 5, 6]

# Access Lists
print("     Item 1:", list_sample[0])
print("     Item 4:", list_sample[3])
print("  Item Last:", list_sample[-1])
print("Slice items:", list_sample[2:len(list_sample)])   #  slicing --> [start_index:end_index]
# Loop through Lists
print(" ---- Listing Items in List ----")
for item in list_sample:
  print(item)
print(" ---- Listing Items using range() ----")
# for using range(start,stop,step) / range(stop)
for ctr in range(len(list_sample)):     #   ctr means counter
  print(ctr, ":", list_sample[ctr])
print(HORIZONTAL_RULE)

email = "j@em2.com"

# Dictionary : { key_1: value_1, key_2: value_2, ..... key_n: value_n }
dictionary_sample = {
  "id" : 123,
  "name": "John",
  "email" : [
      "j@em.com",
      email
  ]
}

# Access dictionaries individually
print("   ---- Access Dictionaries ----")
print("     Id:", dictionary_sample["id"])
print("   Name:", dictionary_sample["name"])
print(" Emails:", dictionary_sample["email"])
print("Email 1:", dictionary_sample["email"][0])
print("Email 2:", dictionary_sample["email"][1])
print(HORIZONTAL_RULE)
# Loop through dictionaries print key : value - element type
for key in dictionary_sample:
  print(key, ":", dictionary_sample[key])
print("-"*20)

