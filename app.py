import streamlit as st
import pandas as pd
import json
import io

st.title("館長用: 刀剣データ構造化ツール")

st.markdown("""
このツールは、99件の刀剣データ（CSV形式）を館長がコピー＆ペーストして、
**構造化JSONに変換する簡易ツール** です。 🔧
""")

# テキストエリア
csv_text = st.text_area("ここにコピーしたCSVテキストを貼り付けてください:", height=300)

if st.button("JSONに変換"):
    if csv_text:
        try:
            # pandasでCSV読み込み
            df = pd.read_csv(io.StringIO(csv_text))

            # DataFrame → JSON
            records = df.to_dict(orient='records')
            json_str = json.dumps(records, ensure_ascii=False, indent=2)

            st.success("✅ 変換成功！ 以下がJSONです👇")
            st.code(json_str, language="json")

            st.download_button(
                label="JSONをダウンロード",
                data=json_str,
                file_name="swords.json",
                mime="application/json"
            )
        except Exception as e:
            st.error(f"変換時にエラーが発生しました: {e}")
    else:
        st.warning("⚠️ テキストが入力されていません。")
