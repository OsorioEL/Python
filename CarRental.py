import datetime   # The datetime module supplies classes for manipulating dates and times.

#---------------------------------The Rental Class---------------------------------#

class Rental(): # Class to manage the vehicles in the inventory, rentals, and billing. It is instantiated from the main() program each time it starts.
    
    def __init__(self):   # The rental class gets initiated with the following attributes: completed_billing, completed_rentals, rentals, billing, and inventory.
        self.completed_billing = [] # Holds historical records of billing transactions as tupple (driver_license,billing_info)
        self.completed_rentals = [] # Holds historical records of rental transactions as list of dictionaries, where each directory holds the rental information for a single customer.
        self.rentals = {}  # Dictionary for tracking active rentals. Key is driver license and value is a list of rented cars.
        self.billing = {} # Dictionary for tracking billing information. Key is driver license and value is a dictionary of billing information.
        self.inventory = [
                            {'VehicleID': 'Vin1', 'Make': 'Ferrari', 'Model': '488 Pista Coupe', 'Year': 2020, 'Color': 'Red', 'Passengers': 2, 'Luggage': 4, 'Transmission': 'Auto', 'Doors': 2, 'Available': True, 'Rates': {'Hourly':105,'Daily':2520,'Weekly':17640}},
                            {'VehicleID': 'Vin2', 'Make': 'Lamborghini', 'Model': 'Aventador SVJ', 'Year': 2022, 'Color': 'Black', 'Passengers': 4, 'Luggage': 4, 'Transmission': 'Auto', 'Doors':4, 'Available': True, 'Rates': {'Hourly':125,'Daily':3000,'Weekly':21000}},
                            {'VehicleID': 'Vin3', 'Make': 'McLaren', 'Model': '720S', 'Year': 2022, 'Color': 'Blue','Passengers':2,'Luggage':2,'Transmission':'Auto','Doors':2, 'Available': True, 'Rates': {'Hourly':105,'Daily':2520,'Weekly':17640}},
                            {'VehicleID': 'Vin4', 'Make': 'Porsche', 'Model': '911 GT3', 'Year': 2022, 'Color': 'White','Passengers':2,'Luggage':2,'Transmission':'Auto','Doors':2, 'Available': True, 'Rates': {'Hourly':85,'Daily':2040,'Weekly':14280}},
                            {'VehicleID': 'Vin5', 'Make': 'Audi', 'Model': 'R8', 'Year': 2020, 'Color': 'Silver', 'Passengers':2,'Luggage':4,'Transmission':'Manual','Doors':2,'Available': True, 'Rates': {'Hourly':125,'Daily':3000,'Weekly':21000}},
                            {'VehicleID': 'Vin6', 'Make': 'BMW', 'Model': 'M8', 'Year': 2022, 'Color': 'Black','Passengers':2,'Luggage':2,'Transmission':'Manual','Doors':2, 'Available': True, 'Rates': {'Hourly':115,'Daily':2760,'Weekly':19320}},
                            {'VehicleID': 'Vin7', 'Make': 'Mercedes-Benz', 'Model': 'AMG GT', 'Year': 2024, 'Color': 'Red', 'Passengers':2, 'Luggage':2,'Transmission':'Auto','Doors':2, 'Available': True, 'Rates': {'Hourly':146,'Daily':3504,'Weekly':24528}},
                            {'VehicleID': 'Vin8', 'Make': 'Roll Royce', 'Model': 'Phantom', 'Year': 2022, 'Color': 'Blue', 'Passengers':4, 'Luggage':5, 'Transmission':'Auto', 'Doors':4,'Available': True, 'Rates': {'Hourly':167,'Daily':4008,'Weekly':28056}},
                            {'VehicleID': 'Vin9', 'Make': 'Lamborghini', 'Model': 'Aventador SV Roadster', 'Year': 2018, 'Color': 'Yellow', 'Passengers':2,'Luggage':2,'Transmission':'Auto','Doors':2,'Available': True, 'Rates': {'Hourly':95,'Daily':2280,'Weekly':15960}},
                            {'VehicleID': 'Vin10', 'Make': 'Mercedes-Benz', 'Model': 'Brabus G Class 4x4 AMG', 'Year': 2019, 'Color': 'Red','Passengers':5,'Luggage':9,'Transmission':'Auto','Doors':5, 'Available': True, 'Rates': {'Hourly':188,'Daily':4512,'Weekly':31584}},  
                            {'VehicleID': 'Vin11', 'Make': 'Nissan', 'Model': 'GT-R', 'Year': 2018, 'Color': 'Blue', 'Passengers':2,'Luggage':4,'Transmission':'Manual','Doors':2,'Available': True, 'Rates': {'Hourly':85,'Daily':2040,'Weekly':14280}},
                            {'VehicleID': 'Vin12', 'Make': 'Rolls Royce', 'Model': 'Dawn Convertible', 'Year': 2019, 'Color': 'Blue','Passengers':4,'Luggage':4,'Transmission':'Auto','Doors':2, 'Available': True, 'Rates': {'Hourly':146,'Daily':3504,'Weekly':24528}},
                            {'VehicleID': 'Vin13', 'Make': 'Ferrari', 'Model': '488 GTS Convertible', 'Year': 2019, 'Color': 'Blue', 'Passengers':2,'Luggage':2,'Transmission':'Auto','Doors':2,'Available': True, 'Rates': {'Hourly':125,'Daily':3000,'Weekly':21000}},
                            {'VehicleID': 'Vin14', 'Make': 'Maserati', 'Model': 'Quatroporte S Granlusso', 'Year': 2021, 'Color': 'White','Passengers':5,'Luggage':4,'Transmission':'Auto','Doors':4, 'Available': True, 'Rates': {'Hourly':146,'Daily':3504,'Weekly':24528}},
                            {'VehicleID': 'Vin15', 'Make': 'Lamborghini', 'Model': 'Huracan EVO SPyder', 'Year': 2021, 'Color': 'Green','Passengers':2,'Luggage':2,'Transmission':'Auto','Doors':2, 'Available': True, 'Rates': {'Hourly':157,'Daily':3768,'Weekly':26376}},
                            {'VehicleID': 'Vin16', 'Make': 'Rolls Royce', 'Model': 'Cullinan', 'Year': 2021, 'Color': 'White','Passengers':7,'Luggage':5,'Transmission':'Auto','Doors':4, 'Available': True, 'Rates': {'Hourly':157,'Daily':3768,'Weekly':26376}},
                            {'VehicleID': 'Vin17', 'Make': 'Dodge', 'Model': 'Charger SRT Hellcat Widebody', 'Year': 2022, 'Color': 'Blue','Passengers':5,'Luggage':5,'Transmission':'Auto','Doors':4, 'Available': True, 'Rates': {'Hourly':130,'Daily':3120,'Weekly':21840}},
                            {'VehicleID': 'Vin18', 'Make': 'Porsche', 'Model': '911 Carrera 4S Cabriolet', 'Year': 2023, 'Color': 'Red','Passengers':2,'Luggage':2,'Transmission':'Auto','Doors':2, 'Available': True, 'Rates': {'Hourly':80,'Daily':1920,'Weekly':13440}},
                            {'VehicleID': 'Vin19', 'Make': 'Mercedes-Benz', 'Model': 'Maybach GLS 600 AMG', 'Year': 2023, 'Color': 'Blue', 'Passengers':4,'Luggage':5,'Transmission':'Auto','Doors':4,'Available': True, 'Rates': {'Hourly':146,'Daily':3504,'Weekly':24528}},
                            {'VehicleID': 'Vin20', 'Make': 'Jeep', 'Model': 'Gladiator 6x6', 'Year': 2024, 'Color': 'Red','Passengers':7,'Luggage':8,'Transmission':'Auto','Doors':4, 'Available': True, 'Rates': {'Hourly':208,'Daily':4992,'Weekly':34944}}
                 ]

    # This method displays the inventory of vehicles available for rent based on the availability status of the vehicle which is tracked by the 'Available' key.   
    def display_inventory(self):
        for vehicle in self.inventory:
            vehicle_name = f"\033[4m{vehicle['Make']} {vehicle['Model']}\033[0m"  # Vehicle name in bold
            if vehicle['Available']:
                print(f"Vehicle ID :{vehicle['VehicleID']} | {vehicle_name} {vehicle['Year']} Color: {vehicle['Color']} Passengers: {vehicle['Passengers']} Luggage: {vehicle['Luggage']} Transmission: {vehicle['Transmission']} Doors: {vehicle['Doors']} Rates: Hourly: ${vehicle['Rates']['Hourly']} Daily: ${vehicle['Rates']['Daily']} Weekly: ${vehicle['Rates']['Weekly']}") 
    
    # This method returns the number of available vehicles and the list of vehicle IDs of the available vehicles.
    def available_vehicles(self):
        available_vehicles = 0
        availableVID = []
        for vehicle in self.inventory:
            if vehicle['Available']:
                available_vehicles += 1
                availableVID.append(vehicle['VehicleID'])
        return available_vehicles, availableVID
    
    
    # This method is used to print the list of vehicles that the customer either intends to rent or has rented. Based on whether the list being passed comes from the car_request or car_return method.
    def print_vehicles_rented(self, rental_list):
        print("Rental Details:")
        print("-------------------------------------------------")
        print("Vehicle(s):")
        for car in rental_list:
            if car[8] == 'Hourly':
                print(f"Vehicle: {car[1]} {car[2]} {car[3]} Color: {car[4]} Passengers: {car[5]} Luggage: {car[6]} Transmission: {car[6]} Doors: {car[8]} Rental Period: {car[9]} Rate: ${car[10]}")
            elif car[8] == 'Daily':
                print(f"Vehicle: {car[1]} {car[2]} {car[3]} Color: {car[4]} Passengers: {car[5]} Luggage: {car[6]} Transmission: {car[7]} Doors: {car[8]} Rental Period: {car[9]} Rate: ${car[10]}")
            else:
                print(f"Vehicle: {car[1]} {car[2]} {car[3]} Color: {car[4]} Passengers: {car[5]} Luggage: {car[6]} Transmission: {car[7]} Doors: {car[8]} Rental Period: {car[9]} Rate: ${car[10]}")
        print("-------------------------------------------------")
    
    # This method is used to confirm the reservation details with the customer before proceeding with the rental. The customer is prompted to confirm the reservation details and is given the option to cancel the reservation. True or False is returned based on the customer's choice to confirm or cancel the reservation.
    def confirm_reservation(self, rental_period,reservation_list,start_time,return_time,ontime_return_cost):
        self.print_vehicles_rented(reservation_list)
        print("Pickup Time: ",start_time.strftime("%A, %B %d, %Y %I:%M %p"))
        print("Return Time: ",return_time.strftime('%A, %B %d, %Y %I:%M %p'))
        print("Ontime Return Cost: ",ontime_return_cost)
        print('\n')
        print("NOTE: All vehicles must be rented at the same time and returned at the same time. Early returns will be charged the full rental rate.")
        print('\n')
        print('LATE FEE INFORMATION : ')
        if rental_period == '1':
            print("For Hourly Rentals: There will be a $20 late fee added to the hourly rate for every hour late.")
        elif rental_period == '2':
            print("For Daily Rentals: There will be a $480 late fee added to the daily rate for every day late or part thereof, which is equivalent to a $20 late fee for every hour late.")
        elif rental_period == '3':
            print("Weekly Rental: There will be a $3360 late fee for every week late or part thereof, which is equivalent to a $20 late fee for every hour late.")
        print('\n')
        confirmation = input("Would you like to confirm this reservation? (Y/N): ")
        if confirmation.upper() == 'Y':
            print("Reservation confirmed. Thank you!")
            return True
        else:
            print("Reservation cancelled.")
            return False
        
    # This method's parameter is Vehicle ID of the car that the customer intends to rent. The method updates the 'Available' key of this car in the inventory to False, indicating that the vehicle will no longer available for rent. The method returns the car dictionary holding its information.
    def rent_vehicle(self, vehicle_id):
        for vehicle in self.inventory:
            if vehicle['VehicleID'] == vehicle_id:
                current_rental= vehicle
                vehicle['Available'] = False
        return current_rental
    
    # This method gets called when the customer either cancels or aborts the reservation process or when the customer returns the vehicle(s) after the rental period. 
    # The method takes the list of vehicles that the customer intended to rent or has rented and updates the 'Available' key of these vehicles in the inventory to True, indicating that the vehicles are now available for rent.
    def return_vehicles_to_inventory(self, reservation_list):
        for vehicle in reservation_list:
            for car in self.inventory:
                if car['VehicleID'] == vehicle[0]:
                    car['Available'] = True

    # This method is used to remove the completed rental from the active rentals dictionary and add it to the completed rentals list. This cleanup method is invoked after the customer returns the vehicle(s) after the rental period.
    def remove_completed_rental_from_current_rentals(self,d_license):
            if d_license in self.rentals:
                rental_info=self.rentals.pop(d_license)
                self.completed_rentals.append(rental_info)
    
    # This method is used to remove the completed billing from the active billing dictionary and add it to the completed billing list where it stores the Customer ID and rental information as a tupple. This cleanup method is invoked after the customer returns the vehicle(s) after the rental period.        
    def remove_completed_billing_from_current_billing(self,d_license):
            if d_license in self.billing:
                billing_info=self.billing.pop(d_license)
                self.completed_billing.append((d_license,billing_info))

    # This method is invoked every time the customer is asked for time input such as pickup time, intended return time, or actual return time. The method validates the time input and returns a datetime object if the input is in the correct format.
    def get_time(self):
        while True:
            # User is prompted to enter date and time in a specific format.
            time_input = input("Enter the date and time (MM/DD/YYYY HH:MM AM or PM. THE EXACT FORMAT MUST BE FOLLOWED): ")

            try:
                # Determine the correct format based on the presence of ':' in the time component.
                if ':' in time_input:
                    # Format includes minutes.
                    format_str = "%m/%d/%Y %I:%M %p"
                else:
                    # Format does not include minutes, assumes exact hour.
                    format_str = "%m/%d/%Y %I%p"

                # Try to create a datetime object using the determined format.
                valid_time = datetime.datetime.strptime(time_input, format_str)

                # Check if the entered time is greater than the current time
                current_time = datetime.datetime.now()
                if valid_time <= current_time:
                    print("The time can not be in the past. Please enter a correct date and time.")
                    continue

                print("Validated time:", valid_time.strftime("%A, %B %d, %Y %I:%M %p"))
                return valid_time
            except ValueError:
                print("Invalid format or incorrect date/time values. Please enter a valid date and time.")
        
    # This method is used to establish the pickup and return times for the reservation. The method returns the pickup and return times as datetime objects.
    def establish_pickup_and_return_times(self):
        print('\n')
        print("Please enter the pickup time for your reservation.")
        start_time=self.get_time()
        print('\n')
        print("Please enter the drop off or return time for your reservation.")
        return_time=self.get_time() 
        print('\n')
        return start_time, return_time
    
    # This method calculates the duration of the rental
    def calculate_rental_period(self, start_time, return_time):
        duration = return_time - start_time
        return duration
               
     # This method sets up the billing information for the customer. The billing information includes the driver's license, the car information, pickup time, return time, expected rental duration, rental rate, rental period units, ontime return cost, late fee, and total cost.
     # While the customer has not returned the vehicle(s), the actual return time, actual rental duration, late fee, and total cost are set to None.
     # Once the customer returns the vehicle(s), the actual return time, actual rental duration, late fee, and total cost are updated.   
    def setup_billing(self, driver_license,confirmed_reservation,start_time,return_time,duration,confirmed_rate,period_units,ontime_return_cost):
        self.billing[driver_license] = {
                                            'Car Info':confirmed_reservation[driver_license],
                                            'Pickup Time':start_time,'Return Time':return_time,
                                            'Expected Rental Duration':duration,
                                            'Rental Rate':confirmed_rate,
                                            'Rental Period Units':period_units,
                                            'Actual Return Time':None,
                                            'Actual Rental Duration':None,
                                            'Late Fee':None,
                                            'Ontime Return Cost':ontime_return_cost,
                                            'Total Cost':None
                                          }

     # This method is used to keep track of duration information for hourly rentals       
    def hourly_rental(self,start_time,return_time):
       duration = self.calculate_rental_period(start_time,return_time)
       print('duration : ',duration)
       total_hours=duration.total_seconds()/3600
       print('total_hours : ',total_hours)
       return total_hours

       
    # This method is used to keep track of duration information for daily rentals        
    def daily_rental(self,start_time,return_time):
        duration = self.calculate_rental_period(start_time,return_time)
        print('duration : ',duration)
        total_days=duration.total_seconds()/(3600*24)
        print('total_days : ',total_days)
        return total_days
    
    # This method is used to keep track of duration information for weekly rentals
    def weekly_rental(self,start_time,return_time):
        duration = self.calculate_rental_period(start_time,return_time)
        print('duration : ',duration)
        total_weeks=duration.total_seconds()/(3600*24*7)
        print('total_weeks : ',total_weeks)
        return total_weeks
    
    # This method is used to calculate the total cost of the rental if the customer returns the vehicle(s) on time. The total cost is calculated based on the duration of the rental and the rental rate of the vehicle(s).
    def calculate_total_ontime_return_rental_cost(self,duration, reserved_car_list):
        total_cost=0
        for car in reserved_car_list:
            car_cost=rate=car[10]*duration
            total_cost+=car_cost
        return total_cost

