def end_of_word(number):
    okonchania ={1:'', 2: 'a', 3: 'a', 4: 'а', 0:'ов' , 5: 'ов', 6: 'ов', 7: 'ов', 8: 'ов', 9: 'ов'}
    return okonchania [number % 10]
team_num1 = 5
team_num2 = 3
print('В команде мастера кода %s участник%s' % (team_num1, end_of_word(team_num1)))
print('В команде мастера кода %s участник%s , а в другой команде %s участник%s' % (team_num1, end_of_word(team_num1),
                                                                                   team_num2, end_of_word(team_num2)))
score_2 = 42
print('Команда Волшебники данных решила задач: {0}'.format(42))
team1_time = 18015.2
print('Команда Волшебники данных решила задачи за {0} c '.format(team1_time))
score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2:
    challenge_result = 'победа команды Мастера кода!'
elif score_1 > score_2:
    challenge_result = 'победа команды nubs!'
else:
    challenge_result = 'Ничья'
print(f'Результат битвы: {challenge_result}')
time_first_team = 1568.7
time_secound_team = 1491.1
print (f'Сегодня было решено {score_1 + score_2} задач, '
       f'среднее время выполнения {(time_first_team + time_secound_team)/(score_1 + score_2)}')