[app]
title = Мои Заметки
package.name = mynotesapp
package.domain = com.example
version = 1.0
source.dir = .
source.main = main.py
requirements = python3,kivy==2.1.0
orientation = portrait

# Android settings
android.minapi = 21
android.api = 33
android.ndk = 26.3.11579264  # ИЛИ android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.accept_sdk_license = True

# Оптимизации
fullscreen = 0
log_level = 2