#---------------------------------The CustomerDataManagement Class---------------------------------#
 
class CustomerDataManagement(): # Class to manage customer data. It is instantiated from the main() program each time it starts. It is used to store customer, find customer information, add customers and check for duplicate customer records and active rentals.
    def __init__(self):
        self.customer_list= {} # It is initialized with the customer dictionary to store customer information. Key is driver license and value is a dictionary of customer information.
    
    # This method is used to check if the driver's license is already in the customer list. If the driver's license is already in the customer list, the method returns True. Otherwise, it returns False.    
    def checkDuplicate(self, driver_license):
        for dl_key in self.customer_list:
            if dl_key == driver_license:
                return True
        return False
    
    # This method is used to add a new customer to the customer list. The customer information is stored in the customer dictionary with the driver's license as the key and the customer information as the value.    
    def add_customer(self,fn,lname,dl,email,phone):
        self.customer_list[dl] = {'first_name':fn,'last_name':lname,'email':email,'phone':phone}
    
    # This method is used to find the customer record in the customer list based on the driver's license. If the driver's license is found in the customer list, the method returns the driver's license and the customer information. Otherwise, it returns None.
    def find_customer(self, driver_license):
        for dl_key in self.customer_list:
            if dl_key == driver_license:
                print("Found it!")
                return dl_key, self.customer_list[dl_key]
        return None

    # This method checks for active rentals to makere that the customer does not have any active rentals before proceeding with the rental process. If the driver's license is found in the active rentals, the method returns the driver's license and the list of rented cars. Otherwise, it returns False.
    # It is called in two occasionsfrom the main program:
    # 1. To check if the customer has any active rentals before proceeding with the rental process, when the customer is trying to rent a vehicle.
    # 2. To check if the customer has any active rentals before proceeding with the return process, when the customer is trying to return the vehicle(s).
    def check_for_active_rentals(self, rental, driver_license):
        if driver_license in rental.rentals:
                return rental.rentals[driver_license]
        return False
    # This method is used to display the customer information based on the driver's license. If the driver's license is found in the customer list, the method prints the customer information. Otherwise, it prints "Customer not found."
    # This method is called in two occasions:
    # 1. From the main program right after a successful record creation based on customer information.
    # 2. From the Customer class print_completed_billing method to display the customer information to include in the printing the billing information.
    def display_customers(self,driver_license):
        if driver_license in self.customer_list:
            print('\n')
            print('Customer Information: ')
            print('-------------------------')
            print('Customer Account Number: ',driver_license)
            print('First Name: ',self.customer_list[driver_license]['first_name'])
            print('Last Name: ',self.customer_list[driver_license]['last_name'])
            print('Email: ',self.customer_list[driver_license]['email'])
            print('Phone: ',self.customer_list[driver_license]['phone'])
        else:
            print("Customer not found.")
 
 
    
