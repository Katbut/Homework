income = input('Введите значение выручки фирмы ')
outcome = input('Введите значение издержек фирмы ')
income = int(income)
outcome = int(outcome)
result = income-outcome
if result >0:
    print('Прибыль ')
    rentabelnost = result/income
    print('Рентабельность выручки составляет: ',rentabelnost,)
    number_people = input('Введите количество сотрудников ')
    number_people = int(number_people)
    peoplerent = rentabelnost/number_people
    print('Прибыль в расчете на одного сотрудника ',peoplerent,)
else:
    print('Убыток')
