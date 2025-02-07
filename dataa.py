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

""" verb1 = input("verb1 = ")
verb2 = input("verb2 = ")
number1 = input("number1 = ")
noun1 = input("noun1 = ")
celebrity1 = input("celebrity1 = ")
print(f"{celebrity1} was walking to the park, after he arrived, he {verb1} and decided to leave, he went and met up with {noun1} in order to go to SAT prep to {verb2} for {number1} hours.") """

""" x = "test"
print(f"hello {x}") """
""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

user_input = input("Please enter a sentence: ")
def count_words(sentence):
    words = sentence.split()
    word_count = len(words)
    return world_count
word_count = count_words(user_input)
print(f"The number of words in your sentence is: {word_count}")