"""
https://www.pygame.org/docs/ref/event.html

Pump / pygame.event.pump()
Appllication responsive to system events.

Get / pygame.event.get()
    get(eventtype=None) -> Eventlist
    get(eventtype=None, pump=True) -> Eventlist
    get(eventtype=None, pump=True, exclude=None) -> Eventlist

    If you are only taking specific events from the queue,
    be aware that the queue could eventually fill up with the events you are not interested.

Poll / pygame.event.poll()
    Gets a single event from the queue returning NoEvent immediately
    if no events are on the queue.    

Wait / pygame.event.wait()
    wait() -> Event instance
    wait(timeout) -> Event instance

    Returns a single event from the queue. 
    If the queue is empty this function will wait until one is created.
    The function will return an event of type pygame.NOEVENT if no events enter the queue in timeout milliseconds.
    The event is removed from the queue once it has been returned. 
    While the program is waiting it will sleep in an idle state.

Peek / pygame.event.peek()
    peek(eventtype=None) -> bool
    peek(eventtype=None, pump=True) -> bool

    Returns True if there are any events of the given type waiting on the queue.
    If a sequence of event types is passed, this will return True if any of those events are on the queue.

Clear / pygame.event.clear()
    clear(eventtype=None) -> None
    clear(eventtype=None, pump=True) -> None

    Removes all events from the queue.
    If eventtype is given, removes the given event or sequence of events.
    This has the same effect as pygame.event.get() except None is returned. 

GetName / pygame.event.event_name()
    event_name(type) -> string

    Returns a string representing the name (in CapWords style) of the given event type.
    "UserEvent" is returned for all values in the user event id range. 
    "Unknown" is returned when the event type does not exist.

Block / pygame.event.set_blocked()
    set_blocked(type) -> None
    set_blocked(typelist) -> None
    set_blocked(None) -> None

    The given event types are not allowed to appear on the event queue.
    If None is passed as the argument, ALL of the event types are blocked from being placed on the queue.

Allow / pygame.event.set_allowed()
    set_allowed(type) -> None
    set_allowed(typelist) -> None
    set_allowed(None) -> None
    
    The given event types are allowed to appear on the event queue. 
    If None is passed as the argument, ALL of the event types are allowed to be placed on the queue.

Post / pygame.event.post()
    post(Event) -> bool

        Places the given event at the end of the event queue.
        This is usually used for placing custom events on the event queue.
        Returns a boolean on whether the event was posted or not.

Custom Event / pygame.event.custom_type()
    custom_type() -> int

    Reserves a pygame.USEREVENT for a custom use.
    If too many events are made a pygame.errorstandard pygame exception is raised.

Event object
    Event(type, dict) -> Event
    Event(type, **attributes) -> Event
    
    pygame.event.Event.type: event type identifier.
    pygame.event.Event.__dict__: event attribute dictionary
"""