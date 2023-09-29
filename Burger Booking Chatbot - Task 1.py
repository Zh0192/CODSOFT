#Burger Ordering Bot 

def get_user_input(prompt):
    return input(prompt)
def order_burger():
    print("Chicken - S.patti\nEgg\nVegetarian - S.patti\nChicken - D.patti\nVegetarian - D.patti\n")
    burger_type = get_user_input("What kind of burger would you like from above?\n\n\n\n")
    print("Bacon\nChilies\nAvocado\nLettuce\nChili\nTomatoes\nMushrooms\n")
    burger_top = get_user_input("What toppings would you like from the above?")
    delivery_address = get_user_input("Where would you like your burger delivered?")
    phone_number = get_user_input("What is your phone number?")
    
    if validate_order(burger_type, burger_top, delivery_address, phone_number):
        print("Thank you for your order. Your burger will be delivered soon.")
    else:
        print("Invalid input. Please try again.")
def validate_order(burger_type, burger_top, delivery_address, phone_number):
    # Add your validation logic here
    if burger_type in ["Chicken - S.patti", "Egg", "Vegetarian - S.patti","Chicken - D.patti","Vegetarian - D.patti"]:
        if burger_top in ["Bacon","Chilies","Avocado","Lettuce","Chili","Tomatoes","Mushrooms."]:
            if delivery_address:
                phone_number = phone_number.replace('-', '')
                if len(phone_number) == 10 and phone_number.isdigit():
                    return True
    return False

def chatbot():
    print("Hi, I am a chatbot. I can order a Yummy Burgiiirrrr for you !! . /n Do you want one !?")
    user_input = get_user_input("Please enter your request: ")  # Provide a prompt message
    
    if user_input == "Yes" or user_input == "s" or user_input =="S" or user_input =="definitely":
        order_burger()
    else:
        print("I'm sorry, I can't help you with that. Please try again.")

chatbot()