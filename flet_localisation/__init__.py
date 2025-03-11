import flet as ft


def locale(platform: str) -> str:
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
            from pyobjus.dylib_manager import load_framework

            load_framework("/System/Library/Frameworks/Foundation.framework")

            NSLocale = autoclass("NSLocale")
            preferred_langs = NSLocale.preferredLanguages()
            primary_lang = preferred_langs.objectAtIndex_(0)

            return primary_lang.replace("-", "_")
        except Exception as e:
            return f"Error fetching locale: {str(e)}"
    if platform in ["linux", "macos", "windows"]:
        import locale as lc

        locale = lc.getlocale()[0]
        return locale
    else:
        return f"{platform} not suported"
