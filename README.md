# adb-remote-directional-bar

Cute just a cute little script to give you some directions and buttons to push via ADB when the touch screen is unresponsive. You're trying to hack something and they don't have a back button.

## ADB Directional Bar 🕹️
A simple yet powerful Python GUI tool built with PyQt5 that provides quick access to Android navigation actions using ADB (Android Debug Bridge). With just a click, you can easily trigger Back, Home, Recent Apps, and Swipe Up actions on your connected Android device.

## Features ✨
- 🔙 **Back Button:** Simulates the Android "Back" action.
- 🏠 **Home Button:** Takes you to the home screen.
- 🗂️ **Recent Apps:** Opens the recent apps view.
- 📱 **Swipe Up:** Performs a swipe gesture to unlock or navigate apps.
- 🖥️ **User-Friendly Interface:** Simple and intuitive button layout.
- ✅ **Error Handling:** Displays messages if ADB is not installed or accessible.
- ⚡ **Lightweight & Fast:** No heavy dependencies, quick execution.

## Prerequisites 🛠️
Ensure the following requirements are met before running the application:

- **Python 3.x** ([Download here](https://www.python.org/downloads/))
- **ADB (Android Debug Bridge)** installed and added to your system PATH.

Check by running:
```bash
adb version
```
- **PyQt5 library**

Install it via pip if you haven't already:
```bash
pip install pyqt5
```

## Installation 🚀
Clone the repository:
```bash
git clone https://github.com/johnohhh1/adb-remote-directional-bar.git
cd adb-remote-directional-bar
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the application:
```bash
python adb_directional_bar.py
```

## Usage 📖
1. Connect your Android device via USB and ensure USB debugging is enabled in Developer Options.
2. Launch the application.
3. Click on the respective buttons to perform the actions on your Android device.

- **← Back** – Go back to the previous screen.
- **O Home** – Return to the home screen.
- **☰ Recent Apps** – Open recent apps.
- **↑ Swipe Up** – Perform a swipe-up action.

## Screenshots 🖼️
(Placeholder image - replace with actual screenshot)

## Troubleshooting 🛑
If you encounter any issues, try the following solutions:

- **ADB not found:**
  - Ensure ADB is installed and available in the system path. Try running:
    ```bash
    adb devices
    ```

- **Device not detected:**
  - Check if USB debugging is enabled on your Android phone.
  - Use the command:
    ```bash
    adb devices
    ```
  - If your device doesn't appear, try reconnecting the USB cable or restarting ADB:
    ```bash
    adb kill-server
    adb start-server
    ```

- **Permission denied errors:**
  - Run the script as administrator or check your system's security settings.

## Future Improvements 🚧
Planned enhancements include:
- 🔄 Add swipe left/right gestures.
- 📱 Add multi-device support.
- 🖥️ Create a tray icon for quick access.
- 🎨 Dark mode for the UI.

## Contributing 🤝
Want to contribute? Feel free to fork the project and submit pull requests. Suggestions and improvements are always welcome!

## License 📜
This project is licensed under the MIT License - see the LICENSE file for details.

## Author 👤
Developed by johnohhh1

If you like this project, consider giving it a ⭐ on GitHub!

Enjoy controlling your Android device with ease using ADB Directional Bar! 🚀

