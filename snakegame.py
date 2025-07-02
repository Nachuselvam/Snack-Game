import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(self.master, width=600, height=600, bg="black")
        self.canvas.pack()
        
        self.snake = [(300, 300), (290, 300), (280, 300)]
        self.food = self.generate_food()
        self.direction = "Right"
        self.score = 0
        self.speed = 100
        
        self.master.bind("<KeyPress>", self.change_direction)
        
        self.move_snake()
        
    def generate_food(self):
        while True:
            x = random.randint(0, 59) * 10
            y = random.randint(0, 59) * 10
            if (x, y) not in self.snake:
                self.canvas.create_rectangle(x, y, x+20, y+20, fill="red", tag="food")
                return (x, y)
    
    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym
            
    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            new_head = (head_x, head_y - 20)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 20)
        elif self.direction == "Left":
            new_head = (head_x - 20, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 20, head_y)
        
        self.snake.insert(0, new_head)
        self.canvas.create_rectangle(new_head[0], new_head[1], new_head[0]+20, new_head[1]+20, fill="green", tag="snake")
        
        if new_head == self.food:
            self.score += 1
            self.master.title("Snake Game - Score: {}".format(self.score))
            self.food = self.generate_food()
        else:
            tail = self.snake.pop()
            self.canvas.delete("snake")
            self.canvas.create_rectangle(tail[0], tail[1], tail[0]+20, tail[1]+20, fill="yellow")
        
        if (new_head[0] < 0 or new_head[0] >= 600 or
            new_head[1] < 0 or new_head[1] >= 600 or
            new_head in self.snake[1:]):
            self.canvas.create_text(300, 300, text="Game Over!", fill="white", font=("Arial", 20))
            return
        
        self.master.after(self.speed, self.move_snake)
        
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
