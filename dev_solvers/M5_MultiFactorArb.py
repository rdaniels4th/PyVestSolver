def calculate_expected_return(risk_free_rate, betas, factor_premiums):
    return risk_free_rate + sum(beta * premium for beta, premium in zip(betas, factor_premiums))

def find_arbitrage_opportunities(risk_free_rate, securities, factor_premiums):
    for security in securities:
        calculated_return = calculate_expected_return(risk_free_rate, security["betas"], factor_premiums)
        actual_return = security["expected_return"]
        # Adjusting the logic for identifying arbitrage opportunity
        if actual_return > calculated_return:
            print(f"Arbitrage Opportunity: {security['name']} - Actual Expected Return: {actual_return * 100}%, Calculated Return: {calculated_return * 100}%")
        else:
            print(f"No Arbitrage: {security['name']} - Actual Expected Return: {actual_return * 100}%, Calculated Return: {calculated_return * 100}%")


# Example input
risk_free_rate = 0.02
factor_premiums = [0.05, 0.04]  # Example factor risk premiums
securities = [
    {"name": "Portfolio A", "expected_return": 0.10, "betas": [2, 1]},
    {"name": "Portfolio B", "expected_return": 0.08, "betas": [1, 0.5]}
]

find_arbitrage_opportunities(risk_free_rate, securities, factor_premiums)
