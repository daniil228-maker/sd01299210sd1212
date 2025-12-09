[app]

# Название приложения
title = Мои Заметки

# Имя пакета (УНИКАЛЬНОЕ!)
package.name = mynotesapp

# Домен
package.domain = com.example

# Версия
version = 1.0

# Исходный код
source.dir = .
source.main = main.py

# Зависимости
requirements = python3,kivy==2.1.0

# Ориентация
orientation = portrait

# Разрешения
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Минимальная версия Android
android.api = 31
android.minapi = 21

# Архитектуры (ИСПРАВЛЕНО: archs вместо arch)
android.archs = arm64-v8a, armeabi-v7a

# NDK версия
android.ndk = 25b

# Лицензии
android.accept_sdk_license = True

# Иконка
# icon.filename = %(source.dir)s/icon.png

# Заставка
# presplash.filename = %(source.dir)s/presplash.png

# Полноэкранный режим
fullscreen = 0

# Уровень логирования
log_level = 2

# Версия Android SDK Tools
# android.sdk = 24  # УДАЛИТЬ эту строку - она устарела
