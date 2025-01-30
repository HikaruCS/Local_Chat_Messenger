import socket

# ソケットを作成（今回はUDPを採用）
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
