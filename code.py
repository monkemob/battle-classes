class Character:
    def __init__(self, name):
        self.name=name
        self.health=100
        self.base_attack=15
        self.defence=1
        self.classc=None
    def take_damage(self,ammount):
        self.health-=(ammount-self.defence)
        
    def attack(self,target):
        target.take_damage(self.base_attack)
        
    def is_alive(self):
        if self.health<=0:
            return False
        else:
            return True
    def status(self):
        print(f"{self.name}: {self.classc}\nHealth: {self.health}")
            
class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.defence=5
        self.mana=100
        self.classc="mage"
    
    def cast_spell(self,spell,target):
            if spell.lower()=="fireball":
                if self.mana<20:
                    print(f"Not enough mana to cast {spell}")
                else:
                    self.mana-=20
                    target.take_damage(30)
            elif spell.lower()=="heal":
                if self.mana<15:
                    print(f"Not enough mana to cast {spell}")
                elif self.health>=100:
                    print(f"{self.name} is already at full health")
                else:
                    self.mana-=15
                    self.health+=25
            else: 
                print(f"{spell} is not a valid spell")
        
    def status(self):
        super().status()
        print(f"Mana: {self.mana}")
                
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.base_attack=15
        self.defence=10
        self.rage=0
        self.classc="warrior"
    
    def take_damage(self,ammount):
        super().take_damage(ammount)
        self.rage+=1
    
    def power_strike(self,target):
        if self.rage>=10:
            self.rage=0
            target.take_damage(2*self.base_attack)
        else:
            print("Not enough rage for this attack")
    
    def status(self):
        super().status()
        print(f"Rage: {self.rage}")
            
class Game:
    def __init__(self):
        self.characters=[]
        
    def add_character(self,character):
        self.characters.append(character)
        
    def battle(self, character1,character2):
        x=True
        print(f"{character1.name}'s Turn")
        character1.status()
        if character1.classc=="mage":
            while x:
                action=input("Cast fireball, heal, or punch: ")
                if action.lower()=="fireball":
                    character1.cast_spell(action,character2)
                    x=False
                elif action.lower()=="heal":
                    character1.cast_spell(action,character2)
                    x=False
                elif action.lower()=="punch":
                    character1.attack(character2)
                    x=False
                else:
                    print("Invalid action try again")
        elif character1.classc=="warrior":
            while x:
                action=input("Punch or use Power Strike: ")
                if action.lower()=="punch":
                    character1.attack(character2)
                    x=False
                elif action.lower()=="power strike":
                    character1.power_strike(character2)
                    x=False
                else:
                    print("Invalid action try again")
    
    def start_battle(self):
        if len(self.characters)!=2:
            print("Only 2 characters can battle at a time")
        else:
            x=True
            while x:
                self.battle(self.characters[0],self.characters[1])
                if not self.characters[1].is_alive():
                    self.characters[1].status()
                    print(f"{self.characters[1].name} has died\n{self.characters[0].name} Wins")
                    break
                self.battle(self.characters[1],self.characters[0])
                if not self.characters[0].is_alive():
                    self.characters[0].status()
                    print(f"{self.characters[0].name} has died\n{self.characters[1].name} Wins")
                    break
                

                
    

x=Mage("Wizard of Evil")
y=Warrior("Innocent Civilian")
z=Game()
z.add_character(x)
z.add_character(y)
z.start_battle()
