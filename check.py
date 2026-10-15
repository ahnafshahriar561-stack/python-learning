import banking_upgraded

print("imported fine")
print(banking_upgraded.deposit(50))      # 50
print(banking_upgraded.balance())        # the balance is 50
print(banking_upgraded.withdraw(200))    # refusal message, then False
print(banking_upgraded.withdraw(20))     # successfully withdraw, then 30
print(banking_upgraded.balance())        # the balance is 30