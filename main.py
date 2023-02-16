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
# 4
print(' Олексишина Олена \n Україна\n 5008\n м.Чернівці\n вул.Університетська 30\n н.30')
# 5
n=10
f=32.8084
t=393.7
s= 0.00621371
q=10.9361
print('{0:f} {1:f} {2:f} {3:f} {4:f}'.format(n, f, t, s, q) )
# 6
print('\nОленка\tОлексишина')
# 7
print('\t 1,5h')
print('\t 90min')
print('\t 5,400sec')
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
#10
import math
x1 = 39.9075000
x2 = 116.3972300
y1 = 50.4546600
y2 = 30.5238000
x11 = math.radians(x1)
x22 = math.radians(x2)
y11 = math.radians(y1)
y22 = math.radians(y2)
distancee = 6371.032 * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11 - y22))
print(distancee)  # km
