# AI 全栈 24 周每日学习计划（非计算机专业版）

> **制定依据**：`C:\Users\zzl19\Documents\README.md`（Agent Learning Hub）中的 Stage 0-8、Project Ladder 和学习原则。
>
> **适用对象**：没有计算机学位、编程基础薄弱，但想独立做出并上线 AI 应用的人。
>
> **默认投入**：每天 2 小时，周一到周六学习，周日 1 小时复盘 + 休息；24 周约 300 小时。
>
> **“全栈”的范围**：这里指 **AI 应用全栈**——前端 + 后端 + 数据库 + 模型 API + RAG/Agent + 评测 + 部署；不包含从零训练大模型、微调和算法研究。
>
> **主线项目**：一个“第二大脑 AI”——从命令行工具开始，逐步长成带 RAG、Agent、登录、数据库、评测和部署的全栈产品。

---

## 0. 先校准预期

24 周、每周约 12 小时，能做到的是：

- 独立开发并部署一个 **可用的 AI 全栈应用**；
- 理解并能改造一个 **Agent harness**（智能体运行框架）；
- 会做 RAG、工具调用、MCP、简单多 Agent；
- 有评测、trace、权限、成本和安全意识；
- 有 1 个主项目 + 2-3 个可展示的小项目。

24 周还做不到：

- 算法研究、模型训练、微调；
- 大规模分布式系统；
- 高级前端/后端工程师水平；
- 一毕业就进大厂做核心基础架构。

这不是“速成”，而是把你送到 **能开始做真实项目、能继续自学** 的位置。后续还需要 6-12 个月的项目积累。

**如果每天只有 1 小时**：把周期拉长到 40-48 周，不要压缩内容。  
**如果每天有 3-4 小时**：可以缩短到 16-18 周，但不要跳过评测、安全和部署。

---

## 1. 24 周后你应该具备的能力

| 能力层 | 具体能力 | 主要周次 |
| --- | --- | --- |
| 编程地基 | Python、Git、命令行、HTTP、JSON、SQL、测试 | W1-W4 |
| 后端 | FastAPI、数据校验、数据库、登录、文件上传、API 设计 | W4、W14-W16 |
| 前端 | HTML/CSS/JS、React/Next.js、流式 UI、文件上传 | W3、W13 |
| LLM 应用 | API 调用、提示词、结构化输出、流式、成本控制 | W5-W6 |
| Agent | 工具调用、循环、步数/超时、trace、harness | W7-W8、W17-W19 |
| RAG/记忆 | 切分、embedding、检索、引用、混合检索、长期记忆 | W9-W12 |
| 多 Agent/Skills | supervisor、角色边界、SKILL.md、MCP、A2A/ACP 概念 | W19-W21 |
| 浏览器 Agent | Playwright、观察-动作循环、失败恢复、安全边界 | W22 |
| 工程化 | Docker、CI、日志、监控、评测、回归测试 | W15、W23 |
| 产品化 | 用户、范围、README、演示、部署、成本 | W16、W24 |

---

## 2. 固定技术栈：少换工具，多写代码

| 用途 | 选择 | 说明 |
| --- | --- | --- |
| 语言 | Python 3.12 + TypeScript | Python 做 AI/后端，TS 做前端 |
| 包管理 | `uv`（或 venv + pip） | 学会锁定依赖即可 |
| 后端 | FastAPI + Pydantic | 类型清晰、自带 `/docs`，适合初学者 |
| 前端 | Next.js + Tailwind CSS | 一套框架覆盖页面、路由和部署 |
| 数据库 | SQLite → PostgreSQL | 先学 SQL，再上生产数据库 |
| 向量检索 | 先手写余弦相似度 → Chroma/sqlite-vec → pgvector | 先理解原理，再换工具 |
| 模型 API | OpenAI / Anthropic / Gemini 任选一个；备用 Ollama | 不要同时学四家 SDK |
| RAG 框架 | 先手写，再用 LlamaIndex | 避免只会调包 |
| Agent | 先裸 loop，再用 LangGraph | README 明确不建议重押老式 role-play 框架 |
| Harness 学习 | Claude Code 文档 + `learn-claude-code` | 学工具、权限、session、压缩、trace |
| 工具协议 | MCP | 先跑官方 server，再写自己的 |
| 浏览器 | Playwright → browser-use | 先会定位/点击，再上框架 |
| 部署 | Vercel（前端）+ Fly.io/Render/Railway（后端）+ Neon/Supabase（数据库） | 先能上线，再谈优化 |
| 观测 | Langfuse 或 LangSmith（二选一） | 没有 trace 的 Agent 很难调 |
| CI | GitHub Actions + Docker | 每次 push 自动跑测试 |

**暂缓学习**：CrewAI、AutoGen、微调、Kubernetes、复杂多 Agent 框架。不是它们没用，而是现在学容易只学到“模板 API”，做不出可靠系统。

---

## 3. 每天怎么学：固定 2 小时模板

| 时间 | 动作 | 目的 |
| --- | --- | --- |
| 10 分钟 | 回忆昨天：不看笔记，写下 3 个要点 | 防止“学过就忘” |
| 70 分钟 | 动手：写代码、跑实验、修 bug | 这是主菜 |
| 30 分钟 | 读官方文档，只读当前任务相关部分 | 建立准确概念 |
| 10 分钟 | 写日志：今天做了什么、卡在哪、明天第一步 | 让第二天能无缝开始 |

**每周节奏**：

