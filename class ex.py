class Classs:
	schoolName="abc"
	def __init__(self,name,classTeacher,numStud):
		self.name=name
		self.classTeacher=classTeacher
		self.numStud=numStud
		numSub=self.name+2
class Student(Classs):
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
	def markavg(marks):
		avg=sum(marks)/len(marks)
		return avg
studobj=Student('Sunita',25)
clsobj=Classs(4,'raghini',57)
average=Student.markavg([78,69,89,92,88,78])
print(f"student of class {clsobj.name}th gets {average}% marks by {clsobj.classTeacher} madam")
