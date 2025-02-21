table = int(input("Write the table you want to print: "))
number_of_time = int(input("Enter how many times you want to print the table: "))

for i in range(table, table * number_of_time + 1, table): 
    print(table, "X", (i // table), "=", i)
