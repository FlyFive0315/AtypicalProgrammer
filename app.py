import streamlit as st
from views.assistant import chat, history
from views.project import manage, one_page
from views.preferences import settings, model



def main():
    # 设置页面配置
    st.set_page_config(
        page_title="非典型程序员助手",
        layout="wide"
    )

    # 创建侧边栏导航
    with st.sidebar:
        # st.sidebar.title("非典型程序员助手")  # 这里是系统名称
        
        pg = st.navigation(
            {
                "助手": [chat_page, history_page],
                "项目": [manage_page, one_page_page],
                "偏好": [settings_page, model_page],
            }
        )

    pg.run()

chat_page = st.Page("views/assistant/chat.py", title="助手入口", icon=":material/dashboard:", default=True)
history_page = st.Page("views/assistant/history.py", title="使用记录", icon=":material/dashboard:")

manage_page = st.Page("views/project/manage.py", title="项目管理", icon=":material/dashboard:")
one_page_page = st.Page("views/project/one_page.py", title="项目一页纸", icon=":material/dashboard:")

settings_page = st.Page("views/preferences/settings.py", title="偏好设置", icon=":material/dashboard:")
model_page = st.Page("views/preferences/model.py", title="模型设置", icon=":material/dashboard:")

if __name__ == "__main__":
    main() 