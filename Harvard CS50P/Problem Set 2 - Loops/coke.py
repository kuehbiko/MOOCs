#task:
#coke costs $0.50
#take input of coins $0.25, $0.10, $0.05
#if total paid amt < 50: output remaining amount
#if total paid amt > 50: output change owed

remaining_amt = 50
total_paid = 0

while remaining_amt > 0:
    print("Amount Due: " + str(remaining_amt))

    paid_amt = int(input("Insert Coin: "))

    if paid_amt in [5, 10, 25]:
        remaining_amt -= paid_amt
        total_paid += paid_amt

print("Change Owed: " + str(total_paid - 50))
