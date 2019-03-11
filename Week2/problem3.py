balance = 999999
annualInterestRate = 0.18
monthly_interest_rate = annualInterestRate/12

initial_lower = balance/12
initial_upper = (balance * pow(1 + monthly_interest_rate, 12))/12

def sim_year(balance, monthly_payment, monthly_interest_rate=monthly_interest_rate):
    months_left = 12
    previous_balance = balance
    while months_left:
        previous_balance -= monthly_payment
        monthly_interest = previous_balance * monthly_interest_rate
        previous_balance += monthly_interest
        months_left -= 1
    # returns the final balance after the simulation
    return previous_balance

def min_fixed_monthly_payment(lower, upper, balance, epsilon=0.01):
    candidate = (upper + lower) / 2
    final_balance = sim_year(balance, candidate)
    diff = 0 - final_balance

    if abs(diff) > epsilon:
        if diff > 0:
            new_upper = candidate
            return min_fixed_monthly_payment(lower, new_upper, balance)
        else:
            new_lower = candidate
            return min_fixed_monthly_payment(new_lower, upper, balance)
    else:
        return candidate

result = min_fixed_monthly_payment(initial_lower, initial_upper, balance)
print(round(result, 2))
