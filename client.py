import socket
import sys

# TCP/IPソケットを作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# サーバのアドレス
server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

# サーバに接続
# なにか問題があれば、エラーメッセージを表示してプログラムを終了
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    # プログラムを終了
    sys.exit(1)

# サーバに接続できたら、サーバにメッセージを送信
try:
    # 送信するメッセージを入力するよう求める
    message = input('Enter the message to send to the server >>> ')
    # バイト型に変換
    message = message.encode()
    sock.sendall(message)

    # サーバからの応答を待つ時間を2秒間に設定
    # この時間が過ぎても応答がない場合、プログラムは次のステップに進む。
    sock.settimeout(2)

    # サーバからの応答を待ち、応答があればそれを表示
    try:
        while True:
            # サーバからのデータを受け取る（受け取るデータ量の最大量は16バイトに設定）
            data = str(sock.recv(32))

            # データがあればそれを表示、なかったらループを終了
            if data:
                print(data)
            else:
                break
    
    # 2秒間サーバからの応答がなければ、タイムアウトエラーとなり、エラーメッセージを表示する
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')
    
# すべての操作が完了したら、最後にソケットを閉じて通信を終了
finally:
    print('closing socket')
    sock.close()