from services import travel_agent
from tabulate import tabulate

cart = []
def show_Travel_Agent_list():
    headers = ["No.", "Type", "Destination", "Detail", "Exlude", "price"]        
    formatted_data = []
    for num, item in enumerate(travel_agent):
        for idx, detail in enumerate(item["details"]):
            if idx == 0:
                formatted_data.append(
                    [ num + 1, item["type"], item["destination"], detail, item["exclude"], item["price"]]
                )
            else:
                formatted_data.append(
                    [ None, None, None, detail, None, None ]
                )
        formatted_data.append([])

    print(tabulate(formatted_data, headers=headers, tablefmt="fancy_outline"))

def module() :
    while True:
        num_people = None
        offer = {}

        # choose Itinerary, Mandatory
        show_Travel_Agent_list()
        choice = int(input("Enter the list you like : "))
        idx = choice - 1

        offer['travel_agent'] = travel_agent[idx]

        num_people = int(input("How many people are you : "))
        if num_people <0  and num_people > 20:
            

def add_to_cart(offer, num_people=None, hours=None):
    offer_mapping = {
        "travel_agent": {
            "desc": f"Type: {offer['travel_agent']['type']}, Destination: {offer['itinerary']['destination']}",
            "exclude": offer['exclude'],
            "qty": num_people,
            "unit": "people",
            "unit_price": offer["itinerary"]["price"],
            "subtotal": offer["itinerary"]["price"]
        }     
    }
    cart.append(offer_mapping)


def delete_from_cart(idx: int):
    del cart[idx]


def clear_cart():
    cart.clear()
