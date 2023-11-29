#One Stop Insurance Company 
#Lianne Campbell
#11/19/2023
#QAP 4 Project 1


#Import Required Libraries
import datetime
import FormatValues as FV
import time

#Setup Program Constants
#Set  up  the  following  default  values  for the  next  policy  number, 1944
NextPolicy = 1944

#the  basic  premium, 869.00
BasicPremium = 869.00

#the  discount  for additional  cars, 0.25
AddCarDiscountRate = 0.25

#the  cost  of  extra  liability  coverage, 130.00
LiabilityCoverCost = 130.00

#the  cost  of  glass  coverage,  86.00
GlassCoverCost = 86.00

#the  cost  for  loaner  car coverage, 58.00
LoanCarCost = 58.00

#the HST rate, 0.15
HSTRate = 0.15

#and the processing fee for monthly payments. 39.99
ProcessFeeMonthPay = 39.99

#the values are 1944, , 869.00, .25, 130.00, 86.00, 58.00, .15, and 39.99 respectfully.
CurrentDate = datetime.datetime.now()



#Setup User Inputs
#The user will input the customer’s
#first and last name 
FirstName = input("Please Input Your First Name: ").title()
print()
LastName = input("Please Input Your Last Name: ").title()
print()

#address
HomeAddress = input("Please Input Your Home Adress: ").title()
print()

#city
City = input("Please Input Your City: ").title()
print()

#province(validate using a list to make sure the province is valid), 
ProvLst = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

ProvNum = 1
print()
for Prov in ProvLst:
    print(f"{str(ProvNum)}. {Prov}")
    ProvNum += 1  
print()
while True:
    Prov = input("Please Enter The Province From List Above (XX): ").upper()
    if Prov == "":
        print("Error - Province cannot be blank - Please Re-enter.")
    elif len(Prov) != 2:
        print("Error - Province is a 2 digit code - Please Re-enter.")
    elif Prov not in ProvLst:
        print("Error - Not a valid Province - Please Re-enter.")
    else:
        break
print()

#postal code 
PostalCode = input("Please Enter Your Postal Code (X9X9X9): ").upper()
print()

#phone number 
PhoneNumber = input("Please Enter Your Phone Number (7097779999): ")
print() 

#the number of cars being insured
NumCarIns = input("Please Enter The Number of Cars to be Insured: ")
NumCarIns = int(NumCarIns)
print()

#and  options  for  extra  liability  up  to  $1,000,000  (enter  Y  for  Yes  or  N  for  No)
ExtLiabLst = ["Y", "N"]
while True:
    ExtLiab = input("Would you like to add extra liability up to $1,000,000 (Enter Y for Yes or N for No.): ").upper()
    if ExtLiab == "":
        print("Error - Option cannot be blank - Please Re-enter Y or N.")
    elif ExtLiab not in ExtLiabLst:
        print("Error - Not a valid Option - Please Re-enter Y or N.")
    else:
        break
print()

#optional  glass coverage (Y or N)
GlassCoverLst = ["Y", "N"]
while True:
    GlassCover = input("Would you like to add optional glass coverage (Enter Y for Yes or N for No): ").upper()
    if GlassCover == "":
        print("Error - Option cannot be blank - Please Re-enter Y or N.")
    elif GlassCover not in GlassCoverLst:
        print("Error - Not a valid Option - Please Re-enter Y or N.")
    else:
        break
print()

#and optional loaner car (Y or N).
LoanCarLst = ["Y", "N"]
while True:
    LoanCar = input("Would you like to add an optional loaner car (Enter Y for Yes or N for No): ").upper()
    if LoanCar == "":
        print("Error - Option cannot be blank - Please Re-enter Y or N.")
    elif LoanCar not in LoanCarLst:
        print("Error - Not a valid Option - Please Re-enter Y or N.")
    else:
        break
print()

#Finally enter a value to indicate if they want to pay in full or monthly (Full or Monthly or Down Pay –use a list to validate).
PayOptLst = ["Full", "Monthly", "Down Pay"]
while True:
    PayOpt = input("Would you like to pay in Full or Monthly or with Down Pay: ").title()
    if PayOpt == "":
        print("Error - Payment cannot be blank - Please Re-enter.")
    elif PayOpt not in PayOptLst:
        print("Error - Not a valid Payment Option - Please Re-enter.")
    else:
        break
print()

#If they enter Down Pay allow them to enter  the  amount  of  the  down  payment.  
if PayOpt == "Down Pay":
    DownPayAmt = int(input("Please Enter the Down Payment Amount: "))
if PayOpt == "Down Pay": 
    PayOptDSP = PayOpt
if PayOpt == "Full": 
    PayOptDSP = "Full" 
if PayOpt == "Full": 
    DownPayAmt = int("0")
if PayOpt == "Monthly": 
    PayOptDSP = "Monthly"
if PayOpt == "Monthly": 
    DownPayAmt =  int("0")
print()

#Setup Program Functions
#Claim program to enter  the  date  and  cost  of  all  previous  claims  for  the customer – press Enter to finish.  
#Add at least 2-3 claims and store the values in lists.
ClaimDateLst = []
ClaimAmtLst = []

