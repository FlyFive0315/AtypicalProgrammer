import streamlit as st
from utils.chat_utils import init_session_state, chat_with_internlm, format_message
from utils import prompt
import pyperclip
 
# 生成标识
st.session_state.setdefault('generate', False)
# 用户提示词 缓存
st.session_state.setdefault('prompt_input', '')
# 发送给模型的消息列表
st.session_state.setdefault('messages', [])
# 当前步骤
st.session_state.setdefault('current_step', 1)
# 当前输出内容
st.session_state.setdefault('output_document', '')

st.markdown("""
    <style>
        body {
            background: #fff;
        }
        /* 右侧整体布局背景 */
        .stAppHeader {
            background: transparent;    
        }
        .stSidebar {
            background: #fff;
        }
        .stMain {
            background: rgb(240, 242, 246);
            border-left: 1px solid #dedede; 
        }
        .stMainBlockContainer {
            padding: 0rem 0px 0px 0px;
            background: rgb(240, 242, 246);
        }

        .stChatMessage {
            background: transparent;
        }
        div[data-testid="stChatMessageContent"] {
            background: #fff;
            padding: 10px 20px;
        }
        div[data-testid="stBottomBlockContainer"] {
            padding: 1rem 1rem;
        }
        /* 右侧面板样式 */
        .side-panel-section {
            margin-bottom: 2rem;
            padding: 1rem;
            background: #fff;
            border-radius: 4px;
        }
        /* 右侧面板卡片样式 */
        .panel-card {
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }
        
        /* 分隔线样式 */
        .divider {
            margin: 20px 0;
            border-bottom: 1px solid #eee;
        }
        
        /* 按钮样式美化 */
        .stButton > button {
            width: 100%;
            border-radius: 5px;
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            margin: 5px 0;
            transition: all 0.3s;
        }
        
        .stButton > button:hover {
            background-color: #e9ecef;
            border-color: #dee2e6;
        }
        
        /* 标题样式 */
        .panel-title {
            color: #1f2937;
            font-size: 18px;
            margin-bottom: 15px;
        }
        
        /* 右侧列固定样式 */
        [data-testid="stColumn"]:nth-of-type(2) {
            background: white;
            position: fixed;
            top: 0;
            right: 0;
            width: 438.75px;  /* 根据7:3的比例计算 */
            height: 100%;
            padding: 20px;
            border-left: 1px solid #eee;
            overflow-y: auto;  /* 如果内容过多允许滚动 */
        }
    
        [data-testid="stColumn"]:nth-of-type(1) {
            margin-right: 438.75px;  /* 为右侧固定区域留出空间 */
            padding: 40px 40px 80px 40px;
            height: 100%;
            position: relative;
        }
        /* 聊天输入框容器样式 */
        [data-testid="stColumn"]:nth-of-type(1) .stChatInput {
            position: fixed;
            bottom: 20px;
            background: white;
            border-top: 1px solid #eee;
            z-index: 100;
        }
        [data-testid="stColumn"]:nth-of-type(1) [data-testid="stVerticalBlockBorderWrapper"] {
            min-height: calc(100vh - 120px);
            padding-bottom: 120px;
        }
        [data-testid="stColumn"]:nth-of-type(1) .stElementContainer {
            background: #fff;
            
        }
        [data-testid="stColumn"]:nth-of-type(1) .stMarkdown {
            padding: 60px 40px;
        }
    </style>
""", unsafe_allow_html=True)

# 初始化会话状态
init_session_state()

# 角色人设
request_messages = []
cpsms_system_prompt = prompt.cpsms_system_prompt
request_messages.append(format_message("system", cpsms_system_prompt))

# 创建左右布局
left_col, right_col = st.columns([7, 3])  # 7:3 的宽度比例

