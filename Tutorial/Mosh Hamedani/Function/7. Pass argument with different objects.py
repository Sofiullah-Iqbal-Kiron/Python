def user_information(**information):
    print(information)  # This will print all the information of user as a dictionary.
    print(information["id"])  # Pass the key at square bracket and enclose with double-quotes.


user_information(name="Kiron", id=65, section='A')
# {'name': 'Kiron', 'id': 65, 'section': 'A'}: This is the dictionary
# or key-value pair. Simply mapping in C++ / Java.
