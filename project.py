class RentalROI():

    def __init__(self):
        self.info = dict()
    def run1(self):
        while True:
            res = input('What do you want to do?\nType "info" to add to info\nType "change" to change info\nType "done" to get ROI\n')
            if res.lower() == 'info':
                self.getInfo()
            
            elif res.lower() == 'change':
                self.changeInfo()
            
            elif res.lower() == 'done':
                self.getRoi()
                break

            else:
                print("Incorrect response.. please type 'Show', 'Add', 'Remove', or 'Quit' to continue with the program")


    def getInfo(self):
        income = input("What is the montly rental income you make on your property?")
        self.info['Income'] = int(income)
       
        expenses = input("What is your total monthly expenses on your income?(tax, utilities, etc)")
        self.info['Expenses'] = int(expenses)     
        
        investment = input("How much money did you put up front for the property? (down payment, closing cost etc)")
        self.info["Investment"] = int(investment)

    def changeInfo(self):
        
        print(f'This is the info you have : {self.info}')
        item = input("What do you want to change from your info?").lower()
        if item == "investment":
            new1 = input("What do you want your new number to be?")
            self.info["Investment"] = int(new1)
        elif item == "income":
            new2 = input("What do you want your new number to be?")
            self.info["Income"] = int(new2)
        elif item == "expenses":
            new3 = input("What do you want your new number to be?")
            self.info["Expenses"] = int(new3)
        else:
            print("Invalid response, please enter (investment, income or expenses")
    def getRoi(self):
        cashOnCashFlow = self.info.get("Income") - self.info.get("Expenses")
        annualFlow = cashOnCashFlow * 12
        ROI = annualFlow / self.info.get("Investment") * 100
        return f"Your ROI is {ROI}%"
    def showInfo(self):
        print(self.info)





prop1 = RentalROI()
prop1.run1()