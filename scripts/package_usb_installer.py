#!/usr/bin/env python3
import os
import sys
import zipfile
import shutil

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    apk_candidates = [
        os.path.join(root_dir, 'dist', 'DiPlay-for-Proton-Android5.1.apk'),
        os.path.join(root_dir, 'mobile', 'build', 'outputs', 'apk', 'debug', 'mobile-debug.apk')
    ]
    apk_path = next((p for p in apk_candidates if os.path.isfile(p)), None)
    if not apk_path:
        print("Error: No APK found to package!", file=sys.stderr)
        sys.exit(1)

    dist_dir = os.path.join(root_dir, 'dist')
    os.makedirs(dist_dir, exist_ok=True)
    temp_dir = os.path.join(dist_dir, 'usb_temp')
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

    trigger_name = 'b832bc61472727635baffcf25dd28e9f239273e2'
    target_trigger = os.path.join(temp_dir, trigger_name)
    os.makedirs(target_trigger, exist_ok=True)

    src_trigger = os.path.join(root_dir, 'installer', 'proton-x50', trigger_name)
    for s in os.listdir(src_trigger):
        shutil.copy2(os.path.join(src_trigger, s), os.path.join(target_trigger, s))

    app_target = os.path.join(temp_dir, 'app', 'hutroops.com.shihab.diplay')
    arm_dir = os.path.join(app_target, 'lib', 'arm')
    arm64_dir = os.path.join(app_target, 'lib', 'arm64')
    os.makedirs(arm_dir, exist_ok=True)
    os.makedirs(arm64_dir, exist_ok=True)

    # Copy companion apps (Android Auto HUR, Open Hidden Settings) if present
    extra_apps_dir = os.path.join(root_dir, 'installer', 'proton-x50', 'app')
    if os.path.isdir(extra_apps_dir):
        for folder in os.listdir(extra_apps_dir):
            src_f = os.path.join(extra_apps_dir, folder)
            dest_f = os.path.join(temp_dir, 'app', folder)
            if os.path.isdir(src_f) and not os.path.exists(dest_f):
                shutil.copytree(src_f, dest_f)


    # Copy APK with the required system name
    shutil.copy2(apk_path, os.path.join(app_target, 'com.shihab.diplay.apk'))

    # Extract .so files for Android 5.1 system app lib directory
    with zipfile.ZipFile(apk_path, 'r') as z:
        for name in z.namelist():
            if name.startswith('lib/armeabi-v7a/') and name.endswith('.so'):
                so_name = os.path.basename(name)
                with open(os.path.join(arm_dir, so_name), 'wb') as f:
                    f.write(z.read(name))
            elif name.startswith('lib/arm64-v8a/') and name.endswith('.so'):
                so_name = os.path.basename(name)
                with open(os.path.join(arm64_dir, so_name), 'wb') as f:
                    f.write(z.read(name))

    zip_path = os.path.join(dist_dir, 'DiPlay-Proton-X50-USB-Installer.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, temp_dir)
                zipf.write(full_path, arcname)

    shutil.rmtree(temp_dir)
    print(f"Successfully created: {zip_path} ({os.path.getsize(zip_path)} bytes)")

if __name__ == '__main__':
    main()
