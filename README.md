# your_shelf

## 概要: 複数人で本を貸し借りするサービスです

## 開発者
- Kento
- Keisuke
- Taisei
- Shizuka
- Yutaro
- Tomohiro
- Hiroyuki
- Taiki

## URL
- root/		                => ログイン画面
- root/admin/                   => 管理者画面
- root/books/                   => 本一覧
- root/books/create		=> 本の登録画面
- root/books/<title>		=> 本<title>の詳細ページ
- root/books/<title>/update/	=> 本<title>の更新ページ
- root/books/<title>/delete/	=> 本<title>の削除ページ
- root/accounts/		=> ユーザ一覧
- root/accounts/ <id> /		=> ユーザ<id>詳細
- root/accounts/<id>/update/    => ユーザ<id>の更新ページ
- root/accounts/<id>/delete/    => ユーザ<id>の削除ページ
- root/profiles/<id>/		=> ユーザ<id>のマイページ

## Model

- CustomUser

	- username (必須, ユニーク)
	- photo
	- email (必須)
	- password (必須)
	- interest 

- Book

	- attrs (User.interestと同じ)
	- owner (必須)
	- borrower
	- title (必須, primary key)
	- isbn
	- image
	- author
	- price
	- publisher
	- publish_date
	- description
