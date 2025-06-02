profit=0
wanna_end=False
resources={
    'water':10000,
    'coffee_beans':1000,
    'milk':20000
}

menu={'expresso':{'ingredients':
          {
           'water':50,
           'milk':100,
           'coffee_beans':20
          },
       'cost':500
},

       'latte': {'ingredients':
          {
           'water':100,
           'milk':200,
           'coffee_beans':40
          },
            'cost':1000
       },

'cappuccino':{'ingredients':
          {
           'water':500,
           'milk':1000,
           'coffee_beans':100
          },
           'cost':5000
       }
}
def ckecking_requirement(coffee_type,resources):
    for item in coffee_type:
        if(coffee_type[item]>resources[item]):
            return False
    return True
def insert_coins():
    total=0
    print("please insert your coins")
    rs_5=int(input("how many 5 rupees coins"))
    rs_10=int(input("how many 10 rupees coins"))
    rs_20=int(input("how many 20 rupees coins"))
    total=total+5*rs_5+10*rs_10+20*rs_20
    return total
def payment_successful(money,cost_type):
    change=0
    if(money>=cost_type):
        print(f"your change is {change+(money-cost_type)}")
        return True
    else:
        print(f"payment is not successfull you have to pay total of {cost_type}")
        return False
def ingredients_deduction(coffee_type,resources):
    #resources2={}
    for item in resources:
        resources[item]=(resources[item]-coffee_type[item])
    return True
while not wanna_end:
      user_choice=input("what would you like to have(expresso/cappuccino/latte/) hint(enter report to see the resources available or off to exit)")
      if(user_choice=='report'):
          print(f"water={resources['water']} \n milk={resources['milk']}\n coffee_beans={resources['coffee_beans']} \n money={profit}")
          wanna_end=False
      elif(user_choice=='off'):
          print("thank you")
          wanna_end=True
      else:
          coffee_type=menu[user_choice]['ingredients']
          cost_type=menu[user_choice]['cost']
          if ckecking_requirement(coffee_type,resources):
             print(f"you have to pay {cost_type}")
             money=insert_coins()
             if payment_successful(money,cost_type):
                 profit = profit + cost_type
                 if ingredients_deduction(coffee_type,resources):
                     print(f"here is your {user_choice}")
                     print("thanks for coming to our coffee shop please recommend others for coffee")
                     review = input("please rate our coffee out of 5 ")
                     print(f"I gave you {review} rating out off 5")












