from kidnapper import Kidnapper, Human

@Kidnapper.ransom
class Volunteer(Human):
    def say_name(self):
        print "I'm Volunteer"

