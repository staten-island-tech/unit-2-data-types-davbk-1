""" x = 3
y = float(3)
print(x,y)  """
""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
print(values[0])
print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

# Step 1: Prompt the user for a sentence
user_input = input("Please enter a sentence: ")

# Step 2: Define the function to count words
def count_words(sentence):
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()
    # Return the number of words
    return len(words)

# Step 3: Display the word count
word_count = count_words(user_input)
print(f"The number of words in your sentence is: {word_count}")
