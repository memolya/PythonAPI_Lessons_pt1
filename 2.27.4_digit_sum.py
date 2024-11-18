def new_func(line):
    counter = 0
    for element in line:
        if element.isnumeric():
            counter += int(element)
    print(counter)


new_func(line=input())
