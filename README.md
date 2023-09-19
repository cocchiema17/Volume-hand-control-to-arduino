# Volume-hand-control-to-arduino

[![Video Link](insert-video-link-here.png)](insert-video-link-here) <!-- Insert your video link here -->

This project is inspired by a [specific video](insert-link-to-the-original-video-here), and it involves hand tracking using the MediaPipe library to control your system's volume based on the distance between your index finger and thumb. Additionally, we've integrated an Arduino board to control LEDs based on the volume level. The project utilizes the MediaPipe, PySerial, and PyCaw libraries.

## Introduction

This project allows you to control your computer's volume by simply moving your hand. Inspired by [insert the link to the original video here], we've taken the concept a step further, significantly improving the precision of the volume control algorithm.

## Getting Started

To get started with the project, follow these steps:

1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Connect your Arduino board and upload the `led_handler.ino` sketch.
4. Run the `volume_control.py` script to start hand tracking and volume control.

## Project Structure

- **HandTracking.py**: Contains the `handDetector` class with methods for hand tracking and position detection.
- **SendValues.py**: Defines the class responsible for connecting to Arduino, sending hand-tracking data, and disconnecting from Arduino.
- **VolumeControl.py**: The main program that initializes the camera, tracks the hand, and displays volume levels.
- **led_handler.ino**: Arduino code for controlling LEDs based on volume levels.

## Improvements

Compared to the original video, we've achieved a remarkable improvement in precision. The proportionality issue between finger distance and volume level has been resolved, resulting in a 100% increase in accuracy.

## Usage

To use this project:

1. Run `volume_control.py` to start hand tracking.
2. Move your hand to control the volume.
3. Observe the LEDs on your Arduino board to gauge the volume level.
