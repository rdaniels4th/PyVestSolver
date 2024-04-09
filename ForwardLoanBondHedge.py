from math import sqrt

test_mode = True  # Set to True for test mode, False otherwise

def calculate_bond_price(face_value, annual_coupon, bond_term_years, yield_to_maturity):
    total_price = 0
    for year in sorted(yield_to_maturity.keys()):
        if year <= bond_term_years:
            ytm = yield_to_maturity[year]
            total_price += annual_coupon / ((1 + ytm) ** year)
    total_price += face_value / ((1 + yield_to_maturity[bond_term_years]) ** bond_term_years)
    return total_price

def calculate_forward_loan(face_value, loan_amount, yield_to_maturity, discount_face_value, purchase_year, sale_year):
    number_of_bonds_to_buy = round(loan_amount / discount_face_value)

    purchase_ytm = yield_to_maturity[purchase_year]
    purchase_discount_price = round(discount_face_value / ((1 + purchase_ytm) ** purchase_year), 2)
    total_purchase_price = round(purchase_discount_price * number_of_bonds_to_buy, 2)

    sale_ytm = yield_to_maturity[sale_year]
    sale_discount_price = round(discount_face_value / ((1 + sale_ytm) ** sale_year), 2)
    number_of_bonds_to_sell = round(total_purchase_price / sale_discount_price)
    total_sale_price = round(number_of_bonds_to_sell * discount_face_value, 2)

    return int(number_of_bonds_to_buy), total_purchase_price, int(number_of_bonds_to_sell), total_sale_price, purchase_discount_price, sale_discount_price

def calculate_annualized_forward_rate(total_sale_price, initial_loan_amount):
    print("Annualized forward rate can be found by:", "sqrt(", total_sale_price, "/", initial_loan_amount, ") - 1")
    return sqrt(total_sale_price / initial_loan_amount) - 1

def calculate_bond_price_excluding_years(face_value, annual_coupon, bond_term_years, yield_to_maturity, exclude_years):
    total_price = 0
    for year in sorted(yield_to_maturity.keys()):
        if year <= bond_term_years and year not in exclude_years:
            ytm = yield_to_maturity[year]
            total_price += annual_coupon / ((1 + ytm) ** year)
    if bond_term_years not in exclude_years:
        total_price += face_value / ((1 + yield_to_maturity[bond_term_years]) ** bond_term_years)
    return total_price

if test_mode:
    # Predefined inputs for testing
    term_structure = {1: 0.06, 2: 0.065, 3: 0.07, 5: 0.065, 10: 0.08}
    face_value = 1000
    annual_coupon = 100
    bond_term_years = 3

    loan_amount = 5000000
    discount_face_value = 100
    purchase_year = 3
    sale_year = 5

    move_forward_yrs = 1
    redefine_term_structure = "y"
else:
    # User inputs for real scenario
    term_structure = {}
    number_of_terms = int(input("Enter the number of different terms: "))
    for _ in range(number_of_terms):
        year = int(input("Enter the year of the term: "))
        ytm = float(input("Enter the YTM for year {} as a decimal (e.g., 0.05 for 5%): ".format(year)))
        term_structure[year] = ytm

    face_value = float(input("Enter the bond's face value: "))
    annual_coupon = float(input("Enter the bond's annual coupon: "))
    bond_term_years = int(input("Enter the bond duration in years: "))
    loan_amount = float(input("Enter the loan amount: "))
    discount_face_value = float(input("Enter the face value pure discount (e.g., 100 or 1000): "))
    purchase_year = int(input("Enter the buy year for the forward loan: "))
    sale_year = int(input("Enter the sell year for the forward loan: "))

    move_forward_yrs = int(input("Enter the number of years to move forward: "))
    redefine_term_structure = input("Would you like to redefine the term structure? (y/n): ")

# Calculating bond price
bond_price = calculate_bond_price(face_value, annual_coupon, bond_term_years, term_structure)
print("Calculated bond price: {:.2f}".format(bond_price))

# Calculating forward loan details
forward_loan_results = calculate_forward_loan(face_value, loan_amount, term_structure, discount_face_value, purchase_year, sale_year)
bonds_to_buy, buy_price, bonds_to_sell, sell_price, purchase_discount_price, sale_discount_price = forward_loan_results
print("Face value pure discount: {:.0f}, Total bonds to buy: {:.0f}".format(discount_face_value, bonds_to_buy))
print("Buy discount price: {:.2f}, Total buy price: {:.2f}".format(purchase_discount_price, buy_price))
print("Sell discount price: {:.2f}, Total bonds to sell: {:.0f}, Total sell price: {:.2f}".format(sale_discount_price, bonds_to_sell, sell_price))

# Calculating annualized forward rate
annualized_forward_rate = calculate_annualized_forward_rate(sell_price, loan_amount)
print("Annualized forward rate: {:.2%}".format(annualized_forward_rate))

if redefine_term_structure == "y":
    
        if not test_mode:
            term_structure = {}
            number_of_terms = int(input("Enter the number of different terms: "))
            for _ in range(number_of_terms):
                year = int(input("Enter the year of the term: "))
                ytm = float(input("Enter the YTM for year {} as a decimal (e.g., 0.05 for 5%): ".format(year)))
                term_structure[year] = ytm
        else:
            term_structure = {1: 0.08, 2: 0.095, 3: 0.09, 5: 0.075, 10: 0.06}
    
        new_bond_term_years = bond_term_years - move_forward_yrs
        exclude_bond_price = calculate_bond_price(face_value, annual_coupon, new_bond_term_years, term_structure)
        print("New bond term years: {:.0f}, new bond price: {:.2f}".format(new_bond_term_years, exclude_bond_price))

else:
    exclude_bond_price = calculate_bond_price_excluding_years(face_value, annual_coupon, bond_term_years, term_structure, [move_forward_yrs])
    print("Calculated bond price excluding year {}: {:.2f}".format(move_forward_yrs, exclude_bond_price))

new_hpr = ((annual_coupon * move_forward_yrs) + exclude_bond_price - bond_price) / bond_price
print("New holding period return given change: {:.2%}".format(new_hpr))