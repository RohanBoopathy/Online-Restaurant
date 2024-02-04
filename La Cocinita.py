#IMPORTING THE MODULES
from collections import namedtuple
from tabulate import tabulate
import csv
import random

#DEFINING MENU ITEMS AND SUBCATEGORIES IN A LIST
MenuItems = ['Pizza', 'Pasta', 'Tacos', 'Lasagna', 'Sides', 'Beverages']
Pizzas = ['Mozzarella Pizza', 'Vegetables Pizza', 'Neapolitan Pizza', 'Hawaiian Pizza', 'Chicken Ranch Pizza']
Pasta = ['Baked Ziti', 'Fettuccine Alfredo', 'Ravioli', 'Pesto Penne Pasta', 'Spaghetti Carbonara']
Tacos = ['Soft Taco', 'Spicy Potato Taco', 'Gourmet Taco', 'Le Roi Taco', 'Nacho Cheese Taco']
Lasagna = ['Plain Lasagna', '4-Cheese Lasagna', 'Meatball Lasagna', 'Shrimp and Scallop Lasagna']
Sides = ['Garlic Bread', 'Calzone', 'Flatbread']
Beverages = ['Coke', 'Diet Coke', 'Sprite', 'Iced Tea', 'Chocolate Milk', 'Strawberry Banana Smoothie',
             'Mango Pineapple Smoothie', 'Bottled Water']
PizzaToppings = ['Olives', 'Onions', 'Mushrooms', 'Pepperoni', 'Jalapeno', 'Pineapple', 'Cheese']

#DEFINING ITEM PRICES IN LISTS TO PRINT THEM DURING ORDERS
RegPizzaPrice = [19.99, 20.49, 22.49, 25.99, 15.99]
MedPizzaPrice = [21.99, 22.49, 24.49, 27.99, 17.99]
LrgPizzaPrice = [23.99, 24.49, 26.49, 29.99, 19.99]
PizzaToppings_Price = [1.45, 0.99, 1.25, 2.25, 1.25, 1.75, 0.99]
Pasta_Price = [9.95, 14.95, 12.99, 13.99, 15.99]
Tacos_Price = [2.98, 1.99, 4.99, 3.89, 3.95]
Lasagna_Price = [12.95, 14.50, 16.99, 17.99]
Sides_Price = [9.75, 11.49, 7.99]
Beverages_Price = [3.99, 3.99, 3.99, 3.99, 4.99, 5.99, 5.99, 1.99]

#NAMEDTUPLES TO DEFINE AND ADD PRICES TO THE FINAL TOTAL
Size_Price_Pizza = namedtuple('Pizza', ['Regular', 'Medium', 'Large'])
VegPizza = Size_Price_Pizza(RegPizzaPrice[0], MedPizzaPrice[0], LrgPizzaPrice[0])
NeapoPizza = Size_Price_Pizza(RegPizzaPrice[1], MedPizzaPrice[1], LrgPizzaPrice[1])
HawaiiPizza = Size_Price_Pizza(RegPizzaPrice[2], MedPizzaPrice[2], LrgPizzaPrice[2])
CRPizza = Size_Price_Pizza(RegPizzaPrice[3], MedPizzaPrice[3], LrgPizzaPrice[3])
MozPizza = Size_Price_Pizza(RegPizzaPrice[4], MedPizzaPrice[4], LrgPizzaPrice[4])

Price_Pasta = namedtuple('Pasta', ['Price'])
BakedZiti = Price_Pasta(Pasta_Price[0])
FettAlfredo = Price_Pasta(Pasta_Price[1])
Ravioli = Price_Pasta(Pasta_Price[2])
PestoPasta = Price_Pasta(Pasta_Price[3])
SpagCarbonara = Price_Pasta(Pasta_Price[4])

Price_Tacos = namedtuple('Tacos', ['Price'])
SoftTaco = Price_Tacos(Tacos_Price[0])
SpicyTaco = Price_Tacos(Tacos_Price[1])
GourmetTaco = Price_Tacos(Tacos_Price[2])
LeRoiTaco = Price_Tacos(Tacos_Price[3])
NachoTaco = Price_Tacos(Tacos_Price[4])

