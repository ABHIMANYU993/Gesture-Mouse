In today's digital world, touchless technology is gaining traction for its potential to enhance user interaction and accessibility. This project demonstrates a virtual mouse controlled by hand gestures using computer vision, providing an innovative way to interact with computers without physical contact.

Methodology
This project utilizes several key technologies and libraries:

OpenCV: For real-time image processing and video capture.
NumPy: For numerical operations.
pyautogui: For simulating mouse movements and actions.
autopy: For controlling the mouse.
pynput: For mouse control.
HandFunctions: A custom module for hand detection and gesture recognition.
The workflow involves:

Video Capture: Using OpenCV to capture frames from the webcam.
Hand Detection: Utilizing a pre-trained model to detect hand landmarks.
Gesture Recognition: Identifying specific gestures to determine mouse actions.
Mouse Control: Mapping hand movements and gestures to mouse actions.
Implementation
The program captures video frames, detects hand landmarks, and recognizes gestures to control mouse actions. For example, the index finger alone moves the cursor, while the combination of the index and middle fingers triggers a click. Additionally, pinching and spreading fingers can be used for scrolling and zooming.



This project exemplifies the potential of computer vision in creating intuitive, touchless interfaces. By converting hand gestures into mouse actions, it opens up new possibilities for user interaction and accessibility. This technology can be particularly beneficial in scenarios where touchless interaction is essential, such as during presentations or for individuals with mobility impairments.

Dependencies: 1.Opencv
              2.Mediapipe
              3.Numpy
Just install the above dependencies and run the VirtualMouse.py
