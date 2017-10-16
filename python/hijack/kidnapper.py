class Human(object):
    def say_name(self):
        raise NotImplementedError

class Kidnapper(object):
    _hostage = None
    class _Victim(Human):
        def say_name(self):
            print "I'm innocent"

    @classmethod
    def ransom(kls, human_kls):
        suffer = kls._hostage or kls._Victim
        kls._hostage = human_kls
        return suffer
