def print_data(**kwargs):
    for key,value in kwargs.items():
        print("{} is {}".format(key,value))

print_data(FirstName="Manu", SecondName="Shivasetty")
print_data(FirstName="Kushi", SecondName="Shetty", City="Bangalore")
print_data(FirstName="Deepa", SecondName="Shetty", City="Somwarpet")