import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")
st.write("DataFrame")
df = pd.DataFrame({
    "1": [1, 2, 3, 4],
    "2": [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項
これはテストです。

'''python
import streamlit as st
import numpy as np
import pandas as pd
'''
"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]
)
st.map(df3)

"""
## Display Image
"""
img = Image.open("ダウンロード (29).png")
st.image(img, caption="icon", use_column_width=True)

"""
## Interactive
### Checkbox
"""
if st.checkbox("Show Image"):
    img = Image.open("ダウンロード (29).png")
    st.image(img, caption="icon", use_column_width=True)

"### Select Box"
option = st.selectbox(
    "あなたが好きな数字を教えてください。",
    list(range(1, 11))
)
"あなたの好きな数字は", option, "です。"

left_column, right_column = st.columns(2)

button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム。")
    
expander = st.expander("問い合わせ1")
expander.write("問い合わせへの回答")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせへの回答")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせへの回答")

"### Text Box"
text = st.text_input("あなたの趣味を教えてください。")
"あなたの趣味: ", text

"### Slider"
condition = st.slider("あなたの今の調子は？", 0, 100, 50)
"コンディション：", condition

# "### Sidebar"
# text2 = st.sidebar.text_input("あなたの趣味を教えてください。")
# condition2 = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)

# "あなたの趣味: ", text2
# "コンディション：", condition2

"### プログレスバーの表示"
"Start!!"
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
"Done!!"