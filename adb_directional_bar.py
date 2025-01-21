import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class ADBDirectionalBar(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set up the window
        self.setWindowTitle('ADB Directional Bar')
        self.setGeometry(100, 100, 300, 300)

        # Create layout and buttons
        layout = QVBoxLayout()

        self.btnBack = QPushButton('Back', self)
        self.btnBack.clicked.connect(self.send_back)
        layout.addWidget(self.btnBack)

        self.btnHome = QPushButton('O (Home)', self)
        self.btnHome.clicked.connect(self.send_home)
        layout.addWidget(self.btnHome)

        self.btnRecents = QPushButton('III (Recent Apps)', self)
        self.btnRecents.clicked.connect(self.send_recent_apps)
        layout.addWidget(self.btnRecents)

        self.btnSwipeUp = QPushButton('Swipe Up', self)
        self.btnSwipeUp.clicked.connect(self.swipe_up)
        layout.addWidget(self.btnSwipeUp)

        # Set the layout
        self.setLayout(layout)

    def send_adb_command(self, command):
        """Run ADB command and send it to the device."""
        try:
            subprocess.run(['adb', 'shell', command], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running ADB command: {e}")

    def send_back(self):
        """Send ADB back command."""
        self.send_adb_command('input keyevent 4')  # Key event 4 is "Back"

    def send_home(self):
        """Send ADB home command (O button)."""
        self.send_adb_command('input keyevent 3')  # Key event 3 is "Home"

    def send_recent_apps(self):
        """Send ADB recent apps command (III button)."""
        self.send_adb_command('input keyevent 187')  # Key event 187 is "Recent Apps"

    def swipe_up(self):
        """Simulate swipe up gesture."""
        self.send_adb_command('input swipe 500 1500 500 500')  # Adjust coordinates as needed

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ADBDirectionalBar()
    window.show()
    sys.exit(app.exec_())
