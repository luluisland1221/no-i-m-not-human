@echo off
setlocal enabledelayedexpansion

echo 开始批量更新角色页面布局...

cd "G:\ai编程\100个网站\07 noimnothuman.xyz\code\guide\characters"

:: 需要更新的文件列表（排除这些文件）
set exclude_files=bandana-guy.html temp_navbar.txt

:: 创建临时文件用于CSS替换
echo @echo off > temp_update_css.bat
echo set "old_css=^<style^>        body {            padding-top: 80px ^!important;            background: #000 ^!important;        }        .character-hero {            margin-top: -80px ^!important;            padding-top: 120px ^!important;        }        .character-container {            background: #000 ^!important;        }        .character-main {            background: #000 ^!important;        }    ^</style^>" >> temp_update_css.bat
echo set "new_css=^<style^>        body {            padding-top: 80px ^!important;            background: #000 ^!important;        }        .character-hero {            margin-top: -80px ^!important;            padding-top: 120px ^!important;        }        .character-container {            background: #000 ^!important;            max-width: 1400px ^!important;            margin: 0 auto ^!important;            padding: 2rem ^!important;            display: block ^!important;        }        .character-main {            background: #000 ^!important;        }        .character-section {            max-width: none ^!important;            width: 100% ^!important;            background: rgba(0, 0, 0, 0.2) ^!important;            border-radius: 12px ^!important;            padding: 2rem ^!important;            margin-bottom: 2rem ^!important;            border: 1px solid rgba(0, 255, 136, 0.1) ^!important;        }    ^</style^>" >> temp_update_css.bat

echo 准备更新脚本...

:: 遍历所有HTML文件并更新
set count=0
for %%f in (*.html) do (
    set "skip=0"
    for %%x in (%exclude_files%) do (
        if "%%f"=="%%x" set "skip=1"
    )

    if !skip!==0 (
        echo 正在更新: %%f
        set /a count+=1

        :: 使用 PowerShell 进行文本替换
        powershell -Command "(Get-Content '%%f') -replace '<style>        body {            padding-top: 80px !important;            background: #000 !important;        }        .character-hero {            margin-top: -80px !important;            padding-top: 120px !important;        }        .character-container {            background: #000 !important;        }        .character-main {            background: #000 !important;        }    </style>', '<style>        body {            padding-top: 80px !important;            background: #000 !important;        }        .character-hero {            margin-top: -80px !important;            padding-top: 120px !important;        }        .character-container {            background: #000 !important;            max-width: 1400px !important;            margin: 0 auto !important;            padding: 2rem !important;            display: block !important;        }        .character-main {            background: #000 !important;        }        .character-section {            max-width: none !important;            width: 100% !important;            background: rgba(0, 0, 0, 0.2) !important;            border-radius: 12px !important;            padding: 2rem !important;            margin-bottom: 2rem !important;            border: 1px solid rgba(0, 255, 136, 0.1) !important;        }    </style>' | Set-Content '%%f'"
    )
)

echo.
echo 批量更新完成！
echo 总共更新了 %count% 个角色文件。

:: 清理临时文件
if exist temp_update_css.bat del temp_update_css.bat

echo 按任意键退出...
pause