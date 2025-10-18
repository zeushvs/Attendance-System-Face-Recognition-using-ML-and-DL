## Attendance System using Face Recognition

An automated **Face Recognition-based Attendance System** built using a combination of **Deep Learning** and **Machine Learning** techniques.
This project aims to eliminate manual attendance marking by automatically identifying students through facial recognition.
An intelligent Face Recognition Attendance System that automates student attendance using Deep Learning (Caffe) and Machine Learning (SVM).
This project leverages OpenCV for real-time face detection, feature extraction via deep neural networks, and SVM classification for precise identity recognition ,
replacing traditional roll-call with an efficient, AI-powered solution.

---

### Tech Stack

* **Deep Learning Framework:** Caffe
* **Machine Learning Algorithm:** SVM (Support Vector Machine)
* **Computer Vision:** OpenCV
* **Languages:** Python
* **Data Handling:** CSV

---

### Features

* Real-time face detection and recognition using webcam feed
* Automatic attendance marking in CSV files
* Student dataset creation with labeled images and roll numbers
* Image preprocessing and feature extraction using Deep Learning
* High accuracy recognition using trained SVM model

---

### Workflow

1. **Data Collection:**
   Captured and labeled student faces using OpenCV.
2. **Preprocessing:**
   Images resized, normalized, and converted into feature vectors using Caffe model.
3. **Model Training:**
   Extracted features trained and tested with SVM classifier for recognition.
4. **Attendance Marking:**
   Recognized students are automatically logged with name, roll number, and timestamp in a CSV file.

---

### Folder Structure

```
📦 FaceRecognition-Attendance
 ┣ 📂 dataset/
 ┣ 📂 models/
 ┣ 📂 scripts/
 ┣ 📜 train.py
 ┣ 📜 recognize.py
 ┣ 📜 attendance.csv
 ┗ 📜 README.md
```

---

### Future Improvements

* Integration with cloud-based database (Firebase / MySQL)
* Adding face mask detection module
* Mobile app for attendance visualization

---
