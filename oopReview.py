# states ; name , balance, branch, accNumber
# behavior,; deposit and withdrawal


class Account:
    def __init__(self, accHolder, accBalance, accType, accNumber, accBranch):
        self.accHolder = accHolder
        self.accBalance = accBalance
        self.accType = accType
        self.accNumber = accNumber
        self.accBranch = accBranch

    def savings(self):
        amountGiven = float(input(print('how much to save:')))
        print('you deposited: ', amountGiven)
        print('new balance: ', amountGiven + self.accBalance)

    def withdrawal(self):
        withdrawnAmount = float(input("enter amount to withdraw"))
        print('your balance is : ', self.accBalance - withdrawnAmount)


object = Account(accBalance=100,
                 accBranch='tomMboya',
                 accHolder='mary',
                 accType='personal',
                 accNumber=7845)
object.savings()
object.withdrawal()
