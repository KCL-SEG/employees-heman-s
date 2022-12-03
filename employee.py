"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, workType, pay, commissionContracts, commissionPay, bonusCommission, hours):
        self.name = name
        self.workType = workType
        self.pay = pay
        self.commissionContracts = commissionContracts
        self.commissionPay = commissionPay
        self.bonusCommission = bonusCommission
        self.hours = hours

    def get_pay(self):
        totalPay = 0
        if self.workType == 'Monthly':
            totalPay += self.pay
        elif self.workType == 'Hourly':
            totalPay += self.pay * self.hours

        totalPay += self.commissionContracts * self.commissionPay
        totalPay += self.bonusCommission
        return totalPay

    def __str__(self):
        fstring = ""
        totalPay = self.get_pay()
        if self.workType == 'Monthly':
            fstring = f"{self.name} works on a monthly salary of {self.pay}"
        elif self.workType == 'Hourly':
            fstring = f"{self.name} works on a contract of {self.hours} hours at {self.pay}/hour"

        if self.commissionContracts != 0:
            fstring += f" and receives a commission for {self.commissionContracts} contract(s) at {self.commissionPay}/contract"
        elif self.bonusCommission != 0:
            fstring += f" and receives a bonus commission of {self.bonusCommission}"
        

        fstring += f". Their total pay is {totalPay}."
        return fstring


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'Monthly', 4000, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'Hourly', 25, 0, 0, 0, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'Monthly', 3000, 4, 200, 0, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'Hourly', 25, 3, 220, 0, 150)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'Monthly', 2000, 0, 0, 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'Hourly', 30, 0, 0, 600, 120)
