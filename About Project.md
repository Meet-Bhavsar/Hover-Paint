<b>Hover Paint</b><br><hr>

<b>Overview</b>

This project explores the application of computer vision techniques to enable gesture-based interaction, specifically focusing on hand gesture recognition. By leveraging OpenCV and MediaPipe, the system tracks hand landmarks in real-time, allowing users to control an air canvas environment through predefined gestures. This approach aims to demonstrate the potential of touchless interfaces in enhancing interactive experiences.

<b>Key Components</b>

Real-Time Hand Landmark Detection: Utilizes MediaPipe’s robust hand-tracking solution to identify and track hand landmarks with precision, forming the foundation for gesture interpretation.
Gesture Recognition for Interaction: Recognizes gestures made by the index and middle fingers to dynamically control the drawing process, highlighting a practical example of human-computer interaction (HCI).
Dynamic Image Rendering: Implements gesture-based image switching, simulating a command-based interaction model.
Adaptive Header Placement: Adjusts image positioning based on gestures, showcasing a customizable visual framework.

<b>Technical Setup</b>
1. Environment Setup: Ensure you have OpenCV and MediaPipe installed:<br>
   pip install opencv-python mediapipe
2. Repository Clone:<br>
   git clone <repo-link>
   <br><hr>
<b>Note for Users</b>
For systems using an external webcam, remember to adjust the VideoCapture parameter in the code, changing the value from 0 to 1 to select the correct camera input.
<hr>
<b>Running the Project</b>
  Run the main script to initiate hand tracking and gesture recognition:
  python main.py