- 周一：学新概念，跟着做；
- 周二：改一个变量/换一个输入，做变体；
- 周三：不看教程，独立重做；
- 周四：加错误处理、测试、边界情况；
- 周五：做成一个小交付；
- 周六：整合进主线项目，写 README；
- 周日：1 小时复盘 + 休息，不学新内容。

**每天必须留下痕迹**：一次 commit、一段日志、或一个可运行的结果。不要“只看视频”。

---

## 4. 24 周总览

| 周 | 阶段 | 主题 | 本周交付 |
| --- | --- | --- | --- |
| W1 | 编程地基 | 环境、Python 基础 | CLI 记账器 |
| W2 | 编程地基 | 模块、测试、HTTP | CLI 学习笔记 |
| W3 | Web 地基 | HTML/CSS/JS、浏览器 | 静态聊天 UI |
| W4 | Web 地基 | FastAPI、SQLite | 笔记 CRUD API |
| W5 | LLM 应用 | 模型 API、流式、JSON | CLI 聊天 |
| W6 | LLM 应用 | 提示词、结构化抽取 | 批量抽取工具 + 小评测 |
| W7 | Agent 入门 | 工具调用、最小循环 | 50-150 行最小 Agent |
| W8 | Agent 入门 | 加固、日志、打包 | Calculator Agent |
| W9 | RAG | embedding、切分、向量检索 | 语义搜索 CLI |
| W10 | RAG | PDF 解析、引用、问答 | PDF QA Agent |
| W11 | RAG | 混合检索、评测、记忆 | 改进版 RAG + 记忆 |
| W12 | RAG | 搜索、抓取、报告 | Web Research Agent |
| W13 | 全栈 | Next.js、流式 UI | Web 聊天界面 |
| W14 | 全栈 | Postgres、登录、持久化 | 多用户应用 |
| W15 | 全栈 | 流式、限流、CI、Docker | 可部署的后端 |
| W16 | 全栈 | 部署、监控、用户测试 | 上线 v1.0 |
| W17 | Harness | 拆解 Claude Code 类系统 | Harness 架构笔记 |
| W18 | Harness | 自建 nano coding agent | 可调试的 coding agent |
| W19 | Harness | MCP、裸 loop 对比 | MCP server + 对比报告 |
| W20 | 多 Agent | supervisor、角色边界 | research→write→review |
| W21 | Skills | SKILL.md、脚本、smoke test | 可复用 Skill Pack |
| W22 | 浏览器 | Playwright、安全边界 | 公开网页研究 Agent |
| W23 | 评测 | eval、trace、注入防护 | 20 题评测报告 |
| W24 | 发布 | Capstone、README、演示 | 公开可用的作品 |

---

## 5. 每日计划

> 每天默认 2 小时。`D1-D6` 是周一到周六；周日只复盘和休息。

### 第 1 阶段｜W1-W4：编程与 Web 地基

> 目标：不学完整的计算机科学课程，只补“能做出 AI 应用”的最小地基。

#### W1｜环境与 Python 基础

**本周交付**：一个能增删查、重启不丢数据的 CLI 记账器。  
**过关标准**：不查教程，能独立写出“输入→处理→输出”的 30 行程序。

- [ ] **D1（2h）环境与第一次运行**：安装 Python 3.12、VS Code、Git；练 `cd/ls/mkdir`；建 `ai-fullstack` 仓库；跑 `hello.py`。产出：环境截图 + 第一次 commit。
- [ ] **D2（2h）变量、类型、条件、循环**：做 10 道小题；写 FizzBuzz；故意制造 3 种报错并读懂。产出：`week1/basics.py`。
- [ ] **D3（2h）函数与参数**：写温度转换、BMI 计算两个 CLI；学会返回值、默认参数、作用域。产出：2 个小脚本。
- [ ] **D4（2h）列表与字典**：用 list/dict 写“内存版记账”，支持添加、删除、查看、合计。产出：可运行 CLI。
- [ ] **D5（2h）文件、JSON、异常**：把记账数据写入 JSON；处理文件不存在、格式错误；重启后数据还在。产出：持久化版本。
- [ ] **D6（2h）整理与交付**：拆目录、写 README、补 3 个边界测试；`git push`。产出：可展示仓库。
- [ ] **周日（1h）**：复盘 + 读 Anthropic《Building effective agents》前半；用自己的话写“workflow 和 agent 的区别”。

#### W2｜模块、测试、HTTP

**本周交付**：CLI 学习笔记，支持增删改查、搜索、导出。  
**过关标准**：能解释“为什么要把代码拆成多个文件”，并能写 5 个 pytest 测试。

- [ ] **D1（2h）推导式、排序、集合**：统计一段文本的词频 Top 20；用 `sorted` 和 `Counter` 各写一遍。
- [ ] **D2（2h）虚拟环境与模块**：建 venv，装 `requests`；把记账器拆成 `cli.py / storage.py / models.py`；写 `requirements.txt`。
- [ ] **D3（2h）pytest 入门**：给存储层写 5 个测试；故意改坏一处再修复；理解 arrange-act-assert。
- [ ] **D4（2h）HTTP 与 JSON**：学方法、状态码、请求头；用 `requests` 调 GitHub API，格式化输出仓库信息。
- [ ] **D5（2h）类型标注与日志**：给函数加 type hints；加 `logging`；给 CLI 加 `--help` 和错误提示。
- [ ] **D6（2h）完成 CLI 学习笔记**：支持增删改查、按关键词搜索、导出 Markdown；写 README 和使用示例。
- [ ] **周日（1h）**：画一张“CLI 请求 API 再返回”的流程图；读 OpenAI《A practical guide to building agents》前半。

