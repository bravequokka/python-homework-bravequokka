class Singer:
    def set_singer(self, name):
        self.name = name

    def hit_song(self, song):
        self.song = song

    def print_singer(self):
        print('가수이름 : {}' .format(self.name))

    
singer = Singer()
singer.set_singer('김동률')
singer.print_singer() 

class Song:
    def set_song(self, song, genre):
        self.song = song
        self.genre = genre

    def print_song(self):
        print('노래제목 : {}({})' .format(self.song, self.genre))

    
song = Song()
song.set_song('취중진담', '발라드')
song.print_song()  