Price_Lasagna = namedtuple('Lasagna', ['Price'])
PlainLasagna = Price_Lasagna(Lasagna_Price[0])
CheeseLasagna = Price_Lasagna(Lasagna_Price[1])
MeatballLasagna = Price_Lasagna(Lasagna_Price[2])
ShrimpScallopLasagna = Price_Lasagna(Lasagna_Price[3])

Price_Sides = namedtuple('Sides', ['Price'])
Garlic_Bread = Price_Sides(Sides_Price[0])
Calzone = Price_Sides(Sides_Price[1])
Flatbread = Price_Sides(Sides_Price[2])

Price_Beverages = namedtuple('Beverages', ['Price'])
Coke = Price_Beverages(Beverages_Price[0])
DietCoke = Price_Beverages(Beverages_Price[1])
Sprite = Price_Beverages(Beverages_Price[2])
IcedTea = Price_Beverages(Beverages_Price[3])
ChocMilk = Price_Beverages(Beverages_Price[4])
StrBanSmoothie = Price_Beverages(Beverages_Price[5])
MangPineSmoothie = Price_Beverages(Beverages_Price[6])
BottleWater = Price_Beverages(Beverages_Price[7])

Price_Toppings = namedtuple('Toppings', ['Price'])
Olives = Price_Toppings(PizzaToppings_Price[0])
Onions = Price_Toppings(PizzaToppings_Price[1])
Mushrooms = Price_Toppings(PizzaToppings_Price[2])
Pepperoni = Price_Toppings(PizzaToppings_Price[3])
Jalapeno = Price_Toppings(PizzaToppings_Price[4])
Pineapple = Price_Toppings(PizzaToppings_Price[5])
Cheese = Price_Toppings(PizzaToppings_Price[6])

#RNG OF THE SERVICE TIME OF AN ORDER
ServiceTime = random.randrange(10, 25)

# PREPARING THE BILL FOR THE NEXT ORDER
f = open('Bill.csv', 'w', newline='')
f.truncate()
f.close()


# DISPLAYING THE FINAL BILL
def Bill():
    f = open('Bill.csv', 'r')
    ReadBill = csv.reader(f)

    rec = []
    for i in ReadBill:
        rec.append(i)

    f.close()
    print(tabulate(rec, headers=['ITEM NAME', 'SIZE', 'TOPPINGS', 'PRICE (USD)'], tablefmt="rounded_outline"))


