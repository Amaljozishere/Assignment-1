def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count =upper_count+1
        elif char.islower():
            lower_count =lower_count+1
    return upper_count, lower_count

string = "This is an introduction to Python"

upper_count, lower_count = count_upper_lower(string)
print("Number of uppercase Characters:", upper_count)
print("Number of lowercase Characters:", lower_count)
