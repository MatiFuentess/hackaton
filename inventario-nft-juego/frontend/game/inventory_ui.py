import pygame
import json
import os
import requests
from typing import List, Dict

class InventoryUI:
    def __init__(self, screen):
        self.screen = screen
        self.items = []
        self.csgo_items = []
        self.selected_item = None
        self.font = pygame.font.Font(None, 32)
        self.small_font = pygame.font.Font(None, 24)
        self.load_items()
        self.load_csgo_items()
        
    def load_items(self):
        """Cargar items del inventario local"""
        cache_path = os.path.join("data", "inventory_cache.json")
        if os.path.exists(cache_path):
            with open(cache_path, "r") as f:
                self.items = json.load(f)
                
    def load_csgo_items(self):
        """Cargar items disponibles de CS:GO"""
        try:
            response = requests.get("http://localhost:8000/csgo/skins")
            if response.status_code == 200:
                self.csgo_items = response.json()[:20]  # Limitamos a 20 items para el ejemplo
        except requests.RequestException:
            print("Error al cargar items de CS:GO")
                
    def save_items(self):
        """Guardar items en caché local"""
        cache_path = os.path.join("data", "inventory_cache.json")
        os.makedirs("data", exist_ok=True)
        with open(cache_path, "w") as f:
            json.dump(self.items, f)
            
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si se hizo clic en un item
            mouse_pos = pygame.mouse.get_pos()
            self.handle_item_click(mouse_pos)
            
    def handle_item_click(self, pos):
        """Manejar clic en un item"""
        x, y = pos
        start_x = 50
        start_y = 50
        cell_size = 64
        padding = 10
        
        for i, item in enumerate(self.csgo_items):
            row = i // 8
            col = i % 8
            item_x = start_x + (cell_size + padding) * col
            item_y = start_y + (cell_size + padding) * row
            
            if (item_x <= x <= item_x + cell_size and 
                item_y <= y <= item_y + cell_size):
                self.selected_item = item
                print(f"Selected item: {item['name']}")
            
    def draw(self):
        """Dibujar la interfaz del inventario"""
        # Dibujar grid de items
        start_x = 50
        start_y = 50
        cell_size = 64
        padding = 10
        
        # Dibujar items de CS:GO
        for i, item in enumerate(self.csgo_items):
            row = i // 8
            col = i % 8
            x = start_x + (cell_size + padding) * col
            y = start_y + (cell_size + padding) * row
            
            # Dibujar slot del item
            color = (200, 200, 200)
            if item == self.selected_item:
                color = (150, 150, 250)
            pygame.draw.rect(self.screen, color, 
                           (x, y, cell_size, cell_size))
            
            # Dibujar nombre del item
            if item.get("name"):
                text = self.small_font.render(item["name"][:10] + "...", True, (0, 0, 0))
                self.screen.blit(text, (x + 5, y + cell_size - 20))
        
        # Dibujar información del item seleccionado
        if self.selected_item:
            self.draw_item_details() 

    def draw_item_details(self):
        """Dibujar detalles del item seleccionado"""
        # Panel de detalles a la derecha
        panel_x = 750
        panel_y = 50
        panel_width = 300
        panel_height = 400
        
        # Fondo del panel
        pygame.draw.rect(self.screen, (220, 220, 220),
                        (panel_x, panel_y, panel_width, panel_height))
        
        # Título
        title = self.font.render(self.selected_item["name"], True, (0, 0, 0))
        self.screen.blit(title, (panel_x + 10, panel_y + 10))
        
        # Rareza
        rarity = self.selected_item.get("rarity", {})
        rarity_color = pygame.Color(rarity.get("color", "#FFFFFF"))
        rarity_text = self.small_font.render(
            f"Rareza: {rarity.get('name', 'Common')}", 
            True, 
            rarity_color
        )
        self.screen.blit(rarity_text, (panel_x + 10, panel_y + 50))
        
        # Descripción
        desc = self.selected_item.get("description", "Sin descripción")
        words = desc.split()
        lines = []
        current_line = []
        
        for word in words:
            current_line.append(word)
            test_line = " ".join(current_line)
            if self.small_font.size(test_line)[0] > panel_width - 20:
                current_line.pop()
                lines.append(" ".join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(" ".join(current_line))
            
        for i, line in enumerate(lines[:8]):  # Limitamos a 8 líneas
            text = self.small_font.render(line, True, (0, 0, 0))
            self.screen.blit(text, (panel_x + 10, panel_y + 90 + i * 25))
            
        # Botón de Mintear
        mint_button_y = panel_y + panel_height - 50
        pygame.draw.rect(self.screen, (100, 200, 100),
                        (panel_x + 10, mint_button_y, 280, 40))
        mint_text = self.font.render("Mintear como NFT", True, (255, 255, 255))
        self.screen.blit(mint_text, (panel_x + 50, mint_button_y + 10)) 