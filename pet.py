class Pet :
    def __init__(self,name,hunger,energy,happiness):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness

    def eat(self):
        print(self.name+ " is eating🥩🤤...")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        print(self.name+ " is sleeping😴...")
        self.energy = min(10, self.energy + 5)
    
    def play(self):
        print(self.name+ " is playing🦴...")
        self.energy = max(0,self.energy - 2)
        self.hunger = min(10,self.hunger + 1)
        self.happiness = min(10,self.happiness + 2)
    
    def get_status(self):    
        print(self.name+"'s current status:\nHunger:"+str(self.hunger)+ "\nEnergy:"+str(self.energy)+"\nHappiness:"+str(self.happiness))

    