#### W3｜Web 前端基础

**本周交付**：一个响应式静态聊天 UI，部署到 GitHub Pages 或 Netlify。  
**过关标准**：能看懂浏览器 Network 面板，能说出 200/400/404/500 的含义。

- [ ] **D1（2h）HTML/CSS**：语义标签、Flex/Grid；做个人介绍页；用 DevTools 改样式。
- [ ] **D2（2h）JavaScript 基础**：变量、函数、数组、DOM 事件；做 Todo List，用 localStorage 保存。
- [ ] **D3（2h）fetch 与 async/await**：调用一个公开 API，渲染列表；处理 loading、空结果、请求失败。
- [ ] **D4（2h）浏览器与 HTTP**：看 Network/Console；理解 CORS、JSON、状态码；写 10 条排查笔记。
- [ ] **D5（2h）聊天 UI**：消息列表、输入框、发送按钮、响应式布局；先用假数据。
- [ ] **D6（2h）部署与自测**：部署静态站点；加“假流式输出”和空状态；写 10 条自测清单。
- [ ] **周日（1h）**：用 5 句话解释“浏览器到服务器发生了什么”；补最弱的一天。

#### W4｜FastAPI 与数据库

**本周交付**：笔记 CRUD API，带 SQLite 持久化、校验、测试和文档。  
**过关标准**：2 小时内从零写出一个 3 接口的 CRUD API。

- [ ] **D1（2h）FastAPI 起步**：`/health`、`GET /notes`、`POST /notes`；打开 `/docs` 调接口。
- [ ] **D2（2h）Pydantic 模型**：请求/响应模型、字段校验、错误响应；完成内存 CRUD。
- [ ] **D3（2h）SQLite 与 SQL**：建表、增删改查、参数化查询防注入；把笔记持久化。
- [ ] **D4（2h）配置与测试**：环境变量、依赖注入；用 `TestClient` 写 6 个接口测试。
- [ ] **D5（2h）完善 API**：分页、搜索、删除；用 curl 跑通；导出 OpenAPI 截图。
- [ ] **D6（2h）交付**：写 API README（启动、示例、错误码）；做 W4 通关任务。
- [ ] **周日（2h）检查点**：不看教程，从零写一个 3 接口 CRUD API；写复盘。

---

### 第 2 阶段｜W5-W8：LLM 应用与 Agent 入门

> 目标：把“会调模型”升级为“会做可靠的小 Agent”。对应 README 的 Stage 0-1。

#### W5｜模型 API 与流式输出

**本周交付**：一个带历史、流式、成本统计的 CLI 聊天。  
**过关标准**：能解释 token、上下文窗口、temperature、system prompt。

- [ ] **D1（2h）跑通模型 API**：选 OpenAI/Anthropic/Gemini 之一（或兼容接口/Ollama）；key 放 `.env`；完成一次对话。
- [ ] **D2（2h）消息角色与流式**：理解 system/user/assistant；实现流式打印；对比不同 temperature。
- [ ] **D3（2h）结构化输出**：让模型输出 JSON；用 Pydantic 校验；失败时自动重试一次。
- [ ] **D4（2h）工程化客户端**：超时、重试、限流、成本记录；封装 `llm_client.py`。
- [ ] **D5（2h）CLI 聊天**：历史、清空、退出、保存 transcript；超长时裁剪历史。
- [ ] **D6（2h）笔记与 review**：写“LLM API 最小知识”；检查密钥没有进 Git；commit。
- [ ] **周日（1h）**：重读《Building effective agents》，这次重点看“什么时候不该用 agent”。

#### W6｜提示词与结构化抽取

**本周交付**：批量职位描述抽取工具 + 20 条小评测集。  
**过关标准**：能说清“提示词版本 A 为什么比 B 好”，并用数据证明。

- [ ] **D1（2h）提示词结构**：角色、任务、输入、约束、输出格式；写 3 个版本对比。
- [ ] **D2（2h）few-shot 与分隔符**：把一段职位描述抽成 JSON（公司、岗位、技能、年限、地点）。
- [ ] **D3（2h）健壮性**：缺字段、格式错、超长输入；加 JSON 修复和重试。
- [ ] **D4（2h）批量处理**：抽 10 条文本，输出 CSV；记录耗时和成本。
- [ ] **D5（2h）小评测**：建 20 条“输入→期望字段”的测试；算字段准确率；改 prompt。
- [ ] **D6（2h）版本记录**：保存 prompt v1/v2/v3 和评测结果；选最佳版本写 README。
- [ ] **周日（1h）**：读 README 中 OpenAI Function Calling 文档的前半；预习“工具”概念。

#### W7｜工具调用与最小 Agent（README Stage 1）

**本周交付**：50-150 行的最小 Agent，能选工具、执行、把结果喂回模型。  
**过关标准**：能画出 observe → think → act → observe 的循环，并解释每一步。

- [ ] **D1（2h）工具调用原理**：定义 calculator 的 JSON Schema；跑通一次 tool call。
- [ ] **D2（2h）实现循环**：模型请求工具 → 本地执行 → 结果回填 → 继续，直到给出最终答案。
- [ ] **D3（2h）增加工具**：search、read_file；严格参数校验；工具异常返回结构化错误。
- [ ] **D4（2h）加护栏**：最大步数、超时、重复调用检测、单次任务预算。
- [ ] **D5（2h）完成最小 Agent**：CLI 输入任务；支持 3 个工具；输出最终答案和步骤日志。
- [ ] **D6（2h）Trace 与对比**：记录 3 次完整 trace；对比“无工具模型”的差异；写 README。
- [ ] **周日（1h）**：读 Claude Tool Use 或 Gemini Function Calling 选一；勾选 README Stage 1 清单。

