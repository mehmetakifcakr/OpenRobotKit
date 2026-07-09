"""
Motor control module for OpenRobotKit.
"""

class Motor:
    def __init__(self, speed=0):
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0
