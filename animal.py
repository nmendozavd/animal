class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print self.name, self.health

animal1 = Animal("Cheetah")
animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __inti__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.heatlh += 5
        return self

dog = Dog("Clifford")
dog.walk().walk().walk().run().run().displayHealth()

class Dragon(Animal):
    def __inti__(self, name):
        super(Dog, self).__init__(name)
        self.health = 170

    def fly (self):
        self.health -= 10
        return self

def displayHealth(self):
    print "I am a Dragon"
    super(Dragon, self).displayHealth()

dragon = Dragon('Nightwing')
dragon.fly().displayHealth()
