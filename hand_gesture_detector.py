import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
finger_tips = [8, 12, 16, 20]

def detect_fist(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        folded_fingers = sum(
            hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y
            for tip in finger_tips
        )
        is_fist = folded_fingers == 4
        return is_fist, hand_landmarks

    return False, None
