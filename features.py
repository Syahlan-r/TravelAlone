# FEATURES
from services import itinerary, tour_guide, visa_handler
from tabulate import tabulate

cart = []

def show_itineraries():
    headers = ["No.", "Type", "Destination", "Detail", "Fee"]        
    formatted_data = []
    for num, item in enumerate(itinerary):
        for idx, detail in enumerate(item["details"]):
            if idx == 0:
                formatted_data.append(
                    [ num + 1, item["type"], item["destination"], detail, item["fee"]]
                )
            else:
                formatted_data.append(
                    [ None, None, None, detail, None ]
                )
        formatted_data.append([])

    print(tabulate(formatted_data, headers=headers, tablefmt="fancy_outline"))

def show_tour_guide():
    headers = ["No.", "Number of People", "Price per hour"]
    formatted_data = []
    for num, item in enumerate(tour_guide) :
        formatted_data.append(
                [ num + 1, item["people"], item["price_per_hour"]]
        )
    
    print(tabulate(formatted_data, headers=headers, tablefmt="fancy_outline"))

def show_visa_handler():
    headers = ["No.", "Service", "Price per person"]
    formatted_data = []
    for num, item in enumerate(visa_handler) :
        formatted_data.append(
                [ num + 1, item["type"], item["price_per_person"]]
        )
    print(tabulate(formatted_data, headers=headers, tablefmt="fancy_outline"))  

def module_itinerary() :
    offer = {}

    show_itineraries()
    while True:
        try:
            choice = input_number("Enter the itinerary you like : ")
        except ValueError:
            print("You should input the number :")
            continue

        if choice <= len(itinerary):
            idx = choice - 1
            offer = itinerary[idx]

            add_to_cart(offer, "itinerary")

            print("Your cart: ")
            display_cart()
            add_more = get_yes_no_input("Add another itineraries? (Y/N) ")
            if add_more.upper() == "N":
                break
        else:
            print("Input the correct number :")

def module_tour_guide():
    while True:
        hours, num_people = None, None
        offer = {}

        show_tour_guide()

        while True:
            num_people = input_number("How many people are you : ")
            if num_people <= 30 :
                break    
            print("if more than 30 person, Please contact us")        
        if num_people > 0  and num_people <= 5:
            offer = tour_guide[0]                
        elif num_people > 5  and num_people <= 10:
            offer = tour_guide[1]
        elif num_people > 10  and num_people <= 20:
            offer = tour_guide[2]
        elif num_people > 20  and num_people <= 30:
            offer = tour_guide[3]
        
        hours = input_number("How many hours you want : ")


        add_to_cart(offer, "tour_guide", num_people, hours)

        print("Your cart: ")
        display_cart()
        add_more = get_yes_no_input("Add another tour guide ? (Y/N) ")
        if add_more.upper() == "N":
            break

def module_visa_handler():
    while True:
        num_people = None
        offer = {}

        show_visa_handler()
        choice = input_number("what service do you need ? : ")
        idx = choice - 1
        offer = visa_handler[idx]

        num_people = int(input("How many people are you : "))

        add_to_cart(offer, "visa_handler", num_people)

        print("Your cart: ", end="")
        display_cart()
        add_more = get_yes_no_input("Add another visa handler ? (Y/N) ")
        if add_more.upper() == "N":
            break

def module_contact_us():
    print("""
        IF You Want to Know More or Want to Make Amazing Private Tour
        You can Contact us On : 0815 1100 1436
        Thank You
    """)

    option = get_yes_no_input("Do you want to back to homepage ? : (Y/N)") 
    if option.upper() == "Y" :
        return
    
# cart
def display_cart() :
    headers = ["No.", "Service Type", "Description", "Qty.", "Unit", "Price", "Subtotal"]

    formatted_data = []
    for idx, item in enumerate(cart, start=1):
        formatted_data.append(
            [
                idx,
                item["service_type"], 
                item["desc"], 
                item["qty"], 
                item["unit"], 
                item["unit_price"], 
                item["subtotal"]
            ]
        )
    print()
    print(tabulate(formatted_data, headers=headers, tablefmt="fancy_outline"))

