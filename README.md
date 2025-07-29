
# Gesture-Controlled Mute System for Video Calls

Control your mic and camera during video calls using simple hand gestures — no clicks needed.

## Project Overview

This project introduces an innovative gesture-recognition system that allows users to mute/unmute audio and turn video on/off during video calls using just a closed fist gesture — simulating WhatsApp or Zoom mute behavior without touching the screen.

### Why?
In real-time video calling apps like WhatsApp, it can be inconvenient to tap mute or turn off the camera while busy or in hands-free situations. This solution offers a contactless and intuitive way to control your call status using gestures detected via webcam.

## Features

- Real-time gesture detection using MediaPipe
- Fist Gesture → Automatically mutes mic and turns off camera
- Open Hand → Unmutes mic and resumes video
- Black screen with red dot when muted
- Green status indicator when mic/video is active
- Easily expandable to support more gestures (e.g., V sign = unmute)

## Project Structure

```
gesture_mute_project/
│
├── main.py                      # Main application to run gesture detection
├── requirements.txt             # Python dependencies
│
├── utils/
│   ├── draw.py                  # Draws UI feedback on video frames
│   ├── hand_gesture_detector.py# Detects open hand vs fist using MediaPipe
│   ├── mute_controller.py       # Simulates mic/video toggle logic
│   └── webcam_stream.py         # Webcam capture module
│
└── README.md                    # This file
```

## How to Run

### Prerequisites
- Python 3.8 or higher
- Webcam

### Installation

```bash
git clone https://github.com/yourusername/gesture-mute.git
cd gesture-mute
pip install -r requirements.txt
python main.py
```

## Demo

| Gesture     | Result                          |
|-------------|---------------------------------|
| Open Hand   | Mic and Camera ON (Green status)|
| Closed Fist | Mic and Camera OFF (Black screen + Red status) |

## Future Improvements

- Integrate with real video call apps (WebRTC, Agora, or Jitsi)
- Android version using CameraX or MediaPipe SDK
- Additional gestures for pause, end call, etc.
- Voice + gesture hybrid control

## Idea Origin

This project was inspired by the common inconvenience users face when needing to mute themselves during WhatsApp video calls while their hands are occupied. This gesture-based approach aims to improve accessibility and ease of use.

## Contact / Collaboration

Built by [Your Name]

If you're from WhatsApp/Meta or are interested in collaboration:
- Email: your.email@example.com
- LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
- Demo Video: [link-to-demo-video]
