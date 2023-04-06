coef=1.0
sum=0
a=0
count=int(input("Количество билетов: \n"))
if count>=3:
	coef=0.9
for i in range(count):
	a=int(input("Возраст для билета "+str(i)+":\n"))
	if 18<=a<=25:
		sum+=990
	elif a>25:
		sum+=1390

print("Сумма:",sum*coef)
input()