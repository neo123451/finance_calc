# use import math for calculations
import math
# user should than be able to choose which calculation they want to do
# users selection should not be affected by how they type bond or interest
# if user selects interest do the following
# user must first see the following:
print("investment - to calculate the mount of interest you'll earn on your investment")
print("to calculate the amount you'll have to pay on a home loan")
print("Enter either 'investment' or 'bond' from the menu above to proceed")
Menu = input("Enter either investment or bond?").lower()
# Ask user to input amount of money that they are depositing,interest rate,number of years
# if user were to take investment:
if Menu.lower() == "investment":
    depositing1 = float(input("Enter the amount of money you want to deposit? "))
    interest_rate = float(input("Enter the interest rate? "))
    number_of_years = int(input("Enter number of years you plan on investing? "))
# ask user if they want simple or compound interest
    interest =input("Do you want simple or compound interest")
    if interest.lower() == "simple":
        P = depositing1
        r = (interest_rate) / 100
        t = number_of_years
        A = P*(1+r*t)
        print(A)
# if user takes compound
    elif interest.lower() == "compound":
        P = depositing1
        r = interest_rate
        t = number_of_years
        i = r/100
        A = P*((1+i)**t)
        print(A)
            # if user were to take bond:
            # Ask user for present value of the house,interest rate,number of months they plan to pay back the bond
if Menu.lower() == "bond":
    value_house = float(input("Enter the value of the house? "))
    interest_rate = float(input("Enter the interest rate? "))
    number_months = int(input("Enter the number of months to pay back? "))
# assign the values to their variables and calculate the amount the  user will pay each month
    P = value_house
    i = (interest_rate / 100)/12
    n = number_months
    each_month = (i * P)/(1 - (1 + i)**( -n ))
    print(each_month)
