from flask import Flask, Response

app = Flask(__name__)

@app.route('/api/text_stream', methods=['GET'])
def text_stream():
    # 这里可以是一个生成器，用于模拟流式数据
    def generate():
        for i in range(10):
            yield f"这是第 {i+1} 行文本数据\n"
            import time
            time.sleep(1)  # 模拟延迟

    return Response(generate(), content_type='text/stream')

if __name__ == '__main__':
    app.run(debug=True)
