#!/usr/bin/env python3
"""
Simple HTTP server for ProNax AI web interface
"""

try:
    import http.server
    import socketserver
    import os
    import sys
    
    PORT = 8080
    
    # Change to web directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create server
    handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"🚀 ProNax AI Web Server running at http://localhost:{PORT}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"🌐 Open your browser and navigate to: http://localhost:{PORT}")
        print(f"⚡ Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped by user")
            
except ImportError as e:
    print(f"❌ Error: {e}")
    print("Please install Python or ensure it's in your PATH")
    input("Press Enter to exit...")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    input("Press Enter to exit...")
