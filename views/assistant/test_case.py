import streamlit as st

# 测试用例管理区域
with st.container():
    # 项目选择
    project = st.selectbox(
        "选择项目",
        ["项目A", "项目B", "项目C"]
    )
    
    # 测试用例类型
    test_type = st.radio(
        "测试类型",
        ["功能测试", "接口测试", "性能测试", "安全测试"]
    )
    
    # 添加新测试用例
    st.write("### 添加测试用例")
    with st.form("test_case_form"):
        case_name = st.text_input("用例名称")
        case_description = st.text_area("用例描述")
        
        col1, col2 = st.columns(2)
        with col1:
            priority = st.select_slider(
                "优先级",
                options=["低", "中", "高", "紧急"]
            )
        with col2:
            status = st.selectbox(
                "状态",
                ["未开始", "进行中", "已完成", "已阻塞"]
            )
        
        # 预期结果
        expected_result = st.text_area("预期结果")
        
        # 提交按钮
        submitted = st.form_submit_button("保存测试用例")
        
    # 测试用例列表
    st.write("### 测试用例列表")
    st.dataframe({
        "用例ID": ["TC001", "TC002"],
        "用例名称": ["登录测试", "注册测试"],
        "优先级": ["高", "中"],
        "状态": ["已完成", "进行中"]
    })
    
    # 导出功能
    st.download_button(
        label="导出测试用例",
        data="测试用例内容",
        file_name="test_cases.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )