## Project Title: Online Car Rental Platform

This project is an implementation of the  Car Rental Platform project below.

This is a Summary. Details can be found in the Comments of the code files themselves.

3 Classes are used:

Rental class uses the relevant methods to keep track of information having to do with the vehicles themselves, like keeping track of which vehicles are being rented out and which are still available to rent, the time calculation for their rentals, total costs based on rates chosen, displaying inventory, implementing cancellations, confirming reservations, setting up billing, etc. Due to constraints in scope the inventory list is kept in memory while the program runs

The CustomerDataManagement class is used to store the customer dictionary and uses relevant methods to add customers to the dictionary, find customers already in the system, check for duplicates to avoid things like renting vehicles while still having vehicles pending return, interacting with the rental class to keep track of active rentals, and displaying customer information. Just like the vehicle inventory, this dictionary is kept in memory while the program runs

The Customer class keeps track of individual customers and uses relevant methods to interact with the Customer Directory and the Car Inventory Directory to complete the car request and the car return processes. It also has a method for printing and finalizing the customer bill, interacting with the rental class to clean up the active rentals and billing ledgers, and moving completed records of rentals and paid bills to lists that keep track of the history of completed rentals and bills.

Throughout the code, loops have been implemented to check valid input for the crucial processes of requesting a rental and returning a car. Checks have not been done for the customer records themselves to make sure that names only contain characters and that emails are valid, etc. But it can be implemented as a new feature  or update in the future.

The program is run by invoking the main() in a cell of the Jupyter Notebook that loads the MainCarRental.ipynb file. The first line of code of this file imports the 3 main classes above from the CarRental.py file. 

The file has been tested successfully to check for:

Display of the inventory
Customers without an account are prompted for their information to create their customer record that will then be used to request cars.
Return to main menu if customer not with an account tries to rent a vehicle
No rental for customers under 18 years of age. Return to main menu
Return to main menu if customer with active rental tries to rent another vehicle before returning the current one
Return to main menu if customer without an active rental tries to return a vehicle
Customers that have previously rented and returned their vehicles can rent new vehicles without any issues.
Inventory is updated each time a customer returns a vehicle or set of vehicles
Inventory is updated if user cancels the rental when asked if they want to cancel during process.
Correct date format must be used (MM/DD/YYYY HH:MM AM or PM)
Not following correct format prompts user for correct format
Putting an invalid date like a date in the past, prompts user for correct date
If a user wants to rent hourly but sets a return date greater than 24 hours an opportunity to cancel is presented so they can choose another Rental Period Option, i.e. Daily or Weekly. 
The same applies if a user renting Daily, tries to use a return over 7 days or if a user renting Weekly tries to use a return date over 4 weeks.
Dates cannot be prior to current date and time
Dates of returns must be greater than time of pickup
Hourly rentals have a limit of 24 hours
Daily rentals have a limit of 7 days
Weekly rentals have a limit of 4 weeks
Once customer types the Vehicle ID of a desired vehicle their Availability is turned to False
Customers are asked to confirm rental details prior to updating active rentals 
If Customer does not confirm, vehicles requested go back to being available.
Inventory display shows any vehicles that were chosen by customer but canceled as being available 
Inventory display does not show any vehicles confirmed for rental
Details of the rental information is displayed to the customer after confirmation
For returns, if a customer not in the system tries to return a vehicle, message tells user and the program goes back to main menu
If during return the user puts in a return date in the past or a date prior to the original pickup time, the system tells the user and loops back to prompt for a correct date
If a valid date is input for a return date, the bill is presented to the user and the system cleans up the active rentals, current billing records and transfers them to historical lists that keep track of completed rentals and bills. It also marks all returned vehicles as available in the inventory


Project Title: Online Car Rental Platform

Project Objective: 
Build an online car rental platform using Object-Oriented Programming in Python.

Problem Statement:
A car rental company has requested you to build an online car rental platform where customers should be able to view the available cars that can be rented on an hourly, daily, or weekly basis. The company can display the available inventory and confirm requests by checking the available stock. Customers will receive an auto-generated bill when they return the car.

For simplicity, let’s assume that:
Customers can rent cars from any one of the following options—hourly, daily, or weekly rental.
Customers are free to choose any number of cars they want, provided the number of available cars is more than the number of requested cars.


You must use the following tools:
Jupyter Notebook: To create the module and main project files

Instructions to Perform:

Create a module (.py file) for car rental and import the built-in module DateTime to handle the rental time and bill.
Create a class for renting the cars and define a constructor in it.
Define a method for displaying the available cars. Also, define methods for renting cars on an hourly, daily and weekly basis, respectively.
Inside these methods, make sure that the number of requested cars is positive and lesser than the total available cars.
Store the time of renting a car in a variable, which can later be used in the bill while returning the car. 
Define a method to return the cars using rental time, rental mode (hourly, daily, or weekly), and the number of cars rented.
Inside the return method; update the inventory stock, calculate the rental period, and generate the final bill.
Create a class for customers and define a constructor in it.
Define methods for requesting the cars and returning them. 
Next, create the main project (.ipynb) file and import the car rental module in it.
Define the main method and create objects for both car rental and customer classes.
Inside the main method, take the customer’s input as a choice for displaying car availability, rental modes, or returning the cars.
Use the relevant method for the customer’s input and print relevant messages.
Run the main method to start your project.
