@echo off
echo 按任意键进入修改身高体重数据

set weight=:
set /p weight=请输入体重:
set height=:
set /p height=请输入身高:
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "update device_weightheight set weight = %weight% where member_id = 1 ;update device_weightheight set height = %height% where member_id = 1"



pause

