#main_menu 
from module import backpacker, travel_agent, contact_us


def main_program() :
    while True:
        print("""
        Welcome to European travelone
            
        What your travel style ?  
        1. Backpacker
        2. With Travel Agent
        3. Visa Handler      
        4. Delete the package
        5. Contact Us for private holliday 
        6. Exit
            """)

        menu = int(input("Enter the corresponding number : "))

        if menu == 1:
            backpacker.module()
        elif menu == 2 :
            travel_agent.module()
        elif menu == 3 :
            backpacker.show_visa_handler()
            
        elif menu == 5 :
            contact_us.module()
        else :
            break 

if __name__ == "__main__":
    main_program()