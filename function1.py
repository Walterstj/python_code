

def ask_for_name():
    answer_name = ""
    while answer_name == "":
        answer_name = input("What is your name ? ")
        # try:
        #     name = int(name_str)
        # except:
        #     print("Errors: you need entry letters for name.")
    return answer_name


def ask_for_age():
    old_int = 0
    while old_int == 0:
        old_str = input("How old are you ? ")
        try:
            old_int = int(old_str)
        except:
            print("ERRORS: You need to entry a number for old.")

    return old_int

# ask for name
name = ask_for_name ()
# name = ""
# while name == "":
#     name = input("What is your name ? ")

# ask for age
old = ask_for_age()


# show the result

print("Your name is " + str(name) + ", your have " + str(old) + " years old.")
print("Next year you will have " + str(old+1) + " years old.")

