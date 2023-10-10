# スクリプト実行手順

想定実行環境 : AWS CloudShell

## Git Clone

```bash
git clone https://github.com/nyankotaro/cm-security-hub-region-restrictions-table ; cd cm-security-hub-region-restrictions-table/
```

## 仮想環境作成

```bash
python3 -m venv .venv && source .venv/bin/activate
```

## ライブラリインストール
  
```bash
pip3 install -r requirements.txt
```

## スクリプト実行

```bash
python3 extract_securityhub_regional_limits.py
```

## ブログリンク

https://dev.classmethod.jp/articles/security-hub-region-restrictions-table/
