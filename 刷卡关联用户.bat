@echo off
echo ѡ�������������
echo �󶨿���Ϊ3EEEFE1D
echo *****************
echo 1.�������
echo 2.Ѫѹ
echo 3.Ѫ��
echo 4.Ѫ֬
echo 5.Ѫ����
echo 6.����ɷ�
echo 7.����
echo 8.Ѫ��
echo 9.���ܶ�
echo 10.�ι���
echo e.�˳�
echo *****************



:begin
set i= 
set /p i=���������:
if not defined i echo ��������ȷ����
if "%i%" == "1" goto :device_weightheight 
if "%i%" == "2" goto :device_bloodpressure 
if "%i%" == "3" goto :device_bloodsugar 
if "%i%" == "4" goto :device_bloodfat 
if "%i%" == "5" goto :device_bloodurine 
if "%i%" == "6" goto :device_body_composition 
if "%i%" == "7" goto :device_body 
if "%i%" == "8" goto :device_bloodoxygen 
if "%i%" == "9" goto :device_bonemineraldensity 
if "%i%" == "10" goto :device_pulmonary 
if "%i%" == "e" exit

pause 
goto :begin


rem �������
:device_weightheight
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_weightheight set exam_id= @exam_id where member_id = @member_id"
echo ������� success��

pause 
goto :begin

rem Ѫѹ
:device_bloodpressure
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bloodpressure set exam_id= @exam_id where member_id = @member_id"
echo Ѫѹ success��

pause
goto :begin

rem Ѫ��
:device_bloodsugar
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bloodsugar set exam_id= @exam_id where member_id = @member_id"
echo Ѫ�� success��

pause
goto :begin

rem Ѫ֬
:device_bloodfat
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bloodfat set exam_id= @exam_id where member_id = @member_id"
echo Ѫ֬ success��

pause
goto :begin

rem Ѫ����
:device_bloodurine
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bloodurine set exam_id= @exam_id where member_id = @member_id"
echo Ѫ���� success��

pause
goto :begin

rem ����ɷ�
:device_body_composition
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_body_composition set exam_id= @exam_id where member_id = @member_id"
echo ����ɷ� success��

pause
goto :begin

rem ����
:device_body
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_body set exam_id= @exam_id where member_id = @member_id"
echo ���� success��

pause
goto :begin

rem Ѫ��
:device_bloodoxygen
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bloodoxygen set exam_id= @exam_id where member_id = @member_id"
echo Ѫ�� success��

pause
goto :begin

rem ���ܶ�
:device_bonemineraldensity
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bonemineraldensity set exam_id= @exam_id where member_id = @member_id"
echo ���ܶ� success��

pause
goto :begin

rem �ι���
:device_pulmonary
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_pulmonary set exam_id= @exam_id where member_id = @member_id"
echo �ι��� success��

pause
goto :begin
