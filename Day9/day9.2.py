travel_log = [
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"],

    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
def add_new_country(new_country = "country", time_visits = "visits", new_cities = "cities"):
    add_country = {
        "country":new_country,
        "visits":time_visits,
        "cities":new_cities
    }
    travel_log.append(add_country)

add_new_country("russia",2,["moscow","Saint petersburg"])

print(travel_log)