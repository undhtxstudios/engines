# time / https://www.pygame.org/docs/ref/time.html

# get the time in milliseconds since pygame.init() was called
# pygame.time.get_ticks() -> milliseconds

# pause the program for an amount of time (less accurate)
# pygame.time.wait(milliseconds) -> time

# pause the program for an amount of time (more accurate)
# pygame.time.delay(milliseconds) -> time

# repeatedly create an event on the event queue
# pygame.time.set_timer(event, millis, loops=0) -> none

# create an object to help track time
# pygame.time.clock() -> clock

# update the clock, possibly limiting the framerate
# pygame.time.Clock.tick(framerate=0) -> milliseconds

# update the clock, with more accurate timing (uses more cpu)
# pygame.time.Clock.tick_busy_loop(framerate=0) -> milliseconds

# get the time used in the previous tick
# pygame.time.Clock.get_time() -> milliseconds

# get the actual time used in the previous tick (excluding delay time)
# pygame.time.Clock.get_rawtime() -> milliseconds

# compute the clock framerate
# pygame.time.Clock.get_fps() -> float
