[app]

# Название приложения (отображается на телефоне)
title = Мои Заметки

# Имя пакета (должно быть уникальным!)
# ВАЖНО: Измените на что-то уникальное!
package.name = mynotesapp

# Домен (в обратном порядке, как в Android)
# ВАЖНО: Измените на свой!
package.domain = com.github.yourusername

# Версия приложения
version = 1.0

# Исходный код
source.dir = .
source.main = main.py

# Требуемые библиотеки
requirements = python3,kivy==2.1.0

# Ориентация экрана
orientation = portrait

# Разрешения Android
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Минимальная версия Android
android.api = 21
android.minapi = 21

# Версия SDK
android.sdk = 24

# Версия NDK
android.ndk = 23b

# Архитектура (armeabi-v7a работает на большинстве устройств)
android.arch = armeabi-v7a

# Ключи для подписи (для debug сборки)
android.release_artifact = .apk

# Дополнительные настройки
android.accept_sdk_license = True

# Иконка (опционально - можно добавить icon.png в папку)
# icon.filename = %(source.dir)s/icon.png

# Заставка при запуске (опционально)
# presplash.filename = %(source.dir)s/presplash.png
# presplash.color = #FFFFFF

# Полноэкранный режим (0 = нет, 1 = да)
fullscreen = 0

# Логи
log_level = 2