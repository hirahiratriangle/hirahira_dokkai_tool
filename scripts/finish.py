# -*- coding: utf-8 -*-
"""要約ファイルを置換で詰め、冒頭の字数表示を実数に書き直す。

使い方： python3 finish.py ファイル 原文字数 < 指示.json
指示  ： {"rep": [["置換前", "置換後"], ...], "tail": "■ 引用（3文）以降の全文"}
         rep は省ける。tail を省くと「■ 引用」以降は元のまま残る。
出力  ： 要約の字数  原文に対する比率  30%目標との差
置換前の文字列がファイルに無ければ、何も書かずに止まる。
"""
import json
import re
import sys

f, orig = sys.argv[1], int(sys.argv[2])
d = json.load(sys.stdin)
s = open(f, encoding="utf-8").read()
for a, b in d.get("rep", []):
    assert a in s, "見つからない: " + a[:25]
    s = s.replace(a, b)
if d.get("tail"):
    i = s.index("■ 引用")
    s = s[:i].rstrip("\n") + "\n\n" + d["tail"].strip("\n") + "\n"
body = s[s.index("■ 構造化要約") + len("■ 構造化要約"):s.index("■ 引用")]
n = len(re.sub(r"\s", "", body))
s = re.sub(r"本ファイルの要約 .*?字（.*?%）",
           "本ファイルの要約 %s字（%.1f%%）" % (format(n, ","), n / orig * 100), s, count=1)
open(f, "w", encoding="utf-8").write(s)
print(n, "%.2f%%" % (n / orig * 100), "%+.2f%%" % ((n / (orig * 0.3) - 1) * 100))
