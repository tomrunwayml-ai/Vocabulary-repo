from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import webbrowser, os

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))
url = f"http://localhost:{PORT}"
print(f"\nSpeak & Save Dictionary is running at {url}")
print("Keep this window open while using the app.")
print("Press Ctrl+C to stop the server.\n")
webbrowser.open(url)
ThreadingHTTPServer(("localhost", PORT), SimpleHTTPRequestHandler).serve_forever()
