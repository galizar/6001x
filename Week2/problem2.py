balance = 3329
annualInterestRate = 0.2

# This get's 11 out of 15 correct. It's fine I guess.

def find_min_fixed_monthly_payment_to_payoff_cd(initial_balance, monthly_interest_rate):
    months_left = 12
    fixed_monthly_pay_no_interest = initial_balance // 12.
    previous_balance = initial_balance
    yearly_interest = 0

    while months_left:
        previous_balance -= fixed_monthly_pay_no_interest
        monthly_interest = previous_balance * monthly_interest_rate
        yearly_interest += monthly_interest
        previous_balance += monthly_interest
        months_left -= 1

    lowest = fixed_monthly_pay_no_interest + (yearly_interest / 12.)

    print(lowest)
    print('Lowest payment:', round(lowest / 10) * 10)

find_min_fixed_monthly_payment_to_payoff_cd(balance, annualInterestRate/12.)

