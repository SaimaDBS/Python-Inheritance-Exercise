from PersonalCustomer import PersonalCustomer
from CorporateCustomer import CorporateCustomer
from Customer import Customer

CustomerId= None 
AddressLine1 = None 
City = None 
PhoneNo = None 
Country=None


personalCustomer=PersonalCustomer(AddressLine1,City,Country,CustomerId,PhoneNo)


personalCustomer.setFirstName()
personalCustomer.setLastName()
personalCustomer.setAge()
personalCustomer.setDateOfBirth()

personalCustomer.setCustomer()


print("\n ##### RETRERIVING VALUES ####### \n ")
print("First Name is : ",personalCustomer.getFirstName())
print("Last Name is:", personalCustomer.getLastName())
print("Age is:", personalCustomer.getAge())
print("Date of birth is:", personalCustomer.getDateOfBirth())
print("Customer ID:",personalCustomer.getCustomerId())
print("City is:", personalCustomer.getCity())
print("Country is :", personalCustomer.getCountry())
print("Address Line 1 :",personalCustomer.getAddressLine1())

corporateCustomer=CorporateCustomer(AddressLine1,City,Country,CustomerId,PhoneNo)
print("\n")
corporateCustomer.setCompanyName()
corporateCustomer.setCompanyRegNo()
corporateCustomer.setDateOfIncorporation() 
corporateCustomer.setVATNo() 

print("\n ##### RETRERIVING VALUES #######  \n ")
print("Company's Name is :", corporateCustomer.getCompanyName())
print("Company's Registration No is :", corporateCustomer.getCompanyRegNo())
print("Company's Date of Incorporation is : ", corporateCustomer.getDateOfIncorporation())
print("Company's Vat No. is :", corporateCustomer.getVATNo())
print("Customer ID:",personalCustomer.getCustomerId())
print("City is:", personalCustomer.getCity())
print("Country is :", personalCustomer.getCountry())
print("Address Line 1 :",personalCustomer.getAddressLine1())



