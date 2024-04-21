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
        "type": "Low Budget", 
        "destination": "Paris, Netherland",
        "details": 
            [
                "Day 1 : Departure at Soekarno-Hatta Airport",
                "Day 2 : Arrival at Paris and go to Eiffel Tower",
                "Day 3 ; Paris, dijon",
                "Day 4 ; Amsterdam, volendam",
                "Day 5 ; Amsterdam",
                "Day 6 ; Arrival at Soekarno-Hatta Airport"
            ],
        "fee": 30000
    },
    {   
        "type": "Premium",
        "destination": "Paris, German, Netherland",
        "details": 
        [
                "Day 1 : departure at Soekarno-Hatta Airport",
                "Day 2 : arrival at Paris and go to Eiffel Tower",
                "Day 3 ; Paris, dijon",
                "Day 4 ; koln, amsterdam",
                "Day 5 : amsterdam, volendam",
                "Day 6 ; amsterdam",
                "Day 7 ; arrival at Soekarno-Hatta Airport",
        ],
        "fee": 40000
    }, 
    {   
        "type": "Luxury Trip",
        "destination": "Paris, German, Swiss, Netherland",
        "details":
        [
                "Day 1 : Departure at Soekarno-Hatta Airport",
                "Day 2 : Arrival at Paris and go to Eiffel Tower",
                "Day 3 ; Paris, dijon",
                "Day 4 ; zurich, frankfrurt",
                "Day 5 ; koln, amsterdam",
                "Day 6 ; amsterdam, volendam",
                "Day 7 ; amsterdam",
                "Day 8 ; Arrival at Soekarno-Hatta Airport",
            
        ],
        "fee": 50000
    }
]

visa_handler = [
        {"type": "visa handler only", "price_per_person": 600000},
        {"type": "visa handler include embassy visa fee", "price_per_person": 2300000},
]

