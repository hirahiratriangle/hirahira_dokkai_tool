# hirahira_dokkai_tool

OCR 済みの文献（本・雑誌の特集号・対談集）を、**章ごとに原文の字数を数え、その 30% の字数で
構造化要約する**ための Claude Code スキルです。

- 章（記事・対談）ごとに 1 ファイル。構造化要約・引用 3 文・概念の定義文を収めます
- 字数は概算ではなく、スクリプトで数えます（目標の ±1%）
- 引用と定義文は紙面の画像と 1 字ずつ照らし、紙面のノンブルを付けます
- 推測・補足はしません。本文に書かれていないことは書きません

書き起こし（OCR）は [hirahira_ocr_tool](https://github.com/hirahiratriangle/hirahira_ocr_tool) の仕事です。
このスキルは、その出力（`OCR/pages/`）を受けて読解します。

## 入れ方

スキルは `~/.claude/skills/hirahira_dokkai_tool/` に置かれている前提で書かれています。
リポジトリをその場所に直接 clone してください。

```bash
git clone https://github.com/hirahiratriangle/hirahira_dokkai_tool ~/.claude/skills/hirahira_dokkai_tool
```

ほかに必要なもの（紙面画像の取り出しに使います）:

```bash
brew install poppler
```

スクリプトは Python 3 の標準ライブラリだけで動きます。

## 使い方

Claude Code で「（書名）を読解して」「いつものように読解して」と頼むと、このスキルが使われます。
手順は [SKILL.md](SKILL.md) にあります。

## 中身

| 場所 | 内容 |
|---|---|
| `SKILL.md` | 10 条件、決めごと、手順、文体、文献の種類による違い |
| `scripts/count_hinagata.py` | 章ごとの字数を数える雛形（一冊ごとに写して書き換える） |
| `scripts/show.py` | 数えるのと同じ除外をかけてページを表示する |
| `scripts/sumcount.py` | 要約の字数と文長を数える |
| `scripts/finish.py` | 要約を置換で詰め、字数表示を書き直す |
| `references/` | プロセス設計書の実例 |

## 精度について

要約は原典の代わりにはなりません。引用に使う箇所は必ず現物と照らしてください。

## ライセンス

MIT
