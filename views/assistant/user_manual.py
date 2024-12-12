import streamlit as st

   
# 侧边栏目录
with st.sidebar:
    st.write("### 目录")
    section = st.radio(
        "",
        ["快速开始", "基础功能", "高级特性", "常见问题", "联系支持"]
    )

# 主要内容区域
if section == "快速开始":
    st.header("快速开始")
    st.write("""
    ### 欢迎使用非典型程序员助手！
    
    本系统旨在帮助程序员更高效地完成开发工作。以下是快速入门的步骤：
    
    1. **系统登录**
        - 使用您的账号密码登录系统
        - 首次使用请联系管理员获取账号
    
    2. **基本功能**
        - 项目管理
        - 代码生成
        - 文档编写
        
    3. **开始使用**
        - 创建您的第一个项目
        - 尝试使用AI助手
    """)
    
elif section == "基础功能":
    st.header("基础功能")
    with st.expander("项目管理", expanded=True):
        st.write("项目的创建、配置和管理说明...")
        
    with st.expander("表设计工具"):
        st.write("如何使用表设计工具...")
        
    with st.expander("测试用例管理"):
        st.write("测试用例的创建和管理方法...")
        
elif section == "高级特性":
    st.header("高级特性")
    st.write("高级功能使用说明...")
    
elif section == "常见问题":
    st.header("常见问题")
    with st.expander("如何创建新项目？"):
        st.write("创建新项目的详细步骤...")
        
    with st.expander("如何使用AI助手？"):
        st.write("AI助手的使用方法和技巧...")
        
else:  # 联系支持
    st.header("联系支持")
    st.write("""
    ### 需要帮助？
    
    - 邮件支持：support@example.com
    - 在线文档：https://docs.example.com
    - 问题反馈：https://github.com/example/issues
    """)
    
    with st.form("support_form"):
        st.write("### 提交问题反馈")
        user_name = st.text_input("您的姓名")
        user_email = st.text_input("联系邮箱")
        issue_type = st.selectbox("问题类型", ["功能建议", "错误报告", "使用咨询", "其他"])
        issue_description = st.text_area("问题描述")
        submitted = st.form_submit_button("提交")