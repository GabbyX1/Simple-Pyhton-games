#simple quiz game in python 

answer=input(str('Start (yes or no)'))
score = 0
number_of_questions= 3

if answer =='yes':
    answer=input('what is 2 + 2?')
    if answer =='4':
        score += 1
        print('good job')
    else:
        print('really!?..')
        
answer=input('what is 6 / 3?')
if answer =='2':
    score += 1
    print('good work')
else:
    print('no...')

answer=input('what is 45 x 3?')
if answer =='135':
    score += 1
    print('nice')
else:
    print('failed')


points=(score/number_of_questions)*100
print('You finished the quiz with', points, 'points')
