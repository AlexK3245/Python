# Define variables for kilograms
kg_value_1 = 2
kg_value_2 = 4
kg_value_3 = 7
kg_value_4 = 10

# Coversion factor
coversion_factor = 2.20462

# Calculating pounds for each kilogram value
lbs_1 = kg_value_1 * coversion_factor
lbs_2 = kg_value_2 * coversion_factor
lbs_3 = kg_value_3 * coversion_factor
lbs_4 = kg_value_4 * coversion_factor

# Output results
print(f"\nSo, {kg_value_1} kilograms is approximately equal to {
      lbs_1:.2f} pounds.")
print(f"So, {kg_value_2} kilograms is approximately equal to {
      lbs_2:.2f} pounds.")
print(f"So, {kg_value_3} kilograms is approximately equal to {
      lbs_3:.2f} pounds.")
print(f"So, {kg_value_4} kilograms is approximately equal to {
      lbs_4:.2f} pounds.")
