import streamlit as st

# 添加表设计的主要功能区
with st.container():
    st.write("### 数据库表设计工具")
    
    # 选择数据库类型
    db_type = st.selectbox(
        "选择数据库类型",
        ["MySQL", "PostgreSQL", "SQLite", "MongoDB"]
    )
    
    # 表名输入
    table_name = st.text_input("表名", placeholder="输入表名")
    
    # 字段设计区域
    st.write("### 字段设计")
    with st.expander("添加新字段", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            field_name = st.text_input("字段名")
        with col2:
            field_type = st.selectbox(
                "字段类型",
                ["INT", "VARCHAR", "TEXT", "DATETIME", "BOOLEAN", "DECIMAL"]
            )
        with col3:
            is_required = st.checkbox("必填")
            
    # 预览按钮
    if st.button("生成建表语句"):
        st.code("-- 这里将显示生成的建表SQL语句")
        
    # 导出选项
    st.download_button(
        label="导出设计文档",
        data="表设计文档内容",
        file_name="table_design.sql",
        mime="text/plain"
    )

