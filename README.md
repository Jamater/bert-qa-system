# 基于 BERT 的智能问答系统

## 项目简介
这是一个基于 Hugging Face 的中文问答系统，使用预训练模型（`uer/roberta-base-chinese-extractive-qa`）和自定义知识库，支持用户提问并返回答案。系统通过 FastAPI 部署为 RESTful 服务。

## 功能特性
- 支持用户输入问题，返回答案片段。
- 通过关键词匹配逻辑和置信度阈值，提升问答准确性。
- 提供简单的 RESTful API，支持高并发访问。

## 技术栈
- Python
- Hugging Face Transformers
- FastAPI
- Uvicorn

## 运行方式

### 1. 克隆项目
```bash
git clone https://github.com/your-username/bert-qa-system.git
