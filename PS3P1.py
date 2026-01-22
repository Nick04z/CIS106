# Nicholas Rodriguez - 1/22/2026

#inputs
sticksymbol = input("Enter Stock Ticker Symbol: ")
numberofshares = float(input("Enter Number of Shares: "))
costpershare = float(input("Enter Cost per Share: "))
#process
amtinvested = numberofshares * costpershare 

#outputs
print("Amount that should be Invested: ", amtinvested)