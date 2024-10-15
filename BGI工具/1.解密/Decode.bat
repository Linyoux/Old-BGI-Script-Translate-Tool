@echo off
setlocal enabledelayedexpansion

:: 设置文件夹路径
set "folderPath=%~dp0DecodeInput"

:: 遍历文件夹中的所有无后缀文件
for %%f in ("%folderPath%\*") do (
    echo Running: %%f
    :: 假设你的exe文件在同一目录下
    "%~dp0ScriptDecoder.exe" "%%f"
)

echo All files processed.
pause