# ---------------------------------The Customer Class---------------------------------#

class Customer(): # Class to interact with the customer dictionary in the CustomerDataManagement class and with the Rental class. It is instantiated from the main() program each time it starts. So as long as the program is running, customer information is remembered and can be used to rent vehicles.
    def __init__(self,fname,lname,dl,email,phone): # The customer class gets initiated with the following attributes: first_name, last_name, driver_license, email, and phone.
        self.first_name = fname
        self.last_name = lname
        self.driver_license = dl
        self.email = email
        self.phone = phone
    
    # This is the method that gets called after the customer has indicated a desire to rent a vehicle.
    def car_request(self, rental):
        temp_reservation = {} # The temporary reservation dictionary is used to store the customer's reservation information before the reservation is confirmed.
        temp_car_selection = []  # The temporary car selection list is used to store the customer's vehicle selection before the reservation is confirmed.
        vehicleIDs=[] # The vehicleIDs list is used to store the vehicle IDs of the vehicles that the customer intends to rent.
        num_car_counter = 1 # The num_car_counter is used to keep track of the number of vehicles that the customer intends to rent.
        
        # The while loop is implemented in order to check enters valid information all along the rental process. If the customer enters invalid information, the loop will continue to prompt the customer to enter valid information or exit to the main menu
        while True:
            print('\n')
            num_vehicles=input("How many vehicles would you like to rent? ")
            valid_input = num_vehicles.isdigit()
            if valid_input: # Check that the input is a number.
                if int(num_vehicles) <= 0: # Check that the input is greater than 0. If number is 0 or less than 0 flow will return to top of while loop to prompt the customer to enter a valid number.
                    print("Invalid input. Please enter a number greater than 0.")
                    continue
                else: #if the input is valid, break the loop and exit to main menu
                    break
            else:
                print("Invalid input. Please enter a number greater than 0.")
                continue
        #Check that available cars are greater than the number of cars requested.
        available=rental.available_vehicles()[0] # Get the number of available vehicles from the available_vehicles method in the Rental class.
        print('AVAILABILITY : ',available,' available cars')
        print('\n')
        if available < int(num_vehicles): # If the number of available vehicles is less than the number of vehicles requested, print a message and return to the main menu.
            print("Sorry, we do not have enough vehicles to rent at the moment.")
            input("Press Enter to continue...")
        else:   # If the number of available vehicles is greater than or equal to the number of vehicles requested, proceed with the rental process.
            validRentalPeriod=False
            while not validRentalPeriod: # This while loop will continue to prompt the customer to enter a valid rental period until a valid rental period is entered, input must a number between 1 and 3.
                print("Rental Period Choices:")
                print("1. Hourly")
                print("2. Daily")
                print("3. Weekly")
                print('\n')
                print("Enter Option for rental period. Example, type: 3 for weekly rental. Note: (All vehicles must be rented at same time and returned at the same time.)")
                rentalPeriod = input()
                if rentalPeriod in ['1','2','3']: # If the input is 1, 2, or 3, the rental period is valid and the loop will break by setting validRentalPeriod to True and the customer will move on to display available inventory
                    validRentalPeriod=True
                    if rentalPeriod == '1':
                        period='Hourly'
                    elif rentalPeriod == '2':
                        period='Daily'
                    else:
                        period='Weekly'
                else:
                    print("Invalid input. Please enter a valid option.")
                    continue    # If the input is not 1, 2, or 3, the flow will go back to the top of the while loop and the customer will be prompted to enter a valid rental period.
            print('\n')
            print("------Available Vehicles------")
            print('\n')
            rental.display_inventory() # Display the inventory of vehicles available for rent. So the customer can see the vehicles available for rent.
            print('\n')
            while num_car_counter <= int(num_vehicles): # This while loop will continue to prompt the customer to enter the vehicle ID of the vehicles that the customer intends to rent. It will execute the number of times equal to the number of vehicles the customer intends to rent.
                print("Enter the Vehicle ID for vehicle ", num_car_counter, " Example, type: Vin11")
                vehicleID = input()
                available=rental.available_vehicles()[1] # Get the list of available vehicle IDs from the available_vehicles method in the Rental class.
                if vehicleID not in available: # If the vehicle ID entered by the customer is not in the list of available vehicle IDs, print a message and return to the top of the while loop to prompt the customer to enter a valid vehicle ID.
                    print("Invalid Vehicle ID. Let's try this again.")
                    print(input("Press Enter to continue..."))
                    continue
                else:
                    vehicleIDs.append(vehicleID) # If the vehicle ID entered by the customer is in the list of available vehicle IDs, add the vehicle ID to the vehicleIDs list. This list is used to store the vehicle IDs of the vehicles that the customer intends to rent. It will be used to get the vehicle information or to reset the availability status of the vehicles in the inventory if the user cancels the process.
                    num_car_counter += 1
             
             # This for loop is used to get the vehicle information for the vehicles that the customer intends to rent. The vehicle information is stored in the temp_car_selection list. This list is used to store the vehicle information before the reservation is confirmed.       
            for car in vehicleIDs:
                temp_car=rental.rent_vehicle(car)
                temp_car_selection.append([temp_car['VehicleID'],temp_car['Make'],temp_car['Model'],temp_car['Year'],temp_car['Color'],temp_car['Passengers'],temp_car['Luggage'],temp_car['Transmission'],temp_car['Doors'],period,temp_car['Rates'][period]])             
                temp_reservation[self.driver_license]=temp_car_selection
                               
            start_time, return_time = rental.establish_pickup_and_return_times() # The establish_pickup_and_return_times method from the rental class is used to get the pickup and return times for the reservation.
            
            # Based on the rental period the customer selected, the rental duration is calculated using the hourly_rental, daily_rental, or weekly_rental method from the rental class.
            # While loops are used to validate the rental period. If the rental period is invalid, the customer is prompted to enter a valid rental period. The loop will continue until a valid rental period is entered.
            if rentalPeriod == '1':
                    print('Rental Duration Details:')
                    print('-------------------------')
                    period_units = 'Hours'
                    rental_duration=rental.hourly_rental(start_time,return_time)   # The rental.hourly_rental method is used to calculate the rental duration for hourly rentals. Returns duration in hours               
                    invalid_rental_period = rental_duration <4 or rental_duration > 24  # The rental duration for hourly rentals must be between 4 and 24 hours. If the rental duration is less than 4 or greater than 24, the rental period is invalid.
                    while  invalid_rental_period:   # Loop to validate the rental period. If the rental period is invalid, the customer is prompted to enter a valid rental period by just pressing Enter or cancelling the process and returning to main menu by typing 'cancel' at the prompt.
                        print('Rental Duration: ',rental_duration)
                        print('\n')
                        print("Invalid rental period. For hourly rentals, please rent for a minimum of 4 hours with a maximum number of 24 hours.")
                        print('\n')
                        question = input("Press Enter to continue with hourly rental OR Type: cancel and Press Enter to go back to main menu and try again")
                        if question == 'cancel':
                            rental.return_vehicles_to_inventory(temp_reservation[self.driver_license])
                            return
                        start_time, return_time = rental.establish_pickup_and_return_times()
                        rental_duration=rental.hourly_rental(start_time,return_time)
                        period_units = 'Hours'
                        invalid_rental_period = rental_duration <4 or rental_duration > 24
                        continue
                    print('Rental Period: Hourly')
            elif rentalPeriod == '2':
                    print('Rental Duration Details:')
                    print('-------------------------')
                    period_units = 'Days'
                    rental_duration=rental.daily_rental(start_time,return_time) # The rental.daily_rental method is used to calculate the rental duration for daily rentals. Returns duration in days
                    invalid_rental_period = rental_duration < 1 or rental_duration > 7  # The rental duration for daily rentals must be between 1 and 7 days. If the rental duration is less than 1 or greater than 7, the rental period is invalid.
                    while invalid_rental_period:    # Loop to validate the rental period. If the rental period is invalid, the customer is prompted to enter a valid rental period by just pressing Enter or cancelling the process and returning to main menu by typing 'cancel' at the prompt.
                        print('Rental Duration: ',rental_duration)
                        print('\n')
                        print("Invalid rental period. For daily rentals please rent for a minimum of 1 day with a maximum number of 7 days.")
                        print('\n')
                        question = input("Press Enter to continue with daily rental OR Type: cancel and Press Enter to go back to main menu and try again")
                        if question == 'cancel':
                            rental.return_vehicles_to_inventory(temp_reservation[self.driver_license])
                            return
                        input("Press Enter to continue...")
                        start_time, return_time = rental.establish_pickup_and_return_times()
                        rental_duration=rental.daily_rental(start_time,return_time)
                        period_units = 'Days'
                        invalid_rental_period = rental_duration < 1 or rental_duration > 7
                        continue
                    print('Rental Period: Daily')
            else:
                    print('Rental Duration Details:')
                    print('-------------------------')
                    period_units = 'Weeks'
                    rental_duration=rental.weekly_rental(start_time,return_time)    # The rental.weekly_rental method is used to calculate the rental duration for weekly rentals. Returns duration in weeks
                    invalid_rental_period = rental_duration < 1 or rental_duration > 4  # The rental duration for weekly rentals must be between 1 and 4 weeks. If the rental duration is less than 1 or greater than 4, the rental period is invalid.
                    while invalid_rental_period:    # Loop to validate the rental period. If the rental period is invalid, the customer is prompted to enter a valid rental period by just pressing Enter or cancelling the process and returning to main menu by typing 'cancel' at the prompt.
                        print('Rental Duration: ',rental_duration)
                        print('\n')
                        print("Invalid rental period. For weekly rentals, please rent for a minimum of 1 week with a maximum of 4 weeks.")
                        print('\n')
                        question = input("Press Enter to continue with daily rental OR Type: cancel and Press Enter to go back to main menu and try again")
                        if question == 'cancel':
                            rental.return_vehicles_to_inventory(temp_reservation[self.driver_license])
                            return
                        start_time, return_time = rental.establish_pickup_and_return_times()
                        rental_duration=rental.weekly_rental(start_time,return_time)
                        period_units = 'Weeks'
                        invalid_rental_period = rental_duration < 1 or rental_duration > 4
                        continue
                    print('Rental Period: Weekly')
            rental_duration=round(rental_duration,3)    # The rental duration is rounded to 3 decimal places.
            print('-------------------------------------------------------------------------------')
            ontime_return_cost=rental.calculate_total_ontime_return_rental_cost(rental_duration,temp_reservation[self.driver_license]) # The calculate_total_ontime_return_rental_cost method is used to calculate the total cost of the rental if the customer returns the vehicle(s) on time.
            
            # The rental.confirm_reservation method is used to confirm the reservation details with the customer before proceeding with the rental.
            # The customer is prompted to confirm the reservation details and is given the option to cancel the reservation. True or False is returned based on the customer's choice to confirm or cancel the reservation.
            confirmed = rental.confirm_reservation(rentalPeriod,temp_reservation[self.driver_license],start_time,return_time,ontime_return_cost)     
            
               
            if confirmed:   # If the customer confirms the reservation, the reservation is confirmed and the active rentals method and rental setup_billing method are used to track active rentals in the system and set up the billing information for the customer.
                confirmed_reservation = temp_reservation
                confirmed_rate=confirmed_reservation[self.driver_license][0][10]
                rental.rentals[self.driver_license] = confirmed_reservation

                rental.setup_billing(self.driver_license,confirmed_reservation,start_time,return_time,rental_duration,confirmed_rate,period_units,ontime_return_cost)

            else:   # If the customer cancels the reservation, the reservation is cancelled and the vehicles that the customer intended to rent are returned to the inventory.
                rental.return_vehicles_to_inventory(temp_reservation[self.driver_license])
                print("Rental has been cancelled.")
                rental.display_inventory()
                print(input("Press Enter to continue..."))
                
     # This method is used to return the vehicle(s) after the rental period. During the return process, the difference between the expected rental duration and the actual rental duration is calculated as the return time delta
     # If this delta is greater than 0, i.e., the customer returns the vehicle(s) after the rental period, the late fee calculation will reflect the additional cost incurred by the customer for returning the vehicle(s) late.
     # This fee works out to adding $20 per hour extra to the hour rate used to calculate the rate for the period the customer rented the vehicle(s).
    def calculate_late_fee(self, delta,rate,type_of_rental):
        if type_of_rental == 'Hours':
            late_fee=delta*(rate+20)
        elif type_of_rental == 'Days':
            late_fee=delta*(rate+480)
        elif type_of_rental == 'Weeks':
            late_fee=delta*(rate+3360)
        return late_fee
    
    # This method is invoked by the main program when customer chooses to return a vehicle
    def car_return(self, dl, rental,customer_data_management):
        while True:
            print("We'll need your return time information to calculate your final total cost.")
            print('\n')
            return_time = rental.get_time() # The actual return time is obtained from the customer using the get_time method in the Rental class. In a live system, this would be given by the current time of system when customer is returning the vehicle.
            pickup_time = rental.billing[dl]['Pickup Time'] # The pickup time is obtained from the billing information stored in the billing dictionary in the Rental class. In order to determine the delta or difference of rental duration, the pickup time is needed.
            if return_time < pickup_time:   # The return time must be after the pickup time. If the return time is before the pickup time, the customer is prompted to enter a valid return time.
                print("Invalid return time. The return time must be after the pickup time.")
                input("Press Enter to continue...")
                continue    # Loops until customer inputs a valid return time
            else:
                break # If the return time is valid, the loop will break and the customer will proceed to the next step.
        expected_rental_duration=rental.billing[dl]['Expected Rental Duration'] # The expected rental duration is obtained from the billing information stored in the billing dictionary in the Rental class. This is the duration the customer intended to rent the vehicle(s) for.
        # Based on whether the rental period is hourly, daily, or weekly, the actual rental duration is calculated using the hourly_rental, daily_rental, or weekly_rental method from the rental class based on the difference betwee picup time and actual return time.
        if rental.billing[dl]['Rental Period Units'] == 'Hours':
            type_of_rental = 'Hours'
            rental_duration = rental.hourly_rental(pickup_time,return_time)
            actual_rental_duration = round(rental_duration,3)
        elif rental.billing[dl]['Rental Period Units'] == 'Days':
            type_of_rental = 'Days'
            rental_duration = rental.daily_rental(pickup_time,return_time)
            actual_rental_duration = round(rental_duration,3)
        elif rental.billing[dl]['Rental Period Units'] == 'Weeks':
            type_of_rental = 'Weeks'
            rental_duration = rental.weekly_rental(pickup_time,return_time)
            actual_rental_duration = round(rental_duration,3)
       
        return_time_delta=actual_rental_duration-expected_rental_duration   # The return time delta is calculated as the difference between the expected rental duration and the actual rental duration.
        
        if return_time_delta > 0:   # If the return time delta is greater than 0, the customer returns the vehicle(s) after the rental period. The late fee calculation will reflect the additional cost incurred by the customer for returning the vehicle(s) late.
            late_fee=self.calculate_late_fee(return_time_delta,rental.billing[dl]['Rental Rate'],type_of_rental)
        else:
            late_fee=0
            
        rental.billing[dl]['Late Fee'] = late_fee
        total_cost=rental.billing[dl]['Ontime Return Cost']+late_fee
        rental.billing[dl]['Total Cost'] = total_cost
        rental.billing[dl]['Actual Return Time'] = return_time
        rental.billing[dl]['Actual Rental Duration'] = actual_rental_duration
        
        print('\n')

        self.print_completed_billing(rental,customer_data_management)
        print('\n')
        rental.return_vehicles_to_inventory(rental.rentals[dl][dl])
        rental.remove_completed_rental_from_current_rentals(dl)
        rental.remove_completed_billing_from_current_billing(dl)
        print("Thank You for renting with us!")
        print('\n')
        input("Press Enter to continue...")
        
    def print_completed_billing(self,rental,customer_data_management):
        print('----------------Billing Information------------------')
        customer_data_management.display_customers(self.driver_license)
        print('\n')
        rental.print_vehicles_rented(rental.billing[self.driver_license]['Car Info'])
        print("Pickup Time : ",rental.billing[self.driver_license]['Pickup Time'].strftime('%A, %B %d, %Y %I:%M %p'))
        print("Expected Return Time : ",rental.billing[self.driver_license]['Return Time'].strftime('%A, %B %d, %Y %I:%M %p'))
        print("Expected Rental Duration : ",rental.billing[self.driver_license]['Expected Rental Duration'])
        print("Actual Return Time : ",rental.billing[self.driver_license]['Actual Return Time'].strftime('%A, %B %d, %Y %I:%M %p'))
        print("Actual Rental Duration : ",rental.billing[self.driver_license]['Actual Rental Duration'])
        print("Rental Rate : ",rental.billing[self.driver_license]['Rental Rate'])
        print("Rental Period Units : ",rental.billing[self.driver_license]['Rental Period Units'])
        print("Late Fee : ",rental.billing[self.driver_license]['Late Fee'])
        print("Ontime Return Cost : ",rental.billing[self.driver_license]['Ontime Return Cost'])
        print("----------------_Total Cost_------------------")
        print("Total Cost (Original Return Cost + Late Fee) : ",rental.billing[self.driver_license]['Total Cost']) 
        

            
