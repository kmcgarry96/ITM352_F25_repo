def check_budget(purchases, budget):
    for purchase in purchases:
        if purchase > budget:
            print("This purchase is over budget!")
        else:
            print("This purchase is within budget")

# Test it
check_budget([25, 75, 40], 50)
check_budget([36.13, 23.87, 183.35], 50)
