# 测试案例

## 案例 1：BERT是什么
- **请求**：
  ```bash
  curl "http://127.0.0.1:8000/qa?question=BERT是什么"
**响应**
  {
  "answer": "BERT是一种预训练语言模型。",
  "confidence": 0.85
}

## 案例 2：Transformer的架构是什么
curl "http://127.0.0.1:8000/qa?question=Transformer的架构是什么"
**预期响应**：
{
  "answer": "Transformer是一种完全基于注意力机制的模型架构。",
  "confidence": 0.88
}
