import enum
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import operator

MAZE_ROOT = 10, 10
PIXELS_PER_SQUARE = 20


# Given a tkinter frame, will attempt to generate and render a maze within it.
class Maze:
    class Direction(enum.Enum):
        Left = 1
        Right = 2
        Up = 3
        Down = 4

    def __init__(self, frame: tk.Frame, height_in_squares, width_in_squares):
        self.canvas = tk.Canvas(frame, bg="grey", height=1000, width=1000)
        self.button = tk.Button(frame, text="Popup",
                                command=Maze.popupCallback)
        self.height = frame.winfo_height() * PIXELS_PER_SQUARE * height_in_squares
        self.width = frame.winfo_width() * PIXELS_PER_SQUARE * width_in_squares
        self.canvas.pack()
        self.button.pack()

    def add_wall(self, center_coords, direction):
        start_offset = None
        end_offset = None
        if direction == Maze.Direction.Left:
            start_offset = -1, -1
            end_offset = -1, 1
        elif direction == Maze.Direction.Right:
            start_offset = 1, -1
            end_offset = 1, 1
        elif direction == Maze.Direction.Up:
            start_offset = -1, -1
            end_offset = 1, -1
        elif direction == Maze.Direction.Down:
            start_offset = -1, 1
            end_offset = 1, 1
        else:
            print("Error")
            return

        scaled_center_coords = Maze.tuple_mul(PIXELS_PER_SQUARE, center_coords)
        wall_start = Maze.tuple_add(scaled_center_coords,
                                    Maze.tuple_mul(PIXELS_PER_SQUARE/2, start_offset))
        wall_end = Maze.tuple_add(
            scaled_center_coords, Maze.tuple_mul(PIXELS_PER_SQUARE/2, end_offset))
        self.canvas.create_line(wall_start + wall_end, width=2)

    def add_square(self, center_coords):
        for direction in Maze.Direction:
            self.add_wall(center_coords, direction)

    @ staticmethod
    def tuple_add(t1, t2):
        return tuple(item1 + item2 for item1, item2 in zip(t1, t2))

    @ staticmethod
    def tuple_mul(scalar, tup):
        return tuple(scalar * item for item in tup)

    @ staticmethod
    def popupCallback():
        tkMessageBox.showinfo("Name", "Popup!")
