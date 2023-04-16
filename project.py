import random
import sys

class Monster:
    def __init__(self, name, level):
        self._name = name
        self._level = level
        self._maxhp = 10
        self._hp = 10
        self._lasthp = self._hp
    def __str__(self):
        return f"[{self._name}] HP: {self._hp:} {'❤️ ' * self._hp}"
    @property
    def level(self):
        return self._level
    @property
    def name(self):
        return self._name
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, hp):
        self._hp = hp
    @property
    def lasthp(self):
        return self._lasthp
    @lasthp.setter
    def lasthp(self, lasthp):
        self._lasthp = lasthp
    def attack(self, to_whom):
        hurt = random.randint(1, self.level)
        if to_whom._hp - hurt > 0:
            to_whom._hp -= hurt
        else:
            to_whom._hp = 0
        print(f"===== {self.name} attack! hurt: {hurt} =====")
    def defense(self, from_whom):
        print(f"===== {self.name} defense! =====")

class Ghost(Monster):
    def __init__(self, name, level):
        super().__init__(name, level)
        self._magic = "threaten"
    @classmethod
    def create(cls, level):
        return cls("👻 Ghost", level)

class Alien(Monster):
    def __init__(self, name, level):
        super().__init__(name, level)
        self._magic = "rebound"
    @classmethod
    def create(cls, level):
        return cls("👽 Alien", level)

def set_level():
    while True:
        try:
            ghost_level = int(input("input your level between 1 and 3: "))
        except ValueError:
            pass
        except EOFError:
            sys.exit("\nQuit, goodbye ~")
        else:
            if 1 <= ghost_level <= 3:
                return ghost_level

def action_choice():
    while True:
        try:
            action = int(input("Choose your action: "))
        except ValueError:
            pass
        except EOFError:
            sys.exit("\nQuit, goodbye ~")
        else:
            if action not in [1, 2, -1]:
                continue
            return action

def game_over():
    return f"\nGame Over ~"

def play():
    ghost_level = set_level()
    alien_level = random.randint(1, 3)
    ghost = Ghost.create(ghost_level)
    alien = Alien.create(alien_level)
    methods = [alien.attack, alien.defense]

    action = None
    while action != -1 and (ghost.hp > 0 and alien.hp > 0):
        print(f"{ghost}")
        print(f"{alien}")
        print("\ntype int number for your action\n(1) attack (2) defense (-1) quit this game")
        action = action_choice()
        print()
        match action:
            case 1:
                alien.lasthp = alien.hp
                hurt = ghost.attack(alien)
                choice = random.choice(methods)
                if choice == alien.defense:
                    alien.hp = alien.lasthp
                choice(ghost)
            case 2:
                choice = random.choice(methods)
                if choice == alien.attack:
                    ghost.lasthp = ghost.hp
                    choice(ghost)
                    ghost.hp = ghost.lasthp
                else:
                    choice(ghost)
                ghost.defense(alien)
            case -1:
                break

    print(game_over())
    print(f"[{ghost.name}] remain HP: {ghost.hp:} {'❤️ ' * ghost.hp}")
    print(f"[{alien.name}] remain HP: {alien.hp:} {'❤️ ' * alien.hp}")
    print(f"\n[🏆🏆🏆] Finally, the winner is [{ghost.name}] !!!") if ghost.hp > alien.hp else print(f"\n[🏆🏆🏆] Finally, the winner is [{alien.name}] !!!")


def main():
    play()

if __name__ == "__main__":
    main()