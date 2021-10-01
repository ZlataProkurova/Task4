years = int(input("Количество лет: "))
exhibits = years*365*96
print("Количество экспонатов: "+ str(exhibits))
exhibits2 = int(input("Количество просмотренных экспонатов: "))
minutes = exhibits2*5
hours = minutes/60
days = hours/8
years2 = days/365
print("Количество лет: "+ str(years2))