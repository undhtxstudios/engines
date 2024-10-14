import pygame
from constants import *

class SoundManager:
    def __init__(self, sound_paths, channel_count=CHANNEL_COUNT):
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
        pygame.mixer.init()
        
        self.sound_effects = {}
        self.channels = []
        self.enabled = True

        # load all effects
        for sound_name, path in sound_paths.items():
            self.sound_effects[sound_name] = pygame.mixer.Sound(path)
        
        pygame.mixer.set_num_channels(channel_count)
        
        # init channels
        for i in range(channel_count):
            self.channels.append(pygame.mixer.Channel(i))

    def play_sound(self, sound_name, loops=0, maxtime=0, fade_ms=0):
        if self.enabled and sound_name in self.sound_effects:
            self.sound_effects[sound_name].play(loops=loops, maxtime=maxtime, fade_ms=fade_ms)

    def stop_all_sounds(self):
        pygame.mixer.stop()

    def fadeout_sound(self, sound_name, time=FADEOUT_TIME_MS):
        if sound_name in self.sound_effects:
            self.sound_effects[sound_name].fadeout(time)

    def enable_sounds(self):
        self.enabled = True

    def disable_sounds(self):
        self.enabled = False
        self.stop_all_sounds()

    def stop_sound(self, sound_name):
        if sound_name in self.sound_effects:
            self.sound_effects[sound_name].stop()

    def set_volume(self, sound_name, volume):
        if sound_name in self.sound_effects:
            self.sound_effects[sound_name].set_volume(volume)

    def get_volume(self, sound_name):
        if sound_name in self.sound_effects:
            return self.sound_effects[sound_name].get_volume()

    def quit_mixer(self):
        pygame.mixer.quit()

    def reserve_channels(self, num_channels):
        pygame.mixer.set_reserved(num_channels)

    def find_channel(self, force=False):
        return pygame.mixer.find_channel(force=force)

if __name__ == "__main__":
    sound_paths = {
        SOUND_PATH1: SOUND_PATH1,
        SOUND_PATH2: SOUND_PATH2,
        SOUND_PATH3: SOUND_PATH3,
    }
    
    pygame.init()
    sound_manager = SoundManager(sound_paths)

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Sound Effects")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    sound_manager.play_sound(SOUND_PATH1)
                elif event.key == pygame.K_2:
                    sound_manager.play_sound(SOUND_PATH2)
                elif event.key == pygame.K_3:
                    sound_manager.play_sound(SOUND_PATH3)

        pygame.display.flip()
    
    sound_manager.quit_mixer()
    pygame.quit()
    
