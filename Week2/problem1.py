# test case 1
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def balance_at_end_of_year(balance, yearly_inter, monthly_rate):
    """
        balance: outstanding balance on the credit card
        yearly_inter: annual interest rate as a decimal
        monthly_rate: minimum monthly payment rate as a decimal
    """
    months_left = 12
    monthly_interest_rate = yearly_inter / 12

    while months_left:
        minimum_monthly_payment = balance * monthly_rate
        monthly_unpaid_balance = balance - minimum_monthly_payment
        balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        print(f'Month {13-months_left} remaining balance is {round(balance, 2)}')
        months_left -= 1

balance_at_end_of_year(balance, annualInterestRate, monthlyPaymentRate)


# Recursive version
def recur(balance, monthly_inter, monthly_rate, months_left):
    if not months_left:
        print(f'Remaining Balance: {round(balance, 2)}')
    else:
        minimum_monthly_payment = balance * monthly_rate
        monthly_unpaid_balance = balance - minimum_monthly_payment
        balance = monthly_unpaid_balance + (monthly_inter * monthly_unpaid_balance)
        recur(balance, monthly_inter, monthly_rate, months_left-1)

print('using recur:')
recur(balance, annualInterestRate/12, monthlyPaymentRate, 12)
