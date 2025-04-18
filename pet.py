class Pet :
    def __init__(self,name,hunger,energy,happiness):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness

    def eat(self):
        print(self.name+ " is eating🥩🤤...")
        self.hunger = self.hunger + 3
        self.happiness = self.happiness +1

    def sleep(self):
        print(self.name+ " is sleeping😴...")
        self.energy = self.energy + 5
    
    def play(self):
        print(self.name+ " is playing🦴...")
        self.energy = self.energy - 2
        self.hunger = self.hunger + 1
    
    def get_status(self):    
        print(self.name+"'s current status:\nHunger:"+str(self.hunger)+ "\nEnergy:"+str(self.energy)+"\nHappiness:"+str(self.happiness))
