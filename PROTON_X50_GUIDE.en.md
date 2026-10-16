# Proton X50 Native Apple CarPlay Complete Installation & Flashing Guide (DiPlay Android 5.1 Port)

[English](PROTON_X50_GUIDE.en.md) · [简体中文 (Chinese Version)](PROTON_X50_GUIDE.md)

This project provides a dongle-free, native Apple CarPlay receiver tailored for the **Proton X50** head unit (IHU).  
Based on the open-source [DiPlay](https://github.com/shihabal3amri/DiPlay) project, it has been ported and backward-adapted to run seamlessly on **Android 5.1.1 (API 22) / ECARX E01 SoC**, supporting both **Wired (USB NCM/OTG)** and **Wireless (Wi-Fi / Hotspot)** connections without requiring external CarPlay adapters (such as Carlinkit, Autokit, etc.).

---

## Table of Contents
1. [Proton X50 Head Unit Hardware & System Specs](#1-proton-x50-head-unit-hardware--system-specs)
2. [Technical Modifications (Changelog for Developers)](#2-technical-modifications-changelog-for-developers)
3. [Prerequisites](#3-prerequisites)
4. [Step 1: Check IHU Firmware Version](#step-1-check-ihu-firmware-version)
5. [Step 2: Firmware Downgrade Guide (Only for newer ATLAS versions)](#step-2-firmware-downgrade-guide-only-for-newer-atlas-versions)
6. [Step 3: USB Exploit & APK Sideloading](#step-3-usb-exploit--apk-sideloading)
7. [Step 4: First-Time CarPlay Connection Walkthrough](#step-4-first-time-carplay-connection-walkthrough)
8. [Step 5: Recommended Performance Settings for ECARX E01 SoC](#step-5-recommended-performance-settings-for-ecarx-e01-soc)
9. [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)

---

## 1. Proton X50 Head Unit Hardware & System Specs

- **Compatible Vehicles**: Proton X50 (Standard, Executive, Premium, Flagship)
- **SoC (Processor)**: ECARX E01 (Quad-Core ARM Cortex-A53 with Mali-T820 GPU)
- **Underlying OS**: Android 5.1.1 Lollipop (API Level 22, 32-bit ARMv7-a runtime)
- **UI Platform**: Geely / Proton ATLAS OS (GKUI 19)
- **USB Port**: Located underneath the lower front center console (supports OTG / NCM host mode)

---

## 2. Technical Modifications (Changelog for Developers)

The original DiPlay required Android 9.0+ (API 28). This port introduces full downward compatibility for Android 5.1 (API 21/22):

1. **Lowered SDK Target**:
   - `minSdk` lowered from `28` to `21` across all modules (`:shared`, `:common`, `:mobile`).
   - Enabled `multiDexEnabled = true` to support Dalvik/early ART multi-dex limitations.
2. **Recompiled C++ Native Layer (NDK / JNI)**:
   - Configured `shared/src/main/jni/Application.mk` and `shared/build.gradle` with `APP_PLATFORM := android-21`.
   - Native libraries cleanly compiled for 4 architectures: `armeabi-v7a`, `arm64-v8a`, `x86`, and `x86_64`.
3. **Android 5.1 API Runtime Guards**:
   - `PendingIntent.FLAG_IMMUTABLE`: Fallback to `0` when running on pre-Android 6.0 (`Build.VERSION.SDK_INT < 23`) to prevent initialization crashes.
   - `Settings.canDrawOverlays`: Guarded with API 23+ check; Android 5.1 permits overlays by default.
   - `Settings.System.canWrite`: Guarded for network and hotspot toggle routines.
   - Added `PlatformCompat.kt` with `getSystemServiceCompat` for safe service retrieval (`UsbManager`, `BluetoothManager`).
4. **Jetpack Compose & Manifest Merger Overrides**:
   - Applied `tools:overrideLibrary` in `AndroidManifest.xml` to bypass API 23 minimum requirement from Compose Material, Animation, Ripple, Media3, and WorkManager.
5. **Vehicle OEM Branding inside Apple CarPlay**:
   - `DEFAULT_OEM_LABEL` configured to `"Proton"`.
   - Replaced default CarPlay OEM exit icon (`ic_car_home.png` 192x192 RGB and `placeholder_icon.png` 1024x1024 RGB) with the official-style **Proton roaring tiger emblem**.
   - Tapping the Proton tile in CarPlay seamlessly returns the screen to the Proton X50 head unit dashboard.

---

## 3. Prerequisites

1. **Hardware**:
   - 1x USB Flash Drive (**8GB to 32GB**, formatted as **FAT32**).
   - 1x High-quality original Apple or MFi-certified USB cable.
   - An iPhone running iOS 13 or later.
2. **Software**:
   - The compiled APK: `DiPlay-for-Proton-Android5.1.apk` (available from [GitHub Releases](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases)).
   - Proton X50 Sideload Toolkit (courtesy of xeon1989's open-source projects).

---

## 4. Step 1: Check IHU Firmware Version

1. Start your car and let the head unit boot up.
2. Navigate to **Settings** -> **System** -> **About / System Information**.
3. Check the firmware version:
   - **High-spec models (Premium / Flagship)**: Target version is **`617v1`**.
   - **Standard / Executive models**: Target version is **`618v1`**.
4. **Action**:
   - If your head unit is currently on `617v1` or `618v1`, skip directly to **[Step 3: USB Exploit & APK Sideloading](#step-3-usb-exploit--apk-sideloading)**.
   - If your version is newer (e.g., `617v2`, `617v3`, etc.) where sideloading is patched, perform **Step 2** to downgrade.

---

## 5. Step 2: Firmware Downgrade Guide (Only for newer ATLAS versions)

> ⚠️ **Warning**: Keep the vehicle engine running (Engine ON) during the entire flashing process. Never turn off the car or remove the USB drive mid-flash!

1. Format your USB drive as **FAT32**.
2. Download the appropriate firmware from:
   - [Proton-X50-IHU-Upgrade-Downgrade](https://github.com/xeon1989/Proton-X50-IHU-Upgrade-Downgrade)
   - [proton_firmware](https://github.com/xeon1989/proton_firmware)
3. Extract the firmware files into the root directory of the USB drive.
4. Plug the USB drive into the data USB port beneath the center console.
5. Follow the system update prompt to flash the firmware.
6. Once rebooted, verify that your version is now `617v1` or `618v1`.

---

## 6. Step 3: USB Exploit & APK Sideloading

Use the automated USB installer script to disable QDLink conflicts and silently install DiPlay:

1. Format your USB drive as **FAT32**.
2. Download [Proton-X50-APK-Installer-ATLAS](https://github.com/xeon1989/Proton-X50-APK-Installer-ATLAS).
3. Copy `DiPlay-for-Proton-Android5.1.apk` into the `install/app/` folder on the USB drive.
   The USB drive structure should look like:
   ```text
   USB Root/
   ├── b832bc43-xxxx-xxxx-xxxx/  (exploit & update detection directory)
   ├── install/
   │   ├── app/
   │   │   └── DiPlay.apk        <-- Put the DiPlay APK here
   │   └── scripts/
   └── autorun scripts
   ```
4. Start your car and wait for the IHU to fully boot.
5. Insert the USB drive into the **bottom center console data USB port**.
6. The script will execute automatically in the background (takes ~1-2 minutes).
7. When complete, remove the USB drive and reboot the head unit (press and hold Mute or double-press the volume roller).
8. Open the app drawer (All Apps), and you will see the **DiPlay** app!

---

## 7. Step 4: First-Time CarPlay Connection Walkthrough

### Method A: Wired Connection (Recommended: Zero Latency, Maximum Stability)
1. Launch **DiPlay** on your Proton X50 screen.
2. Grant all requested permissions on first run.
3. Plug your iPhone into the lower center console USB port using an original or MFi cable.
4. On your iPhone:
   - Tap **"Trust"** when prompted to "Trust This Computer" and enter your passcode.
   - Tap **"Use CarPlay"** when prompted.
5. On the car screen:
   - Check **"Always allow"** and tap **OK** on the USB accessory permission prompt.
6. Apple CarPlay will instantly appear in full screen on your Proton X50 display!

---

### Method B: Wireless Connection (Wi-Fi + Bluetooth)
1. **Network Setup**:
   - **Option 1 (Car Hotspot)**: Turn on Personal Hotspot on the Proton X50, then connect your iPhone to the car's Wi-Fi.
   - **Option 2 (iPhone Hotspot)**: Turn on Personal Hotspot on your iPhone (enable "Maximize Compatibility"), then connect the car's Wi-Fi to your iPhone.
2. Launch the **DiPlay** app on the car unit.
3. Pair your iPhone with the car's Bluetooth.
4. DiPlay will discover the iPhone and establish wireless CarPlay automatically.

---

## 8. Step 5: Recommended Performance Settings for ECARX E01 SoC

Because the ECARX E01 utilizes a power-efficient quad-core Cortex-A53 processor, configuring the following settings ensures smooth and cool operation:

1. In DiPlay settings:
2. **Video Codec**:
   - Must be set to **`H.264 (AVC)`**.
   - ⚠️ **Do NOT select HEVC / H.265 software decoding** (Cortex-A53 software decoding HEVC will cause 100% CPU spikes and thermal throttling).
3. **Resolution & Frame Rate**:
   - Recommended Resolution: `1280 x 720`.
   - Recommended Frame Rate: `30 fps` (optimal thermal and battery balance) or `60 fps` on wired connections.
4. **Audio Routing**:
   - If navigation or phone call audio conflicts occur, select `Car Bluetooth Route` so phone calls use the car's native Bluetooth system with steering wheel call buttons.

---

## 9. Frequently Asked Questions (FAQ)

### Q1: The car only charges my iPhone and does not launch CarPlay.
- Ensure you are using the lower center console USB port (the armrest box port is charging-only in some models).
- Use a genuine Apple or MFi-certified data cable.
- Make sure QDLink has been disabled by the exploit script.

### Q2: Returning to car controls from CarPlay?
- Inside Apple CarPlay, tap the app icon labeled **"Proton"** with the Proton roaring tiger badge. It will immediately bring you back to the Proton X50 dashboard.

---

*Enjoy native Apple CarPlay in your Proton X50! Drive safely!*