#### W8｜Agent 加固与 Calculator Agent

**本周交付**：可安装、可演示、有失败记录的 Calculator Agent（Project Ladder 1）。  
**过关标准**：注入坏 JSON、工具异常、超时，程序不会崩，且日志能定位原因。

- [ ] **D1（2h）重构**：拆成 `loop / tools / config / logger`；消息类型化。
- [ ] **D2（2h）可靠性**：重试退避、取消、成本上限；补单元测试。
- [ ] **D3（2h）可观测**：CLI 美化；JSONL 日志；每一步可回放。
- [ ] **D4（2h）故障注入**：坏 JSON、工具抛错、超时、空结果；逐个修复。
- [ ] **D5（2h）打包交付**：README + 3 个示例 + 架构图；打 tag `v0.1`。
- [ ] **D6（2h）复盘**：写“为什么需要最大步数和超时”；做 W8 检查点。
- [ ] **周日（2h）检查点**：向一个非技术朋友演示，并让他复述这个 Agent 能做什么、不能做什么。

---

### 第 3 阶段｜W9-W12：RAG、记忆与研究 Agent

> 目标：让模型“基于资料回答”，并给出可核查的引用。对应 README Stage 2。

#### W9｜Embedding 与向量检索

**本周交付**：对自己笔记的语义搜索 CLI。  
**过关标准**：能解释 chunk、embedding、余弦相似度、top-k。

- [ ] **D1（2h）相似度**：调 embedding API，对 10 句话做相似度排序；手写余弦相似度。
- [ ] **D2（2h）切分策略**：固定长度、按标题、带重叠；做 3 组对比，记录检索差异。
- [ ] **D3（2h）向量库**：用 Chroma 或 sqlite-vec；导入自己的 Markdown 笔记。
- [ ] **D4（2h）检索细节**：metadata、过滤、top-k；打印命中的片段并人工判断。
- [ ] **D5（2h）语义搜索 CLI**：输入问题，返回最相关的 5 个片段和来源路径。
- [ ] **D6（2h）小评测**：20 条查询测 hit@3；记录失败案例和原因。
- [ ] **周日（1h）**：读 LlamaIndex 或 LangChain 的 RAG 文档，只读 retrieval 部分。

#### W10｜PDF 问答与引用

**本周交付**：PDF QA Agent，回答带页码引用，没有依据时会说“不知道”（Project Ladder 3）。  
**过关标准**：10 个测试问题中，引用都能对应到原文；无依据问题不硬编。

- [ ] **D1（2h）RAG 提示词**：只基于资料回答、引用编号、无依据就说不知道；写 3 版对比。
- [ ] **D2（2h）PDF 解析**：用 pypdf 提取文本；清洗页眉页脚；保留页码 metadata。
- [ ] **D3（2h）问答链路**：检索 → 拼接上下文 → 生成；控制上下文长度。
- [ ] **D4（2h）引用校验**：答案中的编号必须存在；空结果、低相似度要有降级策略。
- [ ] **D5（2h）PDF QA CLI**：用 10 个问题测试；记录错误。
- [ ] **D6（2h）失败分析**：区分“检索错、切分错、模型编造”；写 README。
- [ ] **周日（1h）**：看 RAGFlow 或 AnythingLLM 的 README，画出它们的 ingestion 流程。

#### W11｜检索质量与记忆

**本周交付**：改进版 RAG + 简单长期记忆，并有前后评测表。  
**过关标准**：能用数据说明改动有效，而不是“感觉好多了”。

- [ ] **D1（2h）混合检索**：BM25 + 向量，或加 rerank；对比 top-k 结果。
- [ ] **D2（2h）评测集**：20 题，包含问题、标准答案、正确来源；写自动跑分脚本。
- [ ] **D3（2h）错误分析**：按检索/切分/提示/模型分类；改一处，再跑一遍。
- [ ] **D4（2h）记忆分层**：短期上下文、会话摘要、长期事实；用 SQLite 实现。
- [ ] **D5（2h）接入记忆**：记住用户偏好；加“忘记我”删除；写隐私说明。
- [ ] **D6（2h）前后对比**：评测表 + 1 页“RAG 什么时候不该用”。
- [ ] **周日（1h）**：看 mem0 或 Letta 的 README，记 3 个记忆设计要点。

#### W12｜Web Research Agent

**本周交付**：输入主题，自动搜索、筛选、总结并输出引用链接的研究 Agent（Project Ladder 2）。  
**过关标准**：报告中的每条关键结论都有来源；能识别并忽略网页中的恶意指令。

- [ ] **D1（2h）搜索 API**：接 Tavily/Bing/SerpAPI（没有就先用 mock）；做查询改写。
- [ ] **D2（2h）抓取正文**：去导航/广告；记录 URL、标题、抓取时间。
- [ ] **D3（2h）多轮搜索**：去重、来源可信度、限制轮数；避免无限搜索。
- [ ] **D4（2h）报告生成**：带引用；把网页内容当“数据”而不是“指令”，防 prompt injection。
- [ ] **D5（2h）研究 Agent CLI**：跑 3 个主题；保存 Markdown 报告。
- [ ] **D6（2h）对比与交付**：和人工搜索对比；README + demo；勾选 Stage 2 清单。
- [ ] **周日（2h）检查点**：用 20 题评测表检查 RAG，并演示研究 Agent 的引用。

