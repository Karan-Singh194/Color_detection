import sys
import cv2
from PIL import Image
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QComboBox, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from util_all import get_limits


class ColorDetectionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Detection App")
        self.setGeometry(300, 100, 800, 600)

        # Variables
        self.cap = None
        self.timer = QTimer()
        self.color = [0, 0, 255]  # default red

        # Widgets
        self.video_label = QLabel("Camera feed will appear here", self)
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setStyleSheet("background-color: black; color: white;")

        self.color_combo = QComboBox(self)
        self.color_combo.addItems(["Red", "Green", "Blue", "Yellow"])

        self.start_btn = QPushButton("Start Detection", self)
        self.stop_btn = QPushButton("Stop", self)
        self.stop_btn.setEnabled(False)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.color_combo)
        layout.addWidget(self.start_btn)
        layout.addWidget(self.stop_btn)
        self.setLayout(layout)

        # Signals
        self.start_btn.clicked.connect(self.start_detection)
        self.stop_btn.clicked.connect(self.stop_detection)
        self.timer.timeout.connect(self.update_frame)

    def start_detection(self):
        color_map = {
            "Red": [0, 0, 255],
            "Green": [0, 255, 0],
            "Blue": [255, 0, 0],
            "Yellow": [0, 255, 255]
        }
        selected = self.color_combo.currentText()
        self.color = color_map[selected]

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            QMessageBox.warning(self, "Error", "Camera not detected!")
            return

        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.timer.start(30)  # update every 30 ms

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        if self.color == [0, 0, 255]:  # red needs two ranges
            red_ranges = get_limits(self.color)
            mask1 = cv2.inRange(hsvImage, red_ranges[0][0], red_ranges[0][1])
            mask2 = cv2.inRange(hsvImage, red_ranges[1][0], red_ranges[1][1])
            mask = mask1 | mask2
        else:
            lowerLimit, upperLimit = get_limits(self.color)
            mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)

        # Convert frame for PyQt display
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qt_image))

    def stop_detection(self):
        self.timer.stop()
        if self.cap:
            self.cap.release()
        self.video_label.clear()
        self.video_label.setText("Camera feed will appear here")
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

    def closeEvent(self, event):
        """Ensure camera closes when app is closed"""
        self.stop_detection()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorDetectionApp()
    window.show()
    sys.exit(app.exec_())
