def new_function(line):
    counter = 0
    for sym in line:
        if sym in 'АОУЕИЯЁЮЭЫаоуеияёюэы':
            counter += 1
    print(counter)

new_function(line=input())