from .maze import Maze
import tkinter as tk


def main():
    root = tk.Tk()
    frame = tk.Frame(root, width=100, height=100)
    frame.pack()
    root.update()
    print("frame height: " + str(frame.winfo_height()))
    print("frame width: " + str(frame.winfo_width()))
    m = Maze(frame)
    for x in range(1, 50):
        for y in range(1, 50):
            m.add_square((x, y))
    root.update()
    print("frame height: " + str(frame.winfo_height()))
    print("frame width: " + str(frame.winfo_width()))

    # m.add_wall((5, 5), m.Direction.Left)
    # m.add_wall((5, 5), m.Direction.Right)
    # m.add_wall((5, 5), m.Direction.Up)
    # m.add_wall((5, 5), m.Direction.Down)

    # m.add_wall((15, 5), m.Direction.Right)
    # m.add_wall((15, 5), m.Direction.Up)
    # m.add_wall((15, 5), m.Direction.Down)
    # m.add_wall((15, 5), m.Direction.Left)

    root.mainloop()


if __name__ == "__main__":
    main()
