from kidnapper import Kidnapper, Human

@Kidnapper.ransom
class Sacrifice(Human):
    def say_name(self):
        print "I'm Sacrifice"
