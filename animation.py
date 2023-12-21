import pygame

class Explosion(pygame.sprite.Sprite):

    def __init__(self, x, y, frames):
        super().__init__()
        self.frames = frames
        self.image = self.frames[0]  # Initial frame of the explosion
        self.rect = self.image.get_rect(center=(x, y))
        self.frame_index = 0
        self.animation_speed = 60  # Adjust animation speed as needed
        self.last_update = pygame.time.get_ticks()
        self.explosion_sound = pygame.mixer.Sound(r'assets/explosion/explosion_sound1.wav')

    def update(self):
        """
        Update the explosion animation
        :return: None
        """
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.kill()  # Remove the explosion sprite when animation ends
            else:
                self.image = self.frames[self.frame_index]
                self.rect = self.image.get_rect(center=self.rect.center)

    def play_sound(self):
        """
        Play the explosion sound
        :return: None
        """
        self.explosion_sound.play()