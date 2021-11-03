def helloworld():
    print("Hello world")

def goodbyeworld():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def goodbyeperson():
    print("Hello")
    x=input("What is your name? ")
    print("Goodbye " + x)

def goodteacher():
    x="Mr Horan"
    y=input("Teacher's name (try Mr Horan) ")
    if y==x:
        print("You are lucky, he is a great teacher.")
    else:
        print(y + " is an ok teacher")

def forloop():
    for x in range(1,500):
        print(x)

def whileloop():
    x=input("What is the name of this subject ")
    while x!="IST":
      print("Not Correct - try again")
      x=input("What is the name of this subject ")
    else:
      print("")
      print("")
      print("Congratulations!!")
      print("")
      print("")
      print("")

def start():
    print("")
    print("----Start of Output ---------------------------")
    print("")

def end():
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to Continue ")

def x():
    print("no")


while True:
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Anna                                 |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")
    print("")
    print("1. Hello World")
    print("2. Goodbye World")
    print("3. Goodbye Person")
    print("4. Good Teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. string Loop")
    print("8. convert to ascii")
    print("9. Encode to string")
    print("x. To Exit")
    p=input("Enter an option ")
    correct=["1","2","3","4","5","6","7","8","9","x"]
    start()
    
    if p in correct:
        if p=="x":
            helloworld()
            
        elif p=="2":
            goodbyeworld()

        elif p=="3":
            goodbyeperson()

        elif p=="4":
            goodteacher()

        elif p=="5":
            forloop()

        elif p=="6":
            whileloop()

        elif p=="7":
            helloworld()

        elif p=="8":
            helloworld()

        elif p=="9":
            helloworld()
        
    else:
        print("Invalid Option")

    end()