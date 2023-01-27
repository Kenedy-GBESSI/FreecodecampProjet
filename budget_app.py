

class Category:

    def __init__(self,name):
        self.name = name
        self.ledger = []
    def __str__(self):
        the_str = "{:*^30s}\n".format(self.name)
        for i in self.ledger:
            key,value = i.items()
            str_curr = "{:<23s}".format(value[1][:23])+ "{:7.2f}".format(float(key[1])) + "\n"
            the_str +=str_curr
        the_str +="Total: {:.2f}".format(self.get_balance())
        return the_str

    def get_withdraw(self):
        balanc_total = 0
        for i in self.ledger:
            if(i['amount'] < 0):
                balanc_total += i['amount']
        return -balanc_total
        
        
    
    def deposit(self,amount,descripton=""):
        self.ledger.append({"amount":amount,"description":descripton})
    
    def withdraw(self,amount,descripton=""):
        if(self.check_funds(amount)):
            self.ledger.append({"amount":-amount,"descripton":descripton})
            return True
        return False
    
    def get_balance(self):
        balanc_total = 0
        for i in self.ledger:
            balanc_total += i['amount']
        return balanc_total

    def transfer(self,amount,transfer_to):
        if(self.check_funds(amount)):
            transfer_to.deposit(amount,"Transfer to {}".format(transfer_to.name))
            self.withdraw(amount,descripton="Transfer from {}".format(self.name))
            return True
        return False
    
    def check_funds(self,amount):
        return self.get_balance() >= amount


def create_spend_chart(categories):
    percentage_for_category = [i.get_withdraw() for i in categories]
    somme = sum(percentage_for_category)
    each_per = [round((i/somme)*100) for i in percentage_for_category]
    tab = range(0,110,10)
    range_reverse =tab[::-1]
    for i in range_reverse:
        for j in range(len((each_per))):
            if(each_per[j] < i and each_per[j] > i-10):
                each_per[j] = i-10
        over_tab = [(each_per[i],categories[i].name) for i in range(len(categories))]
    return "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  " 


entertainment = Category("Entertainment")
category = Category("Food")
category.deposit(900,"Initial deposit")
category.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
category.transfer(20, entertainment)

print(category)

enter = Category("Entertainment")
enter.deposit(900)
enter.withdraw(33.40)

secours = Category("Secours")
secours.deposit(900)
secours.withdraw(10.99)

print(create_spend_chart([category,enter,secours]))

    