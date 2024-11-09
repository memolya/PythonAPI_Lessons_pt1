text = input()
while text == text[::-1]:
    print('Good')
    break
else:
    print('Bad')
