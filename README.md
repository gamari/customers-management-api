# 概要

顧客管理用アプリのAPIサンプル。

## 全体仕様

### 認証システム

- JWT認証を採用


### IP制限

- TODO


## API

### お問い合わせ作成API

- URL
  - /inquire
- Method
  - POST
- Request
  - company_name
    - 会社名
  - phone_number
    - 電話番号
  - pdf_file
    - 何かしらのPDFファイル
- Response
  - status
    - 201
  - body
    - 何も返さない（statusで成功は判定する）
- 詳細
  - IDは特定を防ぐためにUUIDにしています
  - pdf_fileの部分を参考に適切なファイル名に変更する必要があります