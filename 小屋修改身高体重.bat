@echo off
echo ������������޸������������

set weight=:
set /p weight=����������:
set height=:
set /p height=���������:
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "update device_weightheight set weight = %weight% where member_id = 1 ;update device_weightheight set height = %height% where member_id = 1"



pause

