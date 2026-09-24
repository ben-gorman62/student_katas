# A1: Given the input string
# 
# "Here is a string Paul wrote. It has CAPITAL letters in it... Wow."
# 
# print out all the capital letters from that string.

# decompose time
# make an empty string
# make a loop through each index in sentence
# check if character in index is uppercase
# add uppercase index to empty string


# use string.findall("([A_Z])")



our_string = "Here is a string Paul wrote. It has CAPITAL letters in it... Wow."
def find_caps(string):
    caps_string = ""
    for char in string:
        if char.isupper():
            caps_string += char
            
    return caps_string

print(find_caps(our_string))
