import http.server
import socketserver

html_content = """
<!DOCTYPE html>
<html lang='sv'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Alla hjärtans dag ❤️</title>
    <style>
        body {
            text-align: center;
            background-color: #ffe6f2;
            font-family: 'Pacifico', cursive;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            color: #ff4081;
            font-size: 3em;
            animation: glow 2s infinite alternate;
        }
        .hearts {
            font-size: 2.5em;
        }
        .message {
            font-size: 1.8em;
            color: #d63384;
            font-weight: bold;
        }
        .button {
            background-color: #ff4d4d;
            color: white;
            padding: 15px 30px;
            font-size: 1.5rem;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 20px;
            animation: pulse 2s infinite;
        }
        .button:hover {
            background-color: #e60000;
        }
        @keyframes glow {
            0% { text-shadow: 0 0 10px #ff4081; }
            100% { text-shadow: 0 0 20px #ff4081, 0 0 30px #ff77a9; }
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class='container'>
        <h1>Emelie, Vill du bli min Valentine? 💖</h1>
        <div class='hearts'>🧸🌸💖💐😍🥰💘💕🌷🌹</div>
        <p class='message'>Du är mitt hjärta, mitt allt, min eviga kärlek! 💞</p>
        <p class='message'>Jag älskar dig mer än ord kan säga, Emelie! 💗</p>
        <button class='button' onclick="alert('Jag älskar dig, Emelie! ❤️ Din Adam')">JA! 💕</button>
    </div>
    <audio autoplay loop>
        <source src='https://www.bensound.com/bensound-music/bensound-love.mp3' type='audio/mpeg'>
        Din webbläsare stöder inte ljuduppspelning.
    </audio>
</body>
</html>
"""

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servern körs på http://localhost:{PORT}")
    httpd.serve_forever()