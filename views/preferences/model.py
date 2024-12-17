import streamlit as st

# 模型选择
st.subheader("模型选择")
model = st.radio(
    "选择要使用的模型：",
    ["internlm2.5-latest"],
    index=["internlm2.5-latest"].index(st.session_state.model_settings["model"]),
)

# 模型参数设置
st.subheader("模型参数设置")

# Temperature 滑动条
temperature = st.slider(
    "Temperature (采样温度)",
    min_value=0.0,
    max_value=2.0,
    value=st.session_state.model_settings["temperature"],
    step=0.1,
    help="较高的值会使输出更加随机，较低的值会使输出更加集中和确定"
)

# Top P 滑动条
top_p = st.slider(
    "Top P (候选 token 的概率下限)",
    min_value=0.0,
    max_value=1.0,
    value=st.session_state.model_settings["top_p"],
    step=0.1,
    help="控制模型生成文本时考虑的候选词的累积概率阈值"
)

# 保存按钮
if st.button("保存设置", type="primary"):
    st.session_state.model_settings.update({
        "model": model,
        "temperature": temperature,
        "top_p": top_p
    })
    st.success("设置已保存！")

# 显示当前设置
st.divider()
st.caption("当前保存的设置：")
st.write(f"- 选择的模型：{st.session_state.model_settings['model']}")
st.write(f"- Temperature：{st.session_state.model_settings['temperature']}")
st.write(f"- Top P：{st.session_state.model_settings['top_p']}") 