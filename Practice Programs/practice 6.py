#AIM:write a python script to calculate electricity bill based on following slab rates
consumption units            rate(in rupees/unit)
  0-100                            4
  101-150                          4.6
  151-200                          5.2
  201-300                          6.3
  above300                         8
"""
ou=imt(input("enter the old units value"))
nu=int(input("enter the new units value"))
if units <=100 and units >-1:
      amount1=units*4
      print(amount1)
elif units <=150 and units >100:
      amount2=units*4.6
      print(amount2)
elif units <=200 and >150:
      amount3=units*5.2
      print(amount3)
elif units <=300 and >200:
      amount4=units*6.3
      print(amount4)
elif units >=300:
      amount5=units*8
      print(amount5)
print("the amount to be paid for"'units'"units")
print("thank you")


"""
INPUT:
enter the old units value:100
enter the new units value:150
OUTPUT:
200
the amount to to be paid for 50 units
thank you

      
