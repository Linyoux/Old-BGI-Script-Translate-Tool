@echo off
setlocal enabledelayedexpansion

:: Step 1: Remove .new extension
for %%f in (*.*) do (
    set "filename=%%~nf"
    set "extension=%%~xf"
    if "!extension!"==".new" (
        ren "%%f" "!filename!"
    )
)

:: Step 2: Remove .txt extension
for %%f in (*.*) do (
    set "filename=%%~nf"
    set "extension=%%~xf"
    if "!extension!"==".txt" (
        ren "%%f" "!filename!"
    )
)

echo Done.
pause