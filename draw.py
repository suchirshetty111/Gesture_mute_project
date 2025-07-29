import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils

def draw_feedback(image, is_fist, hand_landmarks):
    if is_fist:
        cv2.putText(image, '🔇 Mic & Cam Off', (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        cv2.circle(image, (600, 50), 20, (0, 0, 255), -1)
    else:
        cv2.putText(image, '🎤 Mic & Cam On', (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.circle(image, (600, 50), 20, (0, 255, 0), -1)

    if hand_landmarks and not is_fist:
        mp_drawing.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

    return image
