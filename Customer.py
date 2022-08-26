class Customer:
     

    def __init__(self):
        print("")
        
        

    def setCustomer(self):
        customerId=input("Customer ID :")
        addressLine1=input("AddressLine1 :")
        city=input("City :")
        country=input("Country:")
        

        while True:
            try:
               if (any(i.isalpha() for i in country) or all(i.isalpha() for i in country)):
                   self.Country=country
                   break
               else:
                   raise ValueError
            except ValueError:
                print("Please enter alphabets values only ")
                country=input("Enter Country")

        
        while(1):
            try:
                phoneNo=int(input ("Enter PhoneNo :"))
                self.PhoneNo=phoneNo
                break;
            except ValueError:
                print("Please enter a numeric value for the key")

        self.CustomerId=customerId
        self.AddressLine1=addressLine1
        self.City=city
        
   
    def getCustomerId(self):
        return self.CustomerId
  
    def getAddressLine1(self):
        return self.AddressLine1
    
    def getCity(self):
        return self.City
    
    def getCountry(self):
        return self.Country 
    
    def getPhoneNo(self):
        return self.PhoneNo

    #def customerDetails(self):
    #    print("Customer Id is :",self.getCustomerId())
    #    print("Address Line 1 is :",self.getAddressLine1())
    #    print("City is :",self.getCity())
    #    print("Country is : ",self.getCountry())
    #    print("Phone No is :",self.getPhoneNo())
   
