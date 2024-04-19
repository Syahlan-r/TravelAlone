#main_menu 
from module import features


def main_program() :
    while True:
        print("""
        Welcome to European travelone
            
        What your travel style ?  
        1. Itinerary
        2. Travel Guide
        3. Visa Handler      
        4. Payment
        5. Delete item from cart
        6. Contact Us for private holliday 
        7. Exit
            """)

        menu = int(input("Enter the corresponding number : "))

        if menu == 1:
            features.module_itinerary()
        elif menu == 2:
            features.module_tour_guide()
        elif menu == 3 :
            features.module_visa_handler()
        elif menu == 4 :
            features.payment()
        elif menu == 5 :
            pass
        elif menu == 6 :
            features.module_contact_us()
        else :
            break 

if __name__ == "__main__":
    main_program()