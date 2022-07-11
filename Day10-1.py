# function with output

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    # print(f_name.title())
    # print(l_name.title())
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # print(f"{formated_f_name} {formated_l_name}")
    return f"Result: {formated_f_name} {formated_l_name}"


# format_name("miTra", "MhDi")
# formated_string = format_name("miTra", "MhDi")
# print(formated_string)
print(format_name(input("What is your first name?"), input("What is your last name?")))
