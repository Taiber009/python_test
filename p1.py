money=int(input())
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[(x * money)/100 for x in per_cent.values()]
print(deposit)
print("Максимальная сумма, которую вы можете заработать —",max(deposit))