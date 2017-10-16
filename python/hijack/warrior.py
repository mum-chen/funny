from kidnapper import Kidnapper, Human

@Kidnapper.ransom
class Warrior(Human):
    def say_name(self):
        print "I'm Warrior"
