# 🦞 ClawDen - OpenClaw 变种收集站

> 收集基于 OpenClaw 开发的各种变种项目，了解它们的优缺点和适用场景

[![Stars](https://img.shields.io/github/stars/caisd1/ClawDen)](https://github.com/caisd1/ClawDen)
[![License](https://img.shields.io/github/license/caisd1/ClawDen)](LICENSE)

---

## 📋 目录

- [项目地图](#项目地图)
- [热门变种项目](#热门变种项目)
- [核心变种](#核心变种)
- [中国特色变种](#中国特色变种)
- [自动化变种 (AutoClaw 系列)](#自动化变种-autoclaw-系列)
- [垂直领域变种](#垂直领域变种)
- [工具与周边](#工具与周边)
- [记忆与存储](#记忆与存储)
- [其他有趣变种](#其他有趣变种)
- [变种对比表](#变种对比表)
- [版本变更追踪](#版本变更追踪)
- [热门 Skills Top 10](#-热门-skills-top-10)
- [使用场景](#使用场景)

---

## 🗺️ 项目地图

```
OpenClaw (原 Clawdbot / Moltbot) - 335k+ stars 🚀
    │
    ├── 🔥 官方里程碑
    │   └── OpenClaw 官方 (340,985 stars) - GitHub TOP 1 🥇
    │
    ├── 🔥 热门变种
    │   ├── LangChain              (132,000 stars) Agent 工程平台
    │   ├── awesome-openclaw-skills (41,500 stars) 🆕 Skills 精选集
    │   ├── awesome-openclaw-agents (162 stars) 🆕 187个生产级 Agent 模板合集
    │   ├── everything-claude-code (106,320 stars)
    │   ├── superpowers            (111,725 stars)
    │   ├── MetaGPT                (66,100 stars)
    │   ├── autogen                (56,100 stars)
    │   ├── Agent-S               (~5,000+ stars) 🆕 自主 GUI Agent 框架
    │   ├── crewAI                 (47,100 stars)
    │   ├── nanobot (HKUDS)        (35,900 stars)
    │   ├── airi                   (35,400 stars) 🆕
    │   ├── learn-claude-code      (36,897 stars)
    │   ├── TradingAgents          (41,471 stars)
    │   ├── deer-flow             (45,144 stars) 🆕
    │   ├── SuperAGI              (17,295 stars) 🆕
    │   ├── OpenClaw-RL            (5,200+ stars) 🆕 HuggingFace 日榜 #1
    │   ├── Claw-R1                (🆕 OpenClaw + Agent-R1，强化学习推理)
    │   ├── Thoth System           (🆕 OpenClaw 完整 AI Agent 系统)
    │   ├── openclaw-agents        (🆕 9 Agent 协作套件)
    │   ├── ZeroClaw               (28,600 stars)
    │   ├── AstrBot                (26,722 stars)
    │   ├── NanoClaw               (25,028 stars)
    │   ├── cc-switch              (32,700 stars) 🆕
    │   ├── openclaw.net           (.NET 实现，NativeAOT 友好，156 stars)
    │   ├── Mastra                 (22,300 stars)
    │   ├── openai-agents-python   (20,220 stars)
    │   ├── OpenViking             (18,203 stars)
    │   ├── LangBot                (15,644 stars)
    │   ├── OpenFang               (15,329 stars)
    │   ├── memU                   (13,200 stars)
    │   ├── microsoft/agent-framework (8,159 stars) 🆕
    │   ├── OpenCode               (11,549 stars)
    │   ├── MoltWorker             (9,716 stars)
    │   ├── openclaw-multiagent-framework (1,800+ stars) 🆕
    │   ├── openclaw-agents        (🆕 9 Agent 协作套件，75+工具)
    │   ├── openclaw-agent-framework (🆕 活模板框架)
    │   ├── ThinkingMachineLabs/openclaw (🆕 配置驱动框架)
    │   ├── NullClaw               (6,697 stars)
    │   ├── Koog                   (3,900+ stars) 🆕 JetBrains JVM 框架
    │   ├── claw0                  (🆕 从 0 到 1 构建 AI Agent Gateway，10 节 ~7000 行 Python)
    │   ├── PUAClaw                (2,000 stars)
    │   ├── agentic-work-playbook (🆕 活模板框架，工作区/工作流/安全/习惯)
    │   ├── Agent-claw            (🆕 "The lobster way" 任意 OS/平台)
    │   └── Aurogen                (700 stars)
    │
    ├── 🔥 核心变种
    │   ├── nanobot (HKUDS)     (超轻量级，35k+ stars)
    │   ├── nanoclaw            (轻量化替代)
    │   ├── moltworker          (Cloudflare Workers)
    │   ├── poco-claw           (美观替代)
    │   └── secure-openclaw     (安全强化)
    │
    ├── 🚀 AutoClaw 系列
    │   ├── autoclaw         (超轻量容器化)
    │   ├── autoclawd        (macOS ambient AI)
    │   └── autoclaw-browser (浏览器自动化)
    │
    ├── 🇨🇳 中国特色
    │   ├── openclaw-china   (飞书/钉钉/QQ/微信)
    │   ├── openclaw-wechat  (个人微信)
    │   └── OpenClawChineseTranslation (汉化版)
    │
    ├── 🎯 垂直领域
    │   ├── TradingAgents    (41,471 stars) 🆕 多 Agent LLM 金融交易框架
    │   ├── OpenClaw-RL      (强化学习训练)
    │   ├── OpenClaw-Medical-Skills (医疗)
    │   └── nof1.ai         (AI 交易系统)
    │
    ├── 🛠️ 工具与仪表板
    │   ├── openclaw-studio  (Web 仪表板)
    │   ├── openclaw-mission-control (编排仪表板)
    │   ├── ClawX            (桌面客户端)
    │   ├── antfarm          (Agent 团队)
    │   ├── lobster          (工作流引擎)
    │   └── crabwalk         (实时监控)
    │
    └── 📦 记忆与存储
        ├── memU             (记忆系统)
        ├── MemOS            (记忆 OS)
        └── openclaw-supermemory (长期记忆)
```

---

## 🔥 热门变种项目

> 按 GitHub Stars 数量排序，数据来源 GitHub API + GitHub Trending (更新于 2026-03-30)

| 排名 | 项目 | Stars | 描述 | 分类 |
|------|------|-------|------|------|
| 🥇 | **OpenClaw 官方** | ⭐ 340,985 | 官方仓库，AI Agent 框架 TOP 1 | 官方 |
| 🆕 | **Agent-S** | ⭐ ~5,000+ | 🆕 开源 Agentic 框架，支持 Agent-Computer Interface，实现计算机自主交互与 GUI  Agent | Agent 框架 |
| 🥈 | **LangChain** | ⭐ 131,574 | The Agent Engineering Platform，130k+ Stars | Agent 框架 |
| 🥉 | **superpowers** | ⭐ 123,995 | Agentic Skills 框架与软件开发方法论 | Agent 框架 |
| 4 | **everything-claude-code** | ⭐ 117,403 | Agent Harness 性能优化系统，支持 OpenCode/Cursor/Claude Code | 开发者工具 |
| 5 | **MetaGPT** | ⭐ 66,430 | 多 Agent 框架：第一个 AI 软件公司，向自然语言编程迈进 | Agent 框架 |
| 6 | **autogen** | ⭐ 56,425 | 微软开源编程框架 for Agentic AI | Agent 框架 |
| 7 | **crewAI** | ⭐ 47,550 | 多 Agent 协作编排框架，支持自主 AI Agents 角色扮演 | Agent 框架 |
| 8 | **deer-flow** | ⭐ 53,281 | 字节跳动开源 SuperAgent harness，支持研究/编码/创作 | 核心变种 |
| 9 | **awesome-openclaw-skills** | ⭐ 43,048 | OpenClaw Skills 精选集合，5400+ 技能 | 工具与技能 |
| 10 | **TradingAgents** | ⭐ 41,471 | 多 Agent LLM 金融交易框架 | 垂直领域 |
| 11 | **learn-claude-code** | ⭐ 36,897 | Nano Claude Code-like Agent Harness， Bash is all you need | 核心变种 |
| 12 | **nanobot (HKUDS)** | ⭐ 35,900 | Ultra-Lightweight OpenClaw，超轻量级 | 核心变种 |
| 13 | **air i** | ⭐ 35,400 | 自托管 Grok Companion，开源 AI 陪伴助手 | 核心变种 |
| 14 | **cc-switch** | ⭐ 35,412 | 🆕 跨平台桌面 All-in-One 助手，支持 Claude Code/Codex/OpenCode/OpenClaw/Gemini CLI | 开发者工具 |
| 15 | **SuperAGI** | ⭐ 17,295 | dev-first 开源自主 AI agent 框架 | 核心变种 |
| 16 | **AstrBot** | ⭐ 28,224 | Agentic IM Chatbot基础设施，多平台LLM机器人 | 中国特色 |
| 17 | **ZeroClaw** | ⭐ 28,600 | Fast, small, and fully autonomous AI assistant | 核心变种 |
| 18 | **NanoClaw** | ⭐ 25,937 | 轻量级替代方案，容器化运行 | 核心变种 |
| 19 | **Mastra** | ⭐ 22,463 | TypeScript AI 应用框架，支持多 Agent 编排 | 核心变种 |
| 20 | **openai-agents-python** | ⭐ 20,411 | OpenAI 官方 Python Agent SDK，轻量级多 Agent 工作流 | 核心变种 |
| 21 | **OpenViking** | ⭐ 19,957 | 字节跳动开源上下文数据库，专为 AI Agents 设计 | 记忆系统 |
| 22 | **LangBot** | ⭐ 15,699 | 生产级多平台智能机器人开发平台 | 中国特色 |
| 23 | **OpenFang** | ⭐ 15,894 | Open-source Agent Operating System | 工具与仪表板 |
| 24 | **memU** | ⭐ 13,261 | 24/7 主动 Agent 记忆系统 | 记忆系统 |
| 25 | **OpenCode** | ⭐ 11,655 | Go 编写的终端 AI 编码 Agent | 开发者工具 |
| 26 | **MoltWorker** | ⭐ 9,716 | Cloudflare Workers 无服务器运行 | 核心变种 |
| 27 | **microsoft/agent-framework** | ⭐ 8,159 | 微软官方 Agent 框架，支持 Python/.NET 构建、编排和部署 AI Agent 与多 Agent 工作流 | Agent 框架 |
| 28 | **ClawRouter** | ⭐ 6,533 | 🆕 Agent-native LLM Router for OpenClaw，41+ 模型、<1ms 路由、支持 USDC 支付 | 工具与周边 |
| 29 | **NullClaw** | ⭐ 6,697 | 最轻量 Zig 实现，678KB 二进制，<2ms 启动 | 核心变种 |
| 30 | **Koog** | ⭐ 3,900+ | JetBrains 开源 JVM (Java/Kotlin) AI Agent 框架 | 核心变种 |
| 31 | **openclaw-multiagent-framework** | ⭐ 1,800+ | 多 Agent 协作协议与架构，零配置插件系统 | 核心变种 |
| 32 | **PUAClaw** | ⭐ 2,000 | Claw 们终将接管世界 | 其他有趣变种 |
| 33 | **openclaw-agents** | ⭐ 2,202 | 187个生产级 Agent 模板合集，覆盖24个分类，开箱即用 SOUL.md | 工具与技能 |
| 34 | **openclaw.net** | ⭐ 156 | .NET 实现版，NativeAOT 友好，支持 JS/TS 插件生态 | 核心变种 |
| 35 | **Claw-R1** | ⭐ 148 | OpenClaw + Agent-R1，强化学习推理框架，MiddleWare 架构设计 | 垂直领域 |
| 36 | **Thoth System** | 🆕 新发现 | OpenClaw 完整 AI Agent 系统，支持记忆/自我诊断/自我改进/语音/自动化，2分钟配置 | 垂直领域 |
| 37 | **agentic-work-playbook** | 🆕 新发现 | OpenClaw AI Agent 部署与维护的活模板框架，增加工作区架构/工作流/安全/习惯 | 工具与周边 |
| 38 | **Agent-claw** | 🆕 新发现 | "The lobster way" 个人 AI 助手，支持任意 OS/平台 | 其他有趣变种 |
| 39 | **claw0** | 🆕 新发现 | 从 0 到 1 构建 AI Agent Gateway，10 个章节 ~7000 行 Python，零基础入门 OpenClaw 架构设计 | 核心变种 |
| 40 | **openclaw-agent-framework** | 🆕 新发现 | 活模板框架，面向 AI Agent 的可持续自动化基础设施 | 工具与周边 |
| 41 | **ThinkingMachineLabs/openclaw** | 🆕 新发现 | 配置驱动的 AI 智能体框架，支持 Ollama/ChromaDB/Telegram/Webhook | 核心变种 |

### 重点项目详细介绍

#### OpenCode ⭐ 11,462

> Go 编写的终端 AI 编码 Agent

| 属性 | 值 |
|------|-----|
| GitHub | [opencode-ai/opencode](https://github.com/opencode-ai/opencode) |
| 语言 | Go |
| Stars | 11,478 |

**核心功能**: 终端 AI 编码助手、多 LLM 支持、原生 Go 性能

| 优点 | 缺点 |
|------|------|
| ✅ Go 语言实现，性能极佳 | ❌ 功能相对专一（聚焦编码） |
| ✅ 终端原生体验 | ❌ 社区相对较小 |
| ✅ 轻量级部署 | |
| ✅ 多 LLM 支持 | |

**适用场景**: 开发者、终端爱好者、追求高性能编码助手

### 重点项目详细介绍

#### nanobot (HKUDS) ⭐ 35,900

> Ultra-Lightweight OpenClaw - 用更少的代码实现核心功能

| 属性 | 值 |
|------|-----|
| GitHub | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) |
| 语言 | Python |
| Stars | 35,683 |

**支持平台**: Telegram, Slack, Discord, WhatsApp, Feishu, QQ, Email, Matrix 等

**核心功能**: 超轻量级实现、MCP 支持、多渠道接入、实时内存系统

| 优点 | 缺点 |
|------|------|
| ✅ 代码量极简 (比 OpenClaw 少 99%) | ❌ Python 依赖 |
| ✅ 活跃开发 (几乎每天更新) | ❌ 相对较新，社区较小 |
| ✅ MCP 原生支持 | |
| ✅ 多平台支持 | |

**适用场景**: 追求轻量化的用户、需要 MCP 集成的场景、多平台部署

---

#### ZeroClaw ⭐ 28,600

> 最新旗舰 - Fast, small, and fully autonomous AI assistant infrastructure

| 属性 | 值 |
|------|-----|
| GitHub | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) |
| 语言 | Rust |
| Stars | 28,600 |

**优点**: Rust 实现性能极佳、完全自主运行、部署灵活 anywhere、模型可 swap anything

**适用场景**: 高性能需求、资源敏感环境、追求最新技术

---

#### NanoClaw ⭐ 25,028

> 轻量级替代方案，容器化运行

| 属性 | 值 |
|------|-----|
| GitHub | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) |
| 语言 | TypeScript |
| Stars | 25,028 |

**支持平台**: WhatsApp, Telegram, Slack, Discord, Gmail 等

**核心功能**: 内存持久化、定时任务、容器化安全运行

| 优点 | 缺点 |
|------|------|
| ✅ 轻量级，资源占用低 | ❌ 功能相对基础 |
| ✅ 容器化部署，简单快捷 | ❌ 自定义程度较低 |
| ✅ 安全隔离好 | ❌ 需要容器运行环境 |
| ✅ 直接使用 Anthropic Agents SDK | |

**适用场景**: 个人使用、资源有限的服务器、快速部署尝鲜

---

#### learn-claude-code ⭐ 36,897

> Nano Claude Code-like Agent Harness — Bash is all you need

| 属性 | 值 |
|------|-----|
| GitHub | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) |
| 语言 | TypeScript |
| Stars | 36,897 |

**核心理念**: "An agent is a model" — 从头构建的轻量级 Agent Harness，强调神经网络才是真正的 Agent

**核心功能**: 极简设计、Bash 驱动、轻量级 Agent 训练框架

| 优点 | 缺点 |
|------|------|
| ✅ Nano 级别极简实现 | ❌ 相对较新 |
| ✅ 明确的技术定位 | ❌ 社区规模待发展 |
| ✅ 活跃更新 | |
| ✅ 多语言文档（中/英/日） | |

**适用场景**: 追求极简架构的开发者、学习 Agent 底层原理、教育场景

---

#### deer-flow ⭐ 45,144

> 字节跳动开源 - 开源 SuperAgent harness，支持研究/编码/创作

| 属性 | 值 |
|------|-----|
| GitHub | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 语言 | Python |
| Stars | 45,144 |

**支持框架**: OpenClaw, Claude Code, Codex, Cursor 等主流 AI Coding Agents

**核心功能**:
- SuperAgent Harness：研究、编码、创作一体化
- 沙箱环境：安全隔离的代码执行环境
- 记忆系统：长期上下文与知识管理
- 工具调用：内置 MCP 工具支持
- 子 Agent 编排：复杂任务分解与协作

| 优点 | 缺点 |
|------|------|
| ✅ 字节跳动背书，质量有保证 | ❌ 相对较新 (2024年启动) |
| ✅ 增长极快 (38k+ stars) | ❌ 社区生态仍在发展中 |
| ✅ 多框架支持 | ❌ 文档以英文为主 |
| ✅ 活跃开发 | |

**适用场景**: 需要研究+编码+创作一体的场景、企业级 Agent 部署、AI 内容创作

---

#### everything-claude-code ⭐ 106,320

> Agent Harness 性能优化系统 — Skills / Instincts / Memory / Security 全方位增强

| 属性 | 值 |
|------|-----|
| GitHub | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) |
| 语言 | JavaScript/TypeScript |
| Stars | 106,320 |

**支持框架**: Claude Code, Codex, **Opencode**, Cursor 等主流 AI Coding Agents

**核心功能**:
- Skills（技能系统）：即插即用的 Agent 能力扩展
- Instincts（本能系统）：内置行为模式优化
- Memory（记忆系统）：长期上下文与知识管理
- Security（安全系统）：企业级权限与审计
- Research-First Development（研究驱动开发）

| 优点 | 缺点 |
|------|------|
| ✅ 覆盖最主流的 Agent Harness | ❌ 主攻 Claude Code 生态 |
| ✅ Stars 增长极快（100k+） | ❌ 对 OpenClaw 原生支持有限 |
| ✅ 多语言文档（中/英/日/韩） | |
| ✅ 企业级安全特性 | |

**适用场景**: 追求极致 Agent 性能的开发者、企业级 Agent 部署、多框架协同

---

#### Mastra ⭐ 22,251

> TypeScript 原生 AI 应用框架 — 构建 AI 应用和 Agent 的现代 TypeScript 工具

| 属性 | 值 |
|------|-----|
| GitHub | [mastra-ai/mastra](https://github.com/mastra-ai/mastra) |
| 语言 | TypeScript |
| Stars | 22,300 |

**支持平台**: 支持多种 LLM（OpenAI、Anthropic、 Google 等）、多渠道部署

**核心功能**:
- TypeScript 原生：全栈 TypeScript，类型安全
- 多 Agent 编排：灵活的多 Agent 协作框架
- 工具与工作流：内置工作流引擎，支持工具调用
- 记忆系统：内置 Agent 记忆与上下文管理
- 部署灵活：支持 Serverless、容器、本地运行

| 优点 | 缺点 |
|------|------|
| ✅ TypeScript 原生，前端/全栈友好 | ❌ 相对较新 (2024年启动) |
| ✅ 现代化的开发体验 | ❌ 社区生态仍在发展中 |
| ✅ 来自 Gatsby 团队背书 | ❌ 与 OpenClaw 设计理念不同 |
| ✅ 支持多种 LLM 和工具 | |

**适用场景**: TypeScript 全栈开发者、需要在现有 JS/TS 项目中集成 Agent、企业级 AI 应用

---

#### openai-agents-python ⭐ 20,220

> OpenAI 官方 Python Agent SDK — 轻量级多 Agent 工作流框架

| 属性 | 值 |
|------|-----|
| GitHub | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) |
| 语言 | Python |
| Stars | 20,220 |

**核心功能**:
- OpenAI 官方维护：与 GPT 系列深度集成
- 多 Agent 协作：支持多 Agent 任务分配与协作
- Function Calling：原生支持工具调用和工作流
- 轻量级设计：简单易用，快速上手
- 可扩展架构：易于自定义和扩展

| 优点 | 缺点 |
|------|------|
| ✅ OpenAI 官方支持，质量有保证 | ❌ 主要依赖 OpenAI 模型 |
| ✅ 轻量级，容易上手 | ❌ 生态局限于 OpenAI |
| ✅ Python 原生，数据科学友好 | ❌ 与 OpenClaw 设计哲学不同 |
| ✅ 活跃开发，版本迭代快 | |

**适用场景**: Python 开发者、OpenAI 模型重度用户、快速原型验证、教育学习

---

#### openclaw.net 🆕

> .NET 实现版 — NativeAOT 友好，兼容 JS/TS 插件生态

| 属性 | 值 |
|------|-----|
| GitHub | [clawdotnet/openclaw.net](https://github.com/clawdotnet/openclaw.net) |
| 语言 | C# / .NET |
| 许可 | MIT |

**核心理念**: 大多数 Agent 运行时仍假设 Python 或 Node 优先。但当你希望将其他系统保持在 .NET、发布精简自包含二进制或重用现有基础设施时，这就成了问题。

**核心功能**:
- .NET-first Gateway + Agent 运行时，NativeAOT 友好部署通道
- 通过 JSON-RPC Bridge 复用 OpenClaw JS/TS 插件，无需重写
- 显式兼容性诊断，而非模糊的"基本兼容"
- 可选 Microsoft Agent Framework (MAF) 编排器
- 生产级 Agent 基础设施：认证、策略、记忆、渠道、可观测性

| 优点 | 缺点 |
|------|------|
| ✅ .NET 生态深度集成 | ❌ 相对较新 |
| ✅ NativeAOT 发布，极致性能 | ❌ 社区规模待发展 |
| ✅ 兼容 OpenClaw JS 插件生态 | ❌ 需要 .NET 运行时 |
| ✅ 生产级特性开箱即用 | |

**适用场景**: .NET 团队、需要在现有 .NET 项目中集成 Agent、生产级 .NET Agent 部署

---

## 🔥 核心变种

### openclaw-multiagent-framework ⭐ 1,800+

> 多 Agent 协作协议与架构 — 零配置插件系统

| 属性 | 值 |
|------|-----|
| GitHub | [lanyasheng/openclaw-multiagent-framework](https://github.com/lanyasheng/openclaw-multiagent-framework) |
| Stars | 1,800+ |

**核心功能**:
- 多 Agent 协作协议：解决 ACP 通信不可靠问题
- Agent 任务注册记忆：解决注册后失忆问题
- 明确的超时语义：解决超时处理歧义
- 零配置插件系统：开箱即用

**优点**: 
- ✅ 零配置，易用性强
- ✅ 解决 OpenClaw 多 Agent 协作核心痛点
- ✅ 插件化架构，扩展方便
- ✅ 支持生产环境使用

**适用场景**: 多 Agent 协作场景、复杂任务分解、生产级多 Agent 系统

---

### MoltWorker ⭐ 9,716

> 在 Cloudflare Workers 上运行

| 属性 | 值 |
|------|-----|
| GitHub | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) |
| 语言 | TypeScript |
| Stars | 9,716 |

**优点**: 无需服务器、免费托管 (Cloudflare Workers)、全球 CDN 加速、零运维

**缺点**: Workers 资源限制、长时间任务受限、调试困难

**适用场景**: 轻量级个人助手、不想管理服务器的用户、原型验证

---

### Secure OpenClaw ⭐ 1,359

> 安全强化版本

| 属性 | 值 |
|------|-----|
| GitHub | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) |
| 语言 | TypeScript |
| Stars | 1,359 |

**优点**: 企业级安全、权限控制、审计日志

**适用场景**: 企业使用、对安全有高要求的场景

---

### Koog ⭐ 3,900+ 🆕

> JetBrains 开源 - JVM (Java/Kotlin) AI Agent 框架

| 属性 | 值 |
|------|-----|
| GitHub | [JetBrains/koog](https://github.com/JetBrains/koog) |
| 语言 | Kotlin / Java |
| Stars | 3,900+ |
| 更新频率 | 活跃（4小时前更新） |

**核心理念**: 构建可预测、容错、企业级 AI Agent，跨所有平台运行——从后端服务到 Android、iOS、JVM、甚至浏览器环境。

**核心功能**:
- JVM 原生：Java 和 Kotlin 双支持，充分利用现有 Java 生态
- 跨平台：后端、Android、iOS、浏览器全覆盖
- 可预测性：确定性行为，企业友好
- 容错设计：生产级稳定性
- 基于 AI 产品专业知识，提供复杂 LLM 问题的成熟解决方案

| 优点 | 缺点 |
|------|------|
| ✅ JetBrains 背书，质量有保证 | ❌ 相对较新 (2025年启动) |
| ✅ 活跃开发（数小时前更新） | ❌ 社区生态仍在发展中 |
| ✅ Java/Kotlin 生态深度集成 | ❌ 主要面向 JVM 开发者 |
| ✅ 企业级设计理念 | |

**适用场景**: Java/Kotlin 团队、需要在现有 JVM 项目中集成 Agent、企业级 AI 应用、Android AI 助手

---

### airi ⭐ 35,400 🆕

> 自托管 Grok Companion — 开源 AI 陪伴助手

| 属性 | 值 |
|------|-----|
| GitHub | [moeru-ai/airi](https://github.com/moeru-ai/airi) |
| 语言 | TypeScript |
| Stars | 35,400 |

**核心理念**: Self-hosted, you-owned Grok Companion — 包含灵魂灵魂的虚拟角色 AI 陪伴助手

**核心功能**:
- 自托管部署：完全自主控制数据
- 虚拟角色系统：支持创建和定制 AI 角色/伴侣
- 多 LLM 支持：支持各种主流大语言模型
- 长期记忆：持续记住对话和偏好
- 活跃开发：几乎每小时更新

| 优点 | 缺点 |
|------|------|
| ✅ 完全自托管，隐私安全 | ❌ 不是传统 Agent 框架 |
| ✅ 虚拟角色定制灵活 | ❌ 社区相对专一（陪伴场景） |
| ✅ 活跃开发，功能快速迭代 | ❌ 需要较多资源运行 |
| ✅ 多模型支持 | |

**适用场景**: AI 陪伴、虚拟角色爱好者、自托管玩家、情感交互场景

---

### NullClaw ⭐ 6,697

> 最轻量级 Zig 实现

| 属性 | 值 |
|------|-----|
| GitHub | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) |
| 语言 | Zig |
| Stars | 6,697 |

**特点**: 
- 二进制仅 678 KB
- 峰值内存 ~1 MB
- 启动时间 <2 ms
- 完全自主运行
- 任务管理和持久化存储

**优点**: 
- ✅ 极致轻量（资源占用最低）
- ✅ 极快启动（<2ms）
- ✅ Zig 语言实现，性能极佳
- ✅ 无本地系统访问（安全）

**缺点**: 
- ❌ 较新，社区较小
- ❌ 功能相对基础

**适用场景**: 极致轻量化需求、资源极端敏感环境、安全敏感场景

---

## 🇨🇳 中国特色变种

### OpenClaw China ⭐ 2,927

> 中国插件全家桶

| 属性 | 值 |
|------|-----|
| GitHub | [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) |
| 语言 | TypeScript |
| Stars | 2,927 |

**支持平台**: 🦜 飞书 | 💬 钉钉 | 🐧 QQ | 💼 企业微信 | 📱 个人微信

**优点**: 全面支持国内主流 IM、本土化做得好、社区活跃

**缺点**: 部分平台需要企业资质、微信 hook 不稳定

**适用场景**: 国内团队协作、中文环境使用

---

### OpenClaw 中文翻译版 ⭐ 3,031

> 全中文界面

| 属性 | 值 |
|------|-----|
| GitHub | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) |
| Stars | 3,031 |

**优点**: 全流程中文、详细中文教程、每月同步更新

**适用场景**: 中文用户入门、不想看英文文档

---

### 国内平替产品横评 (2026年3月)

> 来源：微信公众号 - 唐韧

#### 本地型产品

| 产品 | 官网 | 特点 | 适合人群 |
|------|------|------|----------|
| 智谱 AutoClaw | autoglm.zhipuai.cn/autoclaw | 容易上手，一键迁移 | 第一次接触 Agent、怕折腾 |
| 腾讯 QClaw | qclaw.qq.com | 直连微信 | 微信用户 |
| 腾讯 WorkBuddy | copilot.tencent.com/work | 纯自研，企业级安全 | 团队、公司 |

#### 云端型产品

| 产品 | 官网 | 特点 | 适合人群 |
|------|------|------|----------|
| MiniMax MaxClaw | agent.minimaxi.com/max-claw | 便宜、预设多、39元/月 | 预算有限、快速体验 |
| 字节 ArkClaw | volcengine.com | 深度适配飞书 | 重度飞书用户 |
| 字节飞书秒搭 | miaoda.feishu.cn/bot | 一键安装、零操作 | 纯小白 |

---

## 🚀 自动化变种 (AutoClaw 系列)

### AutoClaw ⭐ 40

> 超轻量级自动化 Agent

| 属性 | 值 |
|------|-----|
| GitHub | [tsingliuwin/autoclaw](https://github.com/tsingliuwin/autoclaw) |
| Stars | 40 |

**特点**: 超轻量级、Docker 容器内运行、无头/大规模并发设计

**适用场景**: 服务器部署、大规模自动化任务、资源敏感环境

---

## 🎯 垂直领域变种

### OpenClaw-RL ⭐ 5,200+

> 强化学习训练 agent — 🆕 HuggingFace Daily Papers #1！

| 属性 | 值 |
|------|-----|
| GitHub | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) |
| Stars | 5,200+ |
| 官方支持 | OpenClaw 官方插件支持 |

**核心功能**:
- 强化学习训练：通过对话训练个性化 Agent
- 支持本地 GPU 和云端（ Tinker）部署
- 支持 LoRA 训练
- 支持 Hybrid RL、OPD、Binary RL

**优点**: 
- ✅ 🆕 HuggingFace Daily Papers #1！
- ✅ 支持 OpenClaw 官方扩展安装
- ✅ 支持多种 RL 方法
- ✅ 活跃开发（近期多次重大更新）

**适用场景**: AI 研究、自定义 agent 训练、强化学习实验

---

### OpenClaw Medical Skills ⭐ 1,004

> 医疗领域技能库

| 属性 | 值 |
|------|-----|
| GitHub | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) |
| Stars | 1,004 |

**适用场景**: 医疗辅助、健康咨询

---

### nof1.ai ⭐ 569

> AI 交易系统

| 属性 | 值 |
|------|-----|
| GitHub | [195440/nof1.ai](https://github.com/195440/nof1.ai) |
| Stars | 569 |

**适用场景**: 量化交易、金融分析

---

### Claw-R1 🆕

> OpenClaw + Agent-R1 — 强化学习推理框架

| 属性 | 值 |
|------|-----|
| GitHub | [AgentR1/Claw-R1](https://github.com/AgentR1/Claw-R1) |
| Stars | 🆕 新发现 |
| 定位 | OpenClaw + Agent-R1 融合，强化学习推理 |

**核心理念**: 构建于 Agent-R1 基础之上，融合 OpenClaw 的个人 AI 助手范式，采用 MiddleWare 架构设计。

**致谢**: 感谢 MiniMax Forge 在 MiddleWare 设计上的架构洞察，感谢 rLLM 在语言 Agent RL 框架设计上的开创性工作，以及 OpenClaw 在个人 AI 助手方面的卓越工作——启发了我们的愿景。

**核心功能**:
- OpenClaw + Agent-R1 融合框架
- MiddleWare 架构设计
- 强化学习推理能力
- 继承 OpenClaw 个人 AI 助手范式

| 优点 | 缺点 |
|------|------|
| ✅ 融合两大框架优势 | ❌ 相对较新 |
| ✅ MiddleWare 架构清晰 | ❌ 社区生态待发展 |
| ✅ 强化学习推理能力 | ❌ Star 数量待确认 |

**适用场景**: 强化学习推理研究、AI Agent 架构探索、融合 OpenClaw 与 RL 技术的实验

---

### Aurogen ⭐ 700

> The Multi-Agent Evolution of OpenClaw

| 属性 | 值 |
|------|-----|
| GitHub | [UniRound-Tec/Aurogen](https://github.com/UniRound-Tec/Aurogen) |
| 语言 | TypeScript |
| Stars | 700 |

**特点**: 多 Agent 协作框架、扩展 OpenClaw 能力、多智能体系统

**适用场景**: 多 Agent 协作场景、复杂任务分解、AI 研究

---

## 🛠️ 工具与仪表板

### ClawX ⭐ 4,178

> 桌面客户端

| 属性 | 值 |
|------|-----|
| GitHub | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) |
| Stars | 4,178 |

**优点**: 图形界面友好、跨平台 (Windows/macOS)、中国区有独立网站

**适用场景**: 不习惯命令行的用户、桌面办公场景

---

### cc-switch ⭐ 32,700 🆕

> 跨平台桌面 All-in-One 助手，支持 Claude Code / Codex / OpenCode / OpenClaw / Gemini CLI

| 属性 | 值 |
|------|-----|
| GitHub | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) |
| 语言 | Rust |
| Stars | 32,700 |

**核心理念**: 一个桌面应用切换使用多个主流 AI Coding Agent，无需重复配置

**核心功能**:
- 多框架支持：Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI
- 跨平台：Windows / macOS / Linux
- 快速切换：一键在不同 Agent 间切换
- 统一配置管理：集中管理 API keys 和设置

| 优点 | 缺点 |
|------|------|
| ✅ Rust 实现，性能优异 | ❌ 相对较新 |
| ✅ 多框架一站式管理 | ❌ 社区规模待发展 |
| ✅ 跨平台支持 | ❌ 主要面向开发者 |

**适用场景**: 多框架用户、追求统一体验的开发者、需要在不同 Agent 间切换

---

### OpenFang ⭐ 15,400

> Open-source Agent Operating System

| 属性 | 值 |
|------|-----|
| GitHub | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) |
| 语言 | Rust |
| Stars | 15,400 |

**优点**: Rust 实现、完全自主运行、模块化设计、生产级稳定性

**适用场景**: 企业级 Agent 部署、追求稳定性的生产环境

---

### memU ⭐ 13,200

> 24/7 主动 Agent 记忆系统

| 属性 | 值 |
|------|-----|
| GitHub | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) |
| Stars | 13,200 |

---

### MemOS ⭐ 7,671

> 记忆操作系统

| 属性 | 值 |
|------|-----|
| GitHub | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) |
| Stars | 6,713 |

**优点**: 长期记忆、技能进化、多 agent 共享

---

## 📦 记忆与存储

| 项目 | Stars | 描述 |
|------|-------|------|
| memU | 13,200 | 记忆系统 |
| MemOS | 7,671 | 记忆 OS |
| openclaw-supermemory | 584 | 长期记忆 |
| **OpenViking** | **18,203** | **字节跳动开源上下文数据库，专为 AI Agents 设计** |

### OpenViking ⭐ 18,203

> 字节跳动开源 - 专为 AI Agents 设计的上下文数据库

| 属性 | 值 |
|------|-----|
| GitHub | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) |
| 语言 | Python |
| Stars | 18,203 |

**核心功能**: 
- 文件系统范式管理上下文（记忆、资源、技能）
- 三层上下文加载（L0/L1/L2），按需加载，显著节省成本
- 目录递归检索，结合目录定位与语义搜索
- 可视化检索轨迹，可观测上下文
- 自动会话管理，上下文自迭代

**适用场景**: 大规模 AI Agent 部署、需要高效上下文管理、企业级 Agent

---

## 其他有趣变种

### AstrBot ⭐ 26,722

> Agentic IM Chatbot 基础设施

| 属性 | 值 |
|------|-----|
| GitHub | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) |
| 语言 | Python |
| Stars | 26,722 |

**支持平台**: Discord / Slack / LINE / Telegram / WeChat / 飞书 / 钉钉 / QQ 等 10+ 平台

**优点**: 多平台支持、集成 DeepSeek/Claude/Gemini/Ollama 等、插件系统、易于二次开发

**适用场景**: 企业级机器人、多平台运营、需要丰富插件的场景

---

### LangBot ⭐ 15,644

> 生产级多平台智能机器人开发平台

| 属性 | 值 |
|------|-----|
| GitHub | [langbot-app/LangBot](https://github.com/langbot-app/LangBot) |
| Stars | 15,644 |

---

### Edict ⭐ 8,169

> 三省六部制 · OpenClaw 多 Agent 编排系统

| 属性 | 值 |
|------|-----|
| GitHub | [cft0808/edict](https://github.com/cft0808/edict) |
| Stars | 8,169 |

**特点**: 9 个专业化 Agent 协作、实时仪表板、完整审计日志、中国古代官制风格

---

### agentic-work-playbook 🆕

> OpenClaw AI Agent 部署与维护的活模板框架

| 属性 | 值 |
|------|-----|
| GitHub | [Stephane-fci/agentic-work-playbook](https://github.com/Stephane-fci/agentic-work-playbook) |
| Stars | 🆕 新发现 |
| 定位 | OpenClaw 上层框架，增加工作区架构/工作流/安全/习惯 |

**核心理念**: 这是一个加性框架，不替换任何东西——它只是给现有功能添砖加瓦。

**核心功能**:
- 工作区架构（Workspace Architecture）
- 工作流系统（Workflows）
- 企业级安全特性
- Agent 习惯系统（Habits）

| 优点 | 缺点 |
|------|------|
| ✅ 在 OpenClaw 基础上增量开发 | ❌ 相对较新 |
| ✅ 企业级工作流支持 | ❌ 社区规模待发展 |
| ✅ 安全和习惯开箱即用 | ❌ 需要一定学习成本 |

**适用场景**: 企业级 Agent 部署、需要规范化工作流的团队、追求生产级稳定性的用户

---

### Agent-claw 🆕

> "The lobster way" — 任意 OS / 任意平台的个人 AI 助手

| 属性 | 值 |
|------|-----|
| GitHub | [ayaqen/Agent-claw](https://github.com/ayaqen/Agent-claw) |
| Stars | 🆕 新发现 |
| 定位 | 个人 AI 助手，跨平台通用 |

**核心理念**: "Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞"

**核心功能**:
- 跨平台支持：任意操作系统
- 多渠道接入
- OpenClaw 生态兼容

| 优点 | 缺点 |
|------|------|
| ✅ 真正跨平台 | ❌ 相对较新 |
| ✅ 继承 OpenClaw 生态 | ❌ Star 数量待确认 |
| ✅ 轻量化设计 | |

**适用场景**: 追求跨平台一致体验的用户、需要在多系统间切换的个人用户

---

### PUAClaw ⭐ 2,000

> Claw 们终将接管世界

| 属性 | 值 |
|------|-----|
| GitHub | [puaclaw/PUAClaw](https://github.com/puaclaw/PUAClaw) |
| 语言 | HTML |
| Stars | 2,000 |

**特点**: 独特的研究项目、探索 AI Agent 的可能性

**适用场景**: AI 研究、实验性项目

---

## 📊 变种对比表

| 项目 | Stars | 轻量 | 中国支持 | 桌面端 | 记忆 | 安全 |
|------|-------|------|----------|--------|------|------|
| **NullClaw** | 6,697 | ✅ | ❌ | ❌ | ✅ | ✅ |
| **NanoClaw** | 25,028 | ✅ | ❌ | ❌ | ✅ | ✅ |
| **MoltWorker** | 9,716 | ✅ | ❌ | ❌ | ❌ | ✅ |
| **OpenClaw China** | 2,927 | ❌ | ✅ | ❌ | ❌ | ❌ |
| **ClawX** | 4,178 | ❌ | ✅ | ✅ | ❌ | ❌ |
| **LangBot** | 15,644 | ❌ | ✅ | ❌ | ❌ | ❌ |
| **MemOS** | 7,671 | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Secure OpenClaw** | 1,359 | ❌ | ❌ | ❌ | ❌ | ✅ |
| **OpenFang** | 15,400 | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Aurogen** | 700 | ✅ | ❌ | ❌ | ❌ | ❌ |

---

## 🆚 选择指南

| 需求 | 推荐 |
|------|------|
| 快速部署尝鲜 | **NanoClaw** |
| 不想买服务器 | **MoltWorker** |
| 国内微信/钉钉/飞书 | **OpenClaw China** |
| 中文界面 | **中文翻译版** |
| 桌面图形界面 | **ClawX** |
| 团队多 agent | **Mission Control** |
| 长期记忆 | **MemOS** |
| 企业安全 | **Secure OpenClaw** |
| 免 API 成本 | **Zero Token** |

---

## 📊 版本变更追踪

> OpenClaw 官方最新版本动态（数据来源：GitHub API）

**版本特点**：OpenClaw 使用日期格式版本号（如 v2026.3.13），发布非常频繁，几乎每天都有更新。

### 近期版本

| 版本 | 发布日期 | 主要变更 |
|------|----------|----------|
| v2026.3.13-1 | 2026-03-14 | 修复 Compass token 计算、Docker 安全加固、Discord 兼容性、Slack 交互消息、Agent 记忆优化、性能构建优化 |
| v2026.3.12 | 2026-03-13 | Bug 修复和小优化 |
| v2026.3.11 | 2026-03-12 | 安全更新 |
| v2026.3.8 | 2026-03-09 | 常规更新 |
| v2026.3.7 | 2026-03-08 | 常规更新 |

### v2026.3.13-1 详细变更

**新功能 (Features)**
- Android: 全新聊天设置 UI
- iOS: 添加欢迎页面
- Docker: 支持 OPENCLAW_TZ 时区配置
- Slack: 支持交互式回复指令

**Bug 修复 (Fixes)**
- 修复 Telegram 媒体下载 IPv4 回退
- 修复飞书文件上传中文文件名支持
- 修复 macOS PortGuard 与 Docker Desktop 冲突
- 修复 Windows 重启时控制台窗口显示问题
- 修复浏览器批量操作失败处理
- 修复 Session 重置后保留 lastAccountId/lastThreadId

**安全更新 (Security)**
- Docker: 防止 gateway token 在构建时泄露

**性能优化 (Performance)**
- 构建优化：去重 plugin-sdk chunks，修复 ~2x 内存回归

[查看完整版本历史 →](https://github.com/openclaw/openclaw/releases)

---

## 🛠️ 热门 Skills Top 10

> 来自 awesome-openclaw-skills 精选集

| 排名 | Skill | 描述 | 分类 |
|------|-------|------|------|
| 1 | **web-search** | 联网搜索能力 | 工具 |
| 2 | **browser-use** | 浏览器自动化 | 工具 |
| 3 | **code-executor** | 代码执行环境 | 开发 |
| 4 | **memory** | 长期记忆系统 | 记忆 |
| 5 | **file-manager** | 文件管理系统 | 工具 |
| 6 | **slack** | Slack 集成 | 平台 |
| 7 | **telegram** | Telegram 集成 | 平台 |
| 8 | **discord** | Discord 集成 | 平台 |
| 9 | **github** | GitHub 集成 | 开发 |
| 10 | **scheduler** | 定时任务 | 工具 |

[查看全部 5400+ Skills →](https://github.com/VoltAgent/awesome-openclaw-skills)

---

## 💡 使用场景

### 个人助理

- 日程管理提醒
- 邮件自动回复
- 信息聚合推送
- 个人知识助手

### 企业服务

- 客服机器人
- 内部知识库
- 会议纪要生成
- 自动化审批流

### 开发运维

- 代码审查助手
- CI/CD 监控
- 日志分析
- 自动化部署

### 内容创作

- 社交媒体运营
- 文章撰写润色
- 视频脚本生成
- 多语言翻译

---

## 💬 社区与资源

### 中文社区

| 社区 | 链接 |
|------|------|
| OpenClaw 中文社区 | [Discord #中文](https://discord.com/invite/clawd) |
| OpenClaw China | [GitHub](https://github.com/BytePioneer-AI/openclaw-china) |

### 英文社区

| 社区 | 链接 |
|------|------|
| OpenClaw Discord | [discord.gg/clawd](https://discord.com/invite/clawd) |
| OpenClaw Reddit | [reddit.com/r/openclaw](https://reddit.com/r/openclaw) |

### 学习资源

| 资源 | 链接 |
|------|------|
| Awesome OpenClaw | [GitHub](https://github.com/vincentkoc/awesome-openclaw) |
| OpenClaw 文档 | [docs.openclaw.ai](https://docs.openclaw.ai) |

---

## ❓ 常见问题 FAQ

### Q1: NanoClaw 和原版 OpenClaw 有什么区别？

**答**: NanoClaw 是轻量级替代品，更轻量但功能较少；原版功能更全但资源占用更高。

### Q2: 支持中文对话吗？

**答**: 支持！使用 `OpenClaw Chinese Translation` 或 `OpenClaw China` 变种。

### Q3: 需要付费吗？

**答**: 基础使用免费，仅需支付 AI API 调用费用（如 Claude API）。

### Q4: 如何选择部署平台？

| 场景 | 推荐 |
|------|------|
| 个人尝鲜 | Docker + NanoClaw |
| 不想管理服务器 | Cloudflare Workers |
| 国内团队使用 | 飞书/钉钉/微信 |
| 追求美观 UI | ClawX |

### Q5: 微信/飞书机器人会被封吗？

**答**:
- 企业微信/飞书/钉钉：官方支持，风险低
- 个人微信：存在风控风险，建议小号测试
- QQ：机器人协议相对宽松

---

## 📝 如何贡献

欢迎提交 PR 添加新的 OpenClaw 变种！

1. Fork 本项目
2. 添加变种信息到对应章节
3. 提交 Pull Request

---

## 📈 项目统计

> 截至 2026-03-30

| 分类 | 项目数 | 最高 Stars |
|------|--------|------------|
| 官方里程碑 | 1 | 340,985 |
| 热门变种 | 41 | 131,574 |
| 核心变种 | 8 | 35,683 |
| 中国特色 | 3 | 26,722 |
| AutoClaw 系列 | 5 | 40 |
| 垂直领域 | 7 | 38,775 |
| 工具仪表板 | 8 | 41,223 |
| 记忆系统 | 4 | 18,203 |

---

## 🙏 致谢

感谢所有为 OpenClaw 生态贡献的开发者！

- NanoClaw - 轻量级替代
- MoltWorker - Serverless 部署
- OpenClaw China - 国内生态
- ClawHub - 技能市场
- 所有变种维护者

---

*🦞 Last updated: 2026-03-30 | ClawDen - OpenClaw 变种收集站*

---

> 📅 自动更新于 2026-03-30 下午 by ClawDen 自动更新 Cron
