from .maze import Maze
import tkinter as tk


def main():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    m = Maze(frame, 100, 100)
    m.add_wall((50, 50), m.Direction.Left)
    m.add_wall((50, 50), m.Direction.Right)
    m.add_wall((50, 50), m.Direction.Up)
    m.add_wall((50, 50), m.Direction.Down)
    root.mainloop()


if __name__ == "__main__":
    main()
