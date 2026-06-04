# Interactive 3D Sun-Earth-Moon System

## Project Description
This project consists of an interactive 3D graphical simulation that models a simplified astronomical system. It implements the real-time orbital revolution and axial rotation of the Earth and the Moon relative to a static, central Sun. 

The core of the project focuses on two main graphics implementations:
1. **Camera Target Locking**: The viewport center is hardcoded to the Sun's coordinates. This structure forces the camera to orbit exclusively around the central body, giving the user a stable 360-degree viewpoint manipulation via mouse inputs.
2. **Custom Ray Casting and Lighting**: By disabling the global rendering engine's default ambient lights and nesting a localized point light source inside the Sun's geometry, the simulation renders hardware-accelerated shadows. This technique accurately demonstrates day/night terminators on the Earth's surface and physical moon phases depending on its geometric positioning relative to the light source.

## Technologies Used
* **Python 3.x**: Used as the foundational programming language to handle the mathematical loops and kinematic update intervals.
* **VPython (Visual Python)**: Chosen as the primary 3D graphics library. It handles the mapping of spherical coordinates, texturing matrices (such as planetary surface materials), camera vectors, and local light objects.
* **WebGL**: The underlying graphics API utilized by VPython to execute hardware-accelerated WebGL code directly in the web browser, enabling smooth texture filtering and real-time shadow rendering.
