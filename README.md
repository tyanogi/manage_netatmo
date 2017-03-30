#### <span style="color: red; "> 注 : Ubuntu(Linux)で操作することを前提とする </span>


### 目次
1. [環境構築](#1)
2. ThingSpeakのアカウント作成
3. NETATMOのアカウントの作成
4. プログラムの実行方法

### <a name='1'> 環境構築 </a>
##### Ubuntuのアップデート
```
sudo apt-get update
sudo apt-get upgrade
```
##### Python3系のインストール
```
sudo apt-get install -y python3
sudo apt-get install -y python3-pip
```

##### 今回使用するPythonライブラリのインストール
```
pip3 install lnetatmo
pip3 install urllib3
```
##### githubからソースコードを落としてくる
```
cd ~
git clone https://github.com/tyanogi/manage_netatmo.git
```
#### 実行方法
```
cd ~/manage_netatmo
python3 upload.py
```
