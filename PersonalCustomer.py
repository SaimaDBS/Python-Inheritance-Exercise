from Customer import Customer
import datetime

class PersonalCustomer(Customer):
        
    def __init__(self,AddressLine1,Country,City,PhoneNo,CustomerId):
        
        __FirstName=None 
        __LastName=None 
        __DateOfBirth=None 
        __Age=None 

    
    def setFirstName(self):
        firstName=input("Enter Your First Name: ")
        while True:
            try:
                if (any(i.isalpha() for i in firstName) and all(i.isalpha() for i in firstName)):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter alphabets values only ")
                firstName=input("Enter First Name")
                

        self.__FirstName=firstName
    def getFirstName(self):
        return self.__FirstName

    def setLastName(self):
        lastName=input("Enter Your Last Name: ")
        while True:
            try:
                if (any(i.isalpha() for i in lastName) and all(i.isalpha() for i in lastName)):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter alphabets values only ")
                lastName=input("Enter First Name")
        self.__LastName=lastName 

    def getLastName(self):
        return self.__LastName

    def setDateOfBirth(self):
        while True:
            try:
                date=input("Enter your date of birth DD/MM/YY : ")
                weekend= datetime.datetime.strptime(date, "%d/%m/%Y")
                
                break
            except ValueError:
                    print("Sorry, this is in the incorrect format. Try again!")
                    continue
        self.__DateOfBirth=date
    def getDateOfBirth(self):
        return self.__DateOfBirth

    def setAge(self):
            
        while(1):
            try:
                value=int(input("Enter your Age :"))
                break;
            except ValueError:
                print("Please enter a numeric value for the key")
        self.__Age=value 

    def getAge(self):
        return self.__Age
    
        #def Display_info(self):
        #    Customer.customerDetails(self)