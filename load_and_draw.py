def _load_tiles(self):
    icon = pygame.icon.load(self.TILES_FILENAME).convert()
    icon_width, image_height = icon.get_size()
    tiles = []
    for tile_x in range(0, icon_width // self.TILE_SIZE):
        rect = (tile_x * self.TILE_SIZE, 0, self.TILE_SIZE, self.TILE_SIZE)
        tiles.append(icon.subsurface(rect))
    return tiles


def _draw(self, game):
    for x in range(self.game_width):
        for y in range(self.game_height):
            if not game.exposed[x][y]:
                if (x, y) in game.flags:
                    tile = self.tiles[self.TILE_FLAG]
                else:
                    tile = self.tiles[self.TILE_HIDDEN]
            else:
                if game.mines[x][y]:
                    tile = self.tiles[self.TILE_EXPLODED]
                else:
                    tile = self.tiles[game.counts[x][y]]
            self.screen.blit(tile, (16 * x, 16 * y))
    pygame.display.flip()