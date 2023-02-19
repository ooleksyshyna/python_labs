# 7 табір тривав n днів, діти були в таборі -
your_days = int(input("Duration of camp:"))
print(your_days)

seconds = your_days*24*60*60
print(seconds)

min=your_days*24*60
print(min)

hours = your_days*24
print(hours)

duration_seconds = format(seconds, "10")
print(duration_seconds)

duration_minutes = format(min, "10")
print(duration_minutes)

duration_hours = format(hours, "10")
print(duration_hours)