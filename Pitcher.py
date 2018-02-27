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
    def set_stats(self, stats):
        self.era = stats[0]
        self.g = stats[1]
        self.gs = stats[2]
        self.gf = stats[3]
        self.cg = stats[4]
        self.sho = stats[5]
        self.sv = stats[6]
        self.ip = stats[7]
        self.h = stats[8]
        self.r = stats[9]
        self.er = stats[10]
        self.hr = stats[11]
        self.bb = stats[12]
        self.ibb = stats[13]
        self.so = stats[14]
        self.hbp = stats[15]
        self.bk = stats[16] 
        self.wp = stats[17]
        self.bf = stats[18]
        self.eraplus = stats[19]
        self.fip = stats[20]
        self.whip = stats[21]
        self.h9 = stats[22]
        self.hr9 = stats[23]
        self.bb9 = stats[24]
        self.so9 = stats[25]
        self.sow = stats[26]