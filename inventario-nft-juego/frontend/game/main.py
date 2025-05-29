import pygame
import sys
from inventory_ui import InventoryUI
from wallet_connect import WalletConnect

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1100  # Aumentado para acomodar el panel de detalles
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("CS:GO NFT Inventory")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialize components
        self.inventory = InventoryUI(self.screen)
        self.wallet = WalletConnect()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.inventory.handle_event(event)
            
    def update(self):
        pass
        
    def draw(self):
        self.screen.fill(WHITE)
        self.inventory.draw()
        pygame.display.flip()
        
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit() 