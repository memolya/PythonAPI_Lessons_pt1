new_list = input().split()
counter_words = 0

for element in new_list:
    if element.isalpha():
        counter_words += 1

print(counter_words)