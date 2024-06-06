import gradio as gr
import asyncio

# 定义一个异步生成器函数
async def generate_results():
    for i in range(5):
        await asyncio.sleep(1)  # 模拟长时间运行的模型
        yield f"步骤 {i+1} 完成"  # 使用yield逐步产生结果

# 创建Gradio接口
iface = gr.Interface(
    fn=generate_results,
    inputs=None,  # 没有输入组件
    outputs=gr.Textbox(),  # 输出组件是一个文本框
    live=True  # 实时更新
)

# 启动Gradio界面
iface.launch()
