ind = int(input())
string_list = ['10', '20', 'abc']

try:
    result = int(string_list[ind])
    print('Good')
except IndexError:
    print('Bad')
except ValueError:
    print('Bad')
