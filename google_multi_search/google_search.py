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

def get_info(keyword, driver):
    '''
    タイトル、URL、説明文、H1からH5までの情報を取得
    '''

    # 辞書を使って複数のアイテムを整理 -> 引数が減る＋返り値が減る
    items = {
        'keyword': keyword,
        'title': ['タイトル'],
        'url': [],
        'description': ['説明文'],
        'h1': [],
        'h2': [],
        'h3': [],
        'h4': [],
        'h5': []
    }

    # seleniumによる検索結果のurlの取得
    urls = driver.find_elements_by_css_selector('div.NJo7tc.Z26q7c.uUuwM.jGGQ5e > div > a')
    if urls:
        for url in urls:
            items['url'].append(url.get_attribute('href').strip())

    # seleniumによるtitleの取得
    titles = driver.find_elements_by_css_selector('div.NJo7tc.Z26q7c.uUuwM.jGGQ5e > div > a > h3')
    if titles:
        for title in titles:
            items['title'].append(title.text.strip())

    # seleniumによるdescription（説明文）の取得
    descriptions = driver.find_elements_by_css_selector('div > div:nth-child(2) > div > span')
    if descriptions:
        for description in descriptions:
            items['description'].append(description.text.strip())

    # h1?h5見出しの取得
    for url in items['url']:
        try:
        # URLにGETリクエストを送る
        response = requests.get(url)  # GETリクエスト
        soup = BeautifulSoup(response.text, 'html.parser')  # HTMLから情報を取り出す為にBeautifulSoupオブジェクトを得る
        time.sleep(1)  # 1秒待機

        except requests.exceptions.SSLError:  # SSlエラーが起こった時の処理を記入
            response = requests.get(url, verity=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            time.sleep(1)  # 1秒待機

        # h1
        # h1タグを全てリストとして取得
        h1s = soup.find_all('h1')

        # h1タグからテキストを取得してリストに入れる
        h1_list = []
        for h1 in h1s:
            if h1.get_text():
                h1_list.append(h1.get_text())
        items["h1"].append(h1_list)
        
        # h2
        # h2タグを全てリストとして取得
        h2s = soup.find_all('h2')
        
        # h2タグからテキストを取得してリストに入れる
        h2_list = []
        for h2 in h2s:
            if h2.get_text():
                h2_list.append(h2.get_text())
        items['h2'].append(h2_list)

        # h3
        # h3タグを全てリストとして取得
        h3s = soup.find_all('h3')
        
        # h3タグからテキストを取得してリストに入れる
        h3_list = []
        for h3 in h3s:
            if h3.get_text():
                h3_list.append(h3.get_text())
        items['h3'].append(h3_list)

        # h4
        # h4タグを全てリストとして取得
        h4s = soup.find_all('h4')
        
        # h4タグからテキストを取得してリストに入れる
        h4_list = []
        for h4 in h4s:
            if h4.get_text():
                h4_list.append(h4.get_text())
        items['h4'].append(h4_list)

        # h5
        # h5タグを全てリストとして取得
        h5s = soup.find_all('h5')
        
        # h5タグからテキストを取得してリストに入れる
        h5_list = []
        for h5 in h5s:
            if h5.get_text():
                h5_list.append(h5.get_text())
        items['h5'].append(h5_list)
    return items



'''
Googleスプレッドシートに情報を出力
'''

# 制限
# ①ユーザーごとに100秒あたり100件のリクエスト
# ②1秒あたり10件まで

# OAuth2の資格情報を使用してGoogleAPIにログイン
gc = gspread.authorize(credentials)

# シートが作成されているか確認するためのフラグ
flag = False
# 共有設定したスプレッドシートのシート1を開く
workbook = gc.open_by_key(SPREADSHEET_KEY)

# ワークシートを作成（タイトルがkeywordで、50行、50列）
worksheet = Workbook.add_worksheet(title=items['keyword'], rows='50', cols='50')

# シートが作成されたらフラグを立てる
flag = True
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