from math import pow

# Input section with a switch for test mode or user input
test_mode = False

def calculate_expected_return(sigma, rho, sigma_market, expected_return_market, risk_free_rate):
    """Calculate expected return using the CAPM formula."""
    beta = sigma * rho / sigma_market
    return risk_free_rate + beta * (expected_return_market - risk_free_rate)

def calculate_portfolio_stats(weights, sigmas, expected_returns, correlations):
    """Calculate portfolio expected return and standard deviation for any number of securities."""
    portfolio_return = sum(weights[i] * expected_returns[i] for i in range(len(weights)))
    portfolio_variance = sum(weights[i]**2 * sigmas[i]**2 for i in range(len(weights))) + \
                         sum(sum(weights[i] * weights[j] * sigmas[i] * sigmas[j] * correlations.get((i, j), 0) 
                                 for j in range(len(weights)) if i != j) 
                             for i in range(len(weights)))
    return portfolio_return, portfolio_variance**0.5

num_securities = int(input("Enter the number of securities: ")) if not test_mode else 2

securities_data = []
for i in range(num_securities):
    if test_mode:
        sigma = 0.20 if i == 0 else 0.30
        rho = 0.4 if i == 0 else 0.7
    else:
        sigma = float(input("Enter standard deviation of stock {} (σ): ".format(i+1)))
        rho = float(input("Enter correlation of stock {} with the market (ρ): ".format(i+1)))
    securities_data.append((sigma, rho))

sigma_m = 0.15 if test_mode else float(input("Enter standard deviation of the market (σm): "))
expected_return_m = 0.10 if test_mode else float(input("Enter expected market return (E(rm)): "))
risk_free_rate = 0.05 if test_mode else float(input("Enter the risk-free rate: "))

# Calculate expected returns using CAPM
expected_returns = [calculate_expected_return(data[0], data[1], sigma_m, expected_return_m, risk_free_rate) for data in securities_data]

for i in range(len(expected_returns)):
    var = round(expected_returns[i] * 100, 2)
    print("Expected return for security {}: {}%".format(i+1, var))

# Assuming or prompting for weights and correlations
weights = [0.4, 0.6] if test_mode else [float(input("Enter weight for security {}: ".format(i+1))) for i in range(num_securities)]
correlations = {(0, 1): 0.5, (1, 0): 0.5} if test_mode else {}
if not test_mode:
    for i in range(num_securities):
        for j in range(i+1, num_securities):
            corr = float(input("Enter correlation between security {} and {}: ".format(i+1, j+1)))
            correlations[(i, j)] = corr
            correlations[(j, i)] = corr

# Calculate portfolio statistics
portfolio_return, portfolio_std_dev = calculate_portfolio_stats(weights, [data[0] for data in securities_data], expected_returns, correlations)

print("Portfolio Expected Return: {:.2%}".format(portfolio_return))
print("Portfolio Standard Deviation: {:.2%}".format(portfolio_std_dev))

# Given portfolio return to match
portfolio_expected_return = portfolio_return

# Calculate the weight of the risk-free asset in the replicating portfolio
weight_market_portfolio = (portfolio_expected_return - risk_free_rate) / (expected_return_m - risk_free_rate)
weight_risk_free = 1 - weight_market_portfolio

# Calculate the standard deviation of the replicating portfolio
replicating_portfolio_std_dev = weight_market_portfolio * sigma_m  # Only the market part contributes to the std dev

# Display the results
print("Weight of the market in the replicating portfolio: {:.4f}".format(weight_market_portfolio))
print("Weight of the risk-free asset in the replicating portfolio: {:.2f}".format(weight_risk_free))
print("Standard Deviation of the replicating portfolio: {:.2%}".format(replicating_portfolio_std_dev))

# Calculate Sharpe Ratio for the original portfolio
sharpe_ratio_original = (portfolio_return - risk_free_rate) / portfolio_std_dev

# Calculate Sharpe Ratio for the replicating portfolio
sharpe_ratio_replicating = (portfolio_expected_return - risk_free_rate) / replicating_portfolio_std_dev

# Display the Sharpe Ratios
print("Sharpe Ratio of the original portfolio: {:.4f}".format(sharpe_ratio_original))
print("Sharpe Ratio of the replicating portfolio: {:.4f}".format(sharpe_ratio_replicating))

