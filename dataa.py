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

""" user_input = input("enter a sentence: ")
def count_words(sentence):
    words = sentence.split()
    word_count = len(words)
    return word_count
word_count = count_words(user_input)
print(f"number of words: {word_count}") """

#odd or even
""" def odd_or_even():
    num = int(input("Enter a number: "))  
    if num % 2 == 0:
        print("even")
    else:
        print("odd") """
#tip calculator
""" bill = input("Enter the bill amount: ")  
tip = input("Enter the tip percentage: ")  
bill = float(bill)  
tip = int(tip)  
tip_amount = (tip / 100) * bill  
total = bill + tip_amount 

print(f"The total amount to be paid is {total}.") """

#tip calculate
""" def tip_calculator():
    bill = float(input("Enter bill amount: "))  
    service = input("How was the service? (bad, okay, good, great): ")  
    if service == "bad":
        tip_percent = 0
    elif service == "okay":
        tip_percent = 15
    elif service == "good":
        tip_percent = 20
    elif service == "great":
        tip_percent = 25
    else:
        print("Invalid input")
        return
    tip_amount = (tip_percent / 100) * bill  
    total = bill + tip_amount 
    print(f"Total amount to be paid: {total}") 
tip_calculator()
 """
#factor thing
""" def find_factors():
    num = int(input("Enter a number: ")) 
    for i in range(1, num + 1):  
        if num % i == 0:
            print(i) 
find_factors() """
#gcf 
""" def greatest_common_factor():
    num1 = int(input("Enter first number: "))  
    num2 = int(input("Enter second number: "))  
    gcf = 1  
    for i in range(1, min(num1, num2) + 1):  
        if num1 % i == 0 and num2 % i == 0:
            gcf = i  
    print(f"The greatest common factor is {gcf}")  
greatest_common_factor() """
