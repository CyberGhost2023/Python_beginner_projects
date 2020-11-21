# credit_principal = int(input('Enter the credit principal'))
import math
user_choice = input('''What do you want to calculate? 
type "n" - for count of months,
type "a" - for annuity monthly payment, 
type "p" - for credit principal:''')

def month_count():
    credit_principal = int(input('Enter credit principle:'))
    monthly_payment = float(input('Enter monthly payment:'))
    credit_interest = float(input('Enter credit interest: '))
    i = credit_interest/(12*100)
    period = math.ceil(math.log(monthly_payment/(monthly_payment - i*credit_principal),1+i))
    years = period//12
    months = period % 12
    if years == 0 or months==years==0:
        print(f'You need {months} months to repay this credit!')
    elif months == 0:
        print(f'You need {years} years to repay this credit!')
    else:
        print(f'You need {years} years and {months} months to repay this credit!')
        
def principal():
    monthly_payment = float(input('Enter monthly payment:'))
    n = int(input('Enter count of periods: '))
    credit_interest = float(input('Enter credit interest: '))
    i = credit_interest/(12*100)
    credit_principal = monthly_payment/((i * pow(i+1,n))/(pow(i+1,n)-1))
    print(f'Your credit principal = {credit_principal}!')

def annuity():
    credit_principal = int(input('Enter credit principle:'))
    n = int(input('Enter count of periods: '))
    credit_interest = float(input('Enter credit principle:'))
    i = credit_interest/(12*100)
    monthly_payment = math.ceil(credit_principal *((i * pow(i+1,n))/(pow(i+1,n)-1)))
    print(f'Your annuity payment = {monthly_payment}!')
    
    
if user_choice == 'p':
    principal()
elif user_choice == 'a':
    annuity()
elif user_choice == 'n':
    month_count()