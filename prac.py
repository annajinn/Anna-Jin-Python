import sys

def print_menu():
    print("""
 ------------------------------------------------
|                                                |
|    07Menu                                      |
|    Name : Annmarie Thomas                      |
|    Version : 01                                |
|                                                |
 ------------------------------------------------
1. Hello World
2. Goodbye World
3. Goodbye Person
4. Good Teacher
5. forLoop
6. whileLoop
7. string Loop
8. Convert to ascii
9. Encode a string
x. To Exit
    """)

def option1():
   print("Hello World")  

def option2():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def option3():
    print("Hello World")
    name = input("What is your name ? ")
    print("Goodbye " + name)  
 
def option4():
    name = input("Teacher's name (try Mr Horan) ")
    if name == "Mr Horan":
     print ("You are lucky, he is a great teacher")
    else: 
     print(name + " is an ok teacher")

def option5():
    print("Hello World") 
    for i in range(500):
        print(i)

def option6():
    print("Hello World") 
    subject = "IST"
    my_input = ""
    while my_input != subject:
        my_input = input("What is the name of this subject ")
        if my_input == subject:
            print("\nCongratulations!!")
        else:
            print("Not Correct - try again")

def option7():
    answer = input("What is your string? ")
    for i in answer:
        print(i)

def option8():
    answer = input("What is your string? ")
    for i in answer:
        print(i + '=' + str(ord(i)))

def option9():
     answer = input("What is your string? ")
     encoded_str = ""
     for i in answer:
        encoded_char = chr(ord(i)+1)
        print(i + '=' + encoded_char)
        encoded_str += encoded_char
        #encoded_str = encoded_str + encoded_char
        print(encoded_str)

while True:
    print_menu()
    menu_option = input("Enter an option ")
    valid_options = ['1','2','3','4','5','6','7','8','9','x']
    
    print("----Start of Output ---------------------------\n")

    if menu_option in valid_options:
        if menu_option.lower() == 'x': 
            sys.exit()
        elif menu_option == '1':
            option1()
        elif menu_option == '2':
            option2()
        elif menu_option == '3':
            option3()
        elif menu_option == '4':
           option4()
        elif menu_option == '5':
            option5()
        elif menu_option == '6':
            option6()
        elif menu_option == '7':
            option7()
        elif menu_option == '8':
            option8()
        elif menu_option == '9':
            option9()
    else:
        print("invalid option")

    print("\n----End of Output -----------------------------\n\n")

    input("Press Enter to continue ")