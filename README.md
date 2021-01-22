## CloudEndure Bluprint Json Getter

### このスクリプトについて

- [CloudEndure](https://aws.amazon.com/jp/cloudendure-migration/) のBlueprint一覧をJSONで取得します
- user(Email)/password認証、APIKey認証どちらにも対応
- CloudEndureコンソールはBlueprint一覧のUIがなく、設定チェックには不向きな為作成

### 動作環境

- Python 3.7.3(64bit)
- [requests](https://requests-docs-ja.readthedocs.io/en/latest/)

### 実行手順

1. requestsモジュールが環境にない場合はpip3でインストール
2. cbjg.pyを実行
3. 表示に従って認証情報、プロジェクト名を入力
4. BlueprintのJSONが出力

