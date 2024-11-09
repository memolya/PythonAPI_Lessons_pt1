films = input().split()
counter_even = 0

for film in films:
    if len(film) % 2 == 0:
        counter_even += 1
        continue
        
print(counter_even)