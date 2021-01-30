import json

# Fått hjälp och inspiration av Edvin Owetz för read_csv, mycket tacksam för det!
# Så länge filen finns öppnas och läses den in, användarna läggs till i person.
# Finns inte filen får man ett felmeddelande.
def read_csv(persons_csv='labb2-personer.csv', path='./'):
    persons = []
    path += persons_csv

    try:
        with open(path, "r", encoding="utf-8-sig") as persons_csv:
            first_line = True
            for line in persons_csv:
                if first_line:
                    first_line = False
                elif len(line) > 0:
                    rf_line = line.rstrip('\n').split(';')
                    persons.append({'Användarnamn': rf_line[0], 'Förnamn': rf_line[1], 'Efternamn': rf_line[2], 'epost': rf_line[3]})
            return persons
    except FileNotFoundError:
        print('\nFilen du försöker öppna finns inte. ')

# Om json-filen finns får man se alla användare som ligger i den, annars får man meddelande om att filen inte finns.
def display_list():
    try:
        f = open('labb2-personer.json', 'r', encoding='UTF-8-sig').read()
        persons = json.loads(f)
        for row in persons:
            print(f'{row["Användarnamn"]} {row["Förnamn"]} {row["Efternamn"]} {row["epost"]}')
        return persons
    except FileNotFoundError:
        print('\nFilen du försöker öppna finns inte, läs in originalfilen och spar den som json.')

# Låter användaren mata in en ny användare, append för att läggas till i persons.
def add_person(persons):
    username = input('Ange användarnamn: ')
    first_name = input('Ange förnamn: ')
    last_name = input('Ange efternamnet: ')
    email = input('Ange epost: ')
    persons.append({'Användarnamn': username, 'Förnamn': first_name,'Efternamn': last_name, 'epost': email})

# Visar först index på alla som finns i listan, låter sedan användaren ange index för den som skall tas bort.
# Skriver man ett index som inte finns, får man meddelande om detta.
# Skriver man något annat än en siffra får man meddelande om detta.
def remove_person(persons):
    if len(persons) > 0:
        print('Visar index för alla användare: ')
        for index, row in enumerate(persons):
            print(index, f'{row["Användarnamn"]} {row["Förnamn"]} {row["Efternamn"]} {row["epost"]}')
        while True:
            try:
                remove_user = int(input('Ange index för den du vill ta bort: '))
                persons.pop(remove_user)
                break
            except ValueError:
                print('Du måste ange en siffra för index, försök igen. ')
            except IndexError:
                print('Index du angav finns inte, försök igen. ')
    else:
        print('\nDu har inga användare inlästa ännu. Läs in en fil eller lägg till en användare först. ')    

# Sparar persons till labb2-personser.json
# Om man inte läst in originalfilen ännu (dvs persons är tom) får man meddelande om att man inte kan spara en tom fil.
def save_as_json(persons):
    if len(persons) > 0:
        with open('labb2-personer.json', 'w', encoding='utf-8') as f:
            json.dump(persons, f, ensure_ascii=False, indent=4)
    else:
        print('\nDu kan inte spara en tom fil. Läs in originalfilen labb2-personer.csv först. ')