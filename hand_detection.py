import cv2
import mediapipe as mp

# Initialize MediaPipe hands and drawing utils
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Configure the Hands model
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Define a helper function to count fingers
def count_fingers(hand_landmarks):
    tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    fingers = []

    # Thumb
    if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other four fingers
    for id in range(1, 5):
        if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    
    return fingers.count(1)

# Main loop
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers_up = count_fingers(hand_landmarks)
            cv2.putText(frame, f'Fingers: {fingers_up}', (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

            # Example: simple gesture logic
            if fingers_up == 0:
                cv2.putText(frame, 'Gesture: Fist ', (10, 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            elif fingers_up == 5:
                cv2.putText(frame, 'Gesture: Open Palm ', (10, 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            elif fingers_up == 1:
                cv2.putText(frame, 'Gesture: Point ', (10, 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)
            elif fingers_up == 2:
                cv2.putText(frame, 'Gesture: Peace ', (10, 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

    cv2.imshow("Hand Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
