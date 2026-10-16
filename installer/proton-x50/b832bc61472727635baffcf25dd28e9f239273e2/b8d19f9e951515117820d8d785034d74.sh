#!/system/bin/sh

#This script is available at xeon1989's Github https://github.com/xeon1989/Proton-X50-APK-Installer-ATLAS
#All credits to munchy for the script, and everyone that tested it!

logfilename="outputInstall_"
timestamp="$(date +%s)"
logfilename="$logfilename$timestamp"
exec > /mnt/media_rw/udisk1/$logfilename.txt 2>&1
export PATH=/sbin:/system/sbin:/system/xbin:/system/bin
mount -o rw,remount /system

echo "====== show wireless charging to indicates script start ======="
am start -n com.ecarx.gkuiconfig/.setting.SettingActivity 2>/dev/null
input tap 700 200
sleep 0.5
am start -a android.settings.WPC_SETTINGS 2>/dev/null #This open wireless charging, indicates start of script

echo "========show system app directory before copy======="
ls -la /system/app/

echo "========copy content in USB app to system app======="
cp -r -v /mnt/media_rw/udisk1/app/hutroops.* /system/app/

echo "========set permission accordingly======="
chmod -R 755 /system/app/hutroops.*

echo "========show system app directory after copy======="
ls -la /system/app/

echo "========show app directory after copy======="
for app in /system/app/hutroops.*; do ls -la $app; done

function OptimizeApp()
{
echo "======== Optimization disable ========"
OptimiseAp=(com.malaysia.ota com.neusoft.ssp.ces.c4.car.assistant)
#OptimiseAp=(com.malaysia.ota com.neusoft.ssp.ces.c4.car.assistant com.neusoft.na.navigation com.malaysia.naviservice com.malaysia.weather com.malaysia.calendar)

echo ${OptimiseAp[@]}

for Opt in ${OptimiseAp[@]}
do 
	pm disable $Opt
done 
}
OptimizeApp

am start -a android.settings.SETTINGS 	#show settings app to indicates script completed

mv /mnt/media_rw/udisk1/b832bc61472727635baffcf25dd28e9f239273e2 /mnt/media_rw/udisk1/b832bc61472727635baffcf25dd28e9f239273e2_done #stop execution

sleep 5
reboot