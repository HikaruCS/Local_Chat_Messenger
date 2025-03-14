# Local Chat Messenger
Pythonのソケット通信とfakerパッケージを使用して、クライアントサーバ間で情報をやり取りするシンプルなアプリケーション<br>
Recursion (https://recursionist.io/) のバックエンドプロジェクト2で作成したものです。

## 操作方法
1. ターミナルを2つ開く(server.py用とclient.py用に1つずつ)
2. python3 ~/sever.py でサーバを立ち上げる
3. python3 ~/client.py でクライアントを立ち上げる
4. クライアント側のターミナルで指示通りにコマンドを入力する
5. クライアント側の通信が切れたら十字キーの↑を押して、再度3.のコマンドを実行する
6. サーバを切りたい場合、Ctrl+Cを使う

## サーバが返答できること
- 名前: What's your name? と入力するとランダムな名前を返します
- 職業: What is your job? と入力するとランダムな職業を返します
- 誕生日: When is your birthday? と入力するとランダムな誕生日を返します
- 出身国: Where are you from? と入力するとランダムな出身国を返します
- その他: 上記以外の質問や入力をした場合、Sorry, I can't answer this question. Ask me something else... と返されます

### 注意
急ぎ目で作ったため、返答のバリエーションがあまりないのはご容赦ください
