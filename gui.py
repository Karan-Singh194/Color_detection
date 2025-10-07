from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# Create application
app = QApplication([])

# Create a window
window = QWidget()
window.setWindowTitle("My First PyQt App")
window.setGeometry(100, 100, 300, 200)

# Add a label
label = QLabel("Hello, Karan! 👋", parent=window)
label.move(100, 80)

# Show the window
window.show()

# Run the app
app.exec_()
