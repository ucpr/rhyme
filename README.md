# Do you want to rhyme?
部活のLTのために作りました.  
韻を踏みたい単語を渡すと **韻が踏めそうな** 単語を返してくれます.  
急ぎで作ったのでコードが汚いので,時間があるときに直していきます.

## 使い方
実行環境 : python3.5, python3.6では動作を確認しました.
```bash
$ pip install -r requirements.txt

# src内で

# help 
$ python rhyme.py -h
   :)  Application that finds rhyming words. :)
Usage:
    rhyme.py [<hiragana_word>]
    rhyme.py [-s|--show] [<hiragana_word>]
    rhyme.py [-w|--write] [<hiragana_word>]
    rhyme.py [-h|--help]
options:
    -h --help   show this help message
    -s --show   write to file and show rhyming words
    -w --write  write to file

# terminal上に表示
$ python rhyme.py -s ひらがな
    いかさま
    きわやか
    キタガワ
    ヒラサワ
    ...

# ../rhyme_words内に書き出し
$ python rhyme.py -w ひらがな
    add ....
    add ....
    ...
```

## ＃お願い
辞書の語数が少なすぎて韻が全然韻が踏めないので単語を追加してほしいです!!!  

`src/dictionary`の中の`a.txt, k.txt, s.txt ...`というファイルに単語を追加していって欲しいです!  
あ行から始まる単語,か行から始まる単語...とファイルが分かれているのでそれにあわせて書き加えてPRを送ってくれると嬉しいです><
formatは下のように書いて欲しいです.
```
format:
  母音だけの文字(aiueon) + " " + 単語 + " " + よみがな(ひらがなで)
※母音だけの文字と書いてますが"ん"とよむところはnを入れてください
# 例 
aeno アメンボ　あめんぼ

# 例
aeno アメンボ　あめんぼ
aa 赤　あか
oiaa 沖縄 おきなわ
ooi おもり　おもり
...
```
