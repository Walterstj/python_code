


name = input("What is your name ? ")

next_year = 0
while next_year == 0:
    old = input("How old are you ? ")
    try:
        next_year = int(old) + 1
    except:
        print("ERRORS: You need to entry a number for old.")


print("Your name is " + name + ", your have " + str(old) + " years old.")
print("Next year you will have " + str(next_year) + " years old.")

