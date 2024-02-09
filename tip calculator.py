x = "Bill"
y = "Total"
z = "Tip"
total = 0
tip = 0

x = float(input("How much is your bill?"))

Service = input("How was our service?")
if Service == ('Bad'):
    print ('0%')
    tip = x * 0
elif Service == ('Okay'):
    print ('15%')
    tip = x * 0.15
elif Service == ('Good'):
    print ('20%')
    tip = x * 0.20
elif Service == ('Great'):
    print ('25%')
    tip = x * 0.25


total = x+tip
print ('Here is your total')
print (total)
