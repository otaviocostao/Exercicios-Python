class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando...')
            return
        
        print(f'{self.nome} parou de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar pois está filmando...')
            return
        
        print(f'{self.nome} está fotografando...')

camera1 = Camera('Cannon')
camera2 = Camera('Sony')
camera1.filmar()
camera1.fotografar()
camera1.parar_filmar()
camera1.fotografar()

print(camera1.filmando)