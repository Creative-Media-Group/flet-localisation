import flet as ft


def locale(platform: str, web: bool = False) -> str:
    platform = platform.lower()
    if "pageplatform." in platform:
        platform = platform.replace("pageplatform.", "")
    print(platform)
    if platform in ["android", "android_tv"]:
        from jnius import autoclass

        Locale = autoclass("java.util.Locale")
        locale = Locale.getDefault()
        return f"{locale.getLanguage()}_{locale.getCountry()}"
    elif platform == "ios":
        try:
            from pyobjus import autoclass
            from pyobjus.dylib_manager import load_framework, INCLUDE

            load_framework(INCLUDE.Foundation)
            NSLocale = autoclass("NSLocale")
            current_locale = NSLocale.currentLocale().localeIdentifier()
            preferred_languages = NSLocale.preferredLanguages()
            return current_locale
        except Exception as e:
            return f"Error fetching locale: {str(e)}"
    if platform in ["linux", "macos", "windows"]:
        import locale as lc

        locale = lc.getlocale()[0]
        return locale
    if ft.Page.web:
        return f"{platform} not suported"  # locale=ft.Page().
    else:
        return f"{platform} not suported"