def add_to_cart(offer, service_type, num_people=None, hours=None):
    exist = False
    if service_type == "itinerary":
        # Check if already exist
        for service in cart:
            if f"Type: {offer['type']}, Destination: {offer['destination']}" == service["desc"]:
                exist = True
                service["qty"] += 1
                service["subtotal"] += service["unit_price"]
                break
        if exist == False:
            offer_mapping = {
                "service_type": "itinerary",
                "desc": f"Type: {offer['type']}, Destination: {offer['destination']}",
                "qty": 1,
                "unit": "package",
                "unit_price": offer["fee"],
                "subtotal": offer["fee"]
            }
    if service_type == "tour_guide":
        offer_mapping = {
            "service_type": "tour_guide",
            "desc": f"Number of people: {num_people}",
            "qty": hours,
            "unit": "hours",
            "unit_price": offer["price_per_hour"],
            "subtotal": hours * offer["price_per_hour"]
        }
    if service_type == "visa_handler":
        for service in cart:
            if f"Type: {offer['type']}" ==  service["desc"]:
                exist = True
                service["qty"] += num_people 
                service["subtotal"] += service["unit_price"] * num_people
                break
        if exist == False :
            offer_mapping = {
                "service_type": "visa_handler",
                "desc": f"Type: {offer["type"]}",
                "qty": num_people,
                "unit": "pax",
                "unit_price": offer["price_per_person"],
                "subtotal": num_people * offer["price_per_person"]
            }
    if exist == False:
        cart.append(offer_mapping)

def get_total_price():
    total_price = 0
    for item in cart:
        total_price += item["subtotal"] 
    return total_price

def payment():
    total_price = get_total_price()
    print(f"Total price = {total_price}")

    while True:
        cash = int(input("Enter the amount of cash : "))
        if cash >= total_price:
            break    
        print(f"The cash wasn't enough. You need to add {total_price - cash} more")

    print("Thank You!!!\n")
    if cash > total_price:
        print(f"Here is your change : {cash - total_price}")

    
def delete_from_cart():
    num = int(input("Which service you want to delete ? "))
    idx = num - 1
    del cart[idx]

def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).upper()
        if user_input in ["Y", "N"]:
            return user_input
        else :
            print("Invalid choice! Please enter Y/N :")

def input_number(text):
    while True:
        user_input = input(text)
        if user_input.isdigit():
            if int(user_input) == 0:
                print("Number can't be 0!")
            else:
                break
        print("Please insert a number!")
    return int(user_input)

def edit_from_cart():
    index = input_max_number(len(cart), "Which service you want to edit ? ")
    service_type = cart [index]["service_type"]
    if service_type == "tour_guide":
        num_people = input_max_number(30, "Change number of people : ")
        num_people += 1
        qty = input_number("Change the quantity : ")
        cart[index]["desc"] = f"Number of people: {num_people}"
        cart[index]["qty"] = qty
        if num_people > 0  and num_people <= 5:
            price = tour_guide[0]["price_per_hour"]           
        elif num_people > 5  and num_people <= 10:
            price = tour_guide[1]["price_per_hour"]
        elif num_people > 10  and num_people <= 20:
            price = tour_guide[2]["price_per_hour"]
        elif num_people > 20  and num_people <= 30:
            price = tour_guide[3]["price_per_hour"]
        cart[index]["unit_price"] = price
        cart[index]["subtotal"] = qty * price
    else:
        while True:
            qty = input_number("Change the quantity : ")
            # if qty != 0:
            #     break
            # print("Number can't be 0!")
        cart[index]["qty"] = qty
        cart[index]["subtotal"] = cart[index]["unit_price"] * qty
   

def input_max_number(max_number, text) :
    while True:
        # edit_idx = input_number("Which service you want to edit ? ")
        edit_idx = input_number(text)
        if edit_idx == 0:
            print("Index can't be 0!")
        elif edit_idx > max_number:
            print("Number exceed the existing value!")
        else:
            break  
    return edit_idx - 1