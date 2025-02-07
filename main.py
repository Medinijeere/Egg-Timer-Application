import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPalette, QColor
from PyQt5.QtCore import QTimer, QTime, Qt, QSize
from PyQt5.QtMultimedia import QSound

class EggTimerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Egg Timer <3")
        self.setGeometry(100, 100, 350, 350)  # Smaller square dimensions

        # Set window background color
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#F7DC6F"))  # Mustard yellow
        self.setPalette(palette)

        self.setStyleSheet("""
            QLabel {
                color: black;
                background: transparent;
            }
            QPushButton {
                border: none;
                background: transparent;
            }
            QPushButton:hover {
                background-color: #FFF2CC;  # Slight hover effect
            }
        """)

        # Title Label
        self.title_label = QLabel("What are you making today?", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 16, QFont.Bold))

        # Timer Label
        self.timer_label = QLabel("4:00", self)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont("Arial", 28, QFont.Bold))

        # Window Title
        self.window_title_label = QLabel("Egg Timer <3", self)
        self.window_title_label.setAlignment(Qt.AlignCenter)
        self.window_title_label.setFont(QFont("Press Start 2P", 20))  # Pixelated font
        self.window_title_label.setStyleSheet("color: orange;")

        # Get base directory for bundled resources
        base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

        # Egg Types and Icons (with relative paths)
        self.egg_types = {
            "Boiled Egg": (os.path.join(base_dir, "images", "New Piskel-1.png.png"), QTime(0, 4, 0), 250),
            "Omelette": (os.path.join(base_dir, "images", "New Piskel-1.png (2).png"), QTime(0, 3, 0), 250),
            "Bullseye Egg": (os.path.join(base_dir, "images", "New Piskel-1.png (1).png"), QTime(0, 2, 30), 250)
        }

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.remaining_time = QTime(0, 4, 0)

        # Layout for Egg Buttons
        egg_layout = QVBoxLayout()

        # Create the top row for two buttons side by side
        top_layout = QHBoxLayout()

        for i, (egg_name, (image_path, time, icon_size)) in enumerate(self.egg_types.items()):
            egg_button = QPushButton(self)
            egg_pixmap = QPixmap(image_path)
            egg_pixmap = egg_pixmap.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            egg_icon = QIcon(egg_pixmap)
            egg_button.setIcon(egg_icon)
            egg_button.setIconSize(QSize(icon_size, icon_size))
            egg_button.setCursor(Qt.PointingHandCursor)
            egg_button.clicked.connect(lambda checked, t=time: self.start_timer(t))  # Connect button to start_timer

            egg_label = QLabel(egg_name, self)
            egg_label.setAlignment(Qt.AlignCenter)
            egg_label.setFont(QFont("Arial", 12, QFont.Bold))

            # Create individual QVBoxLayout for each egg type: button + label stacked vertically
            egg_item_layout = QVBoxLayout()
            egg_item_layout.addWidget(egg_button)
            egg_item_layout.addWidget(egg_label)

            # Add buttons and labels to either top layout or bottom layout
            if i < 2:  # First two eggs go in the top row
                top_layout.addLayout(egg_item_layout)
            else:  # The last egg goes below
                egg_layout.addLayout(egg_item_layout)

        # Add the window title and other labels to the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.window_title_label)  # Add window title at the top
        main_layout.addSpacing(10)
        main_layout.addWidget(self.title_label)
        main_layout.addSpacing(10)

        # Add the top layout (for two buttons side by side) and the third button below it
        main_layout.addLayout(top_layout)
        main_layout.addSpacing(10)
        main_layout.addLayout(egg_layout)
        main_layout.addSpacing(20)
        main_layout.addWidget(self.timer_label)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def start_timer(self, time):
        self.remaining_time = time
        self.timer_label.setText(time.toString("m:ss"))
        self.timer.start(1000)

    def update_timer(self):
        if self.remaining_time == QTime(0, 0, 0):
            self.timer.stop()
            self.timer_label.setText("Time's up! ⏳")
            QSound.play(os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), 'times_up.wav'))  # Play sound on timer completion
        else:
            self.remaining_time = self.remaining_time.addSecs(-1)
            self.timer_label.setText(self.remaining_time.toString("m:ss"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EggTimerApp()
    window.show()
    sys.exit(app.exec_())   i want my icons in the flashcard project to be as big as these in this code
