from scoops import Scoop


class Bowl():
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(scoop.flavor for scoop in self.scoops)


if __name__ == '__main__':
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')

    b = Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    b.add_scoops(s3)
    print(b)
