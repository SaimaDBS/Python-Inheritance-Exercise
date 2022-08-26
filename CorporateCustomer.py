from Customer import Customer
import datetime

class CorporateCustomer(Customer):
    def __init__(self,AddressLine1,Country,City,PhoneNo,CustomerId):
        __CompanyName=None 
        __DateOfIncorporation=None
        __VATNo=None
        __CompanyRegNo=None


    def setCompanyName(self):
        companyName=input("Enter Company Name :")
        
        self.__CompanyName=companyName 
    def getCompanyName(self):
        return self.__CompanyName

    def setDateOfIncorporation(self):
        while True:
            try:
                date=input("Enter date of Incorporation DD/MM/YY : ")
                weekEnding = datetime.datetime.strptime(date, "%d/%m/%Y")
                break
            
            except ValueError:
                print("Sorry, this is in the incorrect format. Try again!")
                continue

        self.__DateOfIncorporation=date
    def getDateOfIncorporation(self):
        return self.__DateOfIncorporation 

    def setVATNo(self):
        value=input("Enter VAT no. :")
        self.__VATNo=value 
    def getVATNo(self):
        return self.__VATNo

    def setCompanyRegNo(self):
        regNo=input("Enter Registration No :")
        self.__CompanyRegNo=regNo
    def getCompanyRegNo(self):
        return self.__CompanyRegNo
   
    