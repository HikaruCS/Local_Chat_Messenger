import socket
import os
from faker import Faker

# UNIXソケットをストリームモードで作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# このサーバが接続を待つUNIXソケットのパスを設定
server_address = '/tmp/socket_file'

# 以前の接続が残っていた場合に備えて、サーバアドレスをアンリンク（削除）する
try:
    os.unlink(server_address)
# サーバアドレスが存在しない場合は例外を無視
except FileNotFoundError:
    pass

# サーバアドレスにソケットをバインド（接続）する
sock.bind(server_address)

# ソケットに接続要求を待機させる
sock.listen(1)

# 無限ループでクライアントからの接続を待ち続ける
while True:
    # クライアントからの接続を受け入れる
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # サーバが新しいデータを待ち続けるためのループ
        while True:
            # ここでサーバは接続からデータを読み込む
            # 一度に最大16バイト読み込む
            data = connection.recv(32)

            # 受け取ったデータをバイナリ形式から文字列に変換(utf-8)
            data_str = data.decode('utf-8')

            # 受け取ったデータを表示
            print('Received ' + data_str)

            if data:
                fake = Faker()
                # 返信をからの文字列で初期化
                response = ''

                if data_str == "What's your name?":
                    response = 'My name is ' + fake.name()
                elif data_str == "What is your job?":
                    response = 'My job is ' + fake.job()
                elif data_str == "When is your birthday?":
                    response = 'My birthday is ' + fake.date(pattern='%Y/%m/%d')
                elif data_str == "Where are you from?":
                    response = "I'm form " + fake.country()
                else:
                    response = "Sorry, I can't answer this question. Ask me something else..."

                # メッセージをバイナリ形式にしてクライアントに送り返す
                connection.sendall(response.encode())
            
            # クライアントからデータが送られてこなければ、ループを終了
            else:
                print('no data from', client_address)
                break

    # 最終的に接続を閉じる
    finally:
        print('Closing current connection')
        connection.close()