# Proton X50 原生 Apple CarPlay 完整安装与适配指南 (DiPlay Android 5.1 移植版)

本项目为 **Proton X50 (宝腾 X50)** 车机定制的免盒子原生 Apple CarPlay 接收方案。  
基于开源项目 [DiPlay](https://github.com/shihabal3amri/DiPlay) 进行深度逆向分析与向下移植，成功实现 **Android 5.1.1 (API 22) / ECARX E01 车机芯片** 完美运行，支持 **有线 (USB NCM/OTG)** 与 **无线 (Wi-Fi/热点)** 连接，无需购买任何外置 CarPlay 盒子（如 Carlinkit、Autokit 等）。

---

## 目录
1. [Proton X50 车机硬件与系统规格](#1-proton-x50-车机硬件与系统规格)
2. [改动技术细节 (Changelog for Developers)](#2-改动技术细节-changelog-for-developers)
3. [准备工作](#3-准备工作)
4. [第一步：确认车机固件版本](#第一步确认车机固件版本)
5. [第二步：固件降级教程 (仅针对高版本 ATLAS)](#第二步固件降级教程-仅针对高版本-atlas)
6. [第三步：U盘破解与 APK 注入安装](#第三步u盘破解与-apk-注入安装)
7. [第四步：CarPlay 首次连接与使用教程](#第四步carplay-首次连接与使用教程)
8. [第五步：针对 E01 处理器的性能调优配置 (防卡顿)](#第五步针对-e01-处理器的性能调优配置-防卡顿)
9. [常见问题与故障排查 (FAQ)](#常见问题与故障排查-faq)

---

## 1. Proton X50 车机硬件与系统规格

- **适配车型**：Proton X50（Standard 标准版 / Executive 豪华版 / Premium 尊贵版 / Flagship 旗舰版）
- **核心芯片 (SoC)**：ECARX E01（吉利/亿咖通自主研制，四核 ARM Cortex-A53，搭载 Mali-T820 GPU）
- **底层系统**：Android 5.1.1 Lollipop（API Level 22，32位 ARMv7-a 运行环境）
- **车机界面系统**：Geely/Proton ATLAS OS (GKUI 19)
- **USB 接口**：位于前排中控台马鞍底部下方的 USB 数据口（支持 OTG / NCM 主机模式）

---

## 2. 改动技术细节 (Changelog for Developers)

原始 DiPlay 仅支持 Android 9.0+ (API 28)，本项目针对 Android 5.1 (API 21/22) 进行了全栈向下兼容改造：

1. **核心 SDK 门槛降低**：
   - `minSdk` 由 `28` 全面降级为 `21`（支持 Android 5.0 / 5.1 / 5.1.1）。
   - 开启 `multiDexEnabled = true`，适配 Dalvik/ART 早期 Dex 架构限制。
2. **C++ 原生层 (NDK / JNI) 重新编译**：
   - 调整 `shared/src/main/jni/Application.mk` 与 `shared/build.gradle` 中 `APP_PLATFORM := android-21`。
   - 针对 `armeabi-v7a`、`arm64-v8a`、`x86`、`x86_64` 4 种架构全面编译通过，在 Proton X50 32 位系统上高效运行。
3. **Android 5.1 API 运行时兼容防护**：
   - `PendingIntent.FLAG_IMMUTABLE`：增加 `Build.VERSION.SDK_INT >= Build.VERSION_CODES.M` 判定条件，在 Android 5.1 上自动回退为 `0`，杜绝启动崩溃。
   - `Settings.canDrawOverlays` (悬浮窗权限)：增加 API 23+ 防护判定，Android 5.1 默认允许前台悬浮窗绘制。
   - `Settings.System.canWrite` (系统设置修改权限)：防护热点与网络切换接口。
   - `getSystemServiceCompat` 扩展方法：安全向下兼容获取 `UsbManager` 与 `BluetoothManager`。
4. **Jetpack Compose 与 Manifest Merger 依赖规避**：
   - 在 `AndroidManifest.xml` 中配置 `tools:overrideLibrary`，安全忽略 Compose Material、Animation、Media3 与 WorkManager 等库的 API 23 强制限制。
5. **品牌定制与视觉重塑**：
   - 应用包名 Label 由 `DiPlay` 改为 **`Proton`**。
   - 图标重构为 Proton 咆哮虎头立体金属徽标，完美融入车机原生应用列表。

---

## 3. 准备工作

1. **硬件准备**：
   - 1 个 **8GB ~ 32GB** 的 USB 2.0/3.0 U盘（建议格式化为 **FAT32** 格式）。
   - 一根优质 Apple 原装或 MFi 认证数据线（用于有线连接）。
   - 运行 iOS 13 以上的 iPhone。
2. **软件/固件准备**：
   - 本项目编译产物：`dist/Proton-CarPlay-v0.2.20-Android5.1.apk`
   - Proton X50 破解升级工具包（来自 xeon1989 开源贡献）

---

## 4. 第一步：确认车机固件版本

1. 启动车辆，进入车机中控屏幕。
2. 点击 **Settings (设置)** -> **System (系统)** -> **About / System Information (关于系统)**。
3. 查看当前车机版本：
   - **高配车型 (Premium / Flagship)**：目标安全版本为 **`617v1`**。
   - **低配车型 (Standard / Executive)**：目标安全版本为 **`618v1`**。
4. **判定**：
   - 如果当前是 `617v1` 或 `618v1`，直接跳到 **[第三步：U盘破解与 APK 注入安装](#第三步u盘破解与-apk-注入安装)**。
   - 如果当前版本高于 617v1 (如 `617v2`, `617v3` 等) 或被官方升级封堵了 sideload，请先按照 **第二步** 降级。

---

## 5. 第二步：固件降级教程 (仅针对高版本 ATLAS)

> ⚠️ **注意**：刷机过程中请保持车辆处于启动点火状态 (Engine ON)，切勿在中途熄火或拔出 U 盘！

1. 准备一个干净且格式化为 **FAT32** 的 U盘。
2. 访问降级固件库：
   - [Proton-X50-IHU-Upgrade-Downgrade](https://github.com/xeon1989/Proton-X50-IHU-Upgrade-Downgrade)
   - [proton_firmware](https://github.com/xeon1989/proton_firmware)
3. 下载对应车型的 **617v1 (高配)** 或 **618v1 (低配)** 固件包。
4. 将固件升级文件解压到 U 盘根目录。
5. 将 U 盘插入中控马鞍下方的 USB 数据口。
6. 车机会自动检测到升级固件，或在工程设置中选择 "System Update"。
7. 等待进度条走完并自动重启，重新开机后确认系统版本已变为 `617v1` / `618v1`。

---

## 6. 第三步：U盘破解与 APK 注入安装

利用 U盘脚本自动化完成 QDLink 冲突禁用并静默安装本 CarPlay 应用：

1. 格式化 U 盘为 **FAT32**。
2. 下载 [Proton-X50-APK-Installer-ATLAS](https://github.com/xeon1989/Proton-X50-APK-Installer-ATLAS)。
3. 将本项目生成的 APK：`Proton-CarPlay-v0.2.20-Android5.1.apk` 复制并重命名为 `Proton.apk`（或任意简短英文字符名）。
4. 放入 U 盘的 `install/app/` 目录中。
   U 盘最终目录结构应如下：
   ```text
   U盘根目录/
   ├── b832bc43-xxxx-xxxx-xxxx/  (系统更新与提权检测目录)
   ├── install/
   │   ├── app/
   │   │   └── Proton.apk       <-- 放入我们的 Proton CarPlay 安装包
   │   └── scripts/
   └── autorun.sh / update 脚本
   ```
5. 进入车内，打火启动车辆，等待车机完全进入主界面。
6. 将准备好的 U 盘插入前排马鞍下方的 **USB 数据接口**（注意：部分车型扶手箱内为纯充电口，必须插中控台下方支持数据传输的接口）。
7. 屏幕会弹出更新提示或脚本自动在后台执行提权与静默安装（耗时约 1~2 分钟）。
8. 提示成功后拔出 U 盘，重启车机（长按静音键或双击音量滚轮重启）。
9. 在车机应用列表 (All Apps) 中，即可看到带有 Proton 虎头徽标的 **「Proton」** 应用！

---

## 7. 第四步：CarPlay 首次连接与使用教程

### 方式 A：有线连接 (推荐，最稳定，零延迟)
1. 点击打开车机上的 **Proton** 应用。
2. 首次启动时，弹出权限请求，全部点击 **「允许 (Allow)」**。
3. 用优质 Lightning / USB-C 数据线将 iPhone 接入中控台马鞍底部的 USB 数据口。
4. iPhone 屏幕亮起，弹出提示：
   - 提示「要信任此电脑吗？」-> 点击 **「信任」** 并输入锁屏密码。
   - 提示「要在车机上使用 CarPlay 吗？」-> 点击 **「使用 CarPlay」**。
5. 车机屏幕会提示「允许 Proton 访问 USB 设备」-> 勾选 **「默认用于该设备」** 并点击 **「确定」**。
6. 绚丽的 Apple CarPlay 界面立刻全屏呈现在 Proton X50 车机大屏上！

---

### 方式 B：无线连接 (Wi-Fi + 蓝牙)
1. **网络连接**（任选其一）：
   - **方案 1 (手机热点)**：iPhone 打开「个人热点」（建议开启「最大化兼容性」），车机 Wi-Fi 连接至 iPhone 热点。
   - **方案 2 (车机热点)**：车机开启 Wi-Fi 热点，iPhone 连接至车机 Wi-Fi。
2. 打开车机上的 **Proton** 应用。
3. 手机与车机建立蓝牙配对。
4. Proton 应用会自动探测 iPhone 并通过无线链路握手，成功建立无线 CarPlay。

---

## 8. 第五步：针对 E01 处理器的性能调优配置 (防卡顿)

由于 Proton X50 搭载的是四核 Cortex-A53 架构的 ECARX E01 处理器，算力相对有限，强烈建议按照以下参数进行优化配置以保证丝滑流畅：

1. 打开 **Proton** 应用设置（可点击界面右上角齿轮或手机断开时的设置面板）：
2. **视频解码器 (Video Codec)**：
   - 必须设置为 **`H.264 (AVC)`**。
   - ⚠️ **切勿选择 HEVC / H.265 软解**，A53 软解 HEVC 会导致 CPU 占用率 100% 出现发热卡顿。
3. **分辨率与帧率 (Resolution & Frame Rate)**：
   - 推荐分辨率：`1280 x 720`（完美匹配 X50 720P/1080P 屏幕比例）。
   - 推荐帧率：`30 fps`（功耗与流畅度最佳平衡）或 `60 fps`（有线连接下测试平稳时）。
4. **音频通道策略 (Audio Route)**：
   - 如果遇到导航语音或电话声音冲突，可在设置中选择：
     - `Native Audio (车机原生通道)` 或 `Car Bluetooth Route (原车蓝牙通话路由)`。
5. **暗色模式跟随 (Dark Mode)**：
   - 建议设置为「跟随原车大灯开启状态自动切换」，夜晚行车不刺眼。

---

## 9. 常见问题与故障排查 (FAQ)

### Q1: 插入 iPhone 后车机没反应或只显示充电？
- **原因 1**：插错 USB 口。只有前排下方的马鞍数据口支持 OTG 通讯，扶手箱或后排接口仅供供电。
- **原因 2**：数据线品质问题。劣质线缆仅含供电针脚无数据传输线芯，请使用原装或 MFi 认证数据线。
- **原因 3**：原车 QDLink 互联服务占用了 USB 端口。使用破解脚本时已默认冻结/卸载 QDLink，若仍存在请进入应用管理强制停止 QDLink。

### Q2: 声音只有音乐没有导航声音，或者通话无声音？
- 进入 Proton 应用设置中的「音频 (Audio)」栏目：
  - 勾选 `Use Bluetooth for phone calls (通话走原车蓝牙)`。
  - 将原车蓝牙直接与 iPhone 保持连接，原车方向盘接打电话按键可完美协同运作。

### Q3: 倒车影像切回后黑屏？
- Proton 已内置 `CenterMapOverlay` 状态恢复机制。若倒车后未自动返回，触摸中控屏幕任意位置即可重新唤醒画面。

---

## 开发者构建说明 (Build from Source)

如果你需要自行二次开发或修改源码，请按以下步骤操作：

```bash
# 1. 确保安装了 Android SDK (API 37) 与 NDK (28.x+)
# 2. 本地配置 local.properties 指向 Android SDK 路径
sdk.dir=C:\\Users\\your_user\\AppData\\Local\\Android\\Sdk

# 3. 编译 Native NDK C++ 核心库与 Android 5.1 APK
./gradlew :shared:assembleDebug
./gradlew :common:assembleDebug
./gradlew :mobile:assembleDebug

# 4. 生成的 APK 位于：
mobile/build/outputs/apk/debug/mobile-debug.apk
```

---

*祝所有 Proton X50 车主用车愉快！安全驾驶！*
