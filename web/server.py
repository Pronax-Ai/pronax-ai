#!/usr/bin/env python3
"""
ProNax AI Web Server
Simple HTTP server for development and testing
"""

import http.server
import socketserver
import os
import sys
from urllib.parse import urlparse

class ProNaxHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)
    
    def end_headers(self):
        # Add CORS headers to allow cross-origin requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cross-Origin-Embedder-Policy', 'unsafe-none')
        self.send_header('Cross-Origin-Opener-Policy', 'unsafe-none')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def do_GET(self):
        # Serve index.html for root path
        if self.path == '/':
            self.path = '/index.html'
        
        # Handle CORS preflight
        if self.path.startswith('/api/'):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "ok", "message": "ProNax AI API Mock"}')
            return
        
        return super().do_GET()
    
    def do_POST(self):
        if self.path == '/api/v1/chat/completions':
            # Mock API response for testing
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            response = {
                "id": "chatcmpl-mock",
                "object": "chat.completion",
                "created": 1714080000,
                "model": "gemma-4",
                "choices": [{
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "Hello! I'm ProNax AI, powered by 3D spatial intelligence. This is a mock response for testing the web interface. The actual AI responses will be available once the backend is deployed with real models."
                    },
                    "finish_reason": "stop"
                }],
                "usage": {
                    "prompt_tokens": 10,
                    "completion_tokens": 25,
                    "total_tokens": 35
                }
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            import json
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run_server(port=8080):
    """Start the ProNax AI web server"""
    
    # Change to web directory
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)
    
    # Create server
    handler = ProNaxHTTPRequestHandler
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"🚀 ProNax AI Web Server running at http://localhost:{port}")
        print(f"📁 Serving files from: {web_dir}")
        print(f"🌐 Open your browser and navigate to: http://localhost:{port}")
        print(f"⚡ Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped by user")
            httpd.shutdown()

if __name__ == "__main__":
    port = 8080
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8080.")
    
    run_server(port)
