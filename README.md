In today's digital world, touchless technology is gaining traction for its potential to enhance user interaction and accessibility. This project demonstrates a virtual mouse controlled by hand gestures using computer vision, providing an innovative way to interact with computers without physical contact.

VirtualMouse.py

    Key Components
    	1. Imports:
    		o Libraries such as OpenCV (cv2), NumPy, PyAutoGUI, and AutoPy are used for computer vision and mouse control.
    		o The custom HandFunctions script provides hand detection functionalities.
    	2. Initial Setup:
    		o A video capture object is initialized to read frames from the webcam.
    		o The hand detector is set up to track a single hand.
    		o The screen dimensions are obtained to map hand positions to screen coordinates.
    	3. Main Loop:
    		o Frames are continuously captured from the webcam.
    		o The hand detector processes each frame to find hand landmarks.
    		o The positions of specific landmarks (like the tips of the index and middle fingers) are extracted.
    	4. Gesture Recognition:
    		o The script checks which fingers are up to determine the user's intended action.
    		o If only the index finger is up, it enters "moving mode" to control the mouse cursor.
    		o If both the index and middle fingers are up and close together, it enters "clicking mode" to perform a mouse click.
    	5. Mouse Movement:
    		o The position of the index finger is converted to screen coordinates using interpolation.
    		o The cursor movement is smoothened to ensure a natural and responsive feel.
    		o The AutoPy library is used to move the mouse cursor to the calculated position.
    	6. Mouse Clicking:
    		o The distance between the index and middle fingers is calculated.
    		o If the fingers are close enough, a mouse click is triggered.

HandFunctions.py

	The HandFunctions.py script provides the following functionalities:

		* Initialization: Sets up MediaPipe hand detection parameters.
		* Hand Detection: Converts the image to RGB, processes it to detect hands, and optionally draws hand landmarks.
		* Position Finding: Extracts and returns the positions of hand landmarks and the bounding box of the detected hand.
		* Fingers Up Check: Determines which fingers are up based on the landmarks.
		* Distance Calculation: Calculates the distance between two specified landmarks, useful for detecting gestures like clicking.

  Dependencies
  
        * OpenCV
        * Mediapipe
        * NumPy
        * AutoPy
      

This project exemplifies the potential of computer vision in creating intuitive, touchless interfaces. By converting hand gestures into mouse actions, it opens up new possibilities for user interaction and accessibility. This technology can be particularly beneficial in scenarios where touchless interaction is essential, such as during presentations or for individuals with mobility impairments.
