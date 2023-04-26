

# show_personal_information
def show_personal_information(name, old):
    print("Your name is " + str(name) + ", you have " + str(old) + " years old.")
    print("Next year you will have " + str(old + 1) + " years old.")

    # condition = old >= 18
    # print(condition)
# elif = else and if
#     if old == 0:
#         print("")
    # elif old == 1 or == 3
    if old == 17:
        print("You are almost of legal age")
    # age >= 12 and age < 18:
    elif 12 <= old < 18:
        print("you are a teanager")
    elif old == 1 or old == 2:
        print("You are a baby")
    elif old == 18:
        print("You are just of a legal age, Congratulations")
    elif old > 60:
        print("You are a senior")
    elif old < 10:
        print("You are infant")
    elif old >= 18:
        print("You are legal age")
    else:
        print("You are underage")

def ask_for_name():
    answer_name = ""
    while answer_name == "":
        answer_name = input("What is your name ? ")
        # try:
        #     name = int(name_str)
        # except:
        #     print("Errors: you need entry letters for name.")
    return answer_name


def ask_for_age(name_of_people):
    old_int = 0
    while old_int == 0:
        old_str = input(name_of_people + " how old are you ? ")
        try:
            old_int = int(old_str)
        except:
            print("ERRORS: You need to entry a number for old.")

    return old_int

# ask for name
name1 = ask_for_name ()
name2 = ask_for_name ()
# name = ""
# while name == "":
#     name = input("What is your name ? ")

# ask for age
old1 = ask_for_age(name1)
old2 = ask_for_age(name2)


# # show the result
show_personal_information(name1, old1)
show_personal_information(name2, old2)



