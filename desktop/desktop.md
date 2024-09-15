# This code working required python 3.11 version

# install package
```bash
pip install webview
```
### requirements
change the web_url in main.py
```python
web_url = "https://desktop.yourwebsite.com/"
```

# compile the .exe file

```bash
pip install pyinstaller
```

```bash
pyinstaller --onefile --noconsole desktop.py
```

# add icon desktop app example
```python
import webview
web_url = 'https://schedule.mamatmusayev.uz/'
icon_path = 'path_to_your_icon.ico'  # Ikonka faylingizning yo'lini kiriting

webview.create_window("Desktop Web App", web_url, x=0, y=0, resizable=True, fullscreen=True, icon=icon_path)
webview.start()
```