# Touchless Gesture-Controlled Virtual Mouse

An advanced, real-time virtual mouse control system built using Python, OpenCV, MediaPipe, and OS input simulation libraries.

The application detects and tracks hand landmarks to translate natural hand gestures into computer mouse actions—including cursor movement, clicking, scrolling, and zooming—without physical hardware contact.

## 📺 Project Demo

<div align="center">

https://github.com/user-attachments/assets/27708564-d09d-4335-8317-899a41af2353

</div>

---

## 📂 Project Structure

```text
Gesture-Mouse/
├── docs/                             # Documentation files
│   ├── architecture.md               # Architecture details & system flow
│   └── gesture_mapping.md            # Explanation of gesture mappings & actions
├── gesture_mouse/                    # Core application source package
│   ├── utils/                        # Utility modules
│   │   └── hand_tracking.py          # MediaPipe hand tracking & detection class
│   └── main.py                       # Main virtual mouse tracker loop script
├── requirements.txt                  # System dependencies
├── .gitignore                        # Git ignore file (ignores large video assets)
├── LICENSE                           # Project License
└── README.md                         # Project documentation
```

---

## 🛠️ Requirements & Setup

To run this project, you need standard system python libraries. Installing within a virtual environment is recommended.

### Core Dependencies
Dependencies are listed in `requirements.txt`:
* **OpenCV**: Capture frame feeds from your webcam.
* **MediaPipe**: Real-time multi-landmark hand detection (processes frames in RGB).
* **NumPy**: Numeric mapping and coordinate interpolation.
* **AutoPy**: Highly-efficient mouse cursor movement.
* **PyAutoGUI & Pynput**: Virtual keyboard inputs and scrolling actions.
* **Mouse**: System click simulations.

---

## 🚀 Running the Project

Run the application using Python from the root directory of the repository:
```bash
python gesture_mouse/main.py
```

* **Exiting the App**: Press `F2` at any time to terminate the tracking loop.

---

## 🖐️ Gesture Mappings Reference

For a complete detail on each hand state configuration, see the [Gesture Mapping Guide](docs/gesture_mapping.md).