---

### 第 4 阶段｜W13-W16：AI 全栈产品

> 目标：把前面的能力做成一个别人能注册、能使用、能上线的 Web 产品。

#### W13｜Next.js 前端

**本周交付**：连接后端的 Web 聊天界面，支持流式输出和文件上传。  
**过关标准**：能在本地完成“输入问题→看到流式回答→上传文档”的完整流程。

- [ ] **D1（2h）初始化**：Next.js + TypeScript + Tailwind；页面、布局、组件。
- [ ] **D2（2h）聊天 UI**：消息列表、输入框、发送/停止、loading、错误提示。
- [ ] **D3（2h）流式对接**：用 SSE 接 FastAPI `/chat`；处理中断和重连。
- [ ] **D4（2h）文件上传**：进度、类型/大小限制、失败重试；Markdown 渲染。
- [ ] **D5（2h）接 RAG**：会话切换、历史消息、移动端适配。
- [ ] **D6（2h）部署预览**：Vercel 预览；写前端 README 和环境变量说明。
- [ ] **周日（1h）**：读 Next.js App Router 基础，只学当前用到的部分。

#### W14｜数据库、登录与持久化

**本周交付**：多用户应用，能注册、登录、保存会话和文档。  
**过关标准**：用户 A 无法读取用户 B 的会话；刷新页面历史还在。

- [ ] **D1（2h）Postgres**：Docker 或 Supabase；设计 users/conversations/messages/documents 表。
- [ ] **D2（2h）ORM 与迁移**：SQLAlchemy/SQLModel + Alembic；写 repository。
- [ ] **D3（2h）登录**：Supabase Auth 或 JWT；保护接口；处理登出/过期。
- [ ] **D4（2h）持久化**：保存消息；会话列表；所有权校验，防 IDOR。
- [ ] **D5（2h）文件存储**：S3/R2/本地；元数据、大小/类型限制、清理策略。
- [ ] **D6（2h）端到端测试**：注册→上传→问答→历史；做安全自查。
- [ ] **周日（1h）**：读 OWASP Top 10 前 3 项，对照自己的接口。

#### W15｜生产化后端

**本周交付**：可部署的后端，带流式、限流、日志、测试和 Docker Compose。  
**过关标准**：`docker compose up` 能一键起；CI 能自动跑测试。

- [ ] **D1（2h）流式与长任务**：取消、超时；长文档解析放后台任务。
- [ ] **D2（2h）稳定性**：限流、成本上限、重试、幂等；统一错误码。
- [ ] **D3（2h）可观测**：请求 ID、结构化日志、trace（Langfuse/LangSmith/OpenTelemetry 选一）。
- [ ] **D4（2h）测试与 CI**：单测 + 集成测试；GitHub Actions 自动跑。
- [ ] **D5（2h）Docker**：Compose 起后端/数据库；健康检查；`.env.example`。
- [ ] **D6（2h）压测与 runbook**：简单压测；修最慢一处；写故障处理清单。
- [ ] **周日（1h）**：读所选部署平台的“生产建议”，列 5 条待办。

#### W16｜部署 v1.0

**本周交付**：公网可访问的“第二大脑 AI”v1.0。  
**过关标准**：陌生人按 README 能在 10 分钟内跑起来；能完成一次真实问答。

- [ ] **D1（2h）部署后端**：Fly.io/Render/Railway；托管 Postgres；配置密钥。
- [ ] **D2（2h）部署前端**：Vercel；CORS、环境变量、HTTPS、域名（可选）。
- [ ] **D3（2h）监控**：日志、错误告警、成本面板；设置预算上限。
- [ ] **D4（2h）安全检查**：密钥、权限、注入、上传；修高危项。
- [ ] **D5（2h）用户测试**：找 3 个真实用户试用；记录卡点和抱怨。
- [ ] **D6（2h）修 top 3**：README、架构图、3 分钟演示视频；打 tag `v1.0`。
- [ ] **周日（2h）检查点**：让一个陌生人从零部署；记录他卡住的每一步。

---

### 第 5 阶段｜W17-W19：Harness 与 Coding Agent

> 目标：从“会写 Agent”升级到“理解 Agent 的能力从哪里来”。对应 README Stage 3，并为 Stage 5 的 MCP 打基础。

#### W17｜拆解一个现代 Agent Harness

**本周交付**：一页 Harness 架构笔记 + 一个自定义工具。  
**过关标准**：能指出 agent loop、tool registry、permission gate、session store、context compaction 分别在哪个文件/模块。

- [ ] **D1（2h）选型与跑通**：选 Claude Code 或 `learn-claude-code`；读 overview；跑最小示例。
- [ ] **D2（2h）目录结构**：画目录树；找 agent loop 和 tool registry。
- [ ] **D3（2h）关键机制**：找 permission gate、session store、context compaction。
- [ ] **D4（2h）加工具**：给 Harness 加一个自定义工具，跑通。
- [ ] **D5（2h）看 trace**：完整跑一次任务，逐步标注“为什么发生”。
- [ ] **D6（2h）写笔记**：对比自己的 W7-W8 Agent，列出 5 个差距。
- [ ] **周日（1h）**：读 Claude Code 文档的 hooks/subagents/MCP 各 1 节。

#### W18｜自建 Nano Coding Agent

**本周交付**：可调试的 coding agent，能读文件、改文件、跑测试，并有权限确认（Project Ladder 4/6）。  
**过关标准**：在玩具仓库完成 3 个小任务，失败有日志、有回放。

