import csv
import re

import requests
from bs4 import BeautifulSoup

target_url = "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-regions.html"
r = requests.get(target_url)
r.encoding = "utf-8"

soup = BeautifulSoup(r.text, "lxml")

# idが'securityhub-control-support-'で始まる要素を取得
id_elements = soup.find_all(id=lambda x: x and x.startswith("securityhub-control-support-"))

# 出力データをリージョンごとに分割する
regions = []
for element in id_elements:
    region = [element.text]  # ID Element

    # 対応するitemizedlistクラスのdiv要素を取得
    itemizedlist_div = element.find_next("div", class_="itemizedlist")

    # div内のa要素を取得し、[]内のテキストを抽出
    a_elements = itemizedlist_div.select("a")
    for a_element in a_elements:
        match = re.search(r"\[(.*?)\]", a_element.text)
        if match:
            region.append(match.group(1))  # A Element

    regions.append(region)

# リージョンごとのデータを行ごとに整形する
max_len = max(len(r) for r in regions)
formatted_data = [r + [""] * (max_len - len(r)) for r in regions]

# 整形したデータをファイルに書き込む
with open("formatted_output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(zip(*formatted_data))