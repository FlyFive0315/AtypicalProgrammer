import streamlit as st

# 页面标题
st.write("## 模板设置")

# 选择模板类型
template_type = st.radio(
    "选择模板类型",
    ['产品说明书', '表设计', '测试用例', '用户手册'],
    horizontal=True
)

# 模板内容编辑区
template_content = st.text_area(
    "模板内容",
    value=st.session_state.templates[template_type],
    height=400
)

# 保存按钮
if st.button("保存模板"):
    st.session_state.templates[template_type] = template_content
    st.success(f"{template_type}模板保存成功!") 