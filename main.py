#main_menu 
import features


def main_program() :
    while True:
        print("""
        Welcome to European travalone
            
        What service do you need ?  
        1. Itinerary
        2. Travel Guide      
        3. Visa Handler
        4. Edit item from cart
        5. Delete item from cart
        6. Contact Us for private holliday
        7. Show your cart 
        8. Payment
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
            features.payment()
            break
        else :
            print("Input the correct number ! ") 

if __name__ == "__main__":
    main_program()