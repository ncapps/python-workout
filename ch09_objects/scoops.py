class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor


def create_scoops():
    scoops = [Scoop(flavor)
              for flavor in ('chocolate', 'vanilla', 'cookie dough')]
    for scoop in scoops:
        print(scoop.flavor)


create_scoops()
