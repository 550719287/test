@echo off 

color a

echo С�����ݿ⵼���޸����ݽű�
echo ���ݿ���ļ�xiaowu_data��������
echo Ĭ��MySQL�ļ���C��
echo      180320


cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health < %~dp0/xiaowu_data.sql

pause