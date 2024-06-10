class coffeeMachine:
    def __init__(self,water,milk,coffeeBeans,money) -> None:
        self.water=water
        self.milk=milk
        self.coffeeBeans=coffeeBeans
        self.money=money
        self.totalInserted=0
        self.cost=0
        self.change=0
        
    def getReport(self):
        print(f'Water: {self.water}ml',f'Milk: {self.milk}ml',f'Coffee Beans: {self.coffeeBeans}g',f'Money {self.money}',sep='\n')

    def turn_off(self):
        print('Turning off the coffee machine ..')
        exit()

    def checkResources(self,waterNeeded,milkNeeded,beansNeeded):
        result1=True
        if self.water<4*waterNeeded:
            print('RE-Full the water again please :) ')
            result1= False
            exit()
        if self.milk<4*milkNeeded:
            print('Re-Full the milk again please :) ')
            result1= False
            exit()
        if self.coffeeBeans<4*beansNeeded:
            print('Re-Full the coffee beans again :) ')
            result1= False
            exit()
        #print(f'the levels of the recipes:',f'Water: {self.water}ml',f'Milk: {self.milk}ml',f'Coffee Beans: {self.coffeeBeans}g',sep='\n')
        return result1

    def makeCoffee (self,coffeeType,waterNeeded,milkNeeded,beansNeeded):
        self.coffeeType=coffeeType
        self.cost=0
        self.waterNeeded=waterNeeded
        self.milkNeeded=milkNeeded
        self.beansNeeded=beansNeeded
        self.size=''
        if self.checkResources(waterNeeded,milkNeeded,beansNeeded): #and self.checkTransaction()
            match self.coffeeType:
                case 'off':
                    print('thank you! logging off!')
                    exit()
                case 'report':
                    print('write to us your complaint please:  ')
                    print (f'Reporting: ({str(input())})....','thank you :) ',sep='\n')
                    exit()
                case  'l' :
                    factorWater=1
                    factorMilk=2
                    factorCoffee=0.5
                    self.size=str(input('Which size you need please? Big "b" or small "s" : '))
                    if self.size=='s':
                        self.water-=factorWater*self.waterNeeded
                        self.milk -=factorMilk*self.milkNeeded
                        self.coffeeBeans-=factorCoffee*self.beansNeeded
                        self.cost=3.5
                        print (f'Small Latte costs {self.cost}€ ')
                    if self.size=='b':
                        self.water-=2*factorWater*self.waterNeeded
                        self.milk -=2*factorMilk*self.milkNeeded
                        self.coffeeBeans-=2*factorCoffee*self.beansNeeded
                        self.cost=5.5
                        print (f'Big Latte costs {self.cost}€ ')
                case 'e':
                    factorWater=1
                    factorMilk=0
                    factorCoffee=2
                    self.size=str(input('Which size you need please? Big "b" or small "s" : '))
                    if self.size=='s':
                        self.water-=factorWater*self.waterNeeded
                        self.milk -=factorMilk*self.milkNeeded
                        self.coffeeBeans-=factorCoffee*self.beansNeeded
                        self.cost=3
                        print (f'Small Espresso costs: {self.cost}€ ')
                    if self.size=='b':
                        self.water-=2*factorWater*self.waterNeeded
                        self.milk -=2*factorMilk*self.milkNeeded
                        self.coffeeBeans-=2*factorCoffee*self.beansNeeded
                        self.cost=4.5
                        print (f'Big Espresso costs: {self.cost}€ ')
                case 'c':
                    factorWater=1
                    factorMilk=2
                    factorCoffee=2
                    self.size=str(input('Which size you need please? Big "b" or small "s" : '))
                    if self.size=='s':
                        self.water-=factorWater*self.waterNeeded
                        self.milk -=factorMilk*self.milkNeeded
                        self.coffeeBeans-=factorCoffee*self.beansNeeded
                        self.cost=4
                        print (f'Small Cappuccino costs: {self.cost}€ ')
                    if self.size=='b':
                        self.water-=2*factorWater*self.waterNeeded
                        self.milk -=2*factorMilk*self.milkNeeded
                        self.coffeeBeans-=2*factorCoffee*self.beansNeeded
                        self.cost=6
                        print (f'Big Cappuccino costs: {self.cost}€ ')
                case _:
                    print('Error!! ', 'Try again please! :) ', sep='\n')
                    exit()

            #print(f'Making {coffeeType} ...')
            # self.water-=waterNeeded
            # self.milk-=milkNeeded
            # self.coffeeBeans-=beansNeeded
            # self.money2=0
            # self.money2+=self.totalInserted
            # self.change2=0
            # self.change2+=self.change
            # self.money=self.money2-self.change2
            # self.cost+=self.cost
            #print(f'Here is your {coffeeType}! Enjoy! :)')
        else:
            print('Sorry, not enough resources to make your Coffee!')

    def insertCoins(self):
        while True:
            coins=complex(input('Insert the coins please :) "Accept only (0.5 - 1 - 2)Euros!", when you finish press 0 please :)   ')).real
            match coins:
                case 0.5 | 1 | 2:
                    self.totalInserted+=coins
                    print(f'you inserted {coins}, and your balance is {self.totalInserted}','Press "0" to finish paying process',sep='\n')
                    if self.totalInserted>=self.cost:
                        print('Your balance reached to the cost!','Thank you :)',sep='\n')
                        break
                    continue
                case 0:
                    print(f'Your total balance is {self.totalInserted}')#,f'Take the changes please {self.totalInserted-self.cost} :) ',sep='\n')
                    break
                case _:
                    print('Insert only Euro please! ')
                    continue
        self.change=self.totalInserted-self.cost
        self.money+=self.totalInserted-self.change
        self.totalInserted=0

    def checkTransaction(self):
        if self.totalInserted>=self.cost:
            # change=self.totalInserted-cost
            print('Transaction Accepted :)')
            return True
        else:
            print('Sorry the money is not enough.. Money refunded!')
            return False
        
    def giveChange (self):
        if self.change>0:
            print(f'Take the changes please {self.change} :) ') 
        elif self.change==0:
            pass
        else:
            print('The money is not enough! ')

    
    def serveCoffee (self):
        match self.coffeeType:
            case 'l':
                self.coffeeType='Latte'
            case 'e':
                self.coffeeType='Espresso'
            case 'c':
                self.coffeeType='Cappuccino'
        match self.size:
            case 's':
                self.size='Small'
            case 'b':
                self.size='Big'

        print(f'Your order: {self.size} {self.coffeeType} is ready :)')
        print(f'the levels of resources:',f'Water: {self.water}ml',f'Milk: {self.milk}ml',f'Coffee Beans: {self.coffeeBeans}g',sep='\n')


    def checkResourcesAlert(self):
        if self.water<16*self.waterNeeded:
            print('Water level is low!')
        if self.milk<16*self.milkNeeded:
            print('Milk level is low!')
        if self.coffeeBeans<16*self.beansNeeded:
            print('Coffee level is low!')
        #print(f'water:{self.water} Milk:{self.milk} Coffee:{self.coffeeBeans}')
        # a=[]
        # a=a.append(self.size+self.coffeeType)
        # print(a)




        # x=str(input('One more drink? press "y", "n" no thanks! '))
        # match x:
        #     case 'y':
        #         while True:

        #             input2=str(input('chose one of those please: espresso "e" - latte "l" - cappuccino "c", otherwise chose off or report :)'))
        #             self.makeCoffee(input2,1,1,10)
        #             self.getReport()
        #             print('------------------------')
        #             if not self.checkResources(1,1,10):
        #                 print(f'the levels of the recipes:',f'Water: {self.water}ml',f'Milk: {self.milk}ml',f'Coffee Beans: {self.coffeeBeans}g',sep='\n')
        #                 break
                        
                    #self.checkResources(1,1,10)
        #     case 'n':
        #         exit()
        # print(f'the levels of the recipes:',f'Water: {self.water}ml',f'Milk: {self.milk}ml',f'Coffee Beans: {self.coffeeBeans}g',sep='\n')
                
        # self.insertCoins()
        # self.giveChange()
        #self.getReport()
    # def checkResourceAlert(self):
    #     if

 

# coffeeMachine(1000,1000,1000,50)
# print(coffeeMachine.getReport)
        