""" def login(password):
    #if statement evaluates to true we go to the next ine
    if password == "secret":
        print("logged in")
    else:
        print("incorrect")
x = input("What is the password: ")
login(x) """

""" def grade(score):
    if score>=92:
        print("A")
    elif score>= 82:
        print("B")
    elif score >= 72:
        print("C")
    else: 
        print("F")
x = int(input("what is the score: "))
grade(x) """

""" def gamble(age, id):
    if age >= 21:
        if id:
            print("You may come in the Casino")
        else:
            print("You need Id verification")
    else:
        print("You're too young")
         """

""" def gamble(age, id):
    if age >= 21 and id == True:
            print("You may come in the Casino")
    elif age >= 21 and id == False:
          print("You need Id verification")
    else:
          print("you're too young") """
""" if not raining == true:
    print("go take a walk")
if raining == false:
      print("go for walk") """