import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 40
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed_car = 10
        for i in range(0, 30):
            car = Turtle()
            car.penup()
            car.shape("square")
            car.resizemode("user")
            car.shapesize(stretch_len=2)
            car.color(random.choices(COLORS))
            car.goto(random.randint(-29, 32) * 10, random.randint(-24, 24) * 10)
            for i in self.cars:
                if car.distance(i) < STARTING_MOVE_DISTANCE:
                    car.goto(random.randint(-29, 32) * 10, random.randint(-24, 24) * 10)
            car.setheading(180)
            self.cars.append(car)

            
    def update_location(self):
        for car in self.cars:
            if car.xcor() <= -310:
                car.goto(310, random.randint(-24, 24) * 10)
                for i in self.cars:
                    if car.distance(i) < STARTING_MOVE_DISTANCE:
                        if car != i:
                            car.goto(310, random.randint(-24, 24) * 10)

    def car_move(self):
        for car in self.cars:
            car.forward(self.speed_car)
    
    def plus_speed(self):
        self.speed_car += MOVE_INCREMENT



