# -*- coding: utf-8 -*-
"""章のページを、count.py と同じ除外をかけて表示する。count.py と同じフォルダに置いて使う。

使い方： python3 show.py 開始ノンブル 終了ノンブル   （引数は PDF ページではなくノンブル）
"""
import sys

from count import page_lines, pdf_page

s, e = int(sys.argv[1]), int(sys.argv[2])
for p in range(s, e + 1):
    print(f"【p.{p}／PDF {pdf_page(p)}】")
    print("\n".join(page_lines(p)))
