from display import RobotFace
import time

robot = RobotFace()

while True:

    robot.happy(2)

    robot.blink()

    robot.neutral(1)

    robot.sad(2)

    robot.blink()

    robot.angry(2)

    robot.blink()
