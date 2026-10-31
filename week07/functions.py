# Self Assessment Questions

# 1. The first bug I spotted was that there was no colon on line 10. I noticed it before I ran the code because of the red squiggly, which suggests that I can find a bug if it's super obvious.
# 2. apply_discount(price, tier) calculates the price based on the discount tier. Its inputs are the price, the discount, and the tier. It returns the discounted price. A colleague could use it if they know what to input.
# 3. I used some AI for this lab. AI was a shortcut for some code that was repetitive, but I also used it to deepen my understanding.

# Exercise #1: calculate_tax

# Defining a function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")

# Exercise #2: apply_discount

# Defining a function with multiple parameters

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.05
    else:
        return price

# Calling the function with different tiers

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise #3: Compose Them

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise #4: Loop + Function

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# Exercise #5: Debug First, Then Ask

# The fixed code: sales = [120, 80, 250, 175, 90]

# Exercise #6: Scope Experiment

x = 100 # global x 

def double_it():
    x = 999 # local x
    return x * 2

print(x)
print(double_it())
print(x)