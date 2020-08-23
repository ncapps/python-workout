from scoops import Scoop
from bowl import Bowl

class BigBowl(Bowl):
    max_scoops = 5


if __name__ == '__main__':
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')
    s4 = Scoop('chocolate')
    s5 = Scoop('vanilla')
    s6 = Scoop('persimmon')

    b = BigBowl()
    b.add_scoops(s1, s2, s3, s4, s5, s6)
    print(b)