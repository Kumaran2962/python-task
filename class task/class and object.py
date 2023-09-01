class Marvel:
    realName = ""
    superName = ""
    superPower = ""

    def getFullName(self):
        return self.firstName + "@" + self.lastName + " " + self.superPower

obj1=Marvel()
obj2=Marvel()
obj3=Marvel()

obj1.realName = "Tony Stark"
obj1.superName = "Iron Man"
obj1.superPower = "Billionaire"

obj2.realName = "Steve Rogers"
obj2.superName = "Captain America"
obj2.superPower = "Winter Soldier"

obj3.realName = "Bruce Banner"
obj3.superName = "Hulk"
obj3.superPower = "Gamma reader"
