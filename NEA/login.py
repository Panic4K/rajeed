import csv

def start():
    choice = input("Welcome to OCRtunes please press l to login or s to signup: ")
    while choice != "l" or "s":
        choice = input("Incorrect Input. Please press l to login or s to signup")
    if choice == "l":
        login()
    elif choice == "s":
        signup()

def signup():
    first = input("firstname:")
    last = input("sirname")
    email = input("email:")
    dob = input("date of birth")
    favArtist = input("favourite artist:")
    favGenre = input("favourite genre: ")

    inputs = [first,last,email,dob,favArtist,favGenre]
    file_obj = open("details.csv", "a")
    writer = csv.writer(file_obj)
    writer.writerow(inputs)



def login():
    


start()