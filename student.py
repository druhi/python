class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    #getter
    @property
    def house(self):
        return self._house
    #setter
    @house.setter   
    def house(self, house):
        if house not in ["Delhi","noida"]:
           raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
#    student.house = "Delhi"
    print(student)

def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name,house)

if __name__ == "__main__":
    main()