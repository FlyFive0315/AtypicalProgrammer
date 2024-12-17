import streamlit as st

def init_session_state():
    if 'templates' not in st.session_state:
        st.session_state.templates = {
            '产品说明书': '',
            '表设计': '',
            '测试用例': '',
            '用户手册': ''
        }

def main():
    st.title('模板管理系统')
    
    # 初始化session state
    init_session_state()
    
    # 顶部radio选择
    template_type = st.radio(
        "请选择模板类型",
        ['产品说明书', '表设计', '测试用例', '用户手册']
    )
    
    # 模板内容编辑区
    st.subheader(f"{template_type}模板编辑")
    template_content = st.text_area(
        "模板内容",
        value=st.session_state.templates[template_type],
        height=300
    )
    
    # 保存按钮
    if st.button('保存模板'):
        st.session_state.templates[template_type] = template_content
        st.success(f'{template_type}模板保存成功！')
        
    # 显示当前保存的模板内容（用于调试）
    st.subheader("当前保存的模板内容")
    st.json(st.session_state.templates)

if __name__ == "__main__":
    main() 