import csv


class Customer:

    def __init__(self, customer_id, firstName, lastName, companyName, address, city):
        self.customer_id = customer_id
        self.first_name = firstName
        self.last_name = lastName
        self.company_name = companyName
        self.address = address
        self.city = city

##Function for displaying title
def display_title():
    print()
    print("Customer Viewer")
    print()
##function for opening csv file in read mode
def csv_reader():
    csvfile = open('customers.csv','r')
    customers_csv = csv.reader(csvfile)
    return customers_csv
##function for finding customer id and printing the details of corresponding row
def find_customer(cust_id):
    for row in csv_reader():
        i = str(row[0])
        #if i matches the given customer id then it prints the corresponding columns
        if i == str(cust_id):
            firstName = row[1]
            lastName = row[2]
            company = row[3]
            address = row[4]
            city = row[5] + "," + row[6] + "," + row[7]
            print(firstName + " " + lastName)
            if company != '':
                print(company)
            print(address)
            print(city)
            break
    else:
        print('No customer with that specified ID.')
#main function
def main():
    display_title()
    while True:
        # asking customer to enter the customer Id
        cust_id = input("Enter Customer ID:")
        print()
        #Calling find_customer to print the details of corresponding customer id
        find_customer(cust_id)
        print()
        #asking customer to input choice of whether to continue or not
        choice = input("Continue(y/n)?")
        print()
        if choice != "y":
            print("Bye!")
            break



if __name__ == '__main__':
    main()




