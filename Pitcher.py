class Pitcher(object):
    def __init__(self, n, a, t, l):
        self.name = n
        self.age = a
        self.team  = t
        self.league = l
    def set_wl(self, w, l, p):
        self.wins = w
        self.losses = l
        self.w_l = p
