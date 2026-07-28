import webview
from api import Api

def main():
    api = Api()
    window = webview.create_window(
        'Vocab App',
        'frontend/index.html',
        js_api=api,
        width=800,
        height=600
    )
    webview.start()

if __name__ == "__main__":
    main()
