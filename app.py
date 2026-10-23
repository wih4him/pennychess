import os
import sys
import webview


def resource_path(rel):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)


if __name__ == "__main__":
    webview.create_window("Pennychess Fork 1.3", resource_path("index.html"), width=1300, height=1000)
    webview.start()