- [ ] **D1（2h）设计**：shell、read_file、write_file、patch、run_tests 工具；限定工作目录。
- [ ] **D2（2h）实现循环**：工具 schema；写/删前人工确认；危险命令拦截。
- [ ] **D3（2h）上下文管理**：session 持久化、上下文压缩、token 预算。
- [ ] **D4（2h）代码审查**：展示 diff；跑测试；失败结果回传；做一个小型 review 任务。
- [ ] **D5（2h）实战**：玩具仓库跑 3 个任务（改 bug、加功能、补测试）；记录失败。
- [ ] **D6（2h）交付**：README + 失败日志 + 架构图；对照 Project Ladder 6。
- [ ] **周日（1h）**：读 `learn-claude-code` 对应章节，只补没做出来的部分。

#### W19｜MCP 与“裸 loop vs Harness”对比

**本周交付**：一个 MCP server（暴露笔记搜索）+ 一份对比报告。  
**过关标准**：能说清 MCP 的 host/client/server 关系，以及什么时候值得用 Harness。

- [ ] **D1（2h）MCP 概念**：读官方架构；跑官方 filesystem server。
- [ ] **D2（2h）写 MCP server**：暴露 `search_notes` 工具；参数校验。
- [ ] **D3（2h）接入**：接到 MCP 客户端或 Claude Code；加权限白名单。
- [ ] **D4（2h）同题对比**：同一任务分别用裸 loop 和 Harness；记录步骤、成本、成功率。
- [ ] **D5（2h）分析 trace**：找出 Harness 的优势和额外开销；改一处再测。
- [ ] **D6（2h）写报告**：对比表 + 适用场景；勾选 Stage 3/5 清单。
- [ ] **周日（1h）**：画“host-client-server”图；读 A2A/ACP 的概念页（只读概念）。

---

### 第 6 阶段｜W20-W22：多 Agent、Skills 与浏览器

> 目标：理解“协调”和“能力封装”，而不是收集框架。对应 README Stage 4-6。

#### W20｜多 Agent 是协调，不是魔法

**本周交付**：research → write → review → revise 的小型多 Agent 系统（Project Ladder 9）。  
**过关标准**：能用数据说明它比单 Agent 好在哪里、差在哪里。

- [ ] **D1（2h）角色与边界**：planner/executor/reviewer；什么时候单 Agent 更好。
- [ ] **D2（2h）协议设计**：每个角色的输入/输出 schema、停止条件、预算。
- [ ] **D3（2h）实现**：supervisor 或 LangGraph；先串行，再考虑并行。
- [ ] **D4（2h）处理失控**：循环、争论、任务漂移、上下文膨胀；加最大轮次。
- [ ] **D5（2h）对比实验**：5 个任务，单 Agent vs 多 Agent；记录质量/成本/延迟。
- [ ] **D6（2h）决策文档**：评测表 + “什么时候不该用多 Agent”。
- [ ] **周日（1h）**：读 Claude Code Subagents 文档，记 3 条适用边界。

#### W21｜Skills 与能力封装

**本周交付**：一个可复用 Skill Pack，含 `SKILL.md`、脚本/模板、smoke test（Project Ladder 8）。  
**过关标准**：有/无 skill 的 5 题对比中，成功率或稳定性有可量化提升。

- [ ] **D1（2h）概念区分**：Skill vs Tool vs Prompt vs MCP；读 Claude Code Skills 文档。
- [ ] **D2（2h）写 SKILL.md**：name、description、何时使用、步骤、验收标准。
- [ ] **D3（2h）加资源**：脚本/模板；说明何时加载；权限和安全边界。
- [ ] **D4（2h）smoke test**：5 个任务，有/无 skill 各跑一遍；记录成功率。
- [ ] **D5（2h）协议视野**：A2A/ACP 解决什么问题；是否需要，不急着实现。
- [ ] **D6（2h）打包**：独立 repo + README + 示例；对照 Stage 5 清单。
- [ ] **周日（1h）**：读 OpenClaw Skills 文档，对比文件结构和加载方式。

#### W22｜浏览器 Agent

**本周交付**：只操作公开网页的信息提取 Agent，带日志、截图和安全限制（Project Ladder 5）。  
**过关标准**：页面改版/超时/弹窗时能恢复或优雅失败；绝不登录敏感账号。

- [ ] **D1（2h）Playwright 基础**：打开页面、定位元素、点击、截图、等待。
- [ ] **D2（2h）观察-动作循环**：DOM 或截图；限制步数；记录每步动作。
- [ ] **D3（2h）安全边界**：只允许公开站点；不登录、不支付、不发内容；危险动作人工确认。
- [ ] **D4（2h）失败恢复**：超时、选择器变化、弹窗、加载失败；加重试和降级。
- [ ] **D5（2h）实战**：3 个公开网页任务（提取价格/新闻/文档目录）；保存结果。
- [ ] **D6（2h）交付**：截图、动作日志、README；勾选 Stage 6 清单。
- [ ] **周日（1h）**：读 browser-use README，只学 action space 和错误处理。

---

### 第 7 阶段｜W23-W24：评测、安全与发布

> 目标：把“能跑的 demo”变成“可解释、可回归、可上线”的作品。对应 README Stage 7-8。

#### W23｜评测、可观测与安全

**本周交付**：20 题评测报告 + 失败分类 + 安全防护清单。  
**过关标准**：能说清每个失败发生在 prompt、检索、工具、模型还是状态管理。

