@echo off
rem input your directory
:no
set /p directory=input your directory:

rem confirm your directory, simply input yes or no, if yes, break the loop, else return to the loop
:loop
echo Please confirm the directory of gitbook
echo Your current directory is "%directory%"
set /p confirm=input (yes/no):
if %confirm% EQU yes (goto :yes) else (goto :no)
echo Invalid input, please try again
goto loop

rem if yes break the loop, else return to the loop
:yes
echo You have confirmed the directory of gitbook %directory%
cd %directory%

echo %CD%

rem If summary exists, delete it
if exist "SUMMARY.md" (rmdir /s /q "SUMMARY.md")

rem create your summary file
python md_to_gitbook.py %directory%
echo SUMMARY.md has been created

if exist "docs" (rmdir /s /q "docs")

gitbook init && gitbook build && ren "_book" "docs" && gitbook pdf

