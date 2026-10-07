# -*- coding: utf-8 -*-
"""要約ファイルの「■ 構造化要約」〜「■ 引用」の字数（空白・改行を除く）と文長を数える。

使い方： python3 sumcount.py ファイル [目標字数]
出力  ： 字数  目標との差(%)  文数  1文の平均字数  80字を超える文の割合(%)
"""
import re
import sys

t = open(sys.argv[1], encoding="utf-8").read()
body = t[t.index("■ 構造化要約") + len("■ 構造化要約"):t.index("■ 引用")]
n = len(re.sub(r"\s", "", body))
tgt = int(sys.argv[2]) if len(sys.argv) > 2 else 0
S = [s for s in re.split(r"(?<=。)|\n", body) if s and s.strip()]
L = [len(re.sub(r"\s", "", s)) for s in S]
print(n, f"{(n / tgt - 1) * 100:+.2f}%" if tgt else "",
      "文数", len(L), "平均", round(sum(L) / len(L), 1),
      "80字超%", round(sum(x > 80 for x in L) / len(L) * 100, 1))
