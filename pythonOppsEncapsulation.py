class University:
    estb="1992"
    location= "xyz"
    def __init__(self, univ1):
        print("hello")
        self.univName = univ1

class Dept(University):
    def __init__(self, name, hod1 , univ2):
        super().__init__(univ2)
        self.name= name
        self.hod = hod1
    


mathDept = Dept("mathmatics", "mohan", 'namu')
print("{} is hod of {} dept of {} university".format(mathDept.hod, mathDept.name, mathDept.univName ))