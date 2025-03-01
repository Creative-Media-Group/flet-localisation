# flet-localisation
A library for a basic check of your localisation settings.
## Dependencies
- on macos/windows: `pip install pyjnius` / `pip install git+https://github.com/kivy/pyjnius.git`
- On Linux:
    - fedora: `sudo dnf install python3-pyjnius`
    - debian based: `sudo apt install python3-pyjnius`
- for android support add:
```bash
[tool.flet.android]
dependencies = [
  "pyjnius"
]
```
- IOS not supported (Work in progress)