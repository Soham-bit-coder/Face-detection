# Face-detection

📸 Face Recognition + Tracking + WhatsApp Alert System

This project is a real-time face recognition system using OpenCV and face_recognition library. It detects faces from a webcam, identifies known users, tracks faces smoothly, and sends a WhatsApp alert with image when an unknown person is detected.

🚀 Features

-🎥 Real-time webcam face detection
-🧠 Face recognition using face_recognition (dlib)
-📍 Face tracking using OpenCV CSRT tracker
-📸 Auto-capture unknown face
-📲 WhatsApp alert with image using pywhatkit
-⏱️ Optimized detection (runs every 15 frames for performance)
-🔒 Sends alert only once per unknown detection
-🛠️ Technologies Used
    -Python 3.x
    -OpenCV (cv2)
    -face_recognition
    -pywhatkit
    -datetime
    -time
    
📂 Project Structure
project/
│── soham1.jpg              # Known face image
│── main.py                 # Main program file
│── unknown_face_*.jpg      # Auto saved unknown face images
│── README.md               # Project documentation

⚙️ Installation
1️⃣ Install Python libraries
    pip install opencv-python face-recognition pywhatkit

2️⃣ If dlib fails (Windows fix)
⚠️ Note: face_recognition requires dlib, which may need C++ build tools installed.
    pip install cmake
    pip install dlib
    pip install face-recognition

▶️ How to Run
    -Add your known face image:
    -soham1.jpg
    -Update phone numbers in code:
    phone_numbers = [
        "+91XXXXXXXXXX",
        "+91XXXXXXXXXX"
    ]
    Run the program:
      python main.py
      Press Q to exit webcam window.
    📌 How It Works
        -Webcam captures video frames
        -Every 15 frames:
        -Detects faces
        -Compares with known face encoding
        -If match found → Label: "Soham"
        -If unknown face detected:
        -Face is cropped and saved
        -WhatsApp alert is sent with image
        -CSRT tracker continues tracking the face smoothly
        -📲 WhatsApp Alert Example
        ALERT! Unknown face detected.
        [Image of unknown person]
⚠️ Important Notes
      Keep WhatsApp Web logged in before running
      First message may take ~20 seconds due to setup
      Ensure good lighting for better face detection
      Use only for educational/security purposes
🔥 Future Improvements
    Add database of multiple known faces
    Email alert system
    Firebase cloud logging
    Mobile app integration
    Better AI model (DeepFace / FaceNet)
👨‍💻 Author

Developed by: Soham Ghag
Project: AI Face Recognition Security System
