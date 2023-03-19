class GlobalInfo:
    def __init__(self):
        self.surah_num = 0
        self.ayah_num = 1

    def new_surah(self):
        self.surah_num += 1
        self.ayah_num = 1

    def next_ayah(self):
        self.ayah_num += 1