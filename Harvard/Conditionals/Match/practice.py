name = input("What's name? ")

match name:
    case "Saqib" | "Muzamil" | "Mudasir":
        print("Hyderabad")
    case "Afsar":
        print("Larkana")
    case _:
        print("who?")