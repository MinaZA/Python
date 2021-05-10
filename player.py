class Player(pygame.sprite.Sprite):
"""new player thing"""

    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.images = []
        self.pv = 20
        self.name = name

        img = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()