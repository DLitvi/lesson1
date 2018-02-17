def get_answer(question):
	answers = {'Привет':'И тебе привет!', 'Как дела':'Лучше всех', 'Пока':'Увидимся'}
	if question in answers:
		return answers[question].lower()

question = input ('Введите вопрос: ')
print (get_answer(question))




