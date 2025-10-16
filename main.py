import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedWidget, QTextEdit
from PyQt6.QtGui import QPixmap, QPainter, QIcon
from PyQt6.QtCore import Qt, QSize

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.setWindowTitle("Minecraft Backup System - Login")
        self.setFixedSize(450, 600)
        self.setWindowIcon(QIcon("assets/temp_icon.png"))
        self.background_image = QPixmap("assets/background.png")

        self.initUI()
        self.apply_stylesheet()

    def paintEvent(self, event):
        painter = QPainter(self)
        scaled_pixmap = self.background_image.scaled(self.size(),
                                                     Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                                     Qt.TransformationMode.SmoothTransformation
                                                     )
        painter.drawPixmap(self.rect(), scaled_pixmap)

    def initUI(self):
        # The main card that holds our content
        self.login_card = QWidget(self)
        self.login_card.setFixedSize(400, 550)
        self.login_card.setObjectName("LoginCard")

        # --- The QStackedWidget for switching between pages ---
        self.stacked_widget = QStackedWidget()
        
        # Create the two pages (widgets)
        login_page = self.create_login_page()
        privacy_page = self.create_privacy_page()

        # Add the pages to the stacked widget
        self.stacked_widget.addWidget(login_page)
        self.stacked_widget.addWidget(privacy_page)

        # Set the layout for the main card to contain the stacked widget
        card_layout = QVBoxLayout(self.login_card)
        card_layout.addWidget(self.stacked_widget)

        # Main window layout to center the card
        main_layout = QHBoxLayout(self)
        main_layout.addStretch(1)
        main_layout.addWidget(self.login_card)
        main_layout.addStretch(1)

    def create_login_page(self):
        """Creates the widget for the main login page."""
        login_page_widget = QWidget()
        layout = QVBoxLayout(login_page_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Minecraft Backup System")
        title.setObjectName("TitleLabel")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("Sign in to continue")
        subtitle.setObjectName("SubtitleLabel")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        login_button = QPushButton("Sign In with Google")
        login_button.setObjectName("LoginButton")
        login_button.setIcon(QIcon("assets/google_logo.png"))
        login_button.setIconSize(QSize(24, 24))

        privacy_button = QPushButton("Privacy Policy")
        privacy_button.setObjectName("LinkButton")
        privacy_button.setCursor(Qt.CursorShape.PointingHandCursor)
        privacy_button.clicked.connect(self.show_privacy_page) # Switch to privacy page

        layout.addStretch(1)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(30)
        layout.addWidget(login_button)
        layout.addStretch(1)
        layout.addWidget(privacy_button)
        
        return login_page_widget

    def create_privacy_page(self):
            """Creates the widget for the privacy policy page."""
            privacy_page_widget = QWidget()
            layout = QVBoxLayout(privacy_page_widget)
            layout.setContentsMargins(20, 20, 20, 20)
            
            title = QLabel("Privacy Policy")
            title.setObjectName("TitleLabel")
            title.setAlignment(Qt.AlignmentFlag.AlignCenter)

            policy_text_area = QTextEdit()
            policy_text_area.setReadOnly(True)
            policy_text_area.setObjectName("PolicyText")
            
            # --- FIX: Use .setHtml() to render the bold tags ---
            policy_text_area.setHtml("""
            <p>This policy explains how the Minecraft Backup System handles your information.</p>

            <p><b>1. Information We Use</b><br>
            To connect to your Google Drive, this application will ask for permission to access your basic profile information (email address) and the ability to manage files that it creates in your Google Drive.</p>

            <p><b>2. How We Use Information</b><br>
            Your Google account information is used only to authenticate you and to upload/download your backup files to your own Google Drive. Your game files are never sent to us or any third party.</p>

            <p><b>3. Information Sharing</b><br>
            We do not share any of your information with anyone. All data remains on your computer or in your own Google Drive account.</p>

            <p><b>4. Security</b><br>
            We use Google's secure OAuth 2.0 and HTTPS protocols to ensure your data is transferred safely and your account is protected. We never see or store your Google password.</p>

            <p>Thank you for using the Minecraft Backup System!</p>
            """)

            back_button = QPushButton("Back")
            back_button.setObjectName("BackButton")
            back_button.clicked.connect(self.show_login_page) # Switch back to login page
            
            layout.addWidget(title)
            layout.addWidget(policy_text_area)
            layout.addWidget(back_button)

            return privacy_page_widget

    def show_privacy_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_login_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def apply_stylesheet(self):
        stylesheet = """
            #LoginCard {
                background-color: rgba(44, 44, 44, 0.85);
                border-radius: 15px;
            }
            #TitleLabel {
                color: #E0E0E0;
                font-family: "Segoe UI", "Roboto", sans-serif;
                font-size: 20pt;
                font-weight: bold;
                padding-bottom: 10px;
            }
            #SubtitleLabel {
                color: #E0E0E0;
                font-family: "Segoe UI", "Roboto", sans-serif;
                font-size: 12pt;
            }
            #LoginButton {
                background-color: #5DBE79;
                color: white;
                font-family: "Segoe UI", "Roboto", sans-serif;
                font-size: 14pt;
                font-weight: 500;
                border-radius: 8px;
                padding: 12px;
                text-align: center;
                padding-left: 20px;
            }

            #LoginButton:hover {
                background-color: #6DD589;
            }

            #LinkButton {
                color: #6DD5FA;
                font-family: "Segoe UI", "Roboto", sans-serif;
                font-size: 10pt;
                background-color: transparent;
                border: none;
                text-decoration: underline;
            }
            #LinkButton:hover {
                color: #83E0FF;
            }
            #PolicyText {
                background-color: #3C3C3C;
                color: #D0D0D0;
                border-radius: 5px;
                border: 1px solid #555;
                font-family: "Segoe UI", "Roboto", sans-serif;
                font-size: 10pt;
            }
            #BackButton {
                background-color: #555;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-size: 10pt;
                font-weight: bold;
            }
            #BackButton:hover {
                background-color: #666;
            }
        """
        self.setStyleSheet(stylesheet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())