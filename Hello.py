import random


class Enemy:

    def __init__(self, atackl = 60, atackh= 80):
        self.atackl = atackl
        self.atackh = atackh


    def getatack(self):
        print(self.atackl)

get = Enemy(80, 60)
get.getatack()

get1 = Enemy(60, 89)
get1.getatack()






#
# while p > 0:
#     dmg = random.randrange(m, n)
#     p = p - dmg
#     if p <= 30:
#         p = 30
#     print("enmy stries for ", dmg, "points of damage", "current damage is", p)
#
#     if p > 30:
#         continue
#     print("Low helth not able to play")
#     break








































