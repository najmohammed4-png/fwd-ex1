from http.server import HTTPServer, BaseHTTPRequestHandler
content = """



<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            text-align: center;
            margin: 0;
        }

        header {
            background-color: #1e3a5f;
            color: white;
            padding: 20px;
        }

        .container {
            background-color: white;
            width: 80%;
            margin: 30px auto;
            padding: 20px;
            border-radius: 10px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            border: 1px solid #999;
            padding: 12px;
        }

        th {
            background-color: #1e3a5f;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #eeeeee;
        }

        footer {
            background-color: #1e3a5f;
            color: white;
            padding: 12px;
        }
    </style>
</head>

<body>

    <header>
        <h1>TCP/IP Protocol Suite</h1>
        <p>List of Network Protocols</p>
    </header>

    <div class="container">

        <h2>TCP/IP Protocol Layers</h2>

        <table>
            <tr>
                <th>Layer</th>
                <th>Protocols</th>
                <th>Function</th>
            </tr>

            <tr>
                <td>Application</td>
                <td>HTTP, HTTPS, FTP, SMTP, DNS, DHCP</td>
                <td>Provides network services to applications.</td>
            </tr>

            <tr>
                <td>Transport</td>
                <td>TCP, UDP</td>
                <td>Transfers data between devices.</td>
            </tr>

            <tr>
                <td>Internet</td>
                <td>IP, ICMP, ARP, IGMP</td>
                <td>Handles addressing and routing.</td>
            </tr>

            <tr>
                <td>Network Access</td>
                <td>Ethernet, Wi-Fi, PPP</td>
                <td>Transfers data through the physical network.</td>
            </tr>
        </table>

        <h2>About TCP/IP</h2>

        <p>
            TCP/IP stands for Transmission Control Protocol /
            Internet Protocol. It is a set of communication
            protocols used to connect devices over networks
            and the Internet.
        </p>

    </div>

    <footer>
        <p>TCP/IP Protocol Suite - Web Server Practical</p>
    </footer>

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
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()