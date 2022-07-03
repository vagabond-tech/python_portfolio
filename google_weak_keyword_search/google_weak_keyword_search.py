# ブラウザを自動操作するためseleniumをimport
import chromedriver_binary
from selenium import webdriver
# seleniumでEnterキーを送信する際に使用するのでimport
from selenium.webdriver.common.keys import Keys
# seleniumでヘッドレスモードを指定するためにimport
from selenium.webdriver.chrome.options import Options
# 待ち時間を指定するためにtimeをimport
import time
# 正規表現にマッチする文字列を探すためにreをimport
import re

# Googleのトップページ
URL = 'https://www.google.co.jp'

# Googleのトップページに遷移したらタイトルに'Google'が含まれているか確認するために指定

'''
メインの処理
Googleの検索エンジンでキーワードを検索
指定されたドメインが検索結果の１ページ目に含まれていないキーワードをテキストファイルに出力
'''

# '検索キーワードリスト.txt'ファイルを読み込み、リストにする
with open('検索キーワードリスト.txt') as f:
    keywords = [s.rstrip() for s in f.readlines()]  # １行ずつ読み込んで改行コードを削除してリストにする

# 'ドメインリスト.txt'ファイルを読み込み、リストにする
with open('検索キーワードリスト.txt') as f:
    domains = [s.rstrip() for s in f.readlines()]  # １行ずつ読み込んで改行コードを削除してリストにする

# seleniumで自動操作するブラウザはGoogleChrome
# Optionsオブジェクトを作成
options = Options()
# ヘッドレスモードを有効にする
# options.add_argument('--headless')

# ChromeのWebDriverオブジェクトを作成
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome(options=options, executable_path=r"Windowsのchromedriver.exeを置いたパス")

# Googleのトップページを開く
driver.get(URL)
# 2秒待機（読み込みのため）

# タイトルに'Google'が含まれていることを確認

# 検索キーワードを１つずつ取り出す
# search関数実行
# get_url関数を実行し、戻り値をurlsに代入
# domain_checked関数を実行し、戻り値をok_keywordlistに代入

# '結果.txt'という名前を付けて、ドメインチェックしたキーワードをファイルに書き込む

# ドメインチェック済みのキーワードを１行ずつ保存

# ブラウザーを閉じる

'''
検索テキストボックスに検索キーワードを入力し、検索する
'''

# 検索テキストボックスの要素をname属性から取得
input_element = driver.find_element_by_name('q')

# 検索テキストボックスに入力されている文字列を消去
input_element.clear()

# 検索テキストボックスにキーワードを入力
input_element.send_keys("転職")

# Enterキーを送信
input_element.send_keys(Keys.RETURN)

# 2秒待機
time.sleep(2)

# タイトルにkeywordが含まれていることを確認

'''
検索結果ページの1位から10位までのURLを取得
'''

# 各ページのURLを入れるためのリストを指定
urls = []

# a要素（各ページの1位から10位までのURL）取得
objects = driver.find_elements_by_css_selector('div.yuRUbf > a')

# objects = driver.find_elements_by_css_selector('.rc > .r > a')

if objects:
    for object in objects:
        urls.append(object.get_attribute('href'))  # 各ページのURLをリストに追加
else:
    print('URLが取得できませんでした')  # 各ページのURLが取得できなかった場合は警告を出す
# 各ページのURLを戻り値に指定

'''
URLリストからドメインを取得し、指定ドメインに含まれているかチェック
'''
# URLリストから各ページのURLを１つずつ取り出す

# '//〇〇/'に一致する箇所（ドメイン）を抜き出す
# '//〇〇/'の'〇〇'に一致する箇所を抜き出し、domainに代入
# ドメインに'www.'が含まれているかチェック
# 含まれているなら'www.'を除去
# 各ページのドメインが指定ドメインに含まれているかチェック
# 含まれているなら警告を出す
# １つでも含まれているなら他はチェックする必要がないので関数を終了
# 指定ドメインに含まれていないならキーワードをok_keywordlistに追加
# ドメインチェック済みのキーワードを戻り値に指定

# main関数を実行
