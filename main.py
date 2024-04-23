#main_menu 
import features


def main_program() :
    name = input("\n What your name : ")
    while True:
        phone = features.input_number(" What your number : ")
        if len(str(phone)) in [10, 11, 12]:
            break
        print("Invalid phone number, please insert min.10 max.12 digit!")

    while True:

        print(f"""
        Hello, {name}
        Welcome to Travel Alone
            
        What service do you need ?  
        1. Itinerary
        2. Tour Guide      
        3. Visa Handler
        4. Edit item from cart
        5. Delete item from cart
        6. Contact Us for private holliday/ support
        7. Show the cart 
        8. Payment
        9. exit
            """)

        menu = features.input_number("Enter the corresponding number : ")
        if menu == 1:
            features.module_itinerary()
        elif menu == 2 :
            features.module_tour_guide()
        elif menu == 3 :
            features.module_visa_handler()
        elif menu == 4 :
            features.display_cart()
            features.edit_from_cart()
        elif menu == 5 :
            features.display_cart()
            features.delete_from_cart()
        elif menu == 6 :
            features.module_contact_us()
        elif menu == 7:
            features.display_cart()
        elif menu == 8 : 
            features.display_cart()
            features.payment(name, phone)
        elif menu == 9 :
            break
        else :
            print("Input the correct number ! ") 

if __name__ == "__main__":
    main_program()