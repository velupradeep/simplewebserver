from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<table border="2">
<tr>
<td>Rank</td>
<td>Company</td>
<td>Revenue</td>
</tr>
<tr>
<td>1</td>
<td>Microscoft</td>
<td>69B</td>
</tr>
<tr>
<td>2</td>
<td>Oracle</td>
<td>29.6B</td>
</tr>
<tr>
<td>3</td>
<td>IBM</td>
<td>29.1B</td>
</tr>
<tr>
<td>4</td>
<td>sap</td>
<td>19B</td>
</tr>
<tr>
<td>5</td>
<td>hp</td>
<td>10B</td>
</tr>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()