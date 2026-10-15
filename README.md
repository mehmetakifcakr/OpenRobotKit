# OpenRobotKit

An early-stage robotics learning toolkit, starting with a small Python motor
state abstraction. Arduino and ESP32 support are planned.

## What works today

[`Motor`](src/motor.py) stores a speed value in memory. You can set an initial
speed, change it with `set_speed()`, and reset it to zero with `stop()`.
It does not communicate with a motor driver or control physical hardware.
Speed units, ranges, and input validation are not defined yet.

## Run the motor example

From a checkout of this repository, with Python 3 installed:

```sh
git clone https://github.com/mehmetakifcakr/OpenRobotKit.git
cd OpenRobotKit
python3 -m examples.motor_demo
```

On Windows, use `python` if that is your Python 3 command. No third-party
packages, hardware, credentials, or network connection are needed to run the
example after cloning.

Expected output:

```text
Initial speed: 0
Updated speed: 50
Stopped speed: 0
```

The value `50` is illustrative, not a percentage or a hardware command.
See [`examples/motor_demo.py`](examples/motor_demo.py) for the complete example.

## Current source layout

```text
src/motor.py             In-memory Motor class
examples/motor_demo.py   Runnable, hardware-free example
docs/                   Documentation placeholders
LICENSE                 MIT license
```

There is no automated test suite or CI workflow yet. The example demonstrates
state changes only; it does not validate physical motor behavior.

## Planned work

The following are ideas for future development, not implemented features:

- Define motor speed units, valid inputs, and behavior tests.
- Add Arduino and ESP32 hardware adapters with explicit wiring examples.
- Explore PID control, sensor calibration, and serial communication.
- Add robotics examples as the underlying modules become available.

## Contributing

Small, reproducible improvements are welcome. Describe the problem, keep the
change focused, and include the command and output used to check it. Distinguish
software-only checks from tests performed on actual hardware.

## License

[MIT](LICENSE).
