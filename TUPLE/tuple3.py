#a python progarm to sort a tuple with nested tuples.
emp=((10,'Vijay',8900.00),(20,'Nihaar',5500.75),(30,'Vanaja',8900.00),(40,'Kapoor',5000.5))
print(sorted(emp))
print(sorted(emp,reverse=True))
print(sorted(emp,key=lamdax:x[1]))
print(sorted(emp,key=lamdax:x[2]))
"""
OUTPUT:
[(10,'Vijay',8900.00),(20,'Nihaar',5500.75),(30,'Vanaja',8900.00),(40,'Kapoor',5000.5)]
[(40,'Kapoor',5000.5),(30,'Vanaja',8900.00),(20,'Nihaar',5500.75),(10,'Vijay',8900.00)]
[(40,'Kapoor',5000.5),(20,'Nihaar',5500.75),(30,'Vanaja',8900.00),(10,'Vijay',8900.00)]
[(40,'Kapoor',5000.5),(20,'Nihaar',5500.75),(30,'Vanaja',8900.00),(10,'Vijay',8900.00)]


