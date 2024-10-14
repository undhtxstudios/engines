import os
import pygame
import json
from constants import ASSETS_PATH, SUPPORTED_RESOLUTIONS

"""
Sprites clipped at runtime.

Assets Structure
---assets/spritesheets/
------resolution(s)
---------spritesheet.png
---------spritesheet.json

Notes: Spritesheet names should be unique (file extension does not count!)

Metadata JSON (*.json must match the associate *.png or *.psd)
{
  "animation1": { "numFrames": 4, "width": 64, "height": 64, "start_x": 0, "start_y": 0 },
  "animation2": { "numFrames": 6, "width": 64, "height": 64, "start_x": 0, "start_y": 64 },
}
"""
import os
import pygame
import json
from constants import ASSETS_PATH, SUPPORTED_RESOLUTIONS, ANIMATION_SPEED

class SpriteSheetMemoryOptimized:
    def __init__(self, resolution):
        if resolution not in SUPPORTED_RESOLUTIONS:
            raise ValueError(f"Resolution {resolution} not supported")

        self.resolution = resolution
        self.animations = {}
        self.sprite_sheets = {}
        self.frame_counters = {}
        # self.last_update_times = {}
        self.sprite_names = set()

        self._load_assets()

    def _load_assets(self):
        resolution_path = os.path.join(ASSETS_PATH, self.resolution)

        for file in os.listdir(resolution_path):
            if file.endswith(".png") or file.endswith(".psd"):
                sprite_sheet_path = os.path.join(resolution_path, file)
                sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
                sprite_name = file.split('.')[0]
                if sprite_name in self.sprite_names:
                    raise ValueError(f"duplicate spritesheet '{sprite_name}' found")
                self.sprite_names.add(sprite_name)
                self.sprite_sheets[sprite_name] = sprite_sheet

                json_path = os.path.join(resolution_path, f"{sprite_name}.json")
                with open(json_path) as f:
                    data = json.load(f)
                    for animation_name, metadata in data.items():
                        mapped_animation_name = f"{sprite_name}_{animation_name}"
                        self.animations[mapped_animation_name] = {
                            'numFrames': metadata['numFrames'],
                            'width': metadata['width'],
                            'height': metadata['height'],
                            'start_x': metadata['start_x'],
                            'start_y': metadata['start_y']
                        }
                        self.frame_counters[mapped_animation_name] = 0
                        # self.last_update_times[f"{sprite_name}_{animation_name}"] = pygame.time.get_ticks()

    def update_and_get_frame(self, sprite_name, animation_name):
        mapped_animation_name = f"{sprite_name}_{animation_name}"
        if mapped_animation_name not in self.animations:
            raise ValueError(f"Animation '{animation_name}' not found.")

        # current_time = pygame.time.get_ticks()
        # time_elapsed = current_time - self.last_update_times[mapped_animation_name]

        # if time_elapsed > ANIMATION_SPEED * 1000:
        #     self.frame_counters[animation_name] += 1
        #     self.last_update_times[animation_name] = current_time

        #     # Loop the animation if necessary
        #     if self.frame_counters[animation_name] >= self.animations[animation_name]['numFrames']:
        #         self.frame_counters[animation_name] = 0

        animation = self.animations[mapped_animation_name]
        sprite_sheet = self.sprite_sheets[sprite_name]

        self.frame_counters[mapped_animation_name] = (self.frame_counters[mapped_animation_name] + 1) % animation['numFrames']
        current_frame = self.frame_counters[mapped_animation_name]
        frame_width = animation['width']
        frame_height = animation['height']
        start_x = animation['start_x']
        start_y = animation['start_y']

        frame_x = start_x + (current_frame * frame_width)
        frame_y = start_y

        frame = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), (frame_x, frame_y, frame_width, frame_height))

        return frame
