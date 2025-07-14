# LangChain ChatApp

[![CI](https://github.com/mjun0812/python-project-template/actions/workflows/ci.yml/badge.svg)](https://github.com/mjun0812/python-project-template/actions/workflows/ci.yml)

LangChainを使用した翻訳APIサービスです。Google Gemini AIを活用して翻訳機能を提供します。

## 機能

- 🌐 **翻訳API**: LangChainとGoogle Gemini AIを使用した高精度翻訳
- 📦 **LangServe**: LangChainアプリケーションの簡単なデプロイ
- 🐳 **Docker Support**: 完全なDocker開発環境
- 📦 **Devcontainer Support**: VS Code devcontainer対応
- ✨ **AI Editor Support**: [Cursor rules](https://docs.cursor.com/context/rules)と[CLAUDE.md](https://docs.anthropic.com/en/docs/claude-code/overview)対応
- 📝 **Type Hints**: 完全な型注釈サポート
- 🔍 **Code Quality**: Ruffによるリンティングとフォーマット
- 🧪 **Testing**: pytestセットアップ
- 🔧 **Pre-commit Hooks**: 自動コード品質チェック
- 🏗️ **CI Ready**: GitHub Actionsワークフロー

## 技術スタック

- **Python 3.12+**
- **LangChain**: AIアプリケーション開発フレームワーク
- **LangServe**: LangChainアプリケーションのデプロイ
- **Google Gemini AI**: 翻訳エンジン
- **uv**: 高速Pythonパッケージマネージャー

## クイックスタート

### 前提条件

- [uv](https://docs.astral.sh/uv/): 高速Pythonパッケージインストーラー
- Google Gemini AI APIキー

### 環境設定

1. 環境変数ファイルを作成:
```bash
cp .env.example .env
```

2. `.env`ファイルにGoogle Gemini AI APIキーを設定:
```env
GOOGLE_API_KEY=your_api_key_here
```

### ローカルで開発する場合のセットアップ

```bash
# 依存関係をインストール
uv sync

# プリコミットフックをインストール
uv run pre-commit install

# アプリケーションを起動
uv run python src/chat_app/main.py

# テストを実行
uv run pytest

# フォーマットとリンティング（コミット時に自動実行）
uv run ruff format .
uv run ruff check .
# 自動修正
uv run ruff check . --fix
```

### Dockerで開発する場合セットアップ

```bash
# uv.lockファイルを作成
uv sync

# 提供されたスクリプトを使用
./docker/build.sh
./docker/run.sh # または ./docker/run.sh (コマンド)

# Docker Composeでビルドと実行
docker compose build
docker compose up
```

### VS Code Devcontainerの場合のセットアップ

VS Codeでプロジェクトを開き、"Reopen in Container"コマンドを使用して完全に設定された開発環境を利用できます。

## サーバーの起動

```bash
uv run src/chat_app/main.py
```

## API エンドポイント

### 翻訳API

**POST** `/translate`

テキストを翻訳します。

**リクエスト例:**
```json
{
  "input": {
    "text": "Hello, world!",
    "language": "日本語"
  }
}
```

**レスポンス例:**
```json
{
  "output": "こんにちは、世界！"
}
```

### Playground

http://localhost:8000/translate/playground/

## プロジェクト構造

```text
LangChain-ChatApp/
├── src/
│   └── chat_app/              # メインパッケージ
│       ├── api/               # APIエンドポイント
│       ├── chains/            # LangChainチェーン
│       ├── models/            # AIモデル設定
│       ├── prompts/           # プロンプトテンプレート
│       ├── environment/       # 環境設定
│       └── main.py            # アプリケーションエントリーポイント
├── tests/                     # テストファイル
├── docker/                    # Docker設定
├── compose.yml               # Docker Compose設定
├── pyproject.toml            # プロジェクト設定
└── README.md                 # プロジェクトドキュメント
```

## 開発ガイドライン

### パッケージ管理
- uvのみを使用
- インストール: `uv add package`
- アップグレード: `uv add --dev package --upgrade-package package`
- 禁止: `uv pip install`, `@latest`構文

### コード品質
- すべてのコードに型ヒントが必要
- 既存のパターンを正確に従う
- ドキュメント文字列にはGoogleスタイルを使用

### テスト要件
- フレームワーク: `uv run --frozen pytest`
- カバレッジ: エッジケースとエラーをテスト
- 新機能にはテストが必要
- バグ修正には回帰テストが必要

### Git
- コミットメッセージはConventional Commitsスタイルに従う

## コードフォーマットとリンティング

### Ruff
- フォーマット: `uv run --frozen ruff format .`
- チェック: `uv run --frozen ruff check .`
- 修正: `uv run --frozen ruff check . --fix`

### Pre-commit
- 設定: `.pre-commit-config.yaml`
- 実行: git commit時
- ツール: Ruff (Python)

## サポート

- 📖 [LangChain Documentation](https://python.langchain.com/)
- 📖 [LangServe Documentation](https://python.langchain.com/docs/langserve)
- 🐍 [uv Documentation](https://docs.astral.sh/uv/)
- 🔍 [Ruff Documentation](https://docs.astral.sh/ruff/)
