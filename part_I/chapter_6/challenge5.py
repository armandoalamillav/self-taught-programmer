#Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it into a 
# grammatically correct string. There should be a space between each word, but no space 
# between the word fence and the period that follows it. (Don't forget, you learned a
#  method that turns a list of strings into a single string.)

string_list = ["The", "fox", "jumped", "over", "the", "fence", "."]

joined_strings =  " ".join(string_list)
final_string = joined_strings.replace(" .", ".")

print(final_string)