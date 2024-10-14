import pygame
import sys

FPS = 30

def display_message(screen, message, position):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (255, 255, 255))
    screen.blit(text, position)
    pygame.display.flip()

def time_methods(screen):
    # display the time since the game started
    milliseconds = pygame.time.get_ticks()
    seconds = milliseconds // 1000
    display_message(screen, f"Game time / get_ticks(): {seconds} s", (10, 10))
    
    # wait and delay
    pygame.time.wait(500)
    print(screen, "wait(500 ms)", (10, 50))

    delay_time = pygame.time.delay(300)
    print(screen, f"delay(300 ms) -> {delay_time} ms", (10, 90))

def clock_methods(screen, clock):
    clock.tick(FPS)  
    tick_time = clock.get_time()
    print(screen, f"Clock.get_time(): {tick_time} ms", (10, 130))

    raw_time = clock.get_rawtime()
    print(screen, f"Clock.get_rawtime(): {raw_time} ms", (10, 170))

    fps = clock.get_fps()
    print(screen, f"Clock.get_fps(): {fps:.2f} FPS", (10, 210))

def main():
    pygame.init()
    pygame.time.set_timer(pygame.USEREVENT, 2000)  # trigger event every 2 seconds

    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                print(screen, "Timer Event Triggered!", (200, 220))

        screen.fill((0, 0, 0))

        time_methods(screen)
        clock_methods(screen, clock)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
