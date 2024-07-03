import pygame


SCREEN_SIZE = (1000, 800) 
H_MARGIN = 2


MASKS = [
    # TODO: 0
    [0,1,1,0,0,0,0], # this is one
    # TODO: 2
    ...
]


class SevenSegmentDisplay:
    def __init__(self, mask: tuple[int, int, int, int, int, int, int], width: int):
        """
        mask: a tuple of 7 integers representing the state of the segments
        width: the width of the display in pixels
        """
        self.mask = mask
        self.width = width
        self.surface = pygame.Surface((width, width * 2))
        self.apply_segments()

    def apply_segments(self):
        # TODO
        ...
    
    def render(self, surface: pygame.Surface, pos: tuple[int, int]) -> None:
        surface.blit(self.surface, pos)


class Window:
    def __init__(self):
        self.screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
        self.background: pygame.Surface = pygame.Surface(SCREEN_SIZE)

        self.running = True

        self.digits = []

    def render_digits(self):
        # TODO: render all 10 digits in random locations
        ...
    
    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False

    def run(self):
        """Run the main game loop."""
        pygame.init()
        pygame.display.set_caption("Game of Life")

        clock = pygame.time.Clock()
        while self.running:
            time_delta = clock.tick(60) * 0.001
            
            for event in pygame.event.get():
                self.process_event(event)

            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
        pygame.quit()
