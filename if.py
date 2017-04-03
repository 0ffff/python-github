# Filename : if.py


number = 23
guess = int (raw_input('Enter an interger : '))

if guess == number:
    print 'Congratulations , you guessed it'#New bloack starts here 
    print "(but you do not win any prizes!)"# New block ends   here
elif guess < number :
    print 'No ,it is a little higher tahn that'
else :
    print 'No ,it is a little lower than that'

print 'Done '
# This last statement is always executed ,afer the if statement is executed
