class debt:
        def __init__(self, id, name, balance, interestRate, minimumPayment):
            self.id = id
            self.name = name
            self.balance = balance
            self.interestRate = interestRate
            self.minimumPayment = minimumPayment

def findSnowballValue(debts):
    for debt in debts:
        snowballID = 0
        #print(debt.name, debt.balance, debt.id, debt.interestRate)
        #print (debts[snowballID].balance)
        if debt.balance < debts[snowballID].balance:
            #print(debt.name + "lower than "+ debts[snowballID].name)
            snowballID = debt.id
    print("Snowball value", debtListSnowball[snowballID].name)
    return snowballID

def makePayments(debts):
    totalinterest  = 0
    for debt in debts:
        #print (debt.name, debt.balance, debt.interestRate)
        newBalance = (debt.balance - debt.minimumPayment) * (1+ (debt.interestRate/12))
        totalinterest +=  debt.minimumPayment -(debt.balance - newBalance)
        debt.balance = newBalance
    return totalinterest

def calculateRemainingBalance(debts):
    remBalance = 0
    for each in debts:
        remBalance += each.balance
    return remBalance 

def assessPaidOffStatus(debts):
    extraPaymentAdd = 0
    for debt in debts:
        if debt.balance <= 0:
            extraPayment = debt.minimumPayment            
            print("Remove " + debt.name + " and allocate payment of " + str(debt.minimumPayment))
            debts.remove(debt) 
            reassignIds(debts)
    return extraPaymentAdd

def reassignIds(debts):
    iterator = 0
    for debt in debts:
        debt.id = iterator
        iterator += 1

def calculateSnowball(debts):
    totalInterestSnowball = 0
    extraPayment = 0
    #calculate total balance to go through
    totalBalanceRemainingSnowball = calculateRemainingBalance(debts)

    #While Total balance is above zero, (ie debt still to be paid)
    while(totalBalanceRemainingSnowball > 0):
        #make payments
        totalInterestSnowball += makePayments(debtListSnowball)
        totalBalanceRemainingSnowball = calculateRemainingBalance(debtListSnowball)
        #if current SnowballID is paid off select a new ID to pay off next
        if totalBalanceRemainingSnowball <= 0:
            return
        extraPayment = extraPayment +  assessPaidOffStatus(debtListSnowball)
        #if 
        # if (assessPaidOffStatus(debtListSnowball) is true):
        #     snowballExtraPaymentsID = findSnowballValue(debtListSnowball)
        if extraPayment > 0:
            print( "Extra payments towards " + debtListSnowball[snowballExtraPaymentsID].name + " for " + str(extraPayment))
            debtListSnowball[snowballExtraPaymentsID].balance -= extraPayment

        #for debt in debtListSnowball:
            # print(debt.name, debt.balance)






#list of debts
d1 = debt(0, "chase", 8142, .1924, 240)
d2 = debt(1, "home depot", 9034, .2599, 240)
d3 = debt(2,"capital one", 3083, .2, 80)
d4 = debt(3, "pep boys", 674, .2, 80)

#assign to list to iterate through
debtList = [d1, d2, d3, d4]     #master list
debtListSnowball = debtList     #list for snowball
debtListAvalanche = debtList    #list for avalanche

totalBalance = 0
totalBalanceRemainingSnowball = 0 
totalBalanceRemainingAvalanche = 0
totalInterestSnowball = 0
totalInterestAvalanche = 0

for debt in debtList:
    totalBalance += debt.balance

totalBalanceRemainingSnowball = totalBalance
totalBalanceRemainingAvalanche = totalBalance
#print(totalBalance)


#debt snowball: lowest balance 
snowballobjct = calculateSnowball(debtListSnowball)
print("Total Interest SnowBall: " , totalInterestSnowball)
#print(snowballobjct)



#debt avalanche: highest interest first 