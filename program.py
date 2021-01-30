from modules import read_csv, display_list, add_person, remove_person, save_as_json

# Definerar upp persons
persons = []

# Visar menyn, utför respektive val beroende på inmatning, eller meddelande om felaktigt val.
while True:
    print('\nMeny')
    print('1. Läs in originalfil (labb2-personer.csv)')
    print('2. Visa json-data (labb2-personer.json)')
    print('3. Lägg till person')
    print('4. Ta bort person')
    print('5. Spara till json-fil (labb2-personer.json)')
    print('6. Avsluta')
    menu_choice = input('Ange siffran för det menyval du vill till: ')

    if menu_choice == '1':
        persons = read_csv()
    elif menu_choice == '2':
        display_list()
    elif menu_choice == '3':
        print('\nDu kommer nu få mata in användarnamn, förnamn, efternamn och epost för en ny användare ')
        add_person(persons)
    elif menu_choice == '4':
        remove_person(persons)
    elif menu_choice == '5':
        save_as_json(persons)
    elif menu_choice == '6':
        print('Avslutar programmet')
        break
    else: 
        print('Du måste ange ett giltigt val, försök igen. ')