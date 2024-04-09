# Flag to toggle test mode
test_mode = False

# Function to run the script in test mode with predefined values
def run_test_mode():
    risk_free_rate = 0.05
    securities_data = [
        {"expected_return_CAPM": 0.12, "beta1_FF": 0.4, "beta2_FF": 0.5, "beta3_FF": 0.5}
    ]
    EF1 = 0.10
    EF2 = 0.02
    EF3 = 0.05
    return risk_free_rate, securities_data, EF1, EF2, EF3

# Function to run the script with user input
def run_user_input_mode():
    risk_free_rate = float(input("Enter the risk-free rate (as a decimal, e.g., 0.05 for 5%): "))
    num_securities = int(input("Enter the number of securities: "))
    EF1 = float(input("Enter the expected value of Factor 1 (E(F1), as a decimal): "))
    EF2 = float(input("Enter the expected value of Factor 2 (E(F2), as a decimal): "))
    EF3 = float(input("Enter the expected value of Factor 3 (E(F3), as a decimal): "))
    securities_data = []
    for i in range(1, num_securities + 1):
        capm_return_input = input(f"Enter the CAPM expected return for Stock {i} (as a decimal, e.g., 0.12 for 12%) or press enter to skip: ")
        if capm_return_input in ('', 'None', None):
            print(f"Skipping Stock {i} due to missing CAPM expected return.")
            continue
        securities_data.append({
            "expected_return_CAPM": float(capm_return_input),
            "beta1_FF": float(input(f"Enter beta1 for Stock {i} in the Fama-French model: ")),
            "beta2_FF": float(input(f"Enter beta2 for Stock {i} in the Fama-French model: ")),
            "beta3_FF": float(input(f"Enter beta3 for Stock {i} in the Fama-French model: "))
        })
    return risk_free_rate, securities_data, EF1, EF2, EF3

# Choose the mode based on the test_mode flag
if test_mode:
    risk_free_rate, securities_data, EF1, EF2, EF3 = run_test_mode()
else:
    risk_free_rate, securities_data, EF1, EF2, EF3 = run_user_input_mode()

# Process securities
for i, security in enumerate(securities_data, start=1):
    expected_return_FF = risk_free_rate + security["beta1_FF"] * EF1 + security["beta2_FF"] * EF2 + security["beta3_FF"] * EF3
    alpha = expected_return_FF - security["expected_return_CAPM"]
    
    print(f"\nStock {i}:")
    print(f"Expected return based on Fama-French model: {expected_return_FF:.4%}")
    print(f"Alpha compared to CAPM: {alpha:.4%}")
    
    if alpha > 0:
        print("Recommendation: Consider adding more of this stock to the portfolio.")
    elif alpha < 0:
        print("Recommendation: Consider reducing this stock from the portfolio.")
    else:
        print("Recommendation: Keep the current portfolio allocation for this stock.")
