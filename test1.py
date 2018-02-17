mydict = {'Маша':{'city':'Москва', 'temperature':'10', 'wind':'восточный'}, 'Петя': {'city':'Воронеж', 'temperature': '12', 'wind':'западный'}}
name = input('Введите имя: ')
if name in mydict:
	print ('Город: ' + mydict[name]['city'] + '; температура: ' + mydict[name]['temperature'])
else:
	print('Данного имени нет в словаре')
