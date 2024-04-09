# Prompt the user for input
risk_free_rate = float(input("Enter the risk-free rate (as a decimal, e.g., 0.05 for 5%): "))
expected_return1 = float(input("Enter the CAPM expected return for Stock 1 (as a decimal, e.g., 0.12 for 12%): "))

# Fama-French model parameters
beta1_FF = float(input("Enter beta1 for the Fama-French model: "))
beta2_FF = float(input("Enter beta2 for the Fama-French model: "))
beta3_FF = float(input("Enter beta3 for the Fama-French model: "))

EF1 = float(input("Enter the expected value of Factor 1 (E(F1), as a decimal): "))
EF2 = float(input("Enter the expected value of Factor 2 (E(F2), as a decimal): "))
EF3 = float(input("Enter the expected value of Factor 3 (E(F3), as a decimal): "))

# Calculate expected return based on Fama-French three-factor model
expected_return_FF = risk_free_rate + beta1_FF * EF1 + beta2_FF * EF2 + beta3_FF * EF3

# Estimate stock 1’s alpha using CAPM
alpha_stock1 = expected_return_FF - expected_return1

# Display results
print("Expected return based on Fama-French model: {:.2%}".format(expected_return_FF))
print("Alpha of Stock 1 compared to CAPM: {:.2%}".format(alpha_stock1))

# Decision for the active portfolio manager
if alpha_stock1 > 0:
    print("Stock 1 is performing better than CAPM predictions. Consider adding it to the portfolio.")
else:
    print("Stock 1 is not performing as well as CAPM predictions. Consider reviewing its position in the portfolio.")
