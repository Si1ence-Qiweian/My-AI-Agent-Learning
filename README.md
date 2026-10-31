# AI Fullstack Learning

从 Python 基础到 AI 全栈应用的 24 周学习记录。

## 当前进度

- [x] Week 1: Python 基础、函数、文件、JSON、Git/GitHub
- [ ] Week 2: 模块、测试、HTTP
- [ ] Week 3: Web 前端
- [ ] Week 4: FastAPI 后端
- [ ] 后续：LLM、RAG、Agent、全栈产品

## 目录结构

```text
.
├── data/          # 本地数据，ledger.json 不提交
├── notes/         # 每日学习笔记
├── week1/         # Python 基础与小型 CLI
├── README.md
└── .gitignore
```

## 环境要求

- Python 3.12+
- Git
- 无需第三方依赖

## 运行

```powershell
cd ai-fullstack

# 最小示例
python week1/hello.py

# 记账本
python week1/ledger.py

# Day 6 边界测试
python week1/test_ledger.py
```

## Week 1 内容

| 文件 | 内容 |
| --- | --- |
| `hello.py` | 第一个 Python 程序 |
| `basics.py` | 变量、条件、循环、FizzBuzz |
| `functions.py` | 函数、参数、返回值 |
| `temperature.py` | 摄氏/华氏转换 CLI |
| `bmi.py` | BMI 计算 CLI |
| `ledger.py` | JSON 持久化记账 CLI |
| `test_ledger.py` | 记账核心函数的边界测试 |

## 数据说明

`data/ledger.json` 是本地数据，已加入 `.gitignore`，不会提交到 GitHub。  
第一次添加账目时，程序会自动创建该文件。

## 已知限制

- 目前只有命令行界面
- 金额使用 `float`，不适合真实财务计算
- 单用户、本地文件存储
- 还没有自动化测试框架，当前使用 `assert`

## 学习计划

完整 24 周计划见 `docs/AI全栈每日学习计划.md`。