while True:
   ClaimDate = input("Please Enter the Date (YYYY-MM-DD) of Previous Claim or Press Enter to Finish: ")
   if ClaimDate == "":
    print("Enter key pressed. Exiting...")
    break
   print()
   ClaimAmt = float(input("Please Enter the Previous Claim Amount: "))
   print()
   ClaimDateLst.append(ClaimDate)
   ClaimAmtLst.append(ClaimAmt) 
print()




#Setup Program Calculations
PhoneNumber = "(" + PhoneNumber[0:3] + ")" + PhoneNumber[3:6] + "-" + PhoneNumber[6:10]

#Insurance  premiums  are  calculated  using  a  basic  rate  of  $869.00  for  the  first  automobile,
#with  each additional automobile offered at a discount of 25%. 
BasicPremiumRate = BasicPremium
if NumCarIns > 1:
        DiscountAmt = (NumCarIns - 1) * BasicPremium * AddCarDiscountRate
        BasicPremiumRate += DiscountAmt

#If the user enters a Y for any of the options, 
#the costs are $130.00 per car for extra liability,
if ExtLiab == "Y":
    LiabCover = LiabilityCoverCost * NumCarIns
if ExtLiab == "Y":
    ExtLiabDSP = "Yes"
if ExtLiab == "N":
    ExtLiabDSP = "No"

#$86.00 per car for glass coverage,
if GlassCover == "Y":
    GlassCoverAmt = GlassCoverCost * NumCarIns
if GlassCover == "Y":
    GlassCoverDSP = "Yes"
if GlassCover == "N":
    GlassCoverDSP = "No"

#and $58.00 per car for the loaner car option.
if LoanCar == "Y":
    LoanCarAmt = LoanCarCost * NumCarIns
if LoanCar == "N":
    LoanCarAmt = 0
if LoanCar == "Y":
    LoanCarDSP = "Yes"  
if LoanCar == "N":
    LoanCarDSP = "No" 

#All these values are added together for the total extra costs.
TotalExtCosts = LiabCover + GlassCoverAmt + LoanCarAmt

#The total insurance premiumis the premium plus the total extra costs. 
TotalInsPrem = BasicPremiumRate + TotalExtCosts

#HST is calculated at 15% on the total insurancepremium,
HSTCost = TotalInsPrem * HSTRate

#and the total cost is the total insurance premium plus the HST.
TotalCost = TotalInsPrem + HSTCost

#Customers canpay for their insurance in full or in 8  monthly  payments, with  or  without  a  downpayment.
#Calculate  the  monthly  payment  by  adding  a processing  fee  of $39.99  to  the  total costand  dividing  the  total cost  by 8.
for Months in range(1,8):        
    FinFee = 39.99
    TotalPrice = TotalCost + FinFee 
    MonthPay = TotalPrice / 8

#If  the  user  entered  a  down payment, determine the monthly payment based on the total price less the downpayment with the same processing feeover the same 8 months.  
MonthDown = (TotalCost - DownPayAmt + FinFee) / 8
#The invoice date is the current date,and the firstpayment date is the first day of the next month.
FirstPayDate = datetime.datetime.now() + datetime.timedelta(30)

#Print The Receipt
#Display  all  input  and  calculated values  to the screenin  a well-designed  receipt.
#At  the  end  include  the previous claims from the lists with the following format:
print(f"")
print(f"     One Stop Insurance Company")
print(f"-----------------------------------")
print(f"")
print(f" Customer Information:")
print(f" Name:          {FirstName:>9s} {LastName:>9s}") 
print(f" Address:         {HomeAddress:>14s}")
print(f" Phone Number:        {PhoneNumber}")    
print(f" City:                   {City:>10s}")
print(f" Postal Code:                {PostalCode}")
print(f"-----------------------------------")
print(f" ")
print(f" Number of Cars Insured:         {NumCarIns:>2}")
print(f" Extra Liability Option:        {ExtLiabDSP}")
print(f" Glass Coverage Option:         {GlassCoverDSP}")
print(f" Loaner Car Option:             {LoanCarDSP}")
print(f" Payment Option:         {PayOptDSP:>10s}")
print(f" ")
print(f"-----------------------------------")
print(f" Full Payment:            {FV.FDollar2(TotalPrice):>7s}")
print(f" Monthly Payments:          {FV.FDollar2(MonthPay):>7s}")
print(f" Monthly Downpayment:       {FV.FDollar2(MonthDown):>7s}")
print(f" Down Payment Amount:     {FV.FDollar2(DownPayAmt):>7s}")
print(f" ")
print(f" Insurance Premium:       {FV.FDollar2(BasicPremiumRate):>7s}")
print(f" Total Extra Costs:         {FV.FDollar2(TotalExtCosts):>7s}")
print(f" Total Insurance Premium: {FV.FDollar2(TotalInsPrem):>7s}")
print(f" HST Costs:                 {FV.FDollar2(HSTCost):>7s}")
print(f" Total Costs:             {FV.FDollar2(TotalCost):>7s}")
print(f" ")
print(f" Current Date:            {FV.FDateM(CurrentDate)}")
print(f" First Payment Date:      {FV.FDateM(FirstPayDate)}")
print(f"")
print(f" Claim #  Claim Date       Amount")
print(f"-----------------------------------")
ClaimNum = 1
Index = 1
print()
for Date, Index in zip(ClaimDateLst, ClaimAmtLst):
 print(f"  {str(ClaimNum)}.     {Date}      {FV.FDollar2(Index):>10s}")
 ClaimNum += 1 
 Index += 1

