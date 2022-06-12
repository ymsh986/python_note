import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from time import sleep

"""
# Streamlit 学習メモ
Streamlitを学んだ際のメモを記載する  
<ドキュメント>  
https://docs.streamlit.io


## 1. Streamlit の導入
### streamlit のインストール
```bash
pip install streamlit
```

以下で、チュートリアリアルデモを表示させる
```bash
streamlit hello
```

自作ファイル（例：main.py）の実行には、以下のように実施する
```bash
streamlit run main.py
```

## 2. キホンの表示
### 使用ライブラリは以下
```python
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
```

### title表示と、文字列表示
```python
st.title('Streamlit Sample')
st.write('DataFrame')
```
"""
st.title('Streamlit Sample')
st.write('DataFrame')

"""
### DataFrame表示
```python
df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [10, 20, 30, 40]
                  })

# 動的な出力
st.write(df)

# より詳細に引数指定したい場合
st.dataframe(df.style.highlight_max(axis=0), width=500, height=200)

# 静的な出力
st.table(df)
```
"""
df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [10, 20, 30, 40]})

# 動的な出力
st.write('st.write')
st.write(df)

# より詳細に引数指定したい場合
st.write('st.dataframe')
st.dataframe(df.style.highlight_max(axis=0), width=500, height=200)

# 静的な出力
st.write('st.table')
st.table(df)

"""
### チャート表示
```python
df = pd.DataFrame(np.random.rand(20, 3), columns=['a', 'b', 'c'])

# 折れ線グラフ
st.line_chart(df)

# 折れ線下塗りグラフ
st.area_chart(df)

# 棒グラフ
st.bar_chart(df)
```
"""
df = pd.DataFrame(np.random.rand(20, 3), columns=['a', 'b', 'c'])

# 折れ線グラフ
st.line_chart(df)

# 折れ線下塗りグラフ
st.area_chart(df)

# 棒グラフ
st.bar_chart(df)


"""
### MAP表示
```python
# 新宿付近の緯度経度
df = pd.DataFrame(np.random.rand(20, 2) / [10, 10] + [35.69, 139.70], columns=['lat', 'lon'])

st.map(df)
```
"""

# 新宿付近の緯度経度
df = pd.DataFrame(np.random.rand(20, 2) / [10, 10] + [35.69, 139.70], columns=['lat', 'lon'])

st.map(df)


"""
### 画像表示
```python
img = Image.open('./image1.jpg')
st.image(img, use_column_width=True)
# use_column_width=True とすると、画像をページ横幅に合わせて表示する
```
"""
img = Image.open('./image1.jpg')
st.image(img, use_column_width=True, caption='Sample Image')


"""
## 2. ウィジェットの表示
### チェックボックス
チェックボックスにチェックが入っていれば内容を表示し、入っていなければ非表示にする
```python
if st.checkbox('show image'):
    st.image(img, use_column_width=True, caption='Sample Image')
```
"""
if st.checkbox('show image'):
    st.image(img, use_column_width=True, caption='Sample Image')


"""
### セレクトボックス
値を決めた内容の中から選択させるボックス
```python
option = st.selectbox('数字選択', options=list(range(1, 11)))
'選択した数字は ', option, 'です。'
```
"""
option = st.selectbox('数字選択', options=list(range(1, 11)))
'選択した数字は ', option, 'です。'


"""
### テキスト入力ボックス
入力した文字列を得る
```python
text = st.text_input('適当な文字列を入力してください')
'入力された文字列は ', text, 'です。'
```
"""
text = st.text_input('適当な文字列を入力してください')
'入力された文字列は ', text, 'です。'


"""
### スライダー
ドラッグで値を変えることのできるバーを得る
```python
condition = st.slider('本日のコンディションは？', 0, 100, 50)
# 第2引数が最小値, 第3引数が最大値, 第4引数が初期値を示す
'コンディションは ', condition, 'です。'
```
"""
# condition = st.slider('本日のコンディションは？', 0, 100, 50)
# 'コンディションは ', condition, 'です。'


"""
## レイアウト
### サイドバー
サイドバーを作り、同じように表現できる
```python
condition_side = st.sidebar.slider('本日のコンディションは？', 0, 100, 50)
'本当のコンディションは ', condition_side, 'です。'
```
"""
condition_side = st.sidebar.slider('本日のコンディションは？', 0, 100, 50)
'本当のコンディションは ', condition_side, 'です。'


"""
### 2列表示
```python
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラムを表示')
```
"""
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラムを表示')


"""
### エクスパンダー
ワンクリックすると、表示が拡張される機能
```python
expander = st.expander('expand messages...')
expander.write('I live in Japan.')
```
"""

expander = st.expander('expand messages...')
expander.write('I live in Japan.')


"""
### プログレスバー
進捗バーを作り、処理状況を見える化する
```python
lataset_iteration = st.empty()
bar = st.progress(0)
# ここでの順序がページでの表示順になる

for i in range(100):
    lataset_iteration.text(f'Iteration {i + 1}')
    bar.progress(i+1)
    sleep(0.05)

'Done!!'
```
"""

lataset_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    lataset_iteration.text(f'Iteration {i + 1}')
    bar.progress(i+1)
    sleep(0.05)

'Done!!'
