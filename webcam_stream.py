import cv2

def get_frame(cap):
    success, frame = cap.read()
    if success:
        frame = cv2.flip(frame, 1)
    return success, frame
