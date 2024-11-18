def logic(name, country):
    def russia():
        with open('file.txt', 'w') as file:
            file.write(name)

    def england():
        with open('file.txt', 'w') as file:
            file.write(name)

    if country == 'Россия':
        russia()

    else:
        england()

    with open('file.txt', 'r') as file:
        contents = file.read()
        return contents

print(logic(name=input(),country=input()))
