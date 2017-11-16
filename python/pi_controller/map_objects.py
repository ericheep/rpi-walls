import pygame

class Object():
    """A Parent Class for map objects."""
    def __init__(self, ctl_settings, screen, panel, centerx, centery, width,
                 height, label):
        # initialize attributes
        self.ctl_settings = ctl_settings
        self.screen = screen
        self.panel = panel
        self.label = label

        self.on_color = (255, 255, 0)
        self.off_color = (100, 100, 100)
        self.color = self.off_color # starts off

        self.font = pygame.font.SysFont(None, 14)
        self.text_on_color = (0, 0, 0)
        self.text_off_color = (255, 255, 255)
        self.text_color = self.text_off_color # starts off

        # make rect
        self.centerx = centerx
        self.centery = centery
        self.width = width
        self.height = height

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        self.on = False # currently selected or not

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Prep wall label
        self.prep_label()

    def prep_label(self):
        self.label_image = self.font.render(self.label, True, self.text_color,
                                            self.color)
        self.label_image_rect = self.label_image.get_rect()
        self.label_image_rect.centerx = self.rect.centerx
        self.label_image_rect.centery = self.rect.centery

class Puppet(Object):
    """A circular icon to represent Puppet."""
    def __init__(self, ctl_settings, screen, panel, centerx, centery, label):

        # make box which circle will be drawn inside
        self.radius = 7
        self.diameter = self.radius * 2

        super().__init__(ctl_settings, screen, panel, centerx, centery,
                         self.diameter, self.diameter, label)

    def onoff(self):
        if self.on == False:
            self.on = True
            self.color = self.on_color
            self.text_color = self.text_on_color
            self.prep_label()
        else:
            self.on = False
            self.color = self.off_color
            self.text_color = self.text_off_color
            self.prep_label()
            # stop movement
            self.moving_left = False
            self.moving_right = False
            self.moving_up = False
            self.moving_down = False

    def update(self):
        #Update the position based on movement flags
        if self.on:
            # Update center value not the rect
            if self.moving_right and self.rect.right < self.panel.rect.right:
                self.centerx += self.ctl_settings.wall_speed_factor
            if self.moving_left and self.rect.left > self.panel.rect.left:
                self.centerx -= self.ctl_settings.wall_speed_factor
            if self.moving_up and self.rect.top > self.panel.rect.top:
                self.centery -= self.ctl_settings.wall_speed_factor
            if self.moving_down and self.rect.bottom < self.panel.rect.bottom:
                self.centery += self.ctl_settings.wall_speed_factor

            # Update rect object and label
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery
            self.prep_label()

    def draw_puppet(self):
        pygame.draw.circle(self.screen, self.color,
                           (self.centerx, self.centery), self.radius, 0)
        self.screen.blit(self.label_image, self.label_image_rect)


class Wall(Object):
    """Graphic wall icon"""
    def __init__(self, ctl_settings, screen, panel, centerx, centery, label):
        # set dimensions
        self.vertical = True  # False = horizontal
        self.long = 40
        self.short = 10
        super().__init__(ctl_settings, screen, panel, centerx, centery,
                         self.short, self.long, label)

    def update(self):
        #Update the position based on movement flags and rotate with
        # turn 'on' or not
        if self.on == True:
            self.color = self.on_color
            self.text_color = self.text_on_color
        else:
            self.color = self.off_color
            self.text_color = self.text_off_color

        # check collisions
        self.check_collisions()

        # Update wall's center value not the rect
        if self.moving_right and self.rect.right < self.panel.rect.right:
            if self.collisions > -1:
                self.moving_right = False
                self.centerx -= self.ctl_settings.wall_speed_factor
            else:
                self.centerx += self.ctl_settings.wall_speed_factor
        if self.moving_left and self.rect.left > self.panel.rect.left:
            if self.collisions > -1:
                self.moving_left = False
                self.centerx += self.ctl_settings.wall_speed_factor
            else:
                self.centerx -= self.ctl_settings.wall_speed_factor
        if self.moving_up and self.rect.top > self.panel.rect.top:
            if self.collisions > -1:
                self.moving_up = False
                self.centery += self.ctl_settings.wall_speed_factor
            else:
                self.centery -= self.ctl_settings.wall_speed_factor
        if self.moving_down and self.rect.bottom < self.panel.rect.bottom:
            if self.collisions > -1:
                self.moving_down = False
                self.centery -= self.ctl_settings.wall_speed_factor
            else:
                self.centery += self.ctl_settings.wall_speed_factor

        # Update rect object and label
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        self.prep_label()

    def rotate(self):
        # rotate
        self.perform_rotation()
        self.update()

        # reverse rotation if collision
        self.check_collisions()
        if self.collisions > -1:
            self.perform_rotation()
            self.update()

    def perform_rotation(self):
        if self.vertical == True:
            self.vertical = False
            self.rect = pygame.Rect(self.centerx, self.centery, self.long,
                                    self.short)
        else:
            self.vertical = True
            self.rect = pygame.Rect(self.centerx, self.centery, self.short,
                                    self.long)
            self.update()

    def check_collisions(self):
        # check collisions
        self.other_walls = []
        for wall in self.panel.walls:
            if wall != self:
                self.other_walls.append(wall)
        self.collisions = self.rect.collidelist(self.other_walls)

    def draw_wall(self):
        # Draw wall and label
        pygame.draw.rect(self.screen, self.color, self.rect)
        #self.screen.fill(self.color, self.rect)
        self.screen.blit(self.label_image, self.label_image_rect)