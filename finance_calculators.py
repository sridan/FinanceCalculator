#This is a Capstone Project that allows the user to access two different financial calculators:an investment calculator 
# and a home loan repayment calculator and displays the result according to the user's choice.

import math
print("\ninvestment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan\n")

#The user inputs the selection whether to choose investment or bond according to his preference. 
while True:
    
   question = input("Enter either-'investment' or 'bond' from the menu above to proceed:")
   question = question.lower()
   question = question.strip()

#if the user chooses investment then it calculates the total amount including interest depending 
# on the choice of simple interest or compound interest.
      
   if((question == "investment")):
          
   #The user imputs the Principal,interest rate and number of years.   
    P = float(input("\nEnter the amount to be deposited:"))
    r = float(input("Enter the Interest rate:"))
    r /= 100
    t = float(input("Enter the Number of years you are planning to invest in:"))
    
    #User gets to choose whether he want simple interest or compound interest.    
    interest = input("\nDo you want simple interest or compound interest:")
    interest = interest.lower()
    interest = interest.strip()
    
   #if the user chooses simple interest calculate simple interest using the formulae and display the total amount..
    if (interest == "simple interest"):
      
       A = float(P*(1+r*t))
       print(f"\nTotal amount after the interest applied:{A}")
       break
    
   #if the user chooses compound interest calculate compound interest using the formulae and display the total amount..
    elif(interest == "compound interest"):

         A = float(P*math.pow((1+r/100),t))
         print(f"\nTotal amount after the interest applied:{A}")
         break
   
    else:
           
   #warns user if he enters somethingelse othan the simpleinterest or compound interest. 
      print("\nEnter either simple interest or compound interest:")   
      break
   
   #if the user chooses bond then it calculates the home loan monthly repayment amount.
   elif((question == "bond")):
          
   #takes the input fromthe user for value of the house , interest rate  and number of months for repayment.
      P = float(input("\nEnter the value of the house:"))
      i = float(input("Enter the rate of interest:"))
      i /= 100
      i /= 12
      n = int(input("Enter the number of months to repay your bond:"))
      
      #calculates the monthly repayment using the formulae
      x = (1-(math.pow((1+i),(-n))))
      repayment = (i*P)/x
      print(f"\nMonthly Repayment for the Home loan is:{repayment}\n")
      break
   
   else:        
   #warns the userfor invalid input.
      print("\nEnter the valid input please enter Investment or Bond\n")
      
      