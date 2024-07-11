from tkinter import *
import random
import sys


class Hangman:
    def __init__(self) -> None:
        self._window = self.Window(
            title="Hangman",
            layout=[[]],
            finalize=True,
            margins=(100, 100),
        )

    def read_event(self):
        event = self._window.read()
        event_id = event[0] if event is not None else None
        return event_id

    def close(self):
        self._window.close()
