# 🚗 DiPlay for Proton X50 (宝腾 X50 专属版)

[English (英文版)](README.md) · [简体中文 (华文版)](README.zh-CN.md)

> **为 Proton X50 (ECARX E01 芯片 / Android 5.1.1 底层 / ATLAS OS) 定制的免盒子原生 Apple CarPlay。**  
> **无需购买外置 CarPlay 转接盒！** 零硬件成本，告别 Carlinkit、Autokit 等外挂硬件。  
> 完美支持 **有线连接 (USB 数据口)** 与 **无线连接 (车载热点/手机热点)**，并在 CarPlay 内部深度集成 **Proton 咆哮虎头立体车标**。

---

## 📥 安装包快速下载

| 项目 | 说明 / 推荐用途 | 下载链接 |
| :--- | :--- | :--- |
| **⭐ U盘即插即装四合一完整包** | **【车机安装最推荐】**：解压即用的一体化 U盘安装包！一键同时安装 **DiPlay (Apple CarPlay)**、**Headunit Reloaded (Android Auto)**、**Open Hidden Settings (原生隐藏设置)** 与 **Amaze File Manager (文件管理器/日志导出)**，内嵌提权脚本与所有必需的原生 `.so` 动态库。直接解压到 FAT32 U盘根目录即可！ | [⬇️ **点击下载 DiPlay-Proton-X50-USB-Installer.zip**](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases/latest/download/DiPlay-Proton-X50-USB-Installer.zip) |
| **独立 APK 文件** | 纯 APK 安装包，供开发者或高级用户手动 adb 安装调试。 | [⬇️ **点击下载 DiPlay-for-Proton-Android5.1.apk**](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases/latest/download/DiPlay-for-Proton-Android5.1.apk) |
| **所有发布版本** | 更新日志与版本记录 | [查看 GitHub Releases](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases) |

---

## 🌟 核心特性与 Proton X50 适配亮点

- **四合一车载互联与调试套件**：U 盘一插一次性搞定 **Apple CarPlay (DiPlay)** + **Android Auto (Headunit Reloaded)** + **Open Hidden Settings (原生安卓设置)** + **Amaze File Manager (文件管理与日志提取)**。
- **真正纯原生免盒子**：直接在宝腾 X50 车机内置的 ECARX E01 处理器上运行，无额外硬件发热与接口松动问题。
- **向下突破 Android 5.1 (API 22)**：突破开源原版仅支持 Android 9+ 的限制，重新构建 NDK C++ 原生底层（针对 32 位 `armeabi-v7a` 及 64 位深度优化）。
- **CarPlay 专属 Proton 车标集成**：进入 Apple CarPlay 后，返回原车界面的图标定制为 **Proton** 专属名称与**官方咆哮虎头车标**，点击一秒切回原车中控。
- **有线与无线双模**：中控下部数据线即插即连，同时支持车机热点/手机热点无线连携。

---

## 🛠️ Proton X50 车机 (IHU) 一步一步完整安装教程

请按照以下五个阶段逐步操作，从固件检查到顺利点亮 CarPlay。

### 📋 准备工作（安装所需物品）
1. **USB U盘**：容量为 **8 GB 至 32 GB**，文件系统务必格式化为 **FAT32**。
2. **手机数据线**：原装数据线或通过认证的高品质数据线（苹果手机用 Lightning/Type-C，安卓手机用 Type-C）。
3. **手机**：iPhone（iOS 13+ 用于 CarPlay）或 Android 安卓手机（用于 Android Auto）。
4. **下载安装包**：下载 [**`DiPlay-Proton-X50-USB-Installer.zip`**](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases/latest/download/DiPlay-Proton-X50-USB-Installer.zip)。

---

### 第一步：确认车机固件版本

1. 发动车辆，等待车机屏幕开机。
2. 进入车机：点击 **Settings (设置)** ➡️ **System (系统)** ➡️ **About / System Information (关于/系统信息)**。
3. 查看当前的 ATLAS OS 固件版本号：
   - **高配车型 (Premium 尊贵版 / Flagship 旗舰版)**：目标安全版本为 **`617v1`**。
   - **低配车型 (Standard 标准版 / Executive 豪华版)**：目标安全版本为 **`618v1`**。

