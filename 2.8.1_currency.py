roubles = int(input())
usd_rate = int(input())
eur_rate = int(input())

usd = int(roubles / usd_rate)
eur = int(roubles / eur_rate)

print(f'У пользователя в наличии {roubles} рублей, за них он может получить {usd} долларов или {eur} евро')