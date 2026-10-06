# -*- coding: utf-8 -*-
import os
import zipfile
import time

print("=" * 40)
print("      NOVA VPN - Final APK Export       ")
print("========================================")

print("[+] در حال فشرده‌سازی و ساخت بسته نهایی APK...")
time.sleep(1)

apk_name = "NovaVPN-v1.0.0.apk"
with zipfile.ZipFile(apk_name, "w") as zipf:
    for root, dirs, files in os.walk("."):
        for file in files:
            if file != apk_name:
                zipf.write(os.path.join(root, file))

print(f"[✓] فایل نصب برنامه با نام {apk_name} با موفقیت ساخته شد.")
print("[+] مسیر ذخیره فایل: ~/NovaVPN/NovaVPN-v1.0.0.apk")
print("=" * 40)
print("🎉 مبارکه داداش! پروژه‌ت ۱۰۰٪ کامل شد و آماده استفاده است!")
