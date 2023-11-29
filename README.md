# QAP-4-Files-LC
Python Program(s) to be submitted for QAP 4 SD S1

Name: OneStopInsuranceCo.py

Description: The One  Stop  Insurance  Company, A program  to  enter  and  calculate  new  insurance  policy information for its customers. 

How-To-Run: Open File using Visual Studio Code and Run in the Terminal.

Author: Lianne Campbell

Date of Creation: 11/19/2023

How-To: 

Once you run the program, you will be asked to input your information,

Note: Your inputs do not require case sensitivity.

Starting with your First and Last name:

example:
Please Input Your First Name: lianne 

Please Input Your Last Name: campbell
 

Your Home Address Number and Street Name:

example:
Please Input Your Home Adress: 434 thorburn road
 
Input the name of your current City: 

example:


You will be asked to input your Province from a list provided: 

example: 
1. NL
2. PE
3. NS
4. NB
5. QC
6. ON
7. MB
8. SK
9. AB
10. BC
11. YT
12. NT
13. NU

Please Enter The Province From List Above (XX): nl

 
If you enter an incorrect option besides which is not on the list you will incur errors such as:  

example:
Please Enter The Province From List Above (XX):
Error - Province cannot be blank - Please Re-enter.
Please Enter The Province From List Above (XX): LL
Error - Not a valid Province - Please Re-enter.


Enter your Postal Code in the following format:  

example:
Please Enter Your Postal Code (X9X9X9): a1b4r1


Enter your Telephone Number in the following format:  

example:
Please Enter Your Phone Number (7097779999): 7097545430


You will need to enter the number of cars that you wish to insure: 

example:
Please Enter The Number of Cars to be Insured: 2

 
Next you can decide which extra options you would like to add on. 
If you would like to add Extra Liability up to 1,000,000 for $130.00
Please enter Y or N:

example:
Would you like to add extra liability up to $1,000,000 (Enter Y for Yes or N for No.): y
 

If you would like to add Glass Coverage for $86.00 enter Y or N: 

example: 
Would you like to add optional glass coverage (Enter Y for Yes or N for No): y
 
If you would like to add a Loaner Car for $58.00 enter Y or N: 

example:
Would you like to add an optional loaner car (Enter Y for Yes or N for No): y
 

With Y or N questions you can incur errors such as: 
 
example:
Would you like to add extra liability up to $1,000,000 (Enter Y for Yes or N for No.):
Error - Option cannot be blank - Please Re-enter Y or N.
Would you like to add extra liability up to $1,000,000 (Enter Y for Yes or N for No.): O
Error - Not a valid Option - Please Re-enter Y or N.


You can now choose which payment option you would like to select.
You must input an option from Full or Monthly or Down Pay: 

example: 
Would you like to pay in Full or Monthly or with Down Pay: down pay


Input an option that is not presented error occurs:

example: 
Would you like to pay in Full or Monthly or with Down Pay: downpay 
Error - Not a valid Payment Option - Please Re-enter


If you selected Down Pay, you will be required to enter the amount:

example:
Please Enter the Down Payment Amount: 1000 


Next an option which allows you to add as many previous claims as needed:

example:
Please Enter the Down Payment Amount: 1000

Please Enter the Date (YYYY-MM-DD) of Previous Claim or Press Enter to Finish: 1992-11-17

Please Enter the Previous Claim Amount: 1000

Please Enter the Date (YYYY-MM-DD) of Previous Claim or Press Enter to Finish: 2000-10-20

Please Enter the Previous Claim Amount: 500

Please Enter the Date (YYYY-MM-DD) of Previous Claim or Press Enter to Finish: 2023-11-20

Please Enter the Previous Claim Amount: 2000
 

Once you are finished inputting, Press the Enter key to Continue:

example:
Please Enter the Date (YYYY-MM-DD) of Previous Claim or Press Enter to Finish:
Enter key pressed. Exiting...
 

You will be presented with a printed out copy of your Recipt: 

example:

     One Stop Insurance Company
-----------------------------------

 Customer Information:
 Name:             Lianne  Campbell
 Address:         434 Thorburn Road
 Phone Number:        (709)754-5430
 City:                    St. Johns
 Postal Code:                A1B4R1
-----------------------------------

 Number of Cars Insured:          2
 Extra Liability Option:        Yes
 Glass Coverage Option:         Yes
 Loaner Car Option:             Yes
 Payment Option:           Down Pay

-----------------------------------
 Full Payment:            $1,919.38
 Monthly Payments:          $239.92
 Monthly Downpayment:       $114.92
 Down Payment Amount:     $1,000.00

 Insurance Premium:       $1,086.25
 Total Extra Costs:         $548.00
 Total Insurance Premium: $1,634.25
 HST Costs:                 $245.14
 Total Costs:             $1,879.39
 Current Date:            28-Nov-23
 First Payment Date:      28-Dec-23

 Claim #  Claim Date       Amount
-----------------------------------

  1.     1992-11-17       $1,000.00
  2.     2000-10-20         $500.00
  3.     2023-11-20       $2,000.00

       



  

