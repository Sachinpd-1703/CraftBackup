import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap, QPainter, QIcon, QFont
from PyQt6.QtCore import Qt, QSize

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # --- 1. Window Configuration ---
        self.setWindowTitle("Minecraft Backup System - Login")
        self.setFixedSize(450, 600) # Fixed 16:9 ratio window
        self.setWindowIcon(QIcon("assets/temp_icon.png"))
        self.background_image = QPixmap("assets/background.png")
        
        self.initUI()
        self.apply_stylesheet()

    def paintEvent(self, event):
        painter = QPainter(self)
        # Scale the image to fit the window, maintaining aspect ratio
        scaled_pixmap = self.background_image.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        painter.drawPixmap(self.rect(), scaled_pixmap)

    def initUI(self):
        # --- 2. Create Widgets ---
        # Login Card
        self.login_card = QWidget(self)
        self.login_card.setFixedSize(400, 550)
        self.login_card.setObjectName("LoginCard")

        # Title and Subtitle
        title = QLabel("Minecraft Backup System")
        title.setObjectName("TitleLabel")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("Sign in to continue")
        subtitle.setObjectName("SubtitleLabel")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Google Login Button
        self.login_button = QPushButton("Sign In with Google")
        self.login_button.setObjectName("LoginButton")
        self.login_button.setIcon(QIcon("assets/google_logo.png"))
        self.login_button.setIconSize(QSize(24, 24))

        # Center the text inside the button
        self.login_button.setStyleSheet("""
            QPushButton {
                text-align: center;
                padding-left: 10px;
            }
        """)

        # Privacy Policy Link
        privacy_link = QLabel("<a href='https://github.com/Sachinpd-1703/CraftBackup'>Privacy Policy</a>")
        privacy_link.setObjectName("Link")
        privacy_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
        privacy_link.setOpenExternalLinks(True)

        # --- 3. Create Layouts ---
        # Main layout to position the card on the Center
        main_layout = QHBoxLayout(self)
        main_layout.addStretch()
        main_layout.addWidget(self.login_card)
        main_layout.addSpacing(15)

        # Layout for the content inside the card
        card_layout = QVBoxLayout(self.login_card)
        card_layout.setContentsMargins(20, 20, 20, 20)
        card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        card_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addSpacing(30)
        card_layout.addWidget(self.login_button)
        card_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        card_layout.addWidget(privacy_link)

    def apply_stylesheet(self):
        # --- 4. Styling ---
        stylesheet = """
            /* Style for the semi-transparent card */
            #LoginCard {
                background-color: rgba(44, 44, 44, 0.85);
                border-radius: 15px;
            }

            /* Style for the main title */
            #TitleLabel {
                color: #E0E0E0; /* Off-White */
                font-family: "Segoe UI", "Roboto", sans-serif;
                font-size: 20pt;
                font-weight: bold;
            }

            /* Style for the subtitle */
            #SubtitleLabel {
                color: #E0E0E0;
                font-family: "Segoe UI", "Roboto", sans-serif;
                font-size: 12pt;
            }

            /* Style for the main login button */
            #LoginButton {
                background-color: #5DBE79; /* Creeper Green */
                color: white;
                font-family: "Segoe UI", "Roboto", sans-serif;
                font-size: 14pt;
                font-weight: 500; /* Medium weight */
                border-radius: 8px;
                padding: 12px;
                text-align: left;
            }
            /* Style for when the mouse hovers over the button */
            #LoginButton:hover {
                background-color: #6DD589; /* A slightly lighter green */
            }

            /* Style for the privacy link */
            #Link {
                color: #6DD5FA; /* Diamond Blue */
                font-family: "Segoe UI", "Roboto", sans-serif;
                font-size: 10pt;
            }
            #Link a {
                color: #6DD5FA;
                text-decoration: none;
            }
        """
        self.setStyleSheet(stylesheet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())