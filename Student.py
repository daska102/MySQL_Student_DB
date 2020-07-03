class Student:
    def __init__(self, firstName, lastName, gpa, major, facultyAdvisor, address):
        self.firstName = firstName
        self.lastName = lastName
        self.gpa = gpa
        self.major = major
        self.facultyAdvisor = facultyAdvisor
        self.address = address

    #getters
    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getGPA(self):
        return self.gpa

    def getMajor(self):
        return self.major

    def getFacultyAdvisor(self):
        return self.facultyAdvisor

    def getID(self):
        return self

    def getAddress(self):
        return self.address

    #setters
    def setFirstName(self, x):
        self.firstName = x

    def setLastName(self, x):
        self.lastName = x

    def setGPA(self, x):
        self.gpa = x

    def setMajor(self, x):
        self.major = x

    def setAddress(self, x):
        self.address = x

    def setFacultyAdvisor(self, x):
        self.facultyAdvisor = x

    #returns all student info in a tuple
    def getStudentTuple(self):
        return (self.firstName, self.lastName, self.facultyAdvisor, self.gpa, self.major, self.address,)




