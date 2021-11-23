#program for Loaning money and caluation of intrest rate
money_owed=float(input("How much do owed , in pkr: "))
annual_rate=float(input("What's the Annual rate in percentage: "))
payment=float(input("How much monthly payment that you can pay: "))
months=int(input("Enter the duration in months: "))
monthly_Rate= annual_rate/100/12
for i in range(months):
    #divide annual_rate by 100 and then 12 months of year to get the intrest rate
    #Add in Intrest
    intrest_paid=money_owed*monthly_Rate
    money_owed+=intrest_paid
    money_owed-=payment
    if(money_owed-payment<0):
        print("Your last payment was ",money_owed)
        print("you've paid the loan in",i+1,"months")
        break
    print("Paid",payment," of which",intrest_paid,"was Intrest", end=" " )
    print("Now you Owed the money", money_owed)