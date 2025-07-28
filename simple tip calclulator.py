print("welcome to tip calculator!!!")
bill=float(input("what was the total bill?\n"))
tip=int(input("how much tip would you like to give? 10%, 12% or 15%\n"))
people=int(input("how many people would like to split the bill?\n"))
total=(tip/100)*bill+bill
print(f"total bill is: ${total}")
bill_per_person=total/people
final_amount=round(bill_per_person, 2)
print(f"bill per person is {final_amount}")