- [ ] **D1（2h）评测设计**：20 个任务，覆盖 RAG/Research/Browser；写期望结果。
- [ ] **D2（2h）Runner**：记录成功率、工具调用次数、成本、延迟。
- [ ] **D3（2h）跑测与归因**：看 trace，按失败类型分类；找 top 3 问题。
- [ ] **D4（2h）攻击测试**：恶意网页/文档/工具参数；测试 prompt injection 和数据外泄。
- [ ] **D5（2h）防护**：危险工具人工确认；输入隔离；回归测试接 CI。
- [ ] **D6（2h）报告**：评测表 + 修复 top 2；勾选 Stage 7 清单。
- [ ] **周日（1h）**：读 AgentBench/SWE-bench 摘要，只学指标设计。

#### W24｜Capstone 发布

**本周交付**：一个公开可访问、README 完整、有演示视频的 AI 全栈作品（Stage 8）。  
**过关标准**：陌生人能复现；你能讲清用户、成功标准、取舍和限制。

- [ ] **D1（2h）定义 Capstone**：用户、问题、成功标准；砍到 2 周能完成的范围。
- [ ] **D2（2h）打磨核心链路**：修阻塞 bug；补空状态、错误提示、加载状态。
- [ ] **D3（2h）生产部署**：备份、回滚、成本上限、健康检查。
- [ ] **D4（2h）文档**：README（运行/配置/扩展/限制）+ 架构图 + 数据流图。
- [ ] **D5（2h）演示**：3 个用户测试；录 3 分钟视频；写一篇作品集文章。
- [ ] **D6（2h）复盘**：tag `v1.0`；写“如果重做会改什么”；列下一个 90 天计划。
- [ ] **周日（2h）最终检查点**：按 README 从零部署一次；准备 5 分钟面试式讲解。

---

## 6. 阶段检查点：怎么知道自己过关了

| 检查点 | 任务 | 过关线 |
| --- | --- | --- |
| W4 | 不看教程写 CRUD API | 2 小时内完成，接口能跑，测试通过 |
| W8 | 演示 Calculator Agent | 能解释循环、工具、最大步数、超时、trace |
| W12 | RAG + Research Agent | 20 题评测有记录；报告有可核查引用 |
| W16 | 上线 v1.0 | 陌生人能注册使用；README 能复现 |
| W20 | 多 Agent 对比 | 有单/多 Agent 的质量、成本、延迟数据 |
| W24 | Capstone | 公网可访问；3 分钟 demo；评测表完整 |

**没过怎么办**：不要开新坑。用下一周的周日 + 3 个工作日补课；补完再前进。连续两周没过，就把整个计划拉长 2 周。

---

## 7. 每周复盘模板（周日 1 小时）

复制到你的笔记里，每周填一次：

```markdown
## 第 __ 周复盘

1. 本周交付链接：
2. 我用自己话解释的 3 个概念：
   -
   -
   -
3. 两个失败与修复：
   -
   -
4. 一个仍然模糊的问题：
5. 本周时间统计：__ 小时；API 成本：__ 元
6. 下周要改的一个习惯：
7. 本周过关：是 / 否；若否，补课安排：
```

---

## 8. 资源怎么用：只读当前需要的

> README 里资源很多，不要从头刷到尾。下面按阶段给“必读”和“暂缓”。

| 阶段 | 必读 | 选读 | 现在别碰 |
| --- | --- | --- | --- |
| W1-W4 | Python 官方教程（中文）、MDN Web Docs、FastAPI 官方教程 | 《Automate the Boring Stuff》 | 算法导论、编译原理 |
| W5-W8 | Anthropic《Building effective agents》、OpenAI《A practical guide to building agents》、Function Calling 文档 | Lilian Weng《LLM Powered Autonomous Agents》 | CrewAI/AutoGen 全家桶 |
| W9-W12 | LlamaIndex/LangChain 的 RAG 文档、MCP 官方文档、GPT Researcher/Open Deep Research 的 README | RAGFlow、mem0、Letta | 自己训 embedding 模型 |
| W13-W16 | Next.js 文档、FastAPI 部署文档、Postgres 教程、OWASP Top 10 | Vercel/Fly.io 示例 | Kubernetes、微服务 |
| W17-W19 | Claude Code 文档、`learn-claude-code`、`hello-agents`、MCP 文档 | 《Dive into Claude Code》论文 | 逐行读完整源码 |
| W20-W22 | Claude Code Subagents、A2A/ACP 概念页、Playwright 文档、browser-use README | UI-TARS、WebArena | OSWorld 全量复现 |
| W23-W24 | OpenAI Evals、LangSmith/Langfuse 文档、AgentBench/SWE-bench 摘要 | τ-bench、GAIA | 自己造 benchmark |

**论文阅读法**：先读摘要、图和结论，回答“它解决什么问题、怎么评估、有什么限制”。非计算机专业不需要逐行推导公式。

### 关键链接（从 README 中选取，够用即可）

