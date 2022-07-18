# ブラウザを自動操作するためseleniumをimport
from selenium import webdriver
# seleniumでヘッドレスモードを指定するためにimport
from selenium.webdriver.chrome.options import Options
# seleniumでEnterキーを送信する際に使用するのでimport
from selenium.webdriver.common.keys import Keys
# HTTPリクエストを送る為にrequestsをimport
import requests
# HTMLから必要な情報を得る為にBeautifulSoupをimport
from bs4 import BeautifulSoup
# グーグルスプレッドシートを操作する為にimport
import gspread
# グーグルスプレッドシートの認証情報設定の為にimport
from google.oauth2.service_account import Credentials

# コード実行時のワーニング表示を無視
import warnings
warnings.simplefilter('ignore')

# グーグルのURL
URL = "https://google.co.jp"
# グーグルのURLタイトルの確認のため
URL_TITLE = 'Google'

# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

# 認証情報設定
# ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = Credentials.from_service_account_file("daitra-spreadsheet-scraping-99fdf49a6028.json", scopes=scope)

# 共有設定したスプレッドシートキーを格納
SPREADSHEET_KEY = '1S-PQHgVlR7U8Rq8n_H8r0IetWr2Mb1k6AuH1oi37ILI'

'''
メインの処理
Googleでキーワードを検索
１ページ目の情報を取得し、Googleスプレッドシートに出力
'''

# 検索キーワードが入力されたテキストファイルを読み込む
with open("keyword.txt") as f:
    keywords = [s.rstrip() for s in f.readlines()]

# Options()オブジェクトの生成
options = Options()
# options.add_argument('--headless') # ヘッドレスモードを有効にする
options.add_argument('--headless')
# ChromeのWebDriverオブジェクトを作成
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome(options=options, executable_path="chromedriverのpathを書く") -> Windowsの場合

driver.get(URL)  # Googleのトップページを開く

time.sleep(2)  # 2秒待機

# Google検索処理

# 情報取得処理

# Googleスプレッドシート出力処理


# ブラウザーを閉じる

'''
検索テキストボックスに検索キーワードを入力し、検索する
'''

# 検索テキストボックスの要素をname属性から取得

# 検索テキストボックスに入力されている文字列を消去

# 検索テキストボックスにキーワードを入力

# Enterキーを送信

# 2秒待機

'''
タイトル、URL、説明文、H1からH5までの情報を取得
'''

# 辞書を使って複数のアイテムを整理 -> 引数が減る＋返り値が減る

# seleniumによる検索結果のurlの取得

# seleniumによるtitleの取得

# seleniumによるdescription（説明文）の取得

# h1?h5見出しの取得

# URLにGETリクエストを送る

# GETリクエスト

# HTMLから情報を取り出す為にBeautifulSoupオブジェクトを得る

# 1秒待機

# SSlエラーが起こった時の処理を記入

# 1秒待機

# h1
# h1タグを全てリストとして取得

# h1タグからテキストを取得してリストに入れる

# h2
# h2タグを全てリストとして取得

# h2タグからテキストを取得してリストに入れる


# h3


# h4


# h5



'''
Googleスプレッドシートに情報を出力
'''

# 制限
# ①ユーザーごとに100秒あたり100件のリクエスト
# ②1秒あたり10件まで

# OAuth2の資格情報を使用してGoogleAPIにログイン

# シートが作成されているか確認するためのフラグ

# 共有設定したスプレッドシートのシート1を開く

# ワークシートを作成（タイトルがkeywordで、50行、50列）

# シートが作成されたらフラグを立てる

# スプレッドシート書き込み処理

# キーワードの書き込み

# 1秒待機

# 順位の書き込み

# 3秒待機

# 「タイトル」の書き込み

# 3秒待機

# 「URL」の書き込み

# 3秒待機

# 「ディスクリプション」の書き込み

# 3秒待機

# 「h1」の書き込み

# 3秒待機


# 「h2」の書き込み

# 3秒待機


# 「h3」の書き込み

# 3秒待機


# 「h4」の書き込み

# 3秒待機


# 「h5」の書き込み

# 3秒待機


# エラー処理

# グーグルスプレッドシートのAPIの制限に達した場合

# 100秒待機

# スプレッドシートに既にデータが存在している場合