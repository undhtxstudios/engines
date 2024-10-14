import pygame
from constants import *
from ref import *

# just a redundant wrapper, will remove later
class Music:
    def __init__(self):
        pygame.mixer.init()
        self.volume = DEFAULT_VOLUME_LEVEL

    def load_music(self, filename):
        pygame.mixer.music.load(filename)

    def unload_music(self):
        pygame.mixer.music.unload()

    def play_music(self, loops=0, start=0.0, fade_ms=0):
        pygame.mixer.music.play(loops, start, fade_ms)

    def rewind_music(self):
        pygame.mixer.music.rewind()

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def fadeout_music(self, time):
        pygame.mixer.music.fadeout(time)

    def set_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(volume)

    def get_volume(self):
        return pygame.mixer.music.get_volume()

    def is_playing(self):
        return pygame.mixer.music.get_busy()

    def set_position(self, pos):
        pygame.mixer.music.set_pos(pos)

    def get_position(self):
        return pygame.mixer.music.get_pos()

    def queue_music(self, filename):
        pygame.mixer.music.queue(filename)

    def set_end_event(self, event_type=None):
        pygame.mixer.music.set_endevent(event_type)

    def get_end_event(self):
        return pygame.mixer.music.get_endevent()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))
    pygame.display.flip()
    pygame.display.set_caption("Music Menu")

    music_player = Music()
    music_player.load_music(MUSIC_FILE)
    music_player.play_music(0, 0, FADEOUT_TIME)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if music_player.is_playing():
                        music_player.pause_music()
                    else:
                        music_player.unpause_music()
                elif event.key == pygame.K_s:
                    music_player.stop_music()
                elif event.key == pygame.K_r:
                    music_player.rewind_music()
                elif event.key == pygame.K_q:
                    music_player.queue_music(QUEUE_MUSIC_FILE)
                elif event.key == pygame.K_UP:
                    music_player.set_volume(min(music_player.get_volume() + 0.1, 1.0))
                elif event.key == pygame.K_DOWN:
                    music_player.set_volume(max(music_player.get_volume() - 0.1, 0.0))

    pygame.quit()

if __name__ == "__main__":
    main()
