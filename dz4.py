exhibits = int(input("Количество просмотренных экспонатов: "))
minutes = exhibits*5
hours = minutes/60
days = hours/8
years2 = days/365
print (" Количество лет: "+ str(years2))
years = int(input("Количество лет: "))

exhibits2 = years*365*96
print ("Количество экспонатов: "+ str(exhibits2))
input()