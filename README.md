# Ground-station visualization

## Overview
This is an API optimized for fast data transmission between the robot an ground
station for visualization in the field. In short, this is achieved by bypassing
SSH and instead hosting a Redis server on the ground station computer instead.
The robot may then target this server and send data (data = any data structure
with bytearray representation) to the ground station at speeds faster than SSH
and without dealing with storage read/write speeds.

![Image showing the dual connection between the robot and ground station. The
first is two-way, secure, easy-to-use, but slow SSH by which ROS communicates.
The second is Redis, which is less secure, one-way, but faster.](figure it out)

## Use case
This API is best used as a way to demonstrate everyone's work on the robot and
provide feedback to the driver without compromising robot performance. The
system is designed to be efficient computationally, using approximately 20%
single core usage on the robot (about 70% single core usage on the ground
station).

This API can certainly be used for debugging on the fly (i.e. adding charts),
however it is a more involved process than using Rviz. For most debugging
purposes, I would recommend sticking with Rviz or Plotjuggler as much as
possible.

## API Reference