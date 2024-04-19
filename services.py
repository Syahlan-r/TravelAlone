role = ["admin", "customer"]
main_menu = ["Backpacker", "Travel agent", "Contact us"]


tour_guide = [
    {"people": "1 - 5 person", "price_per_hour": 100000},
    {"people": "6 - 10 person", "price_per_hour": 150000},
    {"people": "11 - 20 person", "price_per_hour": 250000},
    {"people": "21 - 30 person", "price_per_hour": 350000},
]

itinerary = [
    {
        "type": "low budget", 
        "destination": "paris, netherland",
        "details": 
            [
                "hari 1 : Departure at Soekarno-Hatta International Airport",
                "hari 2 : Arrival at Charles de Gaulle Airport and go to Eiffel Tower",
                "hari 3 ; paris, dijon",
                "hari 4 ; amsterdam, volendam",
                "hari 5 ; amsterdam",
                "hari 6 ; Arrival at Soekarno-Hatta International Airport"
            ],
        "fee": 30000
    },
    {   
        "type": "premium",
        "destination": "paris, german, netherland",
        "details": 
        [
                "hari 1 : departure at Soekarno-Hatta International Airport",
                "hari 2 : arrival at Charles de Gaulle Airport and go to Eiffel Tower",
                "hari 3 ; paris, dijon",
                "hari 4 ; koln, amsterdam",
                "hari 5 : amsterdam, volendam",
                "hari 6 ; amsterdam",
                "hari 7 ; arrival at Soekarno-Hatta International Airport",
        ],
        "fee": 40000
    }, 
    {   
        "type": "luxury_trip",
        "destination": "paris, german, swiss, netherland",
        "details":
        [
                "hari 1 : Departure at Soekarno-Hatta International Airport",
                "hari 2 : Arrival at Charles de Gaulle Airport and go to Eiffel Tower",
                "hari 3 ; paris, dijon",
                "hari 4 ; zurich, frankfrurt",
                "hari 5 ; koln, amsterdam",
                "hari 6 ; amsterdam, volendam",
                "hari 7 ; amsterdam",
                "hari 8 ; Arrival at Soekarno-Hatta International Airport",
            
        ],
        "fee": 50000
    }
]

visa_handler = [
        {"type": "visa handler only", "price_per_person": 600000},
        {"type": "visa handler include embassy visa fee", "price_per_person": 2300000},
]

