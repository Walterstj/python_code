

# name = input("What is your name ? ")
name = ""
while name == "":
    name = input("What is your name ? ")
    # try:
    #     name = str(name_int)
    # except:
    #     print("ERRORS: You need to entry letters for old.")

old = 0
while old == 0:
    old_str = input("How old are you ? ")
    try:
        old = int(old_str)
    except:
        print("ERRORS: You need to entry a number for old.")


print("Your name is " + str(name) + ", your have " + str(old) + " years old.")
print("Next year you will have " + str(old+1) + " years old.")

