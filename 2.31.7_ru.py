email = input().split()
ru = []
other = []

for mail in email:
    if '.ru' in mail:
        ru.append(mail)
    else:
        other.append(mail)

print(ru, other, sep = '\n')