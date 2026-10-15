"""Demonstrate in-memory motor state; run from the repo root with -m."""

from src.motor import Motor


def main():
    motor = Motor()
    print(f"Initial speed: {motor.speed}")
    motor.set_speed(50)
    print(f"Updated speed: {motor.speed}")
    motor.stop()
    print(f"Stopped speed: {motor.speed}")


if __name__ == "__main__":
    main()
