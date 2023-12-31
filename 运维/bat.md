


cmd文件和bat文件有什么区别
本质上没有区别，都是简单的文本编码方式，都可以用记事本创建、编辑和查看。

两者所用的命令行代码也是共用的，只是cmd文件中允许使用的命令要比bat文件多。

cmd文件只有在windows2000以上的系统中才能运行，而bat文件则没有这个限制。

从它们的文件描述中也可以看出以上的区别：
cmd文件的描述是“windows nt命令脚本” bat文件的描述是“ms dos批处理文件”

cmd是Win32命令，只能在32位系统中的命令行窗口中使用，仅仅是基于windows环境下的假DOS

bat是DOS命令，在任何dos环境下都可以使用。


脚本案例
@echo off
SET /A a = 5
SET /A b = 10
SET /A c = %a% + %b%
echo %c%



@echo off
set message=Hello World
echo %message%



@echo off
echo %1
echo %2
echo %3


"globalvar"是在全局范围内定义的，并且在整个脚本中都可用。

"var"变量是在本地范围内定义的，因为它包含在"SETLOCAL"和"ENDLOCAL"块之间。 因此，一旦执行"ENDLOCAL"语句，该变量就会被销毁。
@echo off
set globalvar = 5
SETLOCAL
set var = 13145
set /A var = %var% + 5
echo %var%
echo %globalvar%
ENDLOCAL

