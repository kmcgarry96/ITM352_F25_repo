# determine weather a list of purchases are within our budget or not. 
# Name: Kyle McGarry
# Date: 10/01/2025


recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget= 500
total_spent = 0
for purchases in recent_purchases:
    total_spent += purchases

    if total_spent > budget:
        print(f"You spent ${total_spent}, which is over budget")
    else:
        print(f"You spent ${total_spent}, which is within budget")