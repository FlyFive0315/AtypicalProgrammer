import streamlit as st
from pages.assistant import chat, history
from pages.project import manage, one_page
from pages.preferences import settings, model

# 设置页面配置
st.set_page_config(
    page_title="非典型程序员助手",
    layout="wide"
)

# 定义导航结构
NAVIGATION = {
    "助手": {
        "助手入口": chat.show,
        "使用记录": history.show
    },
    "项目": {
        "项目管理": manage.show,
        "项目一页纸": one_page.show
    },
    "偏好": {
        "偏好设置": settings.show,
        "模型设置": model.show
    }
}

def main():
    # 创建侧边栏导航
    with st.sidebar:
        st.title("功能导航")
        
        # 当前选中的页面
        if "current_page" not in st.session_state:
            st.session_state.current_page = "助手入口"
            
        # 显示导航菜单
        for category, pages in NAVIGATION.items():
            st.markdown(f"### {category}")
            for page_name in pages.keys():
                if st.button(page_name, key=page_name, use_container_width=True):
                    st.session_state.current_page = page_name
                    st.rerun()
    
    # 显示选中的页面内容
    for category, pages in NAVIGATION.items():
        if st.session_state.current_page in pages:
            pages[st.session_state.current_page]()
            break

if __name__ == "__main__":
    main() 