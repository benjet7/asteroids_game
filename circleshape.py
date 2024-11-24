import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other_object):
        distance = pygame.math.Vector2.distance_to(self.position, other_object.position)
        #print(f"DISTANCE: {distance}, {self} radius: {self.radius}, {other_object} radius: {other_object.radius}")
        if self.radius + other_object.radius < distance:
            return False
        else:
            return True