# MAIN LOOP
OrderMore = 0
while OrderMore == 0:
    
    #FUNTIONS FOR THE ADMIN SECTION
    
    def ReadEmployee():
        f = open('EmployeesLC.csv', 'r')
        EmployeesDBList = []
        EmployeesDBList = csv.reader(f)
        print(tabulate(EmployeesDBList, tablefmt='simple_grid'))
        f.close()


    def InsertEmployee():
        f = open('EmployeesLC.csv', 'a', newline='')
        WriteEmployees = csv.writer(f)
        list = []
        print('*****INSERT A NEW RECORD*****')
        ID = input('Enter Employee ID: ')
        LastName = input('Enter Last Name: ')
        Firstname = input('Enter First Name: ')
        Position = input('Enter Position of Employee: ')
        Salary = input('Enter Salary: ')
        DateOfJoining = input('Enter Date of Joining: ')

        print('\n*****PERSONAL INFORMATION*****\n')
        ContactNumber = input('Enter Contact Number: ')
        Address = input('Enter Address: ')
        DateOfBirth = input('Enter Date of Birth: ')
        IDProof = input('What Type Of ID Provided?: ')
        list = [ID, LastName, Firstname, Position, Salary, DateOfJoining, ContactNumber, Address, DateOfBirth, IDProof]
        WriteEmployees.writerow(list)
        print('*****NEW DATA HAS BEEN INSERTED SUCCESSFULLY*****\n')
        f.close()


    def DeleteEmployee():
        UpdatedList = []
        with open("EmployeesLC.csv", newline="") as f:
            ReadEmployees = csv.reader(f)
            ID_Delete = input("Enter ID to Delete the Employee Record: ")

            for row in ReadEmployees:

                if row[0] != ID_Delete:
                    UpdatedList.append(row)
            print(UpdatedList)
            UpdateFile(UpdatedList)


    def UpdateFile(updatedlist):
        with open("EmployeesLC.csv", "w", newline="") as f:
            WriteEmployees = csv.writer(f)
            WriteEmployees.writerows(updatedlist)
            print("Employee Record has been Deleted!")
        ReadEmployee()


    def UpdateEmployee():
        updatedlist = []
        temporarylist = []

        with open("EmployeesLC.csv", newline="") as f:
            UpdateEmployees = list(csv.reader(f))
            print("*****UPDATE AN EMPLOYEE'S RECORD*****")
            ReadEmployee()
            EmpID = input("Enter an Employee's ID to Update their Record: ")
            print('''******************************
    (1) - UPDATE LAST NAME
    (2) - UPDATE FIRST NAME
    (3) - UPDATE POSITION
    (4) - UPDATE SALARY
    (5) - UPDATE DATE OF JOINING
    (6) - UPDATE CONTACT NUMBER
    (7) - UPDATE ADDRESS
    (8) - UPDATE DATE OF BIRTH
    (9) - UPDATE ID PROOF
    ******************************''')
            UpdationChoice = int(input('CHOOSE AN OPTION: '))

            temporarylist = UpdateEmployees

            for row in UpdateEmployees:
                for field in row:
                    if field == EmpID:
                        updatedlist.append(row)
                        newrecord = input("Enter the Update: ")
                        updatedlist[0][UpdationChoice] = newrecord

            updatepassword(updatedlist, temporarylist)


    def updatepassword(updatedlist, temporarylist):
        for index, row in enumerate(temporarylist):
            for field in row:
                if field == updatedlist[0]:
                    temporarylist[index] = updatedlist

        with open("EmployeesLC.csv", "w", newline="") as f:
            Writer = csv.writer(f)
            Writer.writerows(temporarylist)
            print("Employee Record has been Updated Successfully!\n")


    def AdminPage():
        while True:
            print('*****MANAGE RECORDS OF EMPLOYEES*****')
            print('Add an Employee Record - (1)')
            print('Update an Employee Record - (2)')
            print('Delete an Employee Record - (3)')
            print('View Employees Database - (4)')
            print('Exit - (0)')
            print('-------------------------------------')

            AEChoice = int(input('Enter an Option: '))

            if AEChoice == 1:
                InsertEmployee()

            elif AEChoice == 2:
                UpdateEmployee()

            elif AEChoice == 3:
                DeleteEmployee()

            elif AEChoice == 4:
                ReadEmployee()

            elif AEChoice == 0:
                print('Exit')
                break


            else:
                print('You Have Entered an Invalid Option')

    Customer = 0

    OrderItem = 0
    print(tabulate(zip([1, 2, 3, 4, 5, 6], MenuItems),
                   headers=["*** Welcome to La Cocinita! *** \n  ----- HERE'S OUR MENU -----"],
                   tablefmt="rounded_grid"))

    Welcome_Input = input('What item would you like?: ')
    

    # P_I_Z_Z_A:

    if Welcome_Input == 'Pizza':
        test = int(input('How many Pizzas would you like to have?: '))
        while OrderItem < test:
            print(tabulate(zip([1, 2, 3, 4, 5], Pizzas), headers=['*** La Cocinita - PIZZAS ***'],
                           tablefmt='rounded_outline'))
            Pizza_Type = input('What kind of Pizza would you like?: ')

            if Pizza_Type == 'Vegetables Pizza':
                print(tabulate([['Regular', VegPizza.Regular], ['Medium', VegPizza.Medium], ['Large', VegPizza.Large]],
                               headers=['VEGETABLES PIZZA SIZES', 'PRICE'], tablefmt='simple_grid'))
                Pizza_Size = input(f"What Size of {Pizza_Type} would you like?: ")
                if Pizza_Size == 'Regular':
                    Customer += VegPizza.Regular
                elif Pizza_Size == 'Medium':
                    Customer += VegPizza.Medium
                elif Pizza_Size == 'Large':
                    Customer += VegPizza.Large
                else:
                    print("We don't serve Pizzas of that size :(")

                Toppings_Choice = input('Would you like to add Toppings to your Vegetables Pizza?: (Yes/No) ')
                if Toppings_Choice == 'Yes':
                    print(tabulate(zip(PizzaToppings, PizzaToppings_Price), headers=['*** La Cocinita - Toppings ***', 'Prices'],
                                   tablefmt='simple_grid'))
                    Toppings_Type = input('What Topping would you like to add?: ')
                    if Toppings_Type == 'Olives':

                        print(f"You have added Olives for +${Olives.Price}")
                        Customer += Olives.Price
                    elif Toppings_Type == 'Onions':
                        print(f"You have added Onions for +${Onions.Price}")
                        Customer += Onions.Price
                    elif Toppings_Type == 'Mushrooms':
                        print(f"You have added Mushrooms for +${Mushrooms.Price}")
                        Customer += Mushrooms.Price
                    elif Toppings_Type == 'Pepperoni':
                        print(f"You have added Pepperoni for +${Pepperoni.Price}")
                        Customer += Pepperoni.Price
                    elif Toppings_Type == 'Jalapeno':
                        print(f"You have added Jalapeno for +${Jalapeno.Price}")
                        Customer += Jalapeno.Price
                    elif Toppings_Type == 'Pineapple':
                        print(f"You have added Pineapple for +${Pineapple.Price}")
                        Customer += Pineapple.Price
                    elif Toppings_Type == 'Cheese':
                        print(f"You have added Cheese for +${Cheese.Price}")
                        Customer += Cheese.Price
                    else:
                        print("We don't have that topping on the menu :(")
                elif Toppings_Choice == 'No':
                    Toppings_Type = 'NONE'


            elif Pizza_Type == 'Neapolitan Pizza':
                print(tabulate(
                    [['Regular', NeapoPizza.Regular], ['Medium', NeapoPizza.Medium], ['Large', NeapoPizza.Large]],
                    headers=['NEAPOLITAN PIZZA SIZES', 'PRICE'], tablefmt='simple_grid'))
                Pizza_Size = input(f"What Size of {Pizza_Type} would you like?: ")
                if Pizza_Size == 'Regular':
                    Customer += NeapoPizza.Regular
                elif Pizza_Size == 'Medium':
                    Customer += NeapoPizza.Medium
                elif Pizza_Size == 'Large':
                    Customer += NeapoPizza.Large
                else:
                    print("We don't serve Pizzas of that size :(")

                Toppings_Choice = input('Would you like to add Toppings to your Neapolitan Pizza?: (Yes/No) ')
                if Toppings_Choice == 'Yes':
                    print(tabulate(zip(PizzaToppings, PizzaToppings_Price), headers=['*** La Cocinita - Toppings ***', 'Prices'],
                                   tablefmt='simple_grid'))
                    Toppings_Type = input('What Topping would you like to add?: ')
                    if Toppings_Type == 'Olives':
                        print(f"You have added Olives for +${Olives.Price}")
                        Customer += Olives.Price
                    elif Toppings_Type == 'Onions':
                        print(f"You have added Onions for +${Onions.Price}")
                        Customer += Onions.Price
                    elif Toppings_Type == 'Mushrooms':
                        print(f"You have added Mushrooms for +${Mushrooms.Price}")
                        Customer += Mushrooms.Price
                    elif Toppings_Type == 'Pepperoni':
                        print(f"You have added Pepperoni for +${Pepperoni.Price}")
                        Customer += Pepperoni.Price
                    elif Toppings_Type == 'Jalapeno':
                        print(f"You have added Jalapeno for +${Jalapeno.Price}")
                        Customer += Jalapeno.Price
                    elif Toppings_Type == 'Pineapple':
                        print(f"You have added Pineapple for +${Pineapple.Price}")
                        Customer += Pineapple.Price
                    elif Toppings_Type == 'Cheese':
                        print(f"You have added Cheese for +${Cheese.Price}")
                        Customer += Cheese.Price
                    else:
                        print("We don't have that topping on the menu :(")
                elif Toppings_Choice == 'No':
                    Toppings_Type = 'NONE'

            elif Pizza_Type == 'Hawaiian Pizza':
                print(tabulate(
                    [['Regular', HawaiiPizza.Regular], ['Medium', HawaiiPizza.Medium], ['Large', HawaiiPizza.Large]],
                    headers=['HAWAIIAN PIZZA SIZES', 'PRICE'], tablefmt='simple_grid'))
                Pizza_Size = input(f"What Size of {Pizza_Type} would you like?: ")
                if Pizza_Size == 'Regular':
                    Customer += HawaiiPizza.Regular
                elif Pizza_Size == 'Medium':
                    Customer += HawaiiPizza.Medium
                elif Pizza_Size == 'Large':
                    Customer += HawaiiPizza.Large
                else:
                    print("We don't serve Pizzas of that size :(")

                Toppings_Choice = input('Would you like to add Toppings to your Hawaiian Pizza?: (Yes/No) ')
                if Toppings_Choice == 'Yes':
                    print(tabulate(zip(PizzaToppings, PizzaToppings_Price), headers=['*** La Cocinita - Toppings ***', 'Prices'],
                                   tablefmt='simple_grid'))
                    Toppings_Type = input('What Topping would you like to add?: ')
                    if Toppings_Type == 'Olives':
                        print(f"You have added Olives for +${Olives.Price}")
                        Customer += Olives.Price
                    elif Toppings_Type == 'Onions':
                        print(f"You have added Onions for +${Onions.Price}")
                        Customer += Onions.Price
                    elif Toppings_Type == 'Mushrooms':
                        print(f"You have added Mushrooms for +${Mushrooms.Price}")
                        Customer += Mushrooms.Price
                    elif Toppings_Type == 'Pepperoni':
                        print(f"You have added Pepperoni for +${Pepperoni.Price}")
                        Customer += Pepperoni.Price
                    elif Toppings_Type == 'Jalapeno':
                        print(f"You have added Jalapeno for +${Jalapeno.Price}")
                        Customer += Jalapeno.Price
                    elif Toppings_Type == 'Pineapple':
                        print(f"You have added Pineapple for +${Pineapple.Price}")
                        Customer += Pineapple.Price
                    elif Toppings_Type == 'Cheese':
                        print(f"You have added Cheese for +${Cheese.Price}")
                        Customer += Cheese.Price
                    else:
                        print("We don't have that topping on the menu :(")
                elif Toppings_Choice == 'No':
                    Toppings_Type = 'NONE'


            elif Pizza_Type == 'Chicken Ranch Pizza':
                print(tabulate([['Regular', CRPizza.Regular], ['Medium', CRPizza.Medium], ['Large', CRPizza.Large]],
                               headers=['CHICKEN RANCH PIZZA SIZES', 'PRICE'], tablefmt='simple_grid'))
                Pizza_Size = input(f"What Size of {Pizza_Type} would you like?: ")
                if Pizza_Size == 'Regular':
                    Customer += CRPizza.Regular
                elif Pizza_Size == 'Medium':
                    Customer += CRPizza.Medium
                elif Pizza_Size == 'Large':
                    Customer += CRPizza.Large
                else:
                    print("We don't serve Pizzas of that size :(")

                Toppings_Choice = input('Would you like to add Toppings to your Chicken Ranch Pizza?: (Yes/No) ')
                if Toppings_Choice == 'Yes':
                    print(tabulate(zip(PizzaToppings, PizzaToppings_Price), headers=['*** La Cocinita - Toppings ***', 'Price'],
                                   tablefmt='simple_grid'))
                    Toppings_Type = input('What Topping would you like to add?: ')
                    if Toppings_Type == 'Olives':
                        print(f"You have added Olives for +${Olives.Price}")
                        Customer += Olives.Price
                    elif Toppings_Type == 'Onions':
                        print(f"You have added Onions for +${Onions.Price}")
                        Customer += Onions.Price
                    elif Toppings_Type == 'Mushrooms':
                        print(f"You have added Mushrooms for +${Mushrooms.Price}")
                        Customer += Mushrooms.Price
                    elif Toppings_Type == 'Pepperoni':
                        print(f"You have added Pepperoni for +${Pepperoni.Price}")
                        Customer += Pepperoni.Price
                    elif Toppings_Type == 'Jalapeno':
                        print(f"You have added Jalapeno for +${Jalapeno.Price}")
                        Customer += Jalapeno.Price
                    elif Toppings_Type == 'Pineapple':
                        print(f"You have added Pineapple for +${Pineapple.Price}")
                        Customer += Pineapple.Price
                    elif Toppings_Type == 'Cheese':
                        print(f"You have added Cheese for +${Cheese.Price}")
                        Customer += Cheese.Price
                    else:
                        print("We don't have that topping on the menu :(")
                elif Toppings_Choice == 'No':
                    Toppings_Type = 'NONE'

            elif Pizza_Type == 'Mozzarella Pizza':
                print(tabulate([['Regular', MozPizza.Regular], ['Medium', MozPizza.Medium], ['Large', MozPizza.Large]],
                               headers=['MOZZARELLA PIZZA SIZES', 'PRICE'], tablefmt='simple_grid'))
                Pizza_Size = input(f"What Size of {Pizza_Type} would you like?: ")
                if Pizza_Size == 'Regular':
                    Customer += MozPizza.Regular
                elif Pizza_Size == 'Medium':
                    Customer += MozPizza.Medium
                elif Pizza_Size == 'Large':
                    Customer += MozPizza.Large
                else:
                    print("We don't serve Pizzas of that size :(")

                Toppings_Choice = input('Would you like to add Toppings to your Mozzarella Pizza?: (Yes/No) ')
                if Toppings_Choice == 'Yes':
                    print(tabulate(zip(PizzaToppings, PizzaToppings_Price), headers=['*** La Cocinita - Toppings ***', 'Price'],
                                   tablefmt='simple_grid'))
                    Toppings_Type = input('What Topping would you like to add?: ')
                    if Toppings_Type == 'Olives':
                        print(f"You have added Olives for +${Olives.Price}")
                        Customer += Olives.Price
                    elif Toppings_Type == 'Onions':
                        print(f"You have added Onions for +${Onions.Price}")
                        Customer += Onions.Price
                    elif Toppings_Type == 'Mushrooms':
                        print(f"You have added Mushrooms for +${Mushrooms.Price}")
                        Customer += Mushrooms.Price
                    elif Toppings_Type == 'Pepperoni':
                        print(f"You have added Pepperoni for +${Pepperoni.Price}")
                        Customer += Pepperoni.Price
                    elif Toppings_Type == 'Jalapeno':
                        print(f"You have added Jalapeno for +${Jalapeno.Price}")
                        Customer += Jalapeno.Price
                    elif Toppings_Type == 'Pineapple':
                        print(f"You have added Pineapple for +${Pineapple.Price}")
                        Customer += Pineapple.Price
                    elif Toppings_Type == 'Cheese':
                        print(f"You have added Cheese for +${Cheese.Price}")
                        Customer += Cheese.Price
                    else:
                        print("We don't have that topping on the menu :(")
                elif Toppings_Choice == 'No':
                    Toppings_Type = 'NONE'


            def Pizza_write_Bill():
                f = open('Bill.csv', 'a', newline='')
                PizzaWriter = csv.writer(f)
                InputData = [Pizza_Type, Pizza_Size, Toppings_Type, Customer]
                PizzaWriter.writerow(InputData)
                f.close()


            Pizza_write_Bill()
            Customer *= 0

            OrderItem += 1


    # P_A_S_T_A

    elif Welcome_Input == 'Pasta':

        test3 = int(input('How many Pastas would you like?: '))
        while OrderItem < test3:
            print(tabulate(zip([1, 2, 3, 4, 5], Pasta, Pasta_Price), headers=['*** LA COCINITA - PASTAS ***', 'PRICES'],
                           tablefmt='rounded_outline'))
            Pasta_Type = input('What kind of Pasta would you like?: ')
            if Pasta_Type == 'Baked Ziti':
                Customer += BakedZiti.Price
            elif Pasta_Type == 'Fettucine Alfredo':
                Customer += FettAlfredo.Price
            elif Pasta_Type == 'Ravioli':
                Customer += Ravioli.Price
            elif Pasta_Type == 'Pesto Penne Pasta':
                Customer += PestoPasta.Price
            elif Pasta_Type == 'Spaghetti Carbonara':
                Customer += SpagCarbonara.Price
            else:
                print("We don't have that Pasta on our Menu :(")


            def Pasta_write_Bill():
                f = open('Bill.csv', 'a', newline='')
                PastaWriter = csv.writer(f)
                InputData = [Pasta_Type, 'NONE', 'NONE', Customer]
                PastaWriter.writerow(InputData)
                f.close()


            Pasta_write_Bill()
            Customer *= 0
            OrderItem += 1


    # T_A_C_O_S

    elif Welcome_Input == 'Tacos':
        TacosQuantity = int(input('How many Tacos would you like?: '))
        while OrderItem < TacosQuantity:
            print(tabulate(zip([1, 2, 3, 4, 5], Tacos, Tacos_Price), headers=['*** La Cocinita - TACOS ***', 'PRICES'],
                           tablefmt='rounded_outline'))
            Tacos_Type = input('What kind of Taco would you like?: ')
            if Tacos_Type == 'Soft Taco':
                Customer += SoftTaco.Price
            elif Tacos_Type == 'Spicy Potato Taco':
                Customer += SpicyTaco.Price
            elif Tacos_Type == 'Gourmet Taco':
                Customer += GourmetTaco.Price
            elif Tacos_Type == 'Le Roi Taco':
                Customer += LeRoiTaco.Price
            elif Tacos_Type == 'Nacho Cheese Taco':
                Customer += NachoTaco.Price
            else:
                print("We don't have that Taco on the menu :(")


            def Tacos_write_Bill():
                f = open('Bill.csv', 'a', newline='')
                TacosWriter = csv.writer(f)
                InputData = [Tacos_Type, 'NONE', 'NONE', Customer]
                TacosWriter.writerow(InputData)
                f.close()


            Tacos_write_Bill()
            Customer *= 0
            OrderItem += 1


    # L_A_S_A_G_N_A:

    elif Welcome_Input == 'Lasagna':
        LasagnaQuantity = int(input('How many Lasagnas would you like?: '))
        while OrderItem < LasagnaQuantity:
            print(
                tabulate(zip([1, 2, 3, 4], Lasagna, Lasagna_Price), headers=['*** LA COCINITA - LASAGNA ***', 'PRICES'],
                         tablefmt='rounded_outline'))
            Lasagna_Type = input('What type of Lasagna would you like?: ')
            if Lasagna_Type == 'Plain Lasagna':
                Customer += PlainLasagna.Price
            elif Lasagna_Type == '4-Cheese Lasagna':
                Customer += CheeseLasagna.Price
            elif Lasagna_Type == 'Meatball Lasagna':
                Customer += MeatballLasagna.Price
            elif Lasagna_Type == 'Shrimp and Scallop Lasagna':
                Customer += ShrimpScallopLasagna.Price
            else:
                print("Sorry, we don't serve that Lasagna here :(")


            def Lasagna_write_Bill():
                f = open('Bill.csv', 'a', newline='')
                LasagnaWriter = csv.writer(f)
                InputData = [Lasagna_Type, 'NONE', 'NONE', Customer]
                LasagnaWriter.writerow(InputData)
                f.close()


            Lasagna_write_Bill()
            Customer *= 0
            OrderItem += 1
            

    # S_I_D_E_S:

    elif Welcome_Input == 'Sides':
        SidesQuantity = int(input('How many Sides would you like to have?: '))
        while OrderItem < SidesQuantity:
            print(tabulate(zip([1, 2, 3], Sides, Sides_Price), headers=['*** LA COCINITA - SIDES ***', 'PRICES'],
                           tablefmt='rounded_outline'))
            Sides_Type = input('What Sides would you like?: ')
            if Sides_Type == 'Garlic Bread':
                Customer += Garlic_Bread.Price
            elif Sides_Type == 'Calzone':
                Customer += Calzone.Price
            elif Sides_Type == 'Flatbread':
                Customer += Flatbread.Price
            else:
                print("Sorry, we don't serve that type of Side here :(")


            def Sides_write_Bill():
                f = open('Bill.csv', 'a', newline='')
                SidesWriter = csv.writer(f)
                InputData = [Sides_Type, 'NONE', 'NONE', Customer]
                SidesWriter.writerow(InputData)
                f.close()


            Sides_write_Bill()
            Customer *= 0
            OrderItem += 1


    # B_E_V_E_R_A_G_E_S:

    elif Welcome_Input == 'Beverages':
        BeveragesQuantity = int(input('How many Beverages would you like to have?: '))
        while OrderItem < BeveragesQuantity:
            print(tabulate(zip([1, 2, 3, 4, 5, 6, 7, 8], Beverages, Beverages_Price),
                           headers=['*** LA COCINITA - BEVERAGES ***', 'PRICES'], tablefmt='rounded_outline'))
            Beverages_Type = input('What Beverage would you like to have?: ')
            if Beverages_Type == 'Coke' or '1':
                Customer += Coke.Price
            elif Beverages_Type == 'Diet Coke':
                Customer += DietCoke.Price
            elif Beverages_Type == 'Sprite':
                Customer += Sprite.Price
            elif Beverages_Type == 'Iced Tea':
                Customer += IcedTea.Price
            elif Beverages_Type == 'Chocolate Milk':
                Customer += ChocMilk.Price
            elif Beverages_Type == 'Strawberry Banana Smoothie':
                Customer += StrBanSmoothie.Price
            elif Beverages_Type == 'Mango Pineapple Smoothie':
                Customer += MangPineSmoothie.Price
            elif Beverages_Type == 'Bottled Water':
                Customer += BottleWater.Price
            else:
                print()


            def Beverages_write_Bill():
                f = open('Bill.csv', 'a', newline='')
                BeveragesWriter = csv.writer(f)
                InputData = [Beverages_Type, 'NONE', 'NONE', Customer]
                BeveragesWriter.writerow(InputData)
                f.close()


            Beverages_write_Bill()
            Customer *= 0
            OrderItem += 1

            

    #ACCESSING THE ADMIN SECTION:

    elif Welcome_Input == '****':
        print('\n*****ADMIN ACCESS LOG IN PAGE*****')
        Incorrect_Password = 0
        while Incorrect_Password < 3:
            Username = input('Enter username: ')
            Password = input('Enter password: ')
            if Username == 'Coci_Admin' and Password == '260318':
                print('Access granted\n')
                AdminPage()
                break
            else:
                print('Access denied. Try again.')
                Incorrect_Password += 1
        else:
            print('Invalid')
        break



    def write():
        f = open('Bill.csv', 'a', newline='')
        WriteBill = csv.writer(f)
        Total = []
        f = open('Bill.csv', 'r', newline='')
        BillReader = csv.reader(f)
        for row in BillReader:
            Total.append(float(row[3]))
        Total2 = ['TOTAL', '', '', sum(Total)]
        WriteBill.writerow(Total2)
        f.close()
        f.close()


    # MAIN LOOP TO ORDER AGAIN:
    OrderAgain = input('Would you like to order another item?: (Yes/No)')  
    if OrderAgain == 'Yes':
        OrderMore *= 0
    else:
        OrderMore += 1
        write()
        Bill()
        print(f'''Thank you for ordering at La Cocinita!
Your service time will be {ServiceTime} minutes. Stay put! :)''')


########################################################################################################################