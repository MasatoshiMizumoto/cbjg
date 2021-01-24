# CloudEndure Bluprint Json Getter

## このスクリプトについて

- [CloudEndure](https://aws.amazon.com/jp/cloudendure-migration/) のプロジェクト内データを一覧（JSON）で取得します
- CloudEndureコンソールはBlueprint一覧のUIがなく、設定チェックには不向きな為作成

## 取得可能データ

- Blueprints
- Machines

## 対応認証形式

- user(Email)/password認証
- APIKey認証

## 動作環境

- Python 3.7.3(64bit)
- [requests](https://requests-docs-ja.readthedocs.io/en/latest/)

## 実行手順

1. requestsモジュールが環境にない場合はインストール(pip3 install requests)
2. cbjg.pyを実行
3. 表示に従って認証情報、プロジェクト名を入力、取得種別を入力
4. JSONが出力(Projectname-datatype.json)