| 用途 | 链接 |
| --- | --- |
| Agent 设计入门 | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) |
| Agent 落地指南 | [OpenAI: A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) |
| 工具调用 | [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling) · [Claude Tool Use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) |
| RAG/Agent 框架 | [LlamaIndex Agents](https://docs.llamaindex.ai/en/stable/use_cases/agents/) · [LangChain Docs](https://docs.langchain.com/) |
| MCP | [Model Context Protocol](https://modelcontextprotocol.io/) |
| Harness 拆解 | [Claude Code Docs](https://code.claude.com/docs/en/overview) · [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) |
| 中文系统教程 | [hello-agents](https://github.com/datawhalechina/hello-agents) |
| 浏览器 Agent | [Playwright](https://playwright.dev/) · [browser-use](https://github.com/browser-use/browser-use) |
| 评测与观测 | [OpenAI Evals](https://platform.openai.com/docs/guides/evals) · [LangSmith](https://docs.smith.langchain.com/) |
| 研究 Agent 参考 | [GPT Researcher](https://github.com/assafelovic/gpt-researcher) · [Open Deep Research](https://github.com/langchain-ai/open_deep_research) |

---

## 9. README 与课程的对应关系

| README 内容 | 本计划位置 |
| --- | --- |
| Stage 0：理解 Agent | W1-W2 周日阅读 + W5 重读 |
| Stage 1：最小 Agent Loop | W7-W8 |
| Stage 2：Tool/RAG/Memory | W9-W12 |
| Stage 3：研究一个 Harness | W17-W19 |
| Stage 4：多 Agent 协调 | W20 |
| Stage 5：Skills/协议 | W19（MCP）+ W21（Skills） |
| Stage 6：Browser/Computer Use | W22 |
| Stage 7：评测/可观测/安全 | W23（并贯穿每周） |
| Stage 8：发布真实 Agent | W16 + W24 |
| Project Ladder 1 | W8 Calculator Agent |
| Project Ladder 2 | W12 Web Research Agent |
| Project Ladder 3 | W10 PDF QA Agent |
| Project Ladder 4/6 | W18 Coding Review / Nano Agent |
| Project Ladder 5 | W22 Browser Agent |
| Project Ladder 8 | W21 Skill Pack |
| Project Ladder 9 | W20 Multi-Agent Writer |
| Project Ladder 7/10/11 | 毕业后 90 天扩展：Gateway、Personal Agent、Production Harness |

---

## 10. 常见坑：避开就能超过大多数人

1. **先学框架，不学 API**：只会写 `agent.run()`，出了错不知道是模型、工具还是状态。
2. **同时开三个项目**：最后没有一个能跑。24 周只做一条主线。
3. **只看视频不写代码**：看的时候“懂了”，关掉视频写不出来。
4. **过早多 Agent**：单 Agent 都没调稳，多 Agent 只会放大混乱。
5. **没有评测**：demo 好看，但不知道什么时候会坏。
6. **把 API key 提交到 GitHub**：一晚上可能被盗刷。
7. **忽略成本和超时**：一个循环 bug 就能烧掉很多钱。
8. **Capstone 贪大**：两周做不完的功能，第一版全部砍掉。
9. **不做部署**：本地能跑不等于别人能用。
10. **不写 README**：别人（包括未来的你）不知道怎么运行。

---

## 11. 时间不够时怎么调整

| 情况 | 调整 |
| --- | --- |
| 每天只有 1 小时 | 周期拉到 40-48 周；每天只做 D1/D3/D5 的核心，D2/D4 放周末 |
| 某周加班/考试 | 只保留“本周交付”的最小版本；周日补，不要连续欠三周 |
| 已经有编程基础 | 跳过 W1-W2，把时间加到 W14-W16 的工程化 |
| 已经有前端基础 | 压缩 W3 和 W13，直接做流式 UI |
| 完全零基础 | 在 W1 前加 2 周 Python 补课，总周期 26 周 |
| 卡在一个 bug 超过 2 小时 | 记录复现步骤，先跳过；周日晚集中查，不要让一天崩掉 |

**底线**：宁可 30 周扎实做完，不要 12 周“看过一遍”。

---

## 12. 术语小抄

| 术语 | 一句话解释 |
| --- | --- |
| API | 程序之间约定好的调用接口，比如“发一个问题，返回一段回答” |
| JSON | 一种文本格式，用键值对表示结构化数据 |
| Token | 模型计费和上下文长度的单位，约等于一小段文字 |
| Embedding | 把文本变成向量，让“意思相近”的文本在数学上接近 |
| RAG | 先检索资料，再让模型基于资料回答 |
| Tool call | 模型请求调用一个外部函数，比如计算器、搜索、读文件 |
| Agent loop | 观察 → 思考 → 行动 → 再观察的循环 |
| Harness | 包裹模型的运行框架：工具、权限、状态、日志、压缩、评测 |
| MCP | 让 Agent 标准化连接外部工具和数据源的协议 |
| Eval | 用固定测试集衡量 Agent 是否真的变好 |
| Trace | 一次任务中每一步的完整记录，用来定位失败 |
| Prompt injection | 网页/文档里藏指令，诱导 Agent 做不该做的事 |

---

## 13. 今晚就开始：30 分钟启动清单

- [ ] 安装 Python 3.12、VS Code、Git（如果还没装）。
- [ ] 新建 `ai-fullstack` 文件夹和 GitHub 仓库。
- [ ] 写 `hello.py`，运行成功。
- [ ] 执行 `git add . && git commit -m "start"`。
- [ ] 在日历里锁定周一到周六每天 2 小时，周日 1 小时复盘。
- [ ] 把本文件复制到仓库的 `docs/` 下，作为总路线图。
- [ ] 在笔记里写一句：**“24 周后，我要让一个陌生人能用上我做的 AI 应用。”**

---

## 14. 最后一句

这份计划的核心不是“学完所有知识”，而是 **每两周都有一个能运行、能演示、能复盘的产物**。  
如果某天只写了 20 行代码，也比只看 2 小时视频更接近目标。保持主线，允许慢，不要停。
