import streamlit as st
from utils.chat_utils import init_session_state, chat_with_internlm, format_message
from . import prompt

def show():
    st.title("智能助手")
    
    # 初始化会话状态
    init_session_state()

    user_test_message = '请帮我生成xXX项目的需求说明书'
    assitant_test_message = '''
    ## 项目概述

    ### 产品背景介绍
    集团智慧运营平台旨在通过信息化手段，提升集团的运营效率和管理水平。平台覆盖集团的各个业务领域，包括但不限于 园区管理、投资管理、综合管理等，通过统一的管理平台，实现数据的集中、分析和共享，从而支持集团的高效决策和运 营。

    ### 产品概述及目标
    集团智慧运营平台是一个集成了多种功能的综合管理系统，旨在为集团提供一个统一的操作界面和管理平台。平台的主要 目标包括：
    - 提高集团的运营效率，通过信息化手段简化业务流程。
    - 加强集团内部信息的共享和流通，提升决策的科学性和准确性。
    - 支持集团的多样化业务需求，包括园区管理、投资管理、综合管理等。
    - 提供用户友好的操作界面，提升用户体验。

    ### 阅读对象
    - 需求评审人员
    - 开发人员
    - 测试人员
    - 产品经理
    - 项目管理人员

    ### 参考文档
    - 集团业务需求文档
    - 技术选型报告
    - 用户调研报告

    ### 术语与缩写解释
    | 术语/缩写 | 解释 |
    | --- | --- |
    | 集团智慧运营平台 | 指本项目开发的综合管理系统。 |
    | 园区管理 | 指集团对下属园区的管理，包括园区信息维护、入驻登记等。 |
    | 投资管理 | 指集团的投资项目管理，包括立项信息、投后管理等。 |
    | 综合管理 | 指集团的日常运营管理，包括车辆租赁、数据调度等。 |

    ## 产品角色
    - 集团管理员：负责平台的用户管理和权限设置。
    - 园区管理员：负责园区信息的维护和入驻企业的登记。
    - 投资管理员：负责投资项目的立项管理和投后管理。
    - 综合管理员：负责集团的日常运营管理，包括车辆租赁和数据调度。
    - 普通用户：包括园区入驻企业、投资项目的参与方等，使用平台的部分功能。

    ## 产品设计约束及策略
    - 界面设计简洁明了，易于操作。
    - 功能模块划分清晰，逻辑结构合理。
    - 数据安全性高，确保用户信息的安全。
    - 支持跨平台操作，包括电脑端和移动端。
    '''
    st.session_state.messages.append(format_message("user", user_test_message))
    st.session_state.messages.append(format_message("assitant", assitant_test_message))
    
    # 显示聊天历史
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # 用户输入
    if prompt_input := st.chat_input("请输入您的问题"):
        # 设置系统提示词
        system_prompt = prompt.system_prompt
        st.session_state.messages.append(format_message("system", system_prompt))

        # todo 设置context
        # project_context = '''
        # ## 项目名称
        # 数据治理全流程仿真系统
        # ## 项目目标
        # 基于数据治理和数据资产的大背景，为大学生设计的一套模拟整个数据治理和数据资产流程的仿真系统。
        # ## 项目背景
        # 无
        # '''
        # st.session_state.messages.append(format_message("system", project_context))

        # 添加用户消息
        st.session_state.messages.append(format_message("user", prompt_input))
        with st.chat_message("user"):
            st.write(prompt_input)
            
        # 显示助手正在思考
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("思考中...")
            
            messages = [
                {"role": msg["role"], "content": msg["content"]} 
                for msg in st.session_state.messages
            ]
            
            response = chat_with_internlm(messages)
            response_content = ''
            for chunk in response:
                chunk_content = chunk.choices[0].delta.content
                response_content += chunk_content
                message_placeholder.markdown(response_content)

            print(response_content)
            message_placeholder.markdown(response_content)
            
        st.session_state.messages.append(format_message("assistant", response_content)) 