def is_subpart(substring_var, string_var):
    substring = substring_var.get()
    substring=substring.lower()
    string_var = string_var.lower()
    substring=set(substring)
    string_var=set(string_var)
    # string = string_var.get()

    # Check if substring is a subpart of string
    if substring.intersection(string_var)==substring:
        print("You guessed all the letters")
        return True
    elif substring.issubset(string_var):
        print("Yes it is a subpart")
        return True
        
    else:
        print("No")
        return False
