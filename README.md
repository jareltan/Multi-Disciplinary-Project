# Multi-Disciplinary-Project

![Robot Simulation](robot.gif)
![Results Simulation](results.gif)

## Project Overview
The Multi-Disciplinary Project is a hands-on course where students design, build, and program a functional robotic system. The project integrates hardware and software components, providing students with practical experience in robotics, software engineering, and system integration. The robot must complete specific tasks that test its capabilities in navigation, image recognition, and autonomous exploration.

### Project Objectives
The main objectives of the project are as follows:

1. **Robot Design and Construction:**
   - **Hardware Integration:** Students use various hardware components, such as sensors, actuators, microcontrollers, and Raspberry Pi, to build the robot. The Raspberry Pi serves as the robot's central processing unit, handling the computational tasks required for navigation, image processing, and communication.
   - **Software Development:** Students develop software to control the robot's actions. This includes programming the robot to navigate, recognize images, and explore environments autonomously.

2. **Functionality Checks:**
   - After construction, the robot undergoes functionality checks to ensure that all systems operate correctly. This includes validating hardware connections, verifying software algorithms, and testing communication between the Raspberry Pi and other components.

3. **Task Execution:**
   - The robot is required to complete three main tasks:

   a. **Fastest Path:**
      - The robot must navigate a course as quickly as possible. This task requires developing efficient pathfinding algorithms, which may involve techniques such as Dijkstra’s or A* algorithms. The robot must be able to avoid obstacles and make real-time adjustments to its path.

   b. **Image Recognition:**
      - **YOLOv5 Integration:** The robot uses the YOLOv5 (You Only Look Once, version 5) model for real-time object detection and image recognition. Students collect and annotate training data, creating a dataset that the YOLOv5 model uses to learn and accurately recognize objects in the environment.
      - **Data Collection and Annotation:** To train the YOLOv5 model, students collect images from the robot’s camera and manually annotate them to create labeled training data. This annotated data is essential for training the model to detect specific objects or visual cues within the environment.
      - **Deployment on Raspberry Pi:** The trained YOLOv5 model is deployed on the Raspberry Pi, where it runs inference in real-time, allowing the robot to identify objects as it navigates its environment.

   c. **Exploration:**
      - The robot must autonomously explore and map an unknown environment. Using sensors such as LIDAR or ultrasonic sensors, combined with the image recognition capabilities provided by YOLOv5, the robot builds a map of the area while avoiding obstacles. The exploration algorithm also involves pathfinding to ensure complete coverage of the area.

4. **User Interface Development:**
   - **Android GUI:** An Android-based graphical user interface (GUI) is developed to provide users with control and monitoring capabilities. The GUI allows users to start and stop the robot, monitor its progress in real-time, and view the map generated during the exploration task. The GUI communicates with the Raspberry Pi, providing a seamless interface for robot operation.

### Learning Outcomes
Students gain experience in:
- **Systems Engineering:** Integrating hardware and software components into a cohesive robotic system.
- **Machine Learning:** Training and deploying a YOLOv5 model for image recognition tasks.
- **Software Development:** Writing code for the Raspberry Pi, developing pathfinding algorithms, and creating a user-friendly Android GUI.
- **Data Annotation:** Collecting and annotating data for training machine learning models.
- **Problem-Solving:** Overcoming challenges related to hardware limitations, software bugs, and real-world task complexity.
- **Team Collaboration:** Working in multidisciplinary teams to design, build, and refine the robot.

### Conclusion
The Multi-Disciplinary Project equips students with the skills necessary to tackle complex engineering challenges, combining knowledge from various disciplines to create a functional robotic system. By the project's end, students will have developed a robot capable of efficient navigation, real-time image recognition, and autonomous exploration, all controlled through an intuitive Android GUI.
