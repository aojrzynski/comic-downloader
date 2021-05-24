"""Main file. Runs every"""

import tkinter as tkk
import interface

def main():
    """Starts Tkinter root, calls Interface class and keeps the main loop running."""
    root = tkk.Tk()
    interface.Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