> [!IMPORTANT]
> - 如果你的车机当前正好是 **`617v1`** 或 **`618v1`**，恭喜！直接跳过第二步，直接进入 **第三步**！
> - 如果你的车机版本高于此版本（例如被官方 OTA 升级到了 `617v2`、`617v3` 等封堵了安装权限的版本），需要先按照第二步降级。

---

### 第二步：固件降级教程（仅当版本高于 617v1 时需要）

> [!WARNING]
> 降级/刷机过程中必须保持车辆点火发动状态（**Engine ON**），中途严禁熄火、严禁拔出 U 盘！

1. 将 U 盘格式化为 **FAT32** 格式。
2. 访问固件下载库下载对应版本的固件包：
   - [Proton-X50-IHU-Upgrade-Downgrade (by xeon1989)](https://github.com/xeon1989/Proton-X50-IHU-Upgrade-Downgrade)
   - [Proton 固件库镜像](https://github.com/xeon1989/proton_firmware)
3. 将下载的固件文件解压到 U 盘根目录下。
4. 将 U 盘插入中控台马鞍底部的 USB 数据接口。
5. 车机会自动检测到系统更新提示，点击确认更新，耐心等待进度条走完并自动重启。
6. 重启后在系统信息中确认版本号已恢复为 `617v1` 或 `618v1`。

---

### 第三步：使用免配置 U盘完整包自动化安装

1. 将 U 盘（8 GB ~ 32 GB）在电脑上格式化为 **FAT32** 格式。
2. 下载免配置安装包：[**`DiPlay-Proton-X50-USB-Installer.zip`**](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases/latest/download/DiPlay-Proton-X50-USB-Installer.zip)。
3. 直接将 `DiPlay-Proton-X50-USB-Installer.zip` 解压到 **U 盘的根目录**。

**解压后，你的 U 盘目录结构如下（包含 3 个核心应用与提权脚本）：**
```text
U盘根目录 (FAT32)/
├── b832bc61472727635baffcf25dd28e9f239273e2/
│   ├── b8d19f9e951515117820d8d785034d74.sh
│   └── ecead2369cb605ecb21209d1fb4c654f.sh
└── app/
    ├── hutroops.com.shihab.diplay/          # 🍎 Apple CarPlay (DiPlay 宝腾专属版)
    │   ├── com.shihab.diplay.apk
    │   └── lib/
    │       ├── arm/
    │       └── arm64/
    ├── hutroops.gb.xxy.hr/                  # 🤖 Android Auto (Headunit Reloaded / HUR)
    │   ├── gb.xxy.hr.apk
    │   └── lib/
    │       ├── arm/
    │       └── arm64/
    ├── hutroops.dxidev.openhiddensettings/  # ⚙️ Open Hidden Settings (原生安卓设置 & ADB)
    │   ├── dxidev.openhiddensettings.apk
    │   └── lib/arm/
    └── hutroops.com.amaze.filemanager/      # 📁 Amaze File Manager (文件管理器 & 日志导出)
        ├── com.amaze.filemanager.apk
        └── lib/
            ├── arm/
            └── arm64/
```

4. 启动车辆发动机（**Engine ON**），等待车机大屏完全进入主页面。
5. 将 U 盘插入**前排中控台马鞍底部的 USB 数据接口**（注意：必须插下方的有数据传输标志的口，扶手箱内为纯充电口）。
6. **自动化静默安装与重启**：
   - 插入后几秒内，屏幕会自动切到 **「无线充电设置界面」**（这代表提权安装脚本已成功识别并开始执行）。
   - 脚本会自动挂载 `/system` 系统分区，将全部 4 个应用写入系统目录，配置好 Android 5.1 所需的 `.so` 核心运行库，并冻结原车冲突的后台进程。
   - 随后屏幕会切到 **「系统设置」** 页面（代表全部静默写入完成！）。
   - 车机会在 5 秒内自动重启。
7. 拔出 U 盘。车机重启进入应用列表（All Apps），你就会看到全部 4 个应用已就绪：
   - **DiPlay**：苹果手机原生免盒子 CarPlay（定制宝腾咆哮虎标）。
   - **Headunit Reloaded (HUR)**：安卓手机 Android Auto。
   - **Open Hidden Settings**：原生安卓隐藏设置工具（可开启开发者模式、ADB 与应用管理）。
   - **Amaze File Manager**：全功能文件管理器（浏览车载存储、查看日志、一键复制文件到 U 盘）。

---

### 第四步：CarPlay 首次连接与使用

#### 🔌 方案 A：有线连接（强烈推荐：零延迟、画质最稳）
1. 在 Proton X50 屏幕上点击打开 **DiPlay**。
2. 首次启动时提示的所有权限请求，一律点击 **「允许 (Allow)」**。
3. 用优质数据线连接 iPhone 和前排马鞍下方的 USB 数据口。
4. 在 iPhone 屏幕上：
   - 弹出“要信任此电脑吗？” ➡️ 点击 **「信任」** 并输入 iPhone 锁屏密码。
   - 弹出“要在车机上使用 CarPlay 吗？” ➡️ 点击 **「使用 CarPlay」**。
5. 在车机屏幕上：
   - 弹出“允许 DiPlay 访问该 USB 设备” ➡️ 勾选 **「默认用于该设备」**，点击 **「确定」**。
6. **瞬间全屏点亮！原汁原味的 Apple CarPlay 呈现在 X50 大屏上！**

---

#### 📶 方案 B：无线连接（Wi-Fi + 蓝牙）
1. **网络连接**（任选其一）：
   - **方式 1 (车机热点)**：Proton X50 打开内置 Wi-Fi 热点，iPhone Wi-Fi 连接到车机热点。
   - **方式 2 (手机热点)**：iPhone 打开个人热点（建议勾选“最大兼容性”），车机 Wi-Fi 连接到 iPhone 热点。
2. 打开车机端 **DiPlay** 应用。
3. 手机与原车蓝牙保持配对连接。
4. DiPlay 会自动侦测手机并通过无线协议握手，成功建立无线 CarPlay。

---

### 第五步：针对 ECARX E01 处理器的防卡顿性能调优 (必做)

由于 Proton X50 搭载的是能效四核 Cortex-A53 架构的 ECARX E01 处理器，强烈建议在 DiPlay 设置中进行如下调优，以达到最丝滑流畅的效果并杜绝车机发热卡顿：

1. 打开 **DiPlay 设置面板**（点击齿轮图标）：
2. **视频解码器 (Video Codec)**：
   - 必须设置为 **`H.264 (AVC)`**。
   - > [!CAUTION]
     > **绝对不要勾选 HEVC / H.265 软解**。A53 架构软解 HEVC 会使 CPU 占用瞬间飙至 100%，导致画面卡顿掉帧与车机发烫。
3. **分辨率与帧率 (Resolution & FPS)**：
   - 分辨率推荐：**`1280 x 720`**（完美契合 X50 屏幕比例，清晰且流畅）。
   - 帧率推荐：**`30 fps`**（功耗与流畅度最佳平衡）或 **`60 fps`**（有线连接下测试平顺时）。
4. **音频通道策略 (Audio Routing)**：
   - 建议在音频设置中将通话路线设置为 **`Car Bluetooth Route (原车蓝牙通话)`**，这样可以完美使用原车方向盘接打电话按键，通话无杂音、无回声。

---

### 🔘 在 CarPlay 内部切回 Proton 原车控制

进入 Apple CarPlay 以后：
- 在 CarPlay 应用图标网格中，会看到一个标有 **「Proton」** 的专属图标（带有**宝腾咆哮虎头车标**）。
- 点击此图标，即可一键切回 Proton X50 车机仪表、空调调节、360度倒车影像或原车系统！

---

### 第六步：导出日志与故障排查（供开发者定位 Debug）

如果遇到无法连接、异常断连或闪退，可以按照以下方法导出完整运行日志发给开发者调试：

1. **方式一：通过 DiPlay 设置生成诊断报告**：
   - 打开 **DiPlay** ➡️ 点击右上角 **设置（齿轮图标）**。
   - 点击 **「查看诊断报告 (View Diagnostic Report)」**（或导出报告）。
   - DiPlay 会自动抓取连接握手日志、系统环境及最近崩溃记录，并输出到车机内置存储的 `Download/DiPlay/` 目录下。
2. **方式二：使用 Amaze 文件管理器导出日志到 U 盘**：
   - 将任意 FAT32 U 盘插入车机前排 USB 数据接口。
   - 打开车机应用列表中的 **Amaze File Manager**。
   - 进入路径：
     - `内部存储` ➡️ `Download` ➡️ `DiPlay/`（包含生成的诊断报告）。
     - 或者进入 `/sdcard/Android/data/com.shihab.diplay/files/logs/`（包含实时的 `diplay.log` 与 `last-crash.txt`）。
   - 长按日志文件，点击 **「复制 (Copy)」**。
   - 点击左侧滑出的侧边栏，选中你的 **U 盘 (`udisk1`)**，点击 **「粘贴 (Paste)」**。
   - 拔出 U 盘插回电脑，把导出的 `.txt` 或 `.log` 文件发给开发者即可快速定位！

## ❓ 常见问题排查 (FAQ)

### Q1: 插入 iPhone 后车机只有充电反应，没有启动 CarPlay？
- **原因 1：插错 USB 接口**。部分车型扶手箱内部仅为纯供电口，必须插入前排下方的马鞍数据接口。
- **原因 2：线缆问题**。劣质充电线缺乏数据传输针脚，请更换原装线或 MFi 认证数据线。
- **原因 3：QDLink 互联冲突**。请确保使用了 U盘安装脚本，脚本会自动停用后台冲突的 QDLink 互联进程。

### Q2: 声音只有音乐声，没有导航声音或电话声音？
- 打开 DiPlay 的音频设置，确保勾选了「通话走原车蓝牙」。同时保持原车蓝牙与 iPhone 配对连接，通话体验最佳。

---

## 👨‍💻 开发者与云端全自动编译 (GitHub Actions)

本项目配备了完整的 **GitHub Actions CI/CD** 全自动云端编译：
1. 每次提交代码，GitHub 云端会自动拉取代码，在云端虚拟机配置 Java 25、Android SDK 37 和 NDK 28。
2. 自动运行 `./gradlew :mobile:assembleDebug` 编译出最新的 APK。
3. 自动打包发布在 [GitHub Releases 发布页面](https://github.com/qingtian6325-lang/DiPlay-for-proton/releases)。

---

## 🙏 致谢与开源项目致敬 (Credits & Acknowledgements)

本项目得以成功在宝腾 Proton X50 上实现原生车载互联套件，特别致敬并感谢以下开源项目与开发者的卓越贡献：

- **[DiPlay](https://github.com/shihabal3amri/DiPlay)** (开发者：[@shihabal3amri](https://github.com/shihabal3amri)) — 面向安卓车机的独立 CarPlay 接收端实现。
- **[xcertplay](https://github.com/Frank-Zsy/xcertplay)** (开发者：[@Frank-Zsy](https://github.com/Frank-Zsy)) — CarPlay 核心通信协议与 AirPlay 视频接收引擎。
- **[Headunit Reloaded (HUR)](https://forum.xda-developers.com/t/android-4-1-headunit-reloaded-for-android-auto-touch-wifi-mic-hardware-keys.3432348/)** (开发者：Emil Borconi) — 安卓车机专属的 Android Auto 接收引擎。
- **[Open Hidden Settings](https://github.com/dxidev)** (开发者：[@dxidev](https://github.com/dxidev)) — 原生安卓系统隐藏设置与开发者选项直达工具。
- **[Proton-X50-APK-Installer-ATLAS](https://github.com/xeon1989/Proton-X50-APK-Installer-ATLAS)** (开发者：[@xeon1989](https://github.com/xeon1989)) — 宝腾 Proton X50 ATLAS 系统 U盘自动化提权与静默安装工具包。
- **[Proton-X50-IHU-Upgrade-Downgrade](https://github.com/xeon1989/Proton-X50-IHU-Upgrade-Downgrade)** (开发者：[@xeon1989](https://github.com/xeon1989)) — 宝腾 Proton X50 车机固件升级与降级恢复工具包。
- **[proton_firmware](https://github.com/xeon1989/proton_firmware)** (开发者：[@xeon1989](https://github.com/xeon1989)) — 宝腾车机各版本官方固件库。

---

### ⚖️ 免责声明 (Disclaimer)
Apple 与 CarPlay 均为 Apple Inc. 之注册商标。Proton（宝腾）为 Perusahaan Otomobil Nasional Sdn Bhd 之注册商标。本项目为社区开源爱好者独立逆向与适配成果，与 Apple Inc. 及 Proton 汽车官方无任何隶属、认可或商业关联。

---

*祝所有宝腾 Proton X50 车主用车愉快！安全驾驶！*
