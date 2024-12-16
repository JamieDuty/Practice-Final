#Quiz Management System
def main():
    #main accepts the value from menu
    #it takes the choice and executes the program
    # Contact manager accepts no arguments
    # It calls contact_manager to display a menu to the user
    # and calls each function according to the user input
    
    # Prime the loop with a valid choice from contact_manager
    choice = menu()
    
    # Loop to call the desired function based on the choice
    while choice != 4:
        if choice == 1:
            take_quiz()
        elif choice == 2:
            save_results()
        elif choice == 3:
            load_results()

        # Get the next valid choice from the user
        choice = int(menu())
    
    print("Thank you for using Simple Quiz Management System. Have a great day.")
#-------------------------------------------------------------------------------------------------------------------------
def menu():
    #menu accepts no arguements
    #it displays the choices for the user
    #and it allows them to select a choice
    #which gets passed to menu
    while True:
        # Display menu
        print('\nChoose an option:')
        print('1) Take a quiz')
        print('2) Save Results')
        print('3) Load Results')
        print('4) Exit')

        # Get the user's choice
        choice = input('\nChoice: ')
        
        # Validate if the input is a number and between 1 and 4
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                return choice  # Return valid choice
            else:
                print("Invalid choice! Please choose a number between 1 and 4.")
        else:
            print("Invalid input! Please enter a valid number (not a letter or special character).")
#----------------------------------------------------------------------------------------------------------------------------
def take_quiz():
    #take quiz does a 5 question quiz with simple questions
    
    #get their name
    name = input("\nEnter your name: ")
    
    #Question 1
    print("\nWhat is the Lexus LFA most commonly known for?")
    print("A: The sound the v10 engine makes")
    print("B: The way the doors open")
    print("C: The special interior")
    q1 = input("\nYour answer: ")
    
    #Question 2
    print("\nWhat motivated Ferrucio Lamborghini to start making cars?")
    print("A: He had a dream about making cars")
    print("B: Enzo Ferrari told him to if he thought he could do better")
    print("C: He never made cars")
    q2 = input("\nYour answer: ")
    
    #Question 3
    print("\nWhat year did the events that inspired the movie Ford vs Ferrari happen in?")
    print("A: 1969")
    print("B: 1966")
    print("C: 1955")
    q3 = input("\nYour answer: ")
    
    #Question 4
    print("\nWhat car just set the fastest production car lap time around the Nurburing?")
    print("A: Mclaren W1")
    print("B: Chevrolet Corvette ZR1")
    print("C: Ford Mustang GTD")
    q4 = input("\nYour answer: ")
    
    #Question 5
    print("\nWhat car has the nickname 'The Widowmaker'?")
    print("A: Mclaren P1")
    print("B: Porsche Carrera GTS")
    print("C: Ferrari LaFerrari")
    q5 = input("\nYour answer: ")
    
    #set the total score to 5 to get it ready
    total_score = 5
    
    #add up for the questions
    if q1.upper() != "A":
        total_score += -1
    if q2.upper() != "B":
        total_score += -1
    if q3.upper() != "B":
        total_score += -1
    if q4.upper() != "C":
        total_score += -1
    if q5.upper() != "A":
        total_score += -1
    
    #display the total score
    print(f"\nYou got a {total_score}/5.")
#---------------------------------------------------------------------------------------------------------------------------
#def save_results():
    

#---------------------------------------------------------------------------------------------------------------------------
#def load_results():


#----------------------------------------------------------------------------------------------------------------------------
main()


