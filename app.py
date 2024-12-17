import streamlit as st

# 设置页面配置必须是第一个 Streamlit 命令
st.set_page_config(
    page_title="非典型程序员助手",
    layout="wide"
)
st.logo("assets/logo.png", size="large")

if "templates" not in st.session_state:
    st.session_state.templates = {
        '产品说明书': '',
        '表设计': '',
        '测试用例': '',
        '用户手册': ''
    }
if "model_settings" not in st.session_state:
    st.session_state.model_settings = {
        "model": "internlm2.5-latest",
        "temperature": 0.8,
        "top_p": 0.9
    }

# 助手相关页面
product_demand_page = st.Page("pages/assistant/product_demand.py", title="产品说明书", icon="💬", default=True)
table_design_page = st.Page("pages/assistant/table_design.py", title="表设计⏳", icon="🗄️")
test_case_page = st.Page("pages/assistant/test_case.py", title="测试用例⏳", icon="🧪")
user_manual_page = st.Page("pages/assistant/user_manual.py", title="用户手册⏳", icon="📖")

# 偏好设置页面
manage_page = st.Page("pages/preferences/manage.py", title="项目管理⏳", icon="📁")
settings_page = st.Page("pages/preferences/settings.py", title="偏好设置", icon="⚙️")
model_page = st.Page("pages/preferences/model.py", title="模型设置", icon="🤖")

# 创建导航
pg = st.navigation(
    {
        "助手": [product_demand_page, table_design_page, test_case_page, user_manual_page],
        "偏好": [manage_page, settings_page, model_page],
    }
)

pg.run()