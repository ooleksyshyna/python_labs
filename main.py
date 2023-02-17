import math

print('Hello World! Here ought to practice new skills which I was gaven on our class dedicated to Python')
print('ВПРАВИ:')
# 1
a=60
b=60
c=24
print(f'{a}*{b}={a*b}')
# 2
seconds_per_hour = 3600
print(f'{a}*{b}={seconds_per_hour}')
print(f'{seconds_per_hour}*{c}={seconds_per_hour*c}')
# 3
seconds_per_day = 86400
print(f'{seconds_per_hour}*{c}={seconds_per_day}')
# 4
print(f'{seconds_per_day}/{seconds_per_hour}={seconds_per_day/seconds_per_hour}')
# 5
print(f'{seconds_per_day}//{seconds_per_hour}={seconds_per_day/seconds_per_hour}')
# 6
print(f'{9}+{3}={9+3}')
print(f'{23}-{11}={23-11}')
print(f'{4}*{3}={4*3}')
print(f'{36}/{3}={36/3}')
# 7
number=177
print(number)
# 8
student_name= 'Olenka Oleksyshyna'
print(student_name)
student_Name='olenka oleksyshyna'
print(student_Name)
Student_Name='olenka Oleksyshyna'
print(Student_Name)
# 9
print('''Гетьте думи ви хмари осінні!
То ж тепера весна золота!\nЧи то так у жалю в голосінні\nПроминуть молодії літа?\n
Ні я хочу крізь сльози сміятись,\nСеред лиха співати пісні,\nБез надії таки сподіватись,\nЖити хочу! Геть думи сумні!
\nЯ на вбогім сумнім перелозі\nБуду сіять барвисті квітки,\nБуду сіять квітки на морозі,\nБуду лить на них сльози гіркі.\n
І від сліз тих гарячих розтане\nТа кора льодовая, міцна,\nМоже квіти зійдуть  і настане\nЩе й для мене весела весна.\n
Я на гору круту крем яную\nБуду камінь важкий підіймать\nІ, несучи вагу ту страшную,\nБуду пісню веселу співать.\n
В довгу темную нічку невидну\nНе стулю ні на хвильку очей,\nВсе шукатиму зірку провідну,\nЯсну владарку темних ночей.\n
Так! я буду крізь сльози сміятись,\nСеред лиха співати пісні,\nБез надії таки сподіватись,\nБуду жити! Геть думи сумні!''')

print('ЗАДАЧІ:')
# 1
a='Hello'
print(f'{a}, the weather today is snowy')
b=a
print(f'{b}, the weather today is snowy')
# 2
name='Olenka'
print(f"Hello,{name}, would you like to learn some Python today?")
# 3
famous_person='Albert Einstein'
message='"A person who never made a mistake never tried anything new."'
print(f'{famous_person} once said, {message}')
#4
name="  \t Olenka \n   "
print(name)
t=name.lstrip()
print(t)
q=name.rstrip()
print(q)
z=name.strip()
print(z)
# 5
print(' Олексишина Олена \n Україна\n 5008\n м.Чернівці\n вул.Університетська 30\n н.30')
# 6
n=10
f=32.8084
t=393.7
s= 0.00621371
q=10.9361
print('{0:f} {1:f} {2:f} {3:f} {4:f}'.format(n, f, t, s, q) )
# 7 табір тривав n днів, діти були в таборі -
your_days = int(input("12"))
print(your_days)
seconds=your_days*12*60*60
print(seconds)
min=your_days*12*60
print(min)
hours=your_days*12
print(hours)
secondsfor = format(seconds, "10")
print(secondsfor)
minsfor = format(min, "10")
print(minsfor)
hoursfor = format(hours, "10")
print(hoursfor)
# 8
n=6
f=2
s=5
t=9
print(f'{n}+{f}+{s}+{t}={n+f+s+t}')
с =15
f = 32 + 9/5 * с
k = c + 273,15
print(f'{k}')
print(f'{f}')
#температура на вулиці
your_degrees = int(input("20"))
c = your_degrees
f = your_degrees * 32 + 9/5
k = c + 273.15
formatc = format(c,"14,.2f")
print(formatc)
formatf = format(f,"14,.2f")
print(formatf)
formatk = format(k,"14,.2f")
print(formatk)
#9 розкладання чотирицифрового цілого числа і виведення на екран суми цифр у числі

#10

x1 = 39.9075000
x2 = 116.3972300
y1 = 50.4546600
y2 = 30.5238000
x11 = math.radians(x1)
x22 = math.radians(x2)
y11 = math.radians(y1)
y22 = math.radians(y2)
distancе = 6371.032 * math.acos(math.sin(x11) * math.sin(x22) +
                                 math.cos(x11) * math.cos(x22) * math.cos(y11 - y22))
print(distance)  # km
