# BACKPACKER
from services import backpacker
from tabulate import tabulate

cart = []

def show_itineraries():
    headers = ["No.", "Type", "Destination", "Detail", "Fee"]        
    formatted_data = []
    for num, item in enumerate(backpacker["itinerary"]):
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
    for num, item in enumerate(backpacker["tour_guide"]) :
        formatted_data.append(
                [ num + 1, item["people"], item["price_per_hour"]]
        )
    
    print(tabulate(formatted_data, headers=headers, tablefmt="fancy_outline"))

def show_visa_handler():
    headers = ["No.", "Service", "Price per person"]
    formatted_data = []
    for num, item in enumerate(backpacker["visa_handler"]) :
        formatted_data.append(
                [ num + 1, item["type"], item["price_per_person"]]
        )
    print(tabulate(formatted_data, headers=headers, tablefmt="fancy_outline"))  

def module() :
    while True:
        hours, num_people = None, None
        offer = {}

        # choose Itinerary, Mandatory
        show_itineraries()
        itinerary_choice = int(input("Enter the itinerary you like : "))
        itinerary_idx = itinerary_choice - 1

        offer["itinerary"] = backpacker["itinerary"][itinerary_idx]

        # Choose Tour Guide, Optional
        while True :
            add_tour_guide = input("Do you need a tour guide ? : (Y/N) ")
            if add_tour_guide.upper() == "Y" :
                show_tour_guide()
                break
            else :
                print("your input are wrong! ")
        
        num_people = int(input("How many people are you : "))
        if num_people > 0  and num_people <= 5:
            offer["tour_guide"] = backpacker["tour_guide"][0]                
        elif num_people > 5  and num_people <= 10:
            offer["tour_guide"] = backpacker["tour_guide"][1]
        elif num_people > 10  and num_people <= 20:
            offer["tour_guide"] = backpacker["tour_guide"][2]
        elif num_people > 20  and num_people <= 30:
            offer["tour_guide"] = backpacker["tour_guide"][3]
        elif num_people > 30 :
            print("contact us")
        else :
            print("your input are wrong! ")
        
        hours = int(input("How many hours you want : "))

        # Choose Visa Handler, Optional
        add_visa_handler = input("Do you need a visa handler ? : (Y/N) ")

        if add_visa_handler.upper() == "Y" :
            if not num_people:
                num_people = int(input("How many people are you (max.30): "))

            show_visa_handler()
        
            visa_handler_choice = int(input("what service do you need ? : "))
            visa_handler_idx = visa_handler_choice - 1

            offer["visa_handler"] = backpacker["visa_handler"][visa_handler_idx]

        add_to_cart(offer, num_people, hours)

        print("Your cart: ")
        display_cart()
        add_more = input("Add another itineraries? (Y/N) ")
        if add_more.upper() == "N":
            break

# cart
def display_cart() :
    headers = ["No.", "Service Name", "Description", "Qty.", "Unit", "Price", "Subtotal"]

    formatted_data = []
    for num, offer in enumerate(cart):
        for idx, (service_name, value) in enumerate(cart[num].items()):
            formatted_data.append(
                [
                    num + 1 if idx == 0 else None, 
                    service_name, 
                    value["desc"], 
                    value["qty"], 
                    value["unit"], 
                    value["unit_price"], 
                    value["subtotal"]
                ]
            )
        formatted_data.append([])

    print()
    print(tabulate(formatted_data, headers=headers, tablefmt="fancy_outline"))


def add_to_cart(offer, num_people=None, hours=None):
    offer_mapping = {
        "itinerary": {
            "desc": f"Type: {offer['itinerary']['type']}, Destination: {offer['itinerary']['destination']}",
            "qty": 1,
            "unit": "package",
            "unit_price": offer["itinerary"]["fee"],
            "subtotal": offer["itinerary"]["fee"]
        }     
    }
    if "tour_guide" in offer:
        offer_mapping["tour_guide"] = {
            "desc": f"Number of people: {num_people}",
            "qty": hours,
            "unit": "hours",
            "unit_price": offer["tour_guide"]["price_per_hour"],
            "subtotal": hours * offer["tour_guide"]["price_per_hour"]
        }
    if "visa_handler" in offer:
        offer_mapping["visa_handler"] = {
            "desc": f"Type: {offer["visa_handler"]["type"]}",
            "qty": num_people,
            "unit": "pax",
            "unit_price": offer["visa_handler"]["price_per_person"],
            "subtotal": num_people * offer["visa_handler"]["price_per_person"]
        }
    cart.append(offer_mapping)


def delete_from_cart(idx: int):
    del cart[idx]


def clear_cart():
    cart.clear()
