#One Stop Insurance Company 
#Lianne Campbell
#11/19/2023
#QAP 4 Project 1


#Import Required Libraries
import datetime

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



#Setup User Inputs
#The user will input the customer’s
#first and last name, 
FirstName = input("Please Input Your First Name: ").title
LastName = input("Please Input Your Last Name: ").title
#address, 
HomeAddress = input("Please Input Your Home Adress: ")
#city,
City = input("Please Input Your City: ").title
#province(validate using a list to make sure the province is valid), 
#postal code,and 
#phone number. 
PhoneNumber = input("Please Enter Your Phone Number: ")
#They will also enter 
#the number of cars being insured,
#and  options  for  extra  liability  up  to  $1,000,000  (enter  Y  for  Yes  or  N  for  No), 
#optional  glass coverage (Y or N),
#and optional loaner car (Y or N).
#Finally enter a value to indicate if they want to pay in full or monthly (Full or Monthly or Down Pay –use a list to validate).
#If they enter Down Pay allow them to enter  the  amount  of  the  down  payment.  
#Finally  enter  the  date  and  cost  of  all  previous  claims  for  the customer 
CurrentDate = datetime.datetime.now()
#–press Enter to finish.  
#Convert the first and last name, the city, and the payment Method to title case and the Y/N values upper case. 
#Add at least 2-3 claims and store the values in lists.

#Setup Program Calculations
#Insurance  premiums  are  calculated  using  a  basic  rate  of  $869.00  for  the  first  automobile,
#with  each additional automobile offered at a discount of 25%. 
InsurePremRate = BasicPremium + (BasicPremium / AddCarDiscountRate )
#If the user enters a Y for any of the options, 
#the costs are $130.00 per car for extra liability, 
#$86.00 per car for glass coverage,
#and $58.00 per car for the loaner car option.
#All these values are added together for the total extra costs.
#The total insurance premiumis the premium plus the total extra costs. 
#HST is calculated at 15% on the total insurancepremium,
#and the total cost is the total insurance premium plus the HST.
#Customers canpay for their insurance in full or in 8  monthly  payments, with  or  without  a  downpayment.
#Calculate  the  monthly  payment  by  adding  a processing  fee  of $39.99  to  the  total costand  dividing  the  total cost  by 8.
#If  the  user  entered  a  down payment, determine the monthly payment based on the total price less the downpayment with the same processing feeover the same 8 months.  
#The invoice date is the current date,and the firstpayment date is the first day of the next month.
FirstPayDate = datetime.datetime.now() + datetime.timedelta(30)

#Setup Program Functions


#Start The Main Program


#Print The Receipt
#Display  all  input  and  calculated values  to the screenin  a well-designed  receipt.
#At  the  end  include  the previous claims from the lists with the following format:
print(f" Customer Name: {FirstName} {LastName}    Customer Address: {HomeAddress}")
print(f" Customer Phone Number: {PhoneNumber}     Customer City: {City}")
print(f" Current Date: {CurrentDate}     First Payment Date: {FirstPayDate}")
print(f" Claim #  Claim Date   Amount")
print(f"--------------------------------")
print(f" 1.YYYY-MM-DD    $##,###.##")
print(f" 2.YYYY-MM-DD    $##,###.##")
print(f" 3.YYYY-MM-DD    $##,###.##")