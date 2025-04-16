import random

class Player:
    def __init__(self, health, food, energy, time_left):
        self.health = health
        self.food = food
        self.energy = energy
        self.time_left = time_left
        self.inventory = ["õun", "vesi", "ravim"]

    def status(self):
        print(f"Tervis: {self.health}, Toit: {self.food}, Energia: {self.energy}, Aega alles: {self.time_left}")
        print(f"Inventar: {self.inventory}")

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 10
            self.time_left -= 1
            print("Puhkasid. Energia tõusis, toit vähenes.")
            self.random_event()
        else:
            print("Pole piisavalt toitu puhkamiseks.")

    def eat(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 5
            self.health += 5
            print("Sõid toitu. Energia ja tervis tõusid.")
        else:
            print("Sul ei ole midagi süüa!")

    def walk(self):
        if self.energy >= 5:
            self.energy -= 5
            self.time_left -= 1
            print("Kõndisid edasi. Energia ja aeg vähenesid.")
            self.random_event()
        else:
            print("Oled liiga väsinud kõndimiseks!")

    def check_game_over(self):
        if self.health <= 0:
            print("Mäng läbi – tervis sai otsa.")
            return True
        elif self.time_left <= 0:
            print("Mäng läbi – aeg sai otsa.")
            return True
        return False

    def use_item(self, item):
        if item in self.inventory:
            print(f"Kasutad eset: {item}")
            if item == "õun":
                self.food += 1
            elif item == "vesi":
                self.energy += 5
            elif item == "ravim":
                self.health += 10
            self.inventory.remove(item)
        else:
            print(f"Sul ei ole eset: {item}")

    def random_event(self):
        events = [
            "Sa leidsid toitu!",          
            "Sind ründas metsloom!",      
            "Leidsid pudeli vett.",       
            "Midagi ei juhtunud.",        
        ]
        event = random.choice(events)
        print(f"Sündmus: {event}")

        if event == "Sa leidsid toitu!":
            self.food += 1
        elif event == "Sind ründas metsloom!":
            self.health -= 10
        elif event == "Leidsid pudeli vett.":
            self.inventory.append("vesi")


def test_all_splints():
    print("=== Mängija test (Sprint 1–3) ===")
    player = Player(health=50, food=2, energy=20, time_left=5)
    
    player.status()
    
    print("\n>> Puhka:")
    player.rest()
    player.status()
    
    print("\n>> Söö midagi:")
    player.eat()
    player.status()
    
    print("\n>> Kõnni:")
    player.walk()
    player.status()

    print("\n>> Kasuta eset: ravim")
    player.use_item("ravim")
    player.status()

    print("\n>> Kontrolli mängu lõppu:")
    if player.check_game_over():
        print("Mäng lõppes.")
    else:
        print("Mäng jätkub.")

test_all_splints()