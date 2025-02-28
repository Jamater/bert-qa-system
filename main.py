import os
# 设置 HTTP 和 HTTPS 代理为本地代理地址，端口为1080
os.environ["HTTP_PROXY"] = "http://127.0.0.1:1080"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:1080"


os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"  # 禁用符号链接警告

from transformers import pipeline
from fastapi import FastAPI, HTTPException
import uvicorn


# 1. 加载 Hugging Face 上微调好的问答模型
model_name = "uer/roberta-base-chinese-extractive-qa"
qa_pipeline = pipeline("question-answering", model=model_name)

# 2. 自定义知识库（模拟真实业务场景）
knowledge_base = {
    "BERT": "BERT是一种预训练语言模型。BERT由Google在2018年提出。BERT采用Transformer架构，并通过双向上下文编码来理解文本。",
    "Transformer": "Transformer是一种完全基于注意力机制的模型架构。Transformer摒弃了传统的RNN和CNN结构。Transformer在自然语言处理任务中表现出色。",
    "GPT": "GPT是一种生成式预训练模型。GPT由OpenAI开发。GPT基于Transformer架构，适用于文本生成任务。"
}


# 3. 改进的知识库匹配逻辑
def find_context(question: str):
    # 遍历知识库，检查问题中是否包含知识库的键
    for key in knowledge_base:
        if key in question:
            print(f"匹配到关键词: {key}")  # 调试信息
            return knowledge_base[key]
    print("未匹配到任何关键词")  # 调试信息
    return "未找到相关信息"


# 4. 封装问答逻辑
def answer_question(question: str):
    try:
        # 获取上下文
        context = find_context(question)
        print(f"问题: {question}")  # 调试信息
        print(f"上下文: {context}")  # 调试信息

        # 使用微调模型进行问答
        result = qa_pipeline(question=question, context=context)
        print(f"模型原始输出: {result}")  # 调试信息

        # 如果置信度过低，返回默认提示
        if result["score"] < 0.1:  # 调整置信度阈值
            return {"answer": "未找到相关信息", "confidence": result["score"]}
        return {"answer": result["answer"], "confidence": result["score"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"问答服务内部错误: {e}")


# 5. 使用 FastAPI 部署问答服务
app = FastAPI()


@app.get("/qa")
def qa_endpoint(question: str):
    return answer_question(question)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)