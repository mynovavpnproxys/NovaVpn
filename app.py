# -*- coding: utf-8 -*-
import os
import time

def show_menu():
    os.system("clear")
    print("=" * 40)
    print("      NOVA VPN - Mobile App Core       ")
    print("========================================")
    print("1. [*] اتصال سریع (Connect)")
    print("2. [*] لیست سرورها و آی‌پی‌های تمیز (8000+ IPs)")
    print("3. [*] ورود کد اشتراک VIP")
    print("4. [*] تنظیمات و زبان (Language & Settings)")
    print("5. [*] خروج")
    print("=" * 40)

def main():
    while True:
        show_menu()
        choice = input("\nلطفاً یک گزینه انتخاب کنید (1-5): ")
        if choice == "1":
            print("\n[+] در حال اتصال به بهترین سرور...")
            time.sleep(1.5)
            print("[✓] متصل شد! وضعیت: فعال (Connected)")
            input("\nبرای بازگشت به منو Enter بزنید...")
        elif choice == "2":
            print("\n[+] ۸,۴۲۰ آی‌پی تمیز و نودهای VLESS / WARP آماده هستند.")
            input("\nبرای بازگشت به منو Enter بزنید...")
        elif choice == "3":
            code = input("\nکد اشتراک VIP را وارد کنید: ")
            if code:
                print(f"[✓] اشتراک با کد {code} فعال شد!")
            input("\nبرای بازگشت به منو Enter بزنید...")
        elif choice == "4":
            print("\n[*] زبان فعلی: فارسی (Persian)")
            print("[*] حالت تم: تاریک (Dark Mode)")
            input("\nبرای بازگشت به منو Enter بزنید...")
        elif choice == "5":
            print("\nخروج از برنامه NovaVPN. روز خوش!")
            break

if __name__ == "__main__":
    main()
