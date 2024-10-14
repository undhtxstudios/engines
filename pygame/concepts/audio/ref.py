"""
Music / https://www.pygame.org/docs/ref/music.html

pygame.mixer.music.load(filename or fileobj, namehint="") -> none
    load a music file for playback

pygame.mixer.music.unload() -> none
    unload the currently loaded music to free up resources

pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0) -> none
    start the playback of the music stream

pygame.mixer.music.rewind() -> none
    restart music from the beginning

pygame.mixer.music.stop() -> none
    stop the music playback

pygame.mixer.music.pause() -> none
    temporarily stop music playback

pygame.mixer.music.unpause() -> none
    resume paused music playback

pygame.mixer.music.fadeout(time) -> none
    stop music playback after fading out

pygame.mixer.music.set_volume(volume) -> none
    set the music volume (0.0 to 1.0)

pygame.mixer.music.get_volume() -> float
    get the current music volume

pygame.mixer.music.get_busy() -> bool
    check if the music stream is playing

pygame.mixer.music.set_pos(pos) -> none
    set position to play from

pygame.mixer.music.get_pos() -> int
    get the music play time in milliseconds

pygame.mixer.music.queue(filename or fileobj, namehint="", loops=0) -> none
    queue a sound file to follow the current one

pygame.mixer.music.set_endevent(type=none) -> none
    have the music send an event when playback stops

pygame.mixer.music.get_endevent() -> int
    get the event type that will be sent when playback stops
"""

"""
Mixer / https://www.pygame.org/docs/ref/mixer.html

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=none, allowedchanges=audio_allow_frequency_change | audio_allow_channels_change)
    initialize the mixer module

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=none, allowedchanges=audio_allow_frequency_change | audio_allow_channels_change)
    preset the mixer init arguments

pygame.mixer.quit()
    uninitialize the mixer

pygame.mixer.get_init()
    test if the mixer is initialized

pygame.mixer.stop()
    stop playback of all sound channels

pygame.mixer.pause()
    temporarily stop playback of all sound channels

pygame.mixer.unpause()
    resume paused playback of sound channels

pygame.mixer.fadeout(time)
    fade out the volume on all sounds before stopping

pygame.mixer.set_num_channels(count)
    set the total number of playback channels

pygame.mixer.get_num_channels()
    get the total number of playback channels

pygame.mixer.set_reserved(count)
    reserve channels from being automatically used

pygame.mixer.find_channel(force=false)
    find an unused channel

pygame.mixer.get_busy()
    test if any sound is being mixed

pygame.mixer.get_sdl_mixer_version(linked=true)
    get the mixer's sdl version


# sound
play(loops=0, maxtime=0, fade_ms=0): plays the sound.
stop(): stops the sound.
fadeout(time): fades out the sound over a given time.
set_volume(value): sets the volume (0.0 to 1.0).
get_volume(): returns the current volume.
get_num_channels(): returns the number of times this sound is playing.
get_length(): returns the length of the sound.
get_raw(): returns a bytestring copy of the sound samples.

# channel
play(sound, loops=0, maxtime=0, fade_ms=0): plays a sound on this channel.
stop(): stops playback on this channel.
pause(): pauses playback.
unpause(): resumes paused playback.
fadeout(time): fades out sound and stops playback.
set_volume(value): sets volume (0.0 to 1.0).
get_volume(): returns current volume.
get_busy(): returns true if the channel is in use.
queue(sound): queues a sound to follow the current one.
get_sound(): returns the currently playing sound.
"""
