import os
import time

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

frames = [
    """
    (*_*)
    """,
    """
    (o_o)
    """,
    """
    (^_^)
    """
]

def animate(frames, delay=0.5, repetitions=5):
    for _ in range(repetitions):
        for frame in frames:
            clear_console()
            print(frame)
            time.sleep(delay)

if __name__ == "__main__":
    animate(frames)
