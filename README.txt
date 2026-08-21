# Speak & Save Dictionary

## Easiest desktop/local setup

1. Install Python 3 if it is not already installed.
2. Extract this ZIP.
3. Open the extracted folder.
4. Run:
   - Windows: double-click `start_server.bat`
   - Mac/Linux: run `python3 server.py`
5. Your browser will open `http://localhost:8000`.

Because the app is served from localhost instead of being opened as a downloaded file, browser security treats the local origin as trustworthy for microphone-related web APIs. The browser will still ask you to allow microphone access.

## Android

A Python server running on your PC is not the same as a server on your Android phone. For Android use, the easiest permanent option is to host this app on an HTTPS website (for example GitHub Pages). HTTPS is important for browser microphone APIs.

## What the app does

Speak -> speech recognition -> automatic dictionary lookup -> edit -> save.

Google is only used as an optional additional search. The app does NOT attempt to scrape Google's results, because a browser page cannot reliably read Google's cross-origin search page.

Saved words are stored in the browser's localStorage on the device/browser where you use the app.
