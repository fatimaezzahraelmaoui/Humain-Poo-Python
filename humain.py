class humain:
#attribut static
    count = 0
#attribut
    def __init__(self,first,last,age):
        self.__first = first 
        self.__last = last 
        self.__age = age 
        self.__fullname = self.__first +" "+ self.__last 
        humain.count += 1
#GETTER et SETTER
    def getfirst(self):
        return self.__first
    def setfirst(self,first):
        self.__first = first
    def getlast(self):
        return self.__last
    def setlast(self,last):
        self.__last = last
    def getage(self):
        return self.__age
    def setage(self,age):
        self.__age = age
    def getfullname(self):
        return self.__fullname
    def setfullname(self,fullname):
        self.__fullname = fullname
#Méthodes

    def Ischild(age):
        if age < 15 :
            return True
        else :
            return False

    def make_email(self):
        if Student self.__age < 15 :
        self.email = self.__first +'.'+ self.__last + "@cs.com"
        return self.email
    def addage(self):
        self.__age += 1
        return self.__age

#héritage
class Student(humain):
    def __init__(self,first,last,age,note):
        super().__init__(first,last,age)
        self.__note = note
    def getnote(self):
        return self.__note
    def setnote(self,note):
        self.__note = note
#héritage cascade
class SecondaryStudent(Student):
    pass

h1 = humain("hassan","rhs",23)
h1.setfirst("kamal")
print(h1.getfirst())
email1 = h1.make_email()
age1 = h1.addage()
print(h1.email)
print(h1.getage())
print(humain.count)