# 右侧操作面板
with right_col:
    # 生成文章区域
    st.markdown('<div class="side-panel-section">', unsafe_allow_html=True)
    st.markdown('<p class="panel-title">📝 步骤</p>', unsafe_allow_html=True)
    # st.write(st.session_state.current_step)
    
    # 在右侧面板添加重置按钮
    if st.button("重新开始"):
        st.session_state.generate = False
        st.session_state.prompt_input = ''
        st.session_state.messages = []
        st.session_state.current_step = 1
        st.session_state.output_document = ''
        st.session_state.project_name = ''
        st.session_state.project_background = ''
        st.session_state.project_summary = ''
        st.session_state.function_list = ''
        st.session_state.other_part = ''
        st.rerun()
    
    steps = [
        "填写项目信息",
        "确认思路和方向",
        "确认功能清单",
        "其它补充",
        "生成全文"
    ]
    
    for i, step in enumerate(steps, 1):
        if i == st.session_state.current_step:
            st.markdown(f"**{i}. {step}**")
        else:
            st.markdown(f"{i}. {step}")
        if i == 1:
            project_name = st.text_input("项目名称")
            project_background = st.text_input("项目背景")
                

    # 添加下一步按钮
    if st.session_state.current_step < len(steps):
        if st.button("下一步", disabled=st.session_state.current_step == 5):
            print("下一步点击:", st.session_state.current_step)
            if st.session_state.current_step == 1:
                st.session_state.project_name = project_name
                st.session_state.project_background = project_background  
                st.session_state.generate = True
                st.session_state.prompt_input = prompt.cpsms_prompt_step2 % {
                    'project_name': st.session_state.project_name, 
                    'project_background': st.session_state.project_background
                    }
            elif st.session_state.current_step == 2:
                st.session_state.generate = True
                st.session_state.prompt_input = prompt.cpsms_prompt_step3  % {
                    'project_name': st.session_state.project_name, 
                    'project_background': st.session_state.project_background, 
                    'project_summary': st.session_state.project_summary
                    }
            elif st.session_state.current_step == 3:
                st.session_state.generate = True
                st.session_state.prompt_input = prompt.cpsms_prompt_step4  % {
                    'project_name': st.session_state.project_name, 
                    'project_background': st.session_state.project_background, 
                    'project_summary': st.session_state.project_summary, 
                    'function_list': st.session_state.function_list
                    }
            elif st.session_state.current_step == 4:
                st.session_state.generate = True
                st.session_state.prompt_input = prompt.cpsms_prompt_step5  % {
                    'project_name': st.session_state.project_name, 
                    'project_background': st.session_state.project_background, 
                    'project_summary': st.session_state.project_summary, 
                    'function_list': st.session_state.function_list,
                    'other_part': st.session_state.other_part,
                    'output_template': st.session_state.templates['产品说明书'] if st.session_state.templates and len(st.session_state.templates) > 0 else prompt.cpsms_output_template
                    }
            elif st.session_state.current_step == 5:
                pass
            
            st.session_state.current_step += 1

            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# 主要内容区域
with left_col:
    # 显示聊天历史
    # for index, message in enumerate(st.session_state.messages):
    #     if message["role"] != "system":
    #         with st.chat_message(message["role"]):
    #             st.write(message["content"])
                
                # if message["role"] == 'assistant':
                #     # 添加工具栏
                #     toolbar_container = st.container()
                #     with toolbar_container:
                #         unique_id = f"{index}_{st.session_state.get('message_counter', 0)}"
                        
                #         # 复制按钮逻辑
                #         copy_key = f"copy_message_result_{unique_id}"
                #         if copy_key not in st.session_state:
                #             st.session_state[copy_key] = False

                #         if st.button("🔄 复制", key=f"copy_button_{unique_id}"):
                #             pyperclip.copy(message["content"])
                #             st.session_state[copy_key] = True

                #         if st.session_state[copy_key]:
                #             st.success("内容已复制到剪贴板！")
                #             st.session_state[copy_key] = False

                #         # 导出按钮逻辑
                #         st.download_button(
                #             "📥 导出", 
                #             message["content"], 
                #             file_name="message.md", 
                #             mime="text/markdown", 
                #             key=f"export_button_{unique_id}"
                #         )

    

    # 用户输入
    if st.session_state.current_step != 1:
        chat_input = st.chat_input("请输入您的调整意见")
        if chat_input:
            # 调整意见 prompt
            adjust_prompt = prompt.cpsms_prompt_adjust % {
                'adjust_input': chat_input,
                'original_content': st.session_state.output_document
            }
            st.session_state.prompt_input = adjust_prompt

    # 实际生成
    if st.session_state.generate:
        request_messages.append(format_message("user", st.session_state.prompt_input))
            
        message_placeholder = st.empty()
        message_placeholder.markdown("思考中...")
        
        messages = [
            {"role": msg["role"], "content": msg["content"]} 
            for msg in request_messages
        ]
        
        response = chat_with_internlm(messages)
        response_content = ''
        for chunk in response:
            chunk_content = chunk.choices[0].delta.content
            response_content += chunk_content
            message_placeholder.markdown(response_content)

        # print("response_content:", response_content)
        message_placeholder.markdown(response_content)
        # 存储当前生成内容
        st.session_state.output_document = response_content

        # 保存中间结果，用于下一步生成
        if st.session_state.current_step == 2:
            st.session_state.project_summary = response_content
        elif st.session_state.current_step == 3:
            st.session_state.function_list = response_content
        elif st.session_state.current_step == 4:
            st.session_state.other_part = response_content

