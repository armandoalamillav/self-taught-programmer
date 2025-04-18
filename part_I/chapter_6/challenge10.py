# Slice the string "It was a bright cold day in April, and the clocks were striking thirteen." to 
# only include the characters before the comma.

sentence = "It was a bright cold day in April, and the clocks were striking thirteen."

comma_index = sentence.index(',')

slice_sentence = sentence[0:comma_index]

print(slice_sentence)