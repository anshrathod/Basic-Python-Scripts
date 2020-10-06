""" Snake Game """

import tkinter as tk
import random

#### GLOBAL VARIALBES ####
SNAKE_COLOR, FOOD_COLOR= "light green", "red"
BG_COLOR, TEXT_COLOR = "black", "white"
WIDTH = 40 #Width of squares in pixels.
FOOD_WIDTH = WIDTH * 3 / 4 #Width of food squares in pixels.
SPEED = 100 #Milliseconds between redraw.
CUSHION = 1 #Applied so that adjacent squares don't overlap.
SCREEN = WIDTH * 30, WIDTH * 17 #Screen size in pixels.
FONT = "ms 70"

MAX_T = 1000 // SPEED * 5 #Max steps until food disappears.
FOOD_PROB = 0.04 #Probability a new food appears at any given step.
CONTROLS = LEFT, RIGHT, UP, DOWN = "Left", "Right", "Up", "Down"
EXIT, CHEAT, RESTART = "Escape", "space", "Return"

###############################################################################

def apply_cushion(rect_def):
    """
    Adjust bounds of a rectangular definition.
    rect_def: tuple, (x, y, x+width, y+width).
    """
    x0, y0, x1, y1 = rect_def
    return x0 + CUSHION, y0 + CUSHION, x1 - CUSHION, y1 - CUSHION
	

class Square(object):
    """
    Controls one section of the snake.
    canvas: tk.Canvas object to draw on.
    rect_def: tuple, (x, y, x+WIDTH, y+WIDTH).
    """
    def __init__(self, canvas, rect_def):
        self.square = canvas.create_rectangle(*rect_def, fill=SNAKE_COLOR)
        self.can, self.rect_def = canvas, rect_def
        self.behind, self.dx, self.dy = False, 1, 0

    def draw(self, rect_def):
        dx = rect_def[0] - self.rect_def[0]
        dy = rect_def[1] - self.rect_def[1]
        self.dx = dx if not dx else dx // abs(dx)
        self.dy = dy if not dy else dy // abs(dy)

        self.can.coords(self.square, *rect_def)
        self.rect_def = rect_def
        if self.behind:
            r = self.get_behind_rect_def()
            self.behind.draw(r)

    def add_behind(self):
        if self.behind:
            self.behind.add_behind()
        else:
            r = self.get_behind_rect_def()
            self.behind = Square(self.can, r)

    def get_behind_rect_def(self):
        x0, y0, x1, y1 = self.rect_def
        r = (
            x0 - self.dx * WIDTH, y0 - self.dy * WIDTH,
            x1 - self.dx * WIDTH, y1 - self.dy * WIDTH
        )
        return r

    def get(self):
        return self.square

    def get_overlapping(self):
        return self.can.find_overlapping(*apply_cushion(self.rect_def))

    def intersecting(self, overlapping):
        if self.behind:
            return any((
                self.behind.get() in overlapping,
                self.behind.intersecting(overlapping)
            ))
        else:
            return False
			

class Snake(object):
    """
    Controls the movement of the snake.
    canvas: tk.Canvas to draw on.
    """
    def __init__(self, canvas):
        self.x, self.y = 0, 0
        r = self.x, self.y, self.x + WIDTH, self.y + WIDTH
        self.head = Square(canvas, r)
        self.direction = 1, 0

    def update(self):
        self.x += WIDTH * self.direction[0]
        self.y += WIDTH * self.direction[1]
        r = self.x, self.y, self.x + WIDTH, self.y + WIDTH
        self.head.draw(r)

    def add_behind(self):
        self.head.add_behind()

    def get_overlapping(self):
        return self.head.get_overlapping()

    def is_valid(self):
        return all((
            not self.head.intersecting(self.get_overlapping()),
            self.x >= 0, self.x + WIDTH <= SCREEN[0],
            self.y >= 0, self.y + WIDTH <= SCREEN[1]
        ))

    def change_direction(self, direction):
        """
        direction: LEFT, RIGHT, UP, or DOWN.
        """
        if direction == LEFT: self.direction = -1, 0
        elif direction == RIGHT: self.direction = 1, 0
        elif direction == UP: self.direction = 0, -1
        elif direction == DOWN: self.direction = 0, 1
		

class Food(object):
    """
    Stores information about the food on the screen.
    canvas: tk.Canvas object to draw on.
    rect_def: tuple, (x, y, x+w, y+w)
    """
    def __init__(self, canvas, rect_def):
        self.food = canvas.create_rectangle(*rect_def, fill=FOOD_COLOR)
        self.can, self.t = canvas, 0

    def update(self):
        self.t += 1

    def is_well(self):
        return self.t < MAX_T

    def destroy(self):
        self.can.delete(self.food)

    def get(self):
        return self.food
		

class Game(tk.Frame):
	"""
	Controls the game animation.
	master: tk.Tk window.
	"""
	def __init__(self, master):
		super().__init__(master)
		self.can = tk.Canvas(self, width=SCREEN[0],
							 height=SCREEN[1], bg=BG_COLOR
							 )
		self.can.pack()
		self.snake, self.food = Snake(self.can), []
		
		for key in CONTROLS:
			master.bind("<%s>" % key,
						lambda e: self.snake.change_direction(e.keysym)
						)
		master.bind("<%s>" % CHEAT, lambda e: self.snake.add_behind())
		self.master, self.score = master, 1

	def next(self):
		self.snake.update()
		if random.random() < FOOD_PROB:
			self.add_food()

		overlapping = self.snake.get_overlapping()
		i = 0
		while i < len(self.food):
			f = self.food[i]
			f.update()
			if f.get() in overlapping:
				self.snake.add_behind()
				f.destroy()
				self.food.pop(i)
				self.score += 1
			elif not f.is_well():
				f.destroy()
				self.food.pop(i)
			else:
				i += 1

		self.master.title("Snake: %d" % self.score)
		if self.snake.is_valid():
			self.after(SPEED, self.next)
		else:
			self.can.create_text(SCREEN[0] // 2, SCREEN[1] // 2,
								 fill=TEXT_COLOR, font=FONT,
								 text="Game Over: %d" % self.score
								 )

	def add_food(self):
		x = random.randint(0, SCREEN[0] - FOOD_WIDTH)
		y = random.randint(0, SCREEN[1] - FOOD_WIDTH)
		r = x, y, x + FOOD_WIDTH, y + FOOD_WIDTH
		if not self.can.find_overlapping(*r):
			self.food.append(Food(self.can, r))
		else:
			self.add_food()

	def restart(self):
		self.destroy()
		self.__init__(self.master)
		self.pack()
		self.next()
		

def main():
	root = tk.Tk()
	root.title("Snake")
	root.resizable(0, 0)
	frame = Game(root)
	frame.pack()
	root.bind("<%s>" % RESTART, lambda e: frame.restart())
	root.bind("<%s>" % EXIT, lambda e: root.destroy())
	#root.eval('tk::PlaceWindow %s center'%root.winfo_pathname(root.winfo_id()))
	frame.next()
	root.mainloop()

if __name__ == "__main__":
    main()
