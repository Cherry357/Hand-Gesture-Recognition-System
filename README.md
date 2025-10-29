# Hand-Gesture-Recognition-System
This project is a real-time hand gesture detection system built using OpenCV and MediaPipe. It captures live video from a webcam, detects hand landmarks, counts the number of fingers raised, and identifies simple gestures such as Fist, Open Palm, Point, and Peace in real time.

The system leverages **MediaPipe’s pre-trained hand tracking model**, which accurately identifies 21 key hand landmarks, and uses geometric rules to determine finger positions.  
This project showcases the power of **computer vision** and **AI-based hand tracking** for intuitive, touchless human–computer interaction.

---

## ⚙️ Features
✅ Real-time hand tracking and gesture detection  
✅ Counts fingers automatically based on landmark positions  
✅ Detects gestures like *Fist*, *Open Palm*, *Point*, and *Peace*  
✅ Works with any standard webcam — no extra sensors required  
✅ Built entirely with open-source Python libraries  

---

## 🧩 Technologies Used
- **Python 3.8+**  
- **OpenCV** – Image processing and video handling  
- **MediaPipe** – Hand landmark detection and tracking  
- **NumPy** *(optional)* – Array and coordinate operations  

---

## 🖥️ How It Works
1. The webcam captures live video frames.  
2. Each frame is processed by **MediaPipe Hands**, which detects 21 key landmarks on each hand.  
3. The program analyzes landmark positions to count raised fingers.  
4. Based on the finger count, the system identifies and displays predefined gestures in real time.

2. Install Dependencies:
   pip install opencv-python mediapipe numpy



Created By:
Darshan Krishna
