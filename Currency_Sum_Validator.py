def bill_count(amount,bills):
    if amount<=0:
        raise Exception('Amount should not be negative or zero')
        #raises Exception  if the amount or bills less than or equal to zero
    temp=amount
    total2=0
    sum=0
    while(temp!=0):
        if(bills!=[]):
            max1=max(bills)
            r=int(temp//max1)
            sum=sum+r
            total2=total2+r*max1#total2 is calculated to check if it equals the amount or not
            temp=temp%max1
            bills=bills[0:-1]
        else:
            print("Cannot Process")
            break
    
    if(total2!=amount):
        raise Exception('The Given Denominations does not match the value of the amount')
        #raises an exception if the values in bills are greater than the amount or if the amount is not matched with the total2
    else:
        print("The Minimun no of bills required is:", sum)


amount=int(input("Enter the amount you have:"))
standardIndianCurrency=[1,2,5,10,20,50,100,200,500,2000]
bills=[int(k) for k in input().split()] #Takes inputs seperated by spaces in a single line
bills.sort()
SIC=set(standardIndianCurrency)         #convert standartIndianCurrency to a set
bills1=set(bills)
bills2=list(bills1)
bills2.sort()
for x in bills:
    if x<=0:
        print("You have entered a negative valued bill. Please CHECK.")
        break
if(bills1.issubset(SIC) and bills==bills2):
    bill_count(amount,bills)
else:
    print("Bills are of not Standard Indian Currency or You have entered similar bills twice or more.")