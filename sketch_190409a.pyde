class superbohater():
    def __init__(self,moc,tr,kostium):
        self.supermoc = moc
        self.tregedia = tr
        self.stroj = kostium
        self.pokonani_wrogowie = 0
    def get_pokonani_wrogowie(self):
        return self.pokonani_wrogowie
    def set_pokonani_wrogowie(self, ilosc):
        self.pokonani_wrogowie = ilosc
    def pokonanj_wroga(self):
        self.pokonani_wrogowie +=1
        print ("wróg pokonany")
        return pokonani_wrogowie
    def zmien_stroj(self,kostium):
        self.stroj = kostium
def setup():
    global Batman
    global Spiderman
    Batman = superbohater("supersiła","trudne dzieciństwo","ministranta")
    Spiderman = superbohater("sieci","smierc wujka","stroj pajaka")
def draw():
    Batman.zmien_stroj("specjalny")
    Batman.pokonaj_wroga()
    Spiderman.zmien_stroj("codzienny")
