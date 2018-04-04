@echo off
echo 选择想测量的数据
echo 绑定卡号为3EEEFE1D
echo *****************
echo 1.身高体重
echo 2.血压
echo 3.血糖
echo 4.血脂
echo 5.血尿酸
echo 6.人体成分
echo 7.体温
echo 8.血氧
echo 9.骨密度
echo 10.肺功能
echo e.退出
echo *****************



:begin
set i= 
set /p i=请输入表名:
if not defined i echo 请输入正确表名
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


rem 身高体重
:device_weightheight
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_weightheight set exam_id= @exam_id where member_id = @member_id"
echo 身高体重 success！

pause 
goto :begin

rem 血压
:device_bloodpressure
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bloodpressure set exam_id= @exam_id where member_id = @member_id"
echo 血压 success！

pause
goto :begin

rem 血糖
:device_bloodsugar
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bloodsugar set exam_id= @exam_id where member_id = @member_id"
echo 血糖 success！

pause
goto :begin

rem 血脂
:device_bloodfat
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bloodfat set exam_id= @exam_id where member_id = @member_id"
echo 血脂 success！

pause
goto :begin

rem 血尿酸
:device_bloodurine
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bloodurine set exam_id= @exam_id where member_id = @member_id"
echo 血尿酸 success！

pause
goto :begin

rem 人体成分
:device_body_composition
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_body_composition set exam_id= @exam_id where member_id = @member_id"
echo 人体成分 success！

pause
goto :begin

rem 体温
:device_body
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_body set exam_id= @exam_id where member_id = @member_id"
echo 体温 success！

pause
goto :begin

rem 血氧
:device_bloodoxygen
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bloodoxygen set exam_id= @exam_id where member_id = @member_id"
echo 血氧 success！

pause
goto :begin

rem 骨密度
:device_bonemineraldensity
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_bonemineraldensity set exam_id= @exam_id where member_id = @member_id"
echo 骨密度 success！

pause
goto :begin

rem 肺功能
:device_pulmonary
cd C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin
mysql -uroot -pxikang -Dacorn_health -e "select @exam_id:=max(id) from exam_register;select @member_id:=member_id from member_id_tf where tf_card='3EEEFE1D';update device_pulmonary set exam_id= @exam_id where member_id = @member_id"
echo 肺功能 success！

pause
goto :begin
