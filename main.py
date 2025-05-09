import streamlit as st
from utils import generate_xiaohongshu

st.header("🖊️小红书爆款文案生成器")
with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

theme = st.text_input("🗒️请输入主题")
submit = st.button("开始写作")

if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not theme:
    st.info("请输入生成内容的主题")
    st.stop()
if submit:
    with st.spinner("AI正在努力创作中，请稍后..."):
        result = generate_xiaohongshu(theme, openai_api_key)
        st.success("创作完成！！！")
    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        i = 1
        for title in result.titles:
            st.markdown("##### 小红书标题%d" % i)
            st.write(result.titles[i-1])
            i += 1
    with right_column:
        st.markdown("##### 小红书正文")
        st.write(result.content)