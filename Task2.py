time_insec= input('Введите время в секундах')
time_insec=int(time_insec)
hour=time_insec//3600
minute = time_insec//60-60*hour
second = time_insec- minute*60-hour*3600
print('Вы ввели временной промежуток равный' , hour , 'часам',minute,'минутам' ,second,'секундам')
hour=int(hour)
minute=int(minute)
second=int(second)
hour, minute, second = [hour, minute, second]
print(f'''Временной промежуток равен: {hour}:{minute}:{second} ''')