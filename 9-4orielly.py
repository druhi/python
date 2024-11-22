class Restaurant:
    def __init__(self,name,cuisine):
     self.name = name
     self.cuisine = cuisine
     self.numberserved = 0
    
    def describe_restaurant(self):
       print(f"{self.name} is name")
       print(f"{self.name} is {self.cuisine} type")

    def open_restaurant(self):
       print(f"{self.name} is open")
    def set_number_served(self,number):
       self.numberserved = number
    def increment_number_served(self, number):
       self.numberserved += number
       
myRest = Restaurant('Haldiram','Indian')
DrishiRest=Restaurant('Mcd','US')
print(f"num of customer served are {myRest.numberserved}")
myRest.set_number_served(20)
print(f"num of customer served are {myRest.numberserved}")
myRest.increment_number_served(20)
print(f"num of customer served are {myRest.numberserved}")
myRest.describe_restaurant()
myRest.open_restaurant()
DrishiRest.describe_restaurant()
DrishiRest.open_restaurant()