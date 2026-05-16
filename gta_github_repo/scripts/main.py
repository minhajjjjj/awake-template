class Player:
    def __init__(self, name):
        self.name = name
        self.money = 0

    def complete_mission(self, reward):
        self.money += reward
        print(f"{self.name} earned ${reward}")

player = Player("CJ")
player.complete_mission(7500)
