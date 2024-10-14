import pygame
import sys

if __name__ == '__main__':
    pygame.init()

    WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pygame Key Module Demonstration")

    font = pygame.font.Font(None, 28)
    large_font = pygame.font.Font(None, 36)

    input_box = pygame.Rect(50, 500, 700, 30)
    pygame.key.set_text_input_rect(input_box)

    # start handling text input events
    pygame.key.start_text_input()

    # enable key repeat with a delay of 500ms and interval of 50ms
    pygame.key.set_repeat(500, 50)

    # variables to hold text input
    user_text = ''
    text_input_active = True

    # Main loop
    clock = pygame.time.Clock()
    while True:
        screen.fill((30, 30, 30))

        focused = pygame.key.get_focused()
        focus_text = f"Keyboard Focused: {'Yes' if focused else 'No'}"
        focus_surface = font.render(focus_text, True, (255, 255, 255))
        screen.blit(focus_surface, (50, 20))

        repeat_delay, repeat_interval = pygame.key.get_repeat()
        repeat_text = f"Key Repeat - Delay: {repeat_delay}ms, Interval: {repeat_interval}ms"
        repeat_surface = font.render(repeat_text, True, (255, 255, 255))
        screen.blit(repeat_surface, (50, 60))

        mods = pygame.key.get_mods()
        mod_list = []
        if mods & pygame.KMOD_SHIFT:
            mod_list.append("Shift")
        if mods & pygame.KMOD_CTRL:
            mod_list.append("Ctrl")
        if mods & pygame.KMOD_ALT:
            mod_list.append("Alt")
        if mods & pygame.KMOD_CAPS:
            mod_list.append("CapsLock")
        if mods & pygame.KMOD_NUM:
            mod_list.append("NumLock")
        if mods & pygame.KMOD_MODE:
            mod_list.append("AltGr")
        mod_text = " + ".join(mod_list) if mod_list else "None"
        mods_surface = font.render(f"Modifier Keys: {mod_text}", True, (255, 255, 255))
        screen.blit(mods_surface, (50, 100))

        instructions = [
            "Type in the box below. Press ENTER to clear.",
            "Press F1 to simulate Shift key being held down.",
            "Press F2 to stop simulating Shift key.",
            "Click outside the input box to stop text input.",
        ]
        for idx, instr in enumerate(instructions):
            instr_surface = font.render(instr, True, (200, 200, 200))
            screen.blit(instr_surface, (50, 140 + idx * 30))

        pygame.draw.rect(screen, (50, 50, 50), input_box)
        pygame.draw.rect(screen, (255, 255, 255), input_box, 2)

        text_surface = font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    if not text_input_active:
                        pygame.key.start_text_input()
                        text_input_active = True
                else:
                    if text_input_active:
                        pygame.key.stop_text_input()
                        text_input_active = False

            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                key_code = event.key
                scancode = event.scancode
                unicode_char = event.unicode

                key_info = f"Key Down - Name: {key_name}, Code: {key_code}, Scancode: {scancode}, Unicode: {unicode_char}"
                key_info_surface = font.render(key_info, True, (255, 255, 0))
                screen.blit(key_info_surface, (50, 300))

                if event.key == pygame.K_RETURN:
                    user_text = ''

                elif event.key == pygame.K_F1:
                    pygame.key.set_mods(pygame.KMOD_SHIFT)

                elif event.key == pygame.K_F2:
                    pygame.key.set_mods(0)

                elif text_input_active and event.key != pygame.K_BACKSPACE:
                    user_text += event.unicode

                elif text_input_active and event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]

            elif event.type == pygame.TEXTINPUT and text_input_active:
                user_text += event.text

            elif event.type == pygame.TEXTEDITING:
                composition = event.text
                start = event.start
                length = event.length
                editing_info = f"Composing: {composition} (Start: {start}, Length: {length})"
                editing_surface = font.render(editing_info, True, (0, 255, 0))
                screen.blit(editing_surface, (50, 330))

        pygame.display.flip()
        clock.tick(1)
