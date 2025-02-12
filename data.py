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
#mad project
""" verb1 = input("verb1 = ")
verb2 = input("verb2 = ")
number1 = input("number1 = ")
noun1 = input("noun1 = ")
celebrity1 = input("celebrity1 = ")
print(f"{celebrity1} was walking to the park, after he arrived, he {verb1} and decided to leave, he went and met up with {noun1} in order to go to SAT prep to {verb2} for {number1} hours.") """
#boolean
""" x = "test"
print(f"hello {x}") """
""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """
#word count
""" user_input = input("enter a sentence: ")
def count_words(sentence):
    words = sentence.split()
    word_count = len(words)
    return word_count
word_count = count_words(user_input)
print(f"number of words: {word_count}") """

#odd or even
""" def check_even_odd(number):
    if number % 2 == 0: 
        return "even"
    else:
        return "odd"
number = int(input("Enter a number: ")) 
result = check_even_odd(number)  
print(f"The number {number} is {result}.")   """

#tip calc
""" bill = input("Enter the bill amount: ") 
tip = input("Enter the tip percentage: ")  
bill = float(bill) 
tip = int(tip)  
total = bill + tip
print(f"The total amount to be paid is ${total:.2f}.") """

#service calc
""" def tip_calculate(bill, service):
    if service == "bad":
        tip = 0
    elif service == "ok":
        tip = 0.15 * bill
    elif service == "good":
        tip = 0.20 * bill
    elif service == "great":
        tip = 0.25 * bill
    else:
        print("unknown rating")
        return None, None 
    return tip, bill + tip  
bill_amount = float(input("Enter bill: "))
rating = input("service owo (only accepts bad, ok, good, great): ")
tip, total = tip_calculate(bill_amount, rating)
print(f"tip: ${tip:.2f}, bill: ${total:.2f}") """

#factor thing
""" def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0: 
            factors.append(i)  
    return factors
num = int(input("Enter a number: "))
print("Factors:", find_factors(num)) """
#gcf 
""" def find_gcf(a, b):
    smaller = min(a, b)
    gcf = 1  
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0: 
            gcf = i 
    return gcf
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The GCF of {num1} and {num2} is: {find_gcf(num1, num2)}") """


