def locale(platform: str) -> str:
    platform = platform.lower()
    if "pageplatform." in platform:
        platform = platform.replace("pageplatform.", "")
    print(platform)
    if platform == "android" or platform == "android_tv":
        from jnius import autoclass

        Locale = autoclass("java.util.Locale")
        locale = Locale.getDefault()
        return f"{locale.getLanguage()}_{locale.getCountry()}"

    if platform == "linux" or platform == "macos" or platform == "windows":
        import locale as lc

        locale = lc.getlocale()[0]
        return locale
    else:
        return f"{platform} not suported"
