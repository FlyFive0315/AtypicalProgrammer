import streamlit as st
from views.assistant import chat, history, table_design, test_case, user_manual
from views.preferences import manage, settings, model

def main():
    # 设置页面配置
    st.set_page_config(
        page_title="非典型程序员助手",
        layout="wide"
    )

    # 创建侧边栏导航
    with st.sidebar:
        pg = st.navigation(
            {
                "助手": [chat_page, table_design_page, test_case_page, user_manual_page],
                "偏好": [manage_page, settings_page, model_page],
            }
        )

    pg.run()

# 助手相关页面
chat_page = st.Page("views/assistant/chat.py", title="助手入口", icon="💬")
table_design_page = st.Page("views/assistant/table_design.py", title="表设计", icon="🗄️")
test_case_page = st.Page("views/assistant/test_case.py", title="测试用例", icon="🧪")
user_manual_page = st.Page("views/assistant/user_manual.py", title="用户手册", icon="📖")

# 偏好设置页面
manage_page = st.Page("views/preferences/manage.py", title="项目管理", icon="📁")
settings_page = st.Page("views/preferences/settings.py", title="偏好设置", icon="⚙️")
model_page = st.Page("views/preferences/model.py", title="模型设置", icon="🤖")

if __name__ == "__main__":
    main() 