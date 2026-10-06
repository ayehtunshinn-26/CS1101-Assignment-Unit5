# Daily cups sold (5 days)
daily_orders = [120, 150, 180, 90, 200]
price_per_cup = 5

# Calculate daily revenue using map() and lambda
daily_revenue = list(map(lambda cups: cups * price_per_cup, daily_orders))

# Find the highest sales day using max()
busiest_day_sales = max(daily_orders)


print("Daily cups sold:", daily_orders)
print("Daily revenue ($):", daily_revenue)
print("Busiest day sales (cups):", busiest_day_sales)
