#car_rental.py Contails details of all the methods, funtions related to Car Rentals
from datetime import *
from datetime import datetime
global req_vehicles
global rented_time
global duration_input
global verify
hourly = 30
daily = 500
weekly = 3500
global duration
global return_count
global return_time

class renting:

     #__init__function
    def __init__(self):
        order_confirm = 0
        req_vehicles = 0
        rented_time = ''
        duration_input = 0
        verify = 'N'

     # Method to display the cars
    def cars_display(user_input):
        global CarBrands
        order_confirm = 0
        CarBrands = ['Ford', 'Nissan', 'Mazda', 'Audi', 'BMW', 'Porsche', 'Hyundai', 'Subaru', 'Cadillac', 'Fiat', 'Mercidez', 'Lexus', 'TATA', 'Volvo', 'Austin Martin']
        Availcount = len(CarBrands)
        print('\n', *CarBrands, sep='\n')
        print(f"\nList of Available cars: {Availcount}\n")
        req_vehicles = int(input("Tell us how many cars you need for rent: "))
        order_confirm = renting.sale_module(req_vehicles)


     # Method to display the remaning cars after customer ordering
    def inventory(CarBrands,order_confirm, req_vehicles):
        global modified_count
        global modified_inventory
        if order_confirm == 1:
            modified_count = len(CarBrands) - req_vehicles
            modified_inventory = CarBrands[req_vehicles : ]
            print(f'\nThe rest available cars are: {modified_count}')
            print('\n', *modified_inventory, sep = '\n')
        elif order_confirm == 2:
            restock = modified_count + req_vehicles
            restock_inventory = CarBrands[ : restock]
            print(f'\nThe Updated Inventory has : {restock} cars!')
            print('\n', *restock_inventory, sep = '\n')
        else:
            exit
              

     # Method to display details of Hour_module
    def hour_module(req_vehicles, rented_time, module = 'Hourly'):
        order_confirm = 0
        global duration
        duration = module
        print(f'The Hourly Fare for one vehicle is {hourly}$')
        print(f'Total no of cars ordered for rent: {req_vehicles} ')
        print(f'Duration selected : Hourly')
        #duration = 'Hourly'
        print(f'Ordered time : {rented_time}')
        verify = input("please confirm your order Y/N : ")
        if verify == 'Y':
            order_confirm = 1
            print("Your Order has been confirmed successfully")
            renting.inventory(CarBrands, order_confirm, req_vehicles)
        elif verify == 'N':
            exit
        else:
            print("Please enter either Y/N !")
        return order_confirm


     # Method to display details of Daily_module
    def daily_module(req_vehicles, rented_time, module = 'Daily'):
        order_confirm = 0
        global duration
        duration = module
        print(f"The Daily Rent for one vehicle is {daily}$")
        print(f'Total no of cars ordered for rent: {req_vehicles} ')
        print(f'Duration selected : Hourly')
        #duration = 'Daily'
        print(f'Ordered time : {rented_time}')
        verify = input("please confirm your order Y/N : ")
        if verify == 'Y':
            order_confirm = 1
            print("Your Order has been confirmed successfully")
            renting.inventory(CarBrands, order_confirm, req_vehicles)
        elif verify == 'N':
            exit
        else:
            print("Please enter either Y/N !")
        return order_confirm

     # Method to display details of Weekly_module
    def weekly_module(req_vehicles, rented_time, module ='Weekly'):
        order_confirm = 0
        global duration
        duration = module
        print(f"The Weekly Rent for one vehicle is {weekly}$")
        print(f'Total no of cars ordered for rent: {req_vehicles} ')
        print(f'Duration selected : Weekly')
        #duration = 'Weekly'
        print(f'Ordered time : {rented_time}')
        verify = input("please confirm your order Y/N : ")
        if verify == 'Y':
            order_confirm = 1
            print("Your Order has been confirmed successfully")
            renting.inventory(CarBrands, order_confirm, req_vehicles)
        elif verify == 'N':
            exit
        else:
            print("Please enter either Y/N !")
        return order_confirm


     # Method to display sales modules on Daily/ Hourly/ Weekly basis
    def sale_module(req_vehicles):
        x = 0
        global rented_time
        sale_type = ['1-Hourly', '2-Daily', '3-Weekly']
        print(*sale_type, sep ='\n')
        duration_input = int(input("\nPlease select the duration ( or 0 to exit): "))
        rented_time = datetime.now()
        if duration_input == 1:
            x = renting.hour_module(req_vehicles, rented_time)
        elif duration_input == 2:
            renting.daily_module(req_vehicles, rented_time)
        elif duration_input == 3:
            renting.weekly_module(req_vehicles, rented_time)
        else:
            exit
        return x


     # Method to return bill
    def generate_bill(return_count, return_time):
        global time_difference
        print('/n ============== CAR RENTALS ===========================')
        print(f'The Returning cars are: {return_count}')
        print(f'The Cars Rented at: {rented_time }')
        print(f'The Cars received at: {return_time}')
        print(f'The duration module is: {duration}')
        time_difference = return_time - rented_time
        hours_difference = time_difference.total_seconds() / 3600 # 1 hour = 3600 seconds
        if duration =='Hourly':
            print(f'\n The Bill amount is {return_count} X {hours_difference} = ',
return_count * (hours_difference * hourly))
        elif duration == 'Weekly':
            print(f'\n The Bill amount is {return_count} X {hours_difference} = ',
return_count * (hours_difference * weekly))
        elif duration == 'Daily':
            print(f'\n The Bill amount is {return_count} X {hours_difference} = ',
return_count * (hours_difference * daily))
            print("\n====================================")
            print("XX \t THANK YOU FOR CHOOSING US! \t XX \n")
            print("====================================")
            exit
class customer(renting):
     #__init__function
    def __init__(self):
        return_count = 0
        return_time = ''
                     
    def vehicle_return(user_input):
        global return_time
        order_confirm = 2
        return_count = int(input("Please enter the no of vehicles you are returning: "))
        return_time = datetime.now()
        renting.inventory(CarBrands, order_confirm, return_count)
        bill = renting.generate_bill(return_count, return_time)

