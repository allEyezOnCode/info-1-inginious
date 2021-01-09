def set_a(self, n_a):
    self.a = n_a
    try:
        self.ordered = self.a <= self.b
    except: pass

def set_b(self, n_b):
    self.b = n_b
    try:
        self.ordered = self.a <= self.b
    except: pass
