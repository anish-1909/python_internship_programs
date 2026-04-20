def new_string(input_string):
    first_string=input_string[0]
    middle_num=round(len(input_string)/2)
    middle_string=input_string[middle_num]
    last_string=input_string[-1]
    final_string=first_string+middle_string+last_string
    return final_string
input_string=input("Enter a word to get first,middle and last character:")
output_string = new_string(input_string)
print(f"Input string:{input_string}")
print(f"Output string:{output_string}")
