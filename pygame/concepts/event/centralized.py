import pygame

from constants import SUCCESS, FAIL, EVENT_HANDLERS

class CentralizedEventManager:
    """{event_type: (listeners)}"""
    def __init__(self):
        self.handlers = {}
        
    def register_event(self, event_type, *listeners):
        if event_type not in self.handlers:
            self.handlers[event_type] = set()
        self.handlers[event_type].update(listeners)

    def unregister_event(self, event_type):
        if event_type in self.handlers:
            del self.handlers[event_type]
            return SUCCESS
        return FAIL

    def add_listeners(self, event_type, *listeners):
        if event_type in self.handlers:
            self.handlers[event_type].update(listeners)
            return SUCCESS
        return FAIL
    
    def remove_listeners(self, event_type, *listeners):
        if event_type in self.handlers:
            self.handlers[event_type].difference_update(set(listeners))
            return SUCCESS
        return FAIL
    
    def handle_events(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type in self.handlers:
                for listener in self.handlers[event.type]:
                    listener(event)
    
    def post_custom_event(self, custom_type, attributes):
        return pygame.event.post(pygame.event.Event(custom_type, attributes))

    def load_handlers(self):
        for event_type, listeners in EVENT_HANDLERS.items():
            if event_type not in self.handlers:
                self.handlers[event_type] = set()
            self.handlers[event_type].update(set(listeners))

    def get_events(self, eventtype=None, pump=True, exclude=None):
        return pygame.event.get(eventtype=eventtype, pump=pump, exclude=exclude)
    
    def poll_event(self):
        return pygame.event.poll()

    def wait_for_event(self, timeout=None):
        return pygame.event.wait(timeout=timeout)

    def peek_event(self, eventtype=None, pump=True):
        return pygame.event.peek(eventtype=eventtype, pump=pump)

    def clear_events(self, eventtype=None, pump=True):
        pygame.event.clear(eventtype=eventtype, pump=pump)

    def get_event_name(self, event_type):
        return pygame.event.event_name(event_type)

    def block_events(self, event_type):
        pygame.event.set_blocked(event_type)

    def allow_events(self, event_type):
        pygame.event.set_allowed(event_type)

    def post_event(self, event):
        return pygame.event.post(event)

    def create_custom_event(self):
        return pygame.event.custom_type()
