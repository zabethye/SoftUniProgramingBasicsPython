meters_for_work = float(input())
total_price = meters_for_work * 7.61
price_discount = 0.18 * total_price
final_price = total_price - price_discount

print(f"The final price is {final_price} lv.")
print(f"The discount is {price_discount}")
