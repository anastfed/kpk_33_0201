from pizzeria import Pizza, Beverages, Contacts, Location

print('*' * 25)
Pizza = Pizza.import_from_file('Pizza.src')
[print(el) for el in Pizza]

print('*' * 25)
Beverages = Beverages.import_from_file('Beverages.src')
[print(el) for el in Beverages]

print('*' * 25)
Contacts = Contacts.import_from_file('Contacts.src')
[print(el) for el in Contacts]

print('*' * 25)
Location = Location.import_from_file('Location.src')
[print(el) for el in Location]