

user_time = int(input("vvedite vremia v sekundah:"))
hours = user_time // 3600
minutes = (user_time - hours * 3600) // 60
sec = user_time - (hours * 3600 + minutes * 60)

print (f"{hours}:{minutes}:{sec}")

