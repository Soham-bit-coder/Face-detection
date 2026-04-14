import cv2 as cv
import face_recognition
import pywhatkit
import time
from datetime import datetime

# -------------------------------
# WhatsApp alert function
# -------------------------------
def send_whatsapp_alert(image_path):
    phone_numbers = [
        "+919324254464",
        "+919004889938"
    ]

    for number in phone_numbers:
        pywhatkit.sendwhats_image(
            receiver=number,
            img_path=image_path,
            caption="ALERT! Unknown face detected.",
            wait_time=20,
            tab_close=False,
            close_time=3
        )
        time.sleep(5)


# -------------------------------
# Load known image
# -------------------------------
known_image = face_recognition.load_image_file("soham1.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

video = cv.VideoCapture(0)

tracker = None
tracking = False
name = "Unknown"
frame_count = 0
alert_sent = False

# -------------------------------
# Main loop
# -------------------------------
while True:
    ret, frame = video.read()

    if not ret:
        break

    frame_count += 1

    # Detect face every 15 frames
    if not tracking or frame_count % 15 == 0:

        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_frame)

        face_encodings = face_recognition.face_encodings(
            rgb_frame,
            face_locations
        )

        if len(face_locations) > 0:

            top, right, bottom, left = face_locations[0]
            face_encoding = face_encodings[0]

            matches = face_recognition.compare_faces(
                [known_encoding],
                face_encoding
            )

            name = "Unknown"

            if matches[0]:
                name = "Soham"
                alert_sent = False

            else:
                name = "Unknown"

                # send alert only once
                if not alert_sent:

                    # crop unknown face
                    unknown_face = frame[top:bottom, left:right]

                    # unique filename with date + time
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

                    image_path = f"unknown_face_{timestamp}.jpg"

                    # save image
                    cv.imwrite(image_path, unknown_face)

                    # send image + alert
                    send_whatsapp_alert(image_path)

                    alert_sent = True

            # Create tracker
            tracker = cv.TrackerCSRT_create()

            bbox = (
                left,
                top,
                right - left,
                bottom - top
            )

            tracker.init(frame, bbox)
            tracking = True

    # -------------------------------
    # Smooth tracking
    # -------------------------------
    if tracking and tracker is not None:

        success, bbox = tracker.update(frame)

        if success:
            x, y, w, h = map(int, bbox)

            cv.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv.putText(
                frame,
                name,
                (x, y - 10),
                cv.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        else:
            tracking = False

    cv.imshow("Face Recognition + Tracking", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()