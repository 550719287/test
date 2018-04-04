@echo off 

color a

echo 小屋数据库导表修改数据脚本
echo 数据库表文件xiaowu_data放在桌面
echo 默认MySQL文件在C盘
echo      180320


cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health < %~dp0/xiaowu_data.sql

pause