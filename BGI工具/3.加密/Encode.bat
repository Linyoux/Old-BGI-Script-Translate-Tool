@echo off
setlocal enabledelayedexpansion

:: 设置文件夹路径
set "folderPath=%~dp0input"

:: 遍历文件夹中的所有txt文件
for %%f in ("%folderPath%\*.txt") do (
    echo Encoding: %%f
    :: 假设你的exe文件在同一目录下
    "%~dp0ScriptEncoder.exe" "%%f"
)

echo All files processed.
pause