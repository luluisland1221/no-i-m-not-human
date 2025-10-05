@echo off
echo Starting image downloads from entertainment14.net...
cd /d "G:\ai编程\100个网站\07 noimnothuman.xyz\code"
setlocal enabledelayedexpansion

:: Create temp_images directory if it doesn't exist
if not exist "temp_images" mkdir temp_images

:: Image URLs to download
set urls[0]=https://img1.entertainment14.net/images/090/03/1758109003_3572.jpg
set urls[1]=https://img1.entertainment14.net/images/090/03/1758109003_3573.jpg
set urls[2]=https://img1.entertainment14.net/images/090/03/1758109003_3574.jpg
set urls[3]=https://img1.entertainment14.net/images/090/03/1758109003_3575.jpg
set urls[4]=https://img1.entertainment14.net/images/090/03/1758109003_3577.jpg
set urls[5]=https://img1.entertainment14.net/images/090/03/1758109003_3578.jpg
set urls[6]=https://img1.entertainment14.net/images/090/03/1758109003_3579.jpg
set urls[7]=https://img1.entertainment14.net/images/090/03/1758109003_3584.jpg
set urls[8]=https://img1.entertainment14.net/images/090/03/1758109003_3585.jpg
set urls[9]=https://img1.entertainment14.net/images/090/03/1758109003_3587.jpg
set urls[10]=https://img1.entertainment14.net/images/090/03/1758109003_3591.jpg
set urls[11]=https://img1.entertainment14.net/images/090/03/1758109003_3594.jpg
set urls[12]=https://img1.entertainment14.net/images/090/03/1758109003_3599.jpg
set urls[13]=https://img1.entertainment14.net/images/090/04/1758109004_3580.jpg
set urls[14]=https://img1.entertainment14.net/images/090/04/1758109004_3590.jpg
set urls[15]=https://img1.entertainment14.net/images/090/04/1758109004_3592.jpg
set urls[16]=https://img1.entertainment14.net/images/090/04/1758109004_3595.jpg
set urls[17]=https://img1.entertainment14.net/images/090/04/1758109004_3597.jpg
set urls[18]=https://img1.entertainment14.net/images/090/04/1758109004_3598.jpg
set urls[19]=https://img1.entertainment14.net/images/090/04/1758109004_3600.jpg

:: Download images
for /l %%n in (0,1,19) do (
    echo Downloading image %%n...
    curl -o "temp_images\image_%%n.jpg" "!urls[%%n]!"
    if !errorlevel! equ 0 (
        echo Successfully downloaded image %%n
    ) else (
        echo Failed to download image %%n
    )
)

echo Download process completed.
pause