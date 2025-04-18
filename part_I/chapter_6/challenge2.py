# Write a program that collects two strings from a user and insterts them into the 
# string "Yesterday I wrote a [response_one]. I sent it to [response_two]!"

response_one = input("Give me a type of text (email, essay, etc.): ")
response_two = input("Give me a person to send it to: ")

sample_string = "Yesterday I wrote a {}. I sent it to {}!".format(response_one, response_two)

print(sample_string)