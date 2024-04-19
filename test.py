import random

class SnakeGame:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.snake = [(10, 10)]
        self.food = (0, 0)
        self.direction = "right"
        self.score = 0

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.snake:
                    print("|", end=" ")
                elif (x, y) == self.food:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    def update(self):
        self.snake.append(self.snake[-1])
        self.snake.pop(0)

        if self.snake[-1] == self.food:
            self.food = (random.randint(0, self.width-1), random.randint(0, self.height-1))
            self.score += 1
        else:
            if self.direction == "right":
                self.snake[-1] = (self.snake[-1][0] + 1, self.snake[-1][1])
            elif self.direction == "left":
                self.snake[-1] = (self.snake[-1][0] - 1, self.snake[-1][1])
            elif self.direction == "up":
                self.snake[-1] = (self.snake[-1][0], self.snake[-1][1] - 1)
            elif self.direction == "down":
                self.snake[-1] = (self.snake[-1][0], self.snake[-1][1] + 1)

    def check_collision(self):
        if self.snake[-1] in self.snake[:-1]:
            return True
        elif self.snake[-1] < (0, 0) or self.snake[-1] > (self.width-1, self.height-1):
            return True

    def run(self):
        while True:
            self.draw()
            self.update()
            if self.check_collision():
                print("Game over! Your score: {}".format(self.score))
                break

game = SnakeGame()
game.run()
