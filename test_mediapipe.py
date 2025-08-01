import cv2
import mediapipe as mp
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0) #index
while True:
    ret, frame = cap.read()
    if not ret:
        break
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow("Mediapipe Hand Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #q to quit
        break
cap.release()
cv2.destroyAllWindows()
