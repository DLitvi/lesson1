names = ['Оля', 'Петя', 'Саша', 'Маша']
is_male = {'Оля' : False, 'Петя' : True, 'Саша' : True, 'Маша':False}
for name in names:
	if is_male[name]:
		print (name + ' - мужчина')
	else:
		print(name + ' - женщина')


groups = [
			['Вася', 'Оля'],
			['Маша', 'Петя', 'Коля']]
print ('Всего ' + str(len(groups)) + ' группы')
for group in groups:
	print ('В группе ' + str(len(group)) + ' участника')
	print ('Группа ' + str((groups.index(group))+1) + ': ' + ', '.join(group))
 