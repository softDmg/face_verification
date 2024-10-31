import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from image_match import Ui_MainWindow  # Import the UI class from the generated file
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, QtCore
from match1 import verify_faces  # Import the verify_faces function

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)

        # Connect buttons to functions
        self.load_image_button.clicked.connect(self.load_image)
        self.match_image_button.clicked.connect(self.match_images)

        # Initialize image paths
        self.image1_path = "lesson_1/image1.jpeg"
        self.image2_path = None

        # Load the constant image
        self.load_constant_image()

    def load_constant_image(self):
        pixmap = QPixmap(self.image1_path)
        # scaled_pixmap = pixmap.scaled(self.original_image.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.original_image.setPixmap(pixmap)
        self.original_image.setScaledContents(True)
        self.MessageLabel.setText(f"Constant Image Loaded")
        self.MessageLabel.setStyleSheet("color: green;")

    def load_image(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Image Files (*.png;*.jpg;*.jpeg)", options=options)
        if fileName:
            self.image2_path = fileName
            self.MessageLabel.setText(f"Image 2 Loaded")
            self.MessageLabel.setStyleSheet("color: green;")
            pixmap = QPixmap(fileName)
            scaled_pixmap = pixmap.scaled(self.new_image.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.new_image.setPixmap(scaled_pixmap)
            self.new_image.setScaledContents(True)

    def match_images(self):
        if self.image1_path and self.image2_path:
            if verify_faces(self.image1_path, self.image2_path):
                QMessageBox.information(self, "Match Images", "<span style='color: green;'>Hurray! The two faces matched!</span>")
            else:
                QMessageBox.information(self, "Match Images", "<span style='color: red'>Ooopss..the faces DO NOT match.</span>")
        else:
            QMessageBox.warning(self, "Match Images", "<span style='color: red'>Please load the second image before matching.</span>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())