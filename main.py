from camera.webcam_stream import get_frame
from gesture.hand_gesture_detector import detect_fist
from controller.mute_controller import mute_if_needed
from utils.draw import draw_feedback

import cv2

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while cap.isOpened():
    success, frame = get_frame(cap)
    if not success:
        break

    is_fist, landmarks = detect_fist(frame)
    mute_if_needed(is_fist)

    if is_fist:
        black_frame = frame.copy()
        black_frame[:] = 0  
        frame = black_frame

    frame = draw_feedback(frame, is_fist, landmarks)
    cv2.imshow('Gesture Mute Control', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
