from math import pow

def calculate_present_value(future_value, yield_to_maturity, years):
    """Calculate the present value of a future cash flow."""
    return future_value / pow(1 + yield_to_maturity, years)

def find_weight_for_target_duration(target_duration, portfolio_weights, unspecified_bond_duration, total_investment_needed):
    """Find weight for the unspecified bond to meet the target portfolio duration."""
    x = 0  # Initial weight for the unspecified bond
    increment = 0.001  # Increment step for adjusting the weight
    tolerance = 0.01  # Tolerance for the difference between target and calculated duration
    
    # Calculate initial portfolio duration without unspecified bond
    current_duration = sum(bond * weight for bond, weight in portfolio_weights.items())
    
    # Iteratively adjust weight of the unspecified bond and check portfolio duration
    while True:
        # Calculate the new portfolio duration including the unspecified bond
        new_duration = ((1 - x) * current_duration) + (x * unspecified_bond_duration)
        if abs(target_duration - new_duration) <= tolerance:
            break  # Stop if within tolerance
        x += increment  # Increment the weight
        
        # Ensure x does not exceed 1
        if x > 1:
            raise ValueError("Cannot achieve target duration with given bond options.")
    
    return x

test_mode = False

if test_mode:
    future_obligation = 10000000
    years_until_obligation = 4
    yield_to_maturity = 0.05
    portfolio_weights = {5: 0.25, 7: 0.25, 10: 0.5}
    unspecified_bonds_duration = [2]  # List of durations of unspecified bonds
else:
    future_obligation = float(input("Enter the future obligation amount: "))
    years_until_obligation = int(input("Enter the number of years until the obligation is due: "))
    yield_to_maturity = float(input("Enter the yield to maturity as a decimal (e.g., 0.05 for 5%): "))
    portfolio_weights = {}
    while True:
        bond_year = input("Enter the bond year (or type 'd' to finish adding weights): ")
        if bond_year.lower() == 'd':
            break
        weight = float(input("Enter the weight for " + bond_year + " year zeros (as a decimal, e.g., 0.25 for 25%): "))
        portfolio_weights[int(bond_year)] = weight

    unspecified_bonds_duration = [int(year.strip()) for year in input("Enter the years of bonds without specified weights (comma-separated, e.g., 2): ").split(',') if year.strip().isdigit()]

total_investment_needed = calculate_present_value(future_obligation, yield_to_maturity, years_until_obligation)

print("Amount needed to invest today: $" + str(total_investment_needed))
for unspecified_bond_duration in unspecified_bonds_duration:
    weight_for_unspecified_bond = find_weight_for_target_duration(years_until_obligation, portfolio_weights, unspecified_bond_duration, total_investment_needed)
    portfolio_weights[unspecified_bond_duration] = weight_for_unspecified_bond

allocations = {str(bond) + " year zeros": total_investment_needed * weight for bond, weight in portfolio_weights.items()}
for bond, amount in allocations.items():
    print("Investment in " + bond + ": $" + str(amount))
