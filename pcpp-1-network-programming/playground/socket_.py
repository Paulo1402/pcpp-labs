import socket

server_addr = "paulobenatto.dev.br"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((server_addr, 80))

sock.sendall(
    b"HEAD / HTTP/1.1\r\n"
    b"Host: paulobenatto.dev.br\r\n"
    b"Connection: close\r\n"
    b"\r\n"
)

response = b""
while True:
    data = sock.recv(4096)
    if not data:
        break
    response += data

print(response.decode(errors="replace"))
sock.shutdown(socket.SHUT_RDWR)
sock.close()
