films = input().split()

with open('file.txt', 'w') as file:
    for film in films:
        file.write(film)
        file.write('\n')

with open('file.txt', 'r') as file:
    content = list(file.read().split()) #split to count words and not letters
    result = []

    for film in content:
        counted = content.count(film)
        result.append(f'{film} - {counted}') #count each occurency of a word

result_final = set(result) #leave unique results only (they're repeated in the appended list above)
def last_letter(word): #use last symbol to sort
    return word[::-1]

res = sorted(result_final, key=last_letter, reverse=True) #return starting from the most frequent
print(*res, sep = '\n')
