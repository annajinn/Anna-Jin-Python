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

while p != "x":
    start()
    print("Invalid Option")
    end()

    if p=="1":
        start()
        helloworld()
        end()
        
    if p=="2":
        start()
        goodbyeworld()
        end()

    if p=="3":
        start()
        goodbyeperson()
        end()

    if p=="4":
        start()
        goodteacher()
        end()

    if p=="5":
        start()
        forloop()
        end()

    if p=="6":
        start()
        whileloop()
        end()

    if p=="7":
        start()
        helloworld()
        end()

    if p=="8":
        start()
        helloworld()
        end()

    if p=="9":
        start()
        helloworld()
        end()

    if p=="x":
        start()
        end()