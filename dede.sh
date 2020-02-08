#! /bin/bash
rm -rf /home/pi/share/tiebapage/*
echo "清空teba文件夹"
unzip -d /home/pi/share/tiebapage /home/pi/share/tiebapage.zip
echo "解压图片"
data_name=$(date +%Y%m%d-%H%M%S)
echo $data_name
cp /home/pi/share/dede_addon17_0_e7248237f0876069.txt /home/pi/share/web/
echo "备份addon17"
mv /home/pi/share/web/dede_addon17_0_e7248237f0876069.txt /home/pi/share/web/$data_name.txt
echo "改名addon17"
python3 dede.py
echo "执行python"
mv -f /home/pi/share/tiebapage/* /var/www/abc/uploads/141108
cp -rf /home/pi/share/dede_addon17_0_e7248237f0876069.txt /var/www/abc/data/backupdata/
