Robotic Grasp AI
================

A ROS2-based project for robotic grasping, demonstrating communication between a publisher and subscriber for grasp commands.

---

Project Overview
----------------

This project implements a robotic grasping system using ROS2 (Humble). It includes:

- A Grasp Publisher that sends grasp commands (GRASP_OBJECT) at regular intervals.
- A Grasp Subscriber that receives these commands and logs them.
- Framework ready to integrate with a real robot or simulator for performing grasp actions.

This project is intended for learning ROS2 communication patterns and basic robotic grasp automation.

---

Folder Structure
----------------

robotic_grasp_ai/
│
├── grasp_publisher.py     # ROS2 node publishing grasp commands
├── grasp_subscriber.py    # ROS2 node subscribing to grasp commands
├── README.txt             # Project documentation
└── ...                    # Additional scripts or configuration files

---

Requirements
------------

- Python 3.8+
- ROS2 Humble
- Standard Python libraries: rclpy, std_msgs

---

Installation & Setup
-------------------

1. Clone the repository:

   git clone https://github.com/Vandana-cherukuri/robotic-grasp-ai.git
   cd robotic_grasp_ai

2. Source ROS2 setup:

   source /opt/ros/humble/setup.bash

3. Run the subscriber node:

   python3 grasp_subscriber.py

4. In a separate terminal, run the publisher node:

   python3 grasp_publisher.py

5. Observe the subscriber receiving grasp commands:

   [INFO] [grasp_subscriber]: Received: GRASP_OBJECT



Future Work
-----------

- Integrate with a robotic simulator (e.g., Gazebo, Webots) to perform actual grasp actions.
- Extend with vision-based object detection to grasp dynamic objects.
- Add feedback control for precise grasping.

---

Author
------

Vandana Cherukuri  
Bharati Vidyapeeth College of Engineering, Pune  
Electronics and Telecommunication

---

License
-------

This project is open-source and free to use under the MIT License.

