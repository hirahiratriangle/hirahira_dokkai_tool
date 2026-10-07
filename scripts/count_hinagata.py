# -*- coding: utf-8 -*-
"""章（記事・対談）ごとの本文字数を数える。一冊ごとに書き換えて使う雛形。

<文献フォルダ>/読解/_tools/count.py として写し、「★」の付いた所をその本に合わせて書き換える。
書き換えた結果が、その本の「数え方」の記録になる。数え方を変えたら、ここの説明も直す。

数え方（どの本でも同じ）：
  - <文献フォルダ>/OCR/pages/ のページファイル（NNNN_ノンブル.txt）を使う
  - 各ページ1行目のページ区切り行を除く
  - 柱、ノンブルだけの行、その本に固有の本文でない行（DROP）を除く
  - 章の題・副題・著者名の行、注は含める
  - 残りから空白・改行をすべて除いた文字数を数える。30% は小数点以下切り捨て
使い方： python3 count.py        （一覧と合計）
         python3 count.py 5     （5番の章だけ）
show.py が page_lines() を借りる。
"""
import glob
import os
import re
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "OCR", "pages")

# ★ 重複スキャンのうち落とす側のファイル名（拡張子なし）。OCR が両方残しているときだけ書く
SKIP = set([
    # "0097_92",
])

# ★ 本文でない行。柱とその誤読形、ノンブルだけの行、収録注記など
DROP = [
    re.compile(r"^[0-9]{1,3}$"),          # ノンブルだけの行
    # re.compile(r"^総?特集\s*[＊*]?"),    # 柱
]

# ★ 番号, 題, 著者, 開始ノンブル, 終了ノンブル。広告や中扉のページは範囲から外す
CHAPTERS = [
    # (1, "序", "著者", 3, 25),
]


def page_files(p):
    """ノンブル p のページファイル。PDF 通しページとノンブルの差が一定でない本でも引けるよう、
    ファイル名の後ろ半分（ノンブル）で探す。"""
    g = sorted(x for x in glob.glob(os.path.join(BASE, f"*_{p}.txt"))
               if os.path.splitext(os.path.basename(x))[0] not in SKIP)
    if len(g) != 1:
        raise SystemExit(f"p.{p} のファイルが {len(g)} 個ある。SKIP と重複スキャンを確かめる")
    return g[0]


def pdf_page(p):
    return int(os.path.basename(page_files(p)).split("_")[0])


def page_lines(p):
    lines = open(page_files(p), encoding="utf-8").read().split("\n")[1:]
    out = []
    for l in lines:
        s = l.strip()
        if not s or any(r.search(s) for r in DROP):
            continue
        out.append(s)
    return out


def chars(s, e):
    return sum(len(re.sub(r"\s", "", "".join(page_lines(p)))) for p in range(s, e + 1))


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    tot = 0
    for no, t, a, s, e in CHAPTERS:
        if only and no != only:
            continue
        n = chars(s, e)
        tot += n
        print(f"{no:>2} p.{s}-{e}  PDF {pdf_page(s)}-{pdf_page(e)}  {n:>7,}  30%={int(n * 0.3):>6,}  {a}｜{t}")
    if not only:
        print(f"合計 {tot:,}  30%={int(tot * 0.3):,}")


if __name__ == "__main__":
    main()
