import webview 
web_url = 'http://127.0.0.1:8000/'
webview.create_window("Desktop Web App", web_url, x=0, y=0, resizable=True, fullscreen=False )
webview.start() 