# 🚗 DiPlay for Proton X50

[English](README.md) · [简体中文 (华文版)](README.zh-CN.md)

> **Native Apple CarPlay for Proton X50 (ECARX E01 / Android 5.1.1 Lollipop / ATLAS OS)**  
> **No dongle required!** Zero external hardware adapters (Carlinkit, Autokit, etc.).  
> Supports both **Wired (USB OTG)** and **Wireless (Wi-Fi / Hotspot)** CarPlay with the official **Proton roaring tiger emblem** inside CarPlay.

---

## 📥 Quick Download

| Package | Purpose / Description | Download Link |
| :--- | :--- | :--- |
| **⭐ USB Flash Drive All-in-One Package** | **Recommended for Car IHU**: Complete, ready-to-unzip installer package! Bundles **DiPlay (CarPlay)**, **Headunit Reloaded (Android Auto)**, and **Open Hidden Settings**, along with trigger scripts & native `.so` libraries. Just extract to USB root! | [⬇️ **Download DiPlay-Proton-X50-USB-Installer.zip**](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases/latest/download/DiPlay-Proton-X50-USB-Installer.zip) |
| **Standalone APK** | Pure APK package for custom/manual installation. | [⬇️ **Download DiPlay-for-Proton-Android5.1.apk**](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases/latest/download/DiPlay-for-Proton-Android5.1.apk) |
| **All Releases** | Changelog & Version History | [View GitHub Releases](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases) |

---

## 🌟 Key Features for Proton X50

- **All-in-One Connectivity Suite**: Installs **Apple CarPlay (DiPlay)**, **Android Auto (Headunit Reloaded)**, and **Open Hidden Settings** in one single USB plug-and-play step.
- **True Native CarPlay**: Runs directly on the car's built-in ECARX E01 processor without third-party USB dongles.
- **Android 5.1.1 (API 22) Downward Port**: Fully patched and recompiled with NDK C++ native binaries (`armeabi-v7a`, `arm64-v8a`) specifically for Proton X50.
- **Proton Vehicle Branding**: Inside Apple CarPlay, the OEM return tile is branded as **Proton** with the official **Proton roaring tiger emblem**. Tapping it returns directly to the Proton X50 car dashboard.
- **Wired & Wireless Options**: Connect via the center console USB cable or wirelessly over vehicle hotspot / iPhone personal hotspot.

---

## 🛠️ Step-by-Step Installation Guide (IHU)

Follow these steps carefully from checking your version to launching CarPlay.

### 📋 Prerequisites (What you need)
1. **USB Flash Drive**: 8 GB to 32 GB, formatted as **FAT32**.
2. **Apple Lightning / USB-C Cable**: Genuine Apple or MFi-certified data cable.
3. **iPhone** (for CarPlay) or **Android Phone** (for Android Auto).
4. **Installer File**: Download [**`DiPlay-Proton-X50-USB-Installer.zip`**](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases/latest/download/DiPlay-Proton-X50-USB-Installer.zip).

---

### Step 1: Check Your Proton X50 IHU Firmware Version

1. Start your car and let the screen boot up.
2. Go to **Settings (设置)** ➡️ **System (系统)** ➡️ **About / System Information (系统信息)**.
3. Check the ATLAS OS version:
   - **High-spec models (Premium / Flagship)**: Target version is **`617v1`**.
   - **Standard / Executive models**: Target version is **`618v1`**.

> [!IMPORTANT]
> - If your current version is **`617v1`** or **`618v1`**, skip Step 2 and proceed directly to **Step 3**!
> - If your car is on a newer version (e.g. `617v2`, `617v3`, etc.) where sideloading is patched by Proton, you must downgrade to `617v1`/`618v1` first (see Step 2).

---

### Step 2: Downgrade IHU Firmware (Only if on 617v2+)

> [!WARNING]
> Keep the car engine running (**Engine ON**) during the entire upgrade/downgrade process. Never turn off the car or pull out the USB drive mid-flash!

