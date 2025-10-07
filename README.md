# 🎨 Color Detection App (PyQt5 + OpenCV)

**A real-time color detection application built with Python, OpenCV, and PyQt5.  
The app detects selected colors (Red, Green, Blue, Yellow) from your camera feed and highlights the detected area — all inside a modern GUI interface.**

---

## 🚀 Features

- 🖥️ **Live Camera Feed** displayed inside the PyQt5 GUI  
- 🎯 **Color Detection** for multiple colors (Red, Green, Blue, Yellow)  
- 🔲 **Bounding Box** around detected color objects  
- 🎛️ **Start / Stop** controls inside the GUI  
- ⚡ **Real-time performance** using OpenCV  
- 🧩 **Modular structure** with a utility file (`util_all.py`) for HSV range calculations  

---

## 📂 Project Structure

Color-Detection-App/
│
├── cv_all_gui_feed.py   # Main GUI + color detection logic
├── util_all.py          # Utility file for color HSV range calculation
└── README.md            # Project documentation



---

## 🧠 How It Works

1. The app opens your system’s camera and continuously reads frames.  
2. You select a color from the dropdown (Red, Green, Blue, or Yellow).  
3. The frame is converted to HSV and a mask is created using color limits.  
4. Detected color regions are highlighted with a green rectangle in real time.  
5. Press **“Stop”** to end the detection or close the window safely.

---

## 🧰 Requirements

Make sure you have Python and pip installed, then install the following:

"pip install opencv-python pillow PyQt5 numpy"


## ▶️ Run the App
**Clone the repository or download the files.**
"[git clone https://github.com/<your-username>/Color-Detection-App.git](https://github.com/Karan-Singh194/Color_detection.git)"
"cd Color-Detection"

### Run the application:
**python cv_all_gui.py**


### The GUI will open:
Choose a color from the dropdown.
Click Start Detection.
Press Stop to stop the camera feed.


📸 Demo

🧠 a short demo video or screenshot here.
![App Demo](demo.gif)(not make )


## 🧩 util_all.py Explanation

**This file contains the function get_limits(color) which:**
Converts BGR color to HSV,
Returns the upper and lower HSV limits,
Handles special cases for Red, Black, and White colors.


## 🛠️ Technologies Used

Python 3
PyQt5 – for GUI
OpenCV (cv2) – for camera and image processing
Pillow (PIL) – for bounding box calculations
NumPy – for array and color range handling

## ✨ Future Enhancements

🎨 Custom RGB color picker
📁 Save screenshots of detections
📊 Show HSV values in the GUI
🧠 Add color tracking for moving objects
👨‍💻 Author

## Karan Singh
💡 Student | Developer 
📫 Connect with me on GitHub: [@Karan-Singh194](https://github.com/Karan-Singh194)

---

Would you like me to include a **preview image section** (for your GUI window layout) or a **badges section** (Python version, license, etc.) to make it look more professional for GitHub?

