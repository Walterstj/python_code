

name = input("What is your name ? ")

old = 0
while old == 0:
    old_str = input("How old are you ? ")
    try:
        old = int(old_str)
    except:
        print("ERRORS: You need to entry a number for old.")


print("Your name is " + name + ", your have " + str(old) + " years old.")
print("Next year you will have " + str(old+1) + " years old.")
