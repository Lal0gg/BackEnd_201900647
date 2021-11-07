class Usuario:
    def __init__(self,name,gender,username,email,password):
        self.name = name
        self.gender = gender
        self.username = username
        self.email = email
        self.password = password

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def setName(self, name):
        self.name = name

    def setGender(self,gender):
        self.gender = gender

    def setUsername(self, username):
        self.username = username

    def setEmail(self,email):
        self.email = email

    def setPassword(self,password):
        self.password = password
