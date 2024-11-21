word = input().lower()

for letter in word:
    counter = word.count(letter)
    if counter > 1:
        flag = True
        break
    else:
        flag = False

if flag == True:
    print('Good')
else:
    print('Bad')