1. Format your USB drive as **FAT32**.
2. Download the safe downgrade firmware matching your vehicle trim:
   - [Proton-X50-IHU-Upgrade-Downgrade (by xeon1989)](https://github.com/xeon1989/Proton-X50-IHU-Upgrade-Downgrade)
   - [Proton Firmware Repository](https://github.com/xeon1989/proton_firmware)
3. Extract the firmware files into the **root directory** of your FAT32 USB drive.
4. Plug the USB drive into the **lower front center console USB data port** (underneath the floating bridge console).
5. The screen will prompt for system update. Confirm and wait for the progress bar to finish and the unit to reboot.
6. Verify in **System Information** that the version is now `617v1` or `618v1`.

---

### Step 3: Install DiPlay via Ready-to-Use USB Drive Package

1. Format your USB drive (8 GB to 32 GB) as **FAT32**.
2. Download [**`DiPlay-Proton-X50-USB-Installer.zip`**](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases/latest/download/DiPlay-Proton-X50-USB-Installer.zip).
3. Unzip `DiPlay-Proton-X50-USB-Installer.zip` directly into the **root directory** of your FAT32 USB drive.

**Your USB drive folder structure will look like this:**
```text
USB Flash Drive (FAT32)/
├── b832bc61472727635baffcf25dd28e9f239273e2/
│   ├── b8d19f9e951515117820d8d785034d74.sh
│   └── ecead2369cb605ecb21209d1fb4c654f.sh
└── app/
    ├── hutroops.com.shihab.diplay/          # 🍎 Apple CarPlay (DiPlay for Proton)
    │   ├── com.shihab.diplay.apk
    │   └── lib/
    │       ├── arm/
    │       └── arm64/
    ├── hutroops.gb.xxy.hr/                  # 🤖 Android Auto (Headunit Reloaded / HUR)
    │   ├── gb.xxy.hr.apk
    │   └── lib/
    │       ├── arm/
    │       └── arm64/
    ├── hutroops.dxidev.openhiddensettings/  # ⚙️ Open Hidden Settings (Android Settings & ADB)
    │   ├── dxidev.openhiddensettings.apk
    │   └── lib/arm/
    └── hutroops.com.amaze.filemanager/      # 📁 Amaze File Manager (Explorer & Log Viewer)
        ├── com.amaze.filemanager.apk
        └── lib/
            ├── arm/
            └── arm64/
```

4. Enter the car, start the engine (**Engine ON**), and wait for the main screen to load.
5. Insert the USB drive into the **bottom center console USB data port** (under the gear shifter area; do NOT use the armrest charging port).
6. **Automatic Sideloading Execution**:
   - The screen will momentarily jump to **Wireless Charging Settings** (indicates the script has successfully started).
   - The script automatically mounts `/system`, installs all 4 apps into `/system/app/`, configures native library permissions, and disables conflicting background processes.
   - The screen will then jump to **System Settings** (indicates installation has completed!).
   - The IHU will automatically reboot in ~5 seconds.
7. Unplug your USB drive.
8. When the screen restarts, open **All Apps**. You will see:
   - **DiPlay**: Native Apple CarPlay with Proton tiger emblem.
   - **Headunit Reloaded (HUR)**: Native Android Auto.
   - **Open Hidden Settings**: Stock Android settings and developer options.
   - **Amaze File Manager**: File explorer to browse files, view logs, and copy files to USB.

---

### Step 4: Connect Apple CarPlay

#### 🔌 Option A: Wired Connection (Recommended: Zero Latency & Most Stable)
1. Tap to open **DiPlay** on your Proton X50 screen.
2. Grant all requested permissions on the first run.
3. Plug your iPhone into the lower center console USB data port using your data cable.
4. On your iPhone:
   - Tap **"Trust"** when prompted to "Trust This Computer" and enter your screen passcode.
   - Tap **"Use CarPlay"** when prompted.
5. On the car screen:
   - Check **"Always allow"** and tap **OK** on the USB accessory permission prompt.
6. **Apple CarPlay will immediately launch in full screen on your Proton X50 display!**

---

#### 📶 Option B: Wireless Connection (Wi-Fi + Bluetooth)
1. **Network Setup** (choose one):
   - **Method 1 (Car Hotspot)**: Turn on Wi-Fi Hotspot on the Proton X50 IHU, then connect your iPhone to the car's Wi-Fi.
   - **Method 2 (iPhone Hotspot)**: Turn on Personal Hotspot on your iPhone (enable "Maximize Compatibility"), then connect the car's Wi-Fi to your iPhone's hotspot.
2. Open **DiPlay** on the car screen.
3. Connect and pair your iPhone with the car's native Bluetooth.
4. DiPlay will automatically discover your iPhone and start wireless CarPlay.

---

### Step 5: Recommended Performance Settings for ECARX E01 SoC

Because the Proton X50's ECARX E01 processor is a power-efficient quad-core Cortex-A53, configure these settings to ensure smooth operation and prevent overheating:

1. Open **DiPlay Settings** (tap the gear icon):
2. **Video Codec (视频解码器)**:
   - Set to **`H.264 (AVC)`**.
   - > [!CAUTION]
     > **Do NOT select HEVC / H.265 software decode.** Software decoding HEVC on Cortex-A53 cores causes high CPU usage, thermal throttling, and frame drops.
3. **Resolution & FPS**:
   - Resolution: **`1280 x 720`** (optimal aspect ratio and crispness for X50 screens).
   - Frame Rate: **`30 fps`** (best battery and thermal balance) or **`60 fps`** (if stable on wired).
4. **Audio Routing**:
   - Set Audio Route to **`Car Bluetooth Route`**. This ensures phone calls and steering wheel call buttons work directly through the car's native Bluetooth system without echo.

---

### 🔘 Exiting CarPlay Back to the Proton Head Unit

Inside Apple CarPlay:
- Look for the app tile named **"Proton"** with the **Proton roaring tiger emblem**.
- Tap it at any time to immediately return to the Proton X50 car dashboard, climate controls, or 360° camera views!

---

### Step 6: Exporting Logs for Troubleshooting & Debugging

If you encounter any connection issues, unexpected disconnects, or crashes, you can easily export the diagnostic logs:

1. **Option A: Generate Report via DiPlay Settings**:
   - Open **DiPlay** ➡️ Tap the **Settings (gear icon)**.
   - Tap **View Diagnostic Report** (or export report).
   - DiPlay automatically aggregates session logs, connection handshakes, and crash traces into `Downloads/DiPlay/`.
2. **Option B: Copy Logs to USB using Amaze File Manager**:
   - Insert any USB flash drive into the car's USB data port.
   - Open **Amaze File Manager** from All Apps.
   - Navigate to:
     - `Internal Storage` ➡️ `Download` ➡️ `DiPlay/` (contains diagnostic reports).
     - Or `/sdcard/Android/data/com.shihab.diplay/files/logs/` (contains `diplay.log` and `last-crash.txt`).
   - Long-press the file, tap **Copy**.
   - Tap the sidebar menu ➡️ Select your **USB Drive** (`udisk1`) ➡️ Tap **Paste**.
   - Remove the USB drive, plug it into your computer, and share the log files for assistance!

## ❓ Frequently Asked Questions (FAQ)

### Q1: The iPhone charges, but CarPlay doesn't launch.
- **Wrong USB port**: Only the front lower console port has OTG data capability. The armrest box port is charging-only in some trims.
- **Cable quality**: Poor quality third-party cables only have power pins and lack data transmission lines. Use an original Apple or MFi-certified cable.
- **QDLink conflict**: Ensure the APK installer script completed, which freezes the conflicting QDLink background service.

### Q2: How do steering wheel buttons work with CarPlay?
- Volume up/down and mute work natively.
- With Audio Route set to `Car Bluetooth Route`, the phone call answer/hangup buttons on the steering wheel work with your incoming/outgoing calls seamlessly.

---

## 👨‍💻 Developer & Cloud Build

This repository includes a fully automated **GitHub Actions CI/CD** workflow. Whenever new code is pushed:
1. GitHub spins up a clean cloud Ubuntu runner with Java 25, Android SDK 37, and NDK 28.
2. The APK is compiled automatically from source (`./gradlew :mobile:assembleDebug`).
3. The latest APK is published directly to [GitHub Releases](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases).

---

## 🙏 Acknowledgements & Credits

Special thanks to the following open-source projects and developers:

- **[DiPlay](https://github.com/shihabal3amri/DiPlay)** by [@shihabal3amri](https://github.com/shihabal3amri) — Independent CarPlay receiver implementation for Android head units.
- **[xcertplay](https://github.com/Frank-Zsy/xcertplay)** by [@Frank-Zsy](https://github.com/Frank-Zsy) — Core CarPlay protocol and AirPlay receiver engine.
- **[Headunit Reloaded (HUR)](https://forum.xda-developers.com/t/android-4-1-headunit-reloaded-for-android-auto-touch-wifi-mic-hardware-keys.3432348/)** by Emil Borconi — Android Auto receiver engine for Android head units.
- **[Open Hidden Settings](https://github.com/dxidev)** by [@dxidev](https://github.com/dxidev) — Hidden Android settings shortcut utility.
- **[Proton-X50-APK-Installer-ATLAS](https://github.com/xeon1989/Proton-X50-APK-Installer-ATLAS)** by [@xeon1989](https://github.com/xeon1989) — Sideloading exploit script and installer for Proton X50 ATLAS OS.
- **[Proton-X50-IHU-Upgrade-Downgrade](https://github.com/xeon1989/Proton-X50-IHU-Upgrade-Downgrade)** by [@xeon1989](https://github.com/xeon1989) — IHU firmware upgrade & downgrade toolkit for Proton X50.
- **[proton_firmware](https://github.com/xeon1989/proton_firmware)** by [@xeon1989](https://github.com/xeon1989) — Repository of Proton X50 IHU firmware images.

---

### ⚖️ Disclaimer
Apple and CarPlay are registered trademarks of Apple Inc. Proton is a registered trademark of Perusahaan Otomobil Nasional Sdn Bhd. This project is an independent community modification and is not officially affiliated with, endorsed by, or supported by Apple Inc. or Proton Holdings Berhad.

---

*Drive safely and enjoy native Apple CarPlay in your Proton X50!*
