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
        self.era = stats[0].strip()
        self.g = stats[1].strip()
        self.gs = stats[2].strip()
        self.gf = stats[3].strip()
        self.cg = stats[4].strip()
        self.sho = stats[5].strip()
        self.sv = stats[6].strip()
        self.ip = stats[7].strip()
        self.h = stats[8].strip()
        self.r = stats[9].strip()
        self.er = stats[10].strip()
        self.hr = stats[11].strip()
        self.bb = stats[12].strip()
        self.ibb = stats[13].strip()
        self.so = stats[14].strip()
        self.hbp = stats[15].strip()
        self.bk = stats[16].strip()
        self.wp = stats[17].strip()
        self.bf = stats[18].strip()
        self.eraplus = stats[19].strip()
        self.fip = stats[20].strip()
        self.whip = stats[21].strip()
        self.h9 = stats[22].strip()
        self.hr9 = stats[23].strip()
        self.bb9 = stats[24].strip()
        self.so9 = stats[25].strip()
        self.sow = stats[26].strip()