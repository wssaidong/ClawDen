# 🦞 ClawDen - OpenClaw 变种收集站

> 收集基于 OpenClaw 开发的各种变种项目，了解它们的优缺点和适用场景

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

---

## 🗺️ 项目地图

```
OpenClaw (原 Clawdbot / Moltbot)
    │
    ├── 🔥 热门变种
    │   ├── ZeroClaw        (最新旗舰，26k+ stars)
    │   ├── nanoclaw        (轻量化替代，21k+ stars)
    │   └── LangBot         (生产级机器人，15k+ stars)
    │
    ├── 🔥 核心变种
    │   ├── nanoclaw         (轻量化替代)
    │   ├── moltworker       (Cloudflare Workers)
    │   ├── poco-claw        (美观替代)
    │   └── secure-openclaw  (安全强化)
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

> 按 GitHub Stars 数量排序，数据来源 GitHub API

| 排名 | 项目 | Stars | 描述 | 分类 |
|------|------|-------|------|------|
| 🥇 | **ZeroClaw** | ⭐ 26,298 | Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀 | 核心变种 |
| 🥈 | **awesome-openclaw-skills** | ⭐ 35,862 | OpenClaw 技能精选集，5400+ 技能 | 工具与技能 |
| 🥉 | **NanoClaw** | ⭐ 21,854 | 轻量级替代方案，容器化运行 | 核心变种 |
| 4 | **LangBot** | ⭐ 15,532 | 生产级多平台智能机器人开发平台 | 中国特色 |
| 5 | **MemOS** | ⭐ 13,900 | 记忆操作系统 | 记忆系统 |
| 6 | **memU** | ⭐ 12,900 | 24/7 主动 Agent 记忆系统 | 记忆系统 |
| 7 | **MoltWorker** | ⭐ 9,573 | Cloudflare Workers 无服务器运行 | 核心变种 |
| 8 | **ClawHub** | ⭐ 5,459 | OpenClaw 官方技能目录 | 工具与技能 |
| 9 | **OpenClaw China** | ⭐ 2,913 | 中国插件全家桶（飞书/钉钉/QQ/微信） | 中国特色 |
| 10 | **ClawX** | ⭐ 3,772 | 桌面客户端 | 工具与仪表板 |

### 新增热门项目介绍

#### 1. ZeroClaw ⭐ 26,298

> 最新旗舰 - Fast, small, and fully autonomous AI assistant infrastructure

| 属性 | 值 |
|------|-----|
| GitHub | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) |
| 语言 | Rust |
| Stars | 26,298 |

**简介**
最新最热的 OpenClaw 变种！用 Rust 编写，提供快速、小巧、完全自主的 AI 助手基础设施。可部署到任何平台，灵活切换任何模型。

**✅ 优点**
- Rust 实现，性能极佳
- 完全自主运行
- 部署灵活 anywhere
- 模型可 swap anything

**❌ 缺点**
- Rust 学习曲线
- 社区较新

**🎯 适用场景**
- 高性能需求
- 资源敏感环境
- 追求最新技术

---

#### 2. awesome-openclaw-skills ⭐ 35,862

> 技能精选集

| 属性 | 值 |
|------|-----|
| GitHub | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) |
| Stars | 35,862 |

**简介**
OpenClaw 官方技能精选集，从官方技能注册表中筛选分类的 5400+ 技能。

**✅ 优点**
- 5400+ 技能可选
- 精选分类
- 持续更新

**🎯 适用场景**
- 技能选择困难
- 需要特定领域技能


---

## 🔥 核心变种

### 1. NanoClaw ⭐ 21,854

> 轻量级替代方案，容器化运行

| 属性 | 值 |
|------|-----|
| GitHub | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) |
| 语言 | TypeScript |
| Stars | 21,782 |
| Forks | 4,374 |

**简介**
NanoClaw 是 OpenClaw 的轻量级替代品，运行在容器中以增强安全性。直接基于 Anthropic Agents SDK 构建。

**支持平台**
- WhatsApp, Telegram, Slack, Discord, Gmail 等

**核心功能**
- 内存持久化
- 定时任务
- 容器化安全运行

**✅ 优点**
- 轻量级，资源占用低
- 容器化部署，简单快捷
- 安全隔离好
- 直接使用 Anthropic Agents SDK

**❌ 缺点**
- 功能相对基础
- 自定义程度较低
- 需要容器运行环境

**🎯 适用场景**
- 个人使用
- 资源有限的服务器
- 快速部署尝鲜

---

### 2. MoltWorker ⭐ 9,573

> 在 Cloudflare Workers 上运行

| 属性 | 值 |
|------|-----|
| GitHub | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) |
| 语言 | TypeScript |
| Stars | 9,573 |

**简介**
原名 Moltbot、Clawdbot，现可在 Cloudflare Workers 上无服务器运行。

**✅ 优点**
- 无需服务器
- 免费托管 (Cloudflare Workers)
- 全球 CDN 加速
- 零运维

**❌ 缺点**
- Workers 资源限制 (CPU 时间、内存)
- 长时间任务受限
- 调试困难

**🎯 适用场景**
- 轻量级个人助手
- 不想管理服务器的用户
- 原型验证

---

### 3. Secure OpenClaw ⭐ 1,362

> 安全强化版本

| 属性 | 值 |
|------|-----|
| GitHub | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) |
| 语言 | TypeScript |
| Stars | 1,362 |

**简介**
专注于安全的 OpenClaw 变种，提供企业级安全特性。

**✅ 优点**
- 企业级安全
- 权限控制
- 审计日志

**❌ 缺点**
- 配置复杂
- 功能可能受限

**🎯 适用场景**
- 企业使用
- 对安全有高要求的场景

---

## 🇨🇳 中国特色变种

### 1. OpenClaw China ⭐ 2,913

> 中国插件全家桶

| 属性 | 值 |
|------|-----|
| GitHub | [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) |
| 语言 | TypeScript |
| Stars | 2,878 |

**支持平台**
- 🦜 飞书
- 💬 钉钉
- 🐧 QQ
- 💼 企业微信
- 📱 个人微信

**✅ 优点**
- 全面支持国内主流 IM
- 本土化做得好
- 社区活跃

**❌ 缺点**
- 部分平台需要企业资质
- 微信 hook 不稳定

**🎯 适用场景**
- 国内团队协作
- 中文环境使用

---

### 2. OpenClaw WeChat ⭐ 1,370

> 连接个人微信

| 属性 | 值 |
|------|-----|
| GitHub | [freestylefly/openclaw-wechat](https://github.com/freestylefly/openclaw-wechat) |
| Stars | 1,370 |

**简介**
让 OpenClaw 稳定连接个人微信的插件。

**✅ 优点**
- 微信生态打通
- 使用简单

**❌ 缺点**
- 微信机器人政策风险
- 需要 hook 技术

**🎯 适用场景**
- 微信营销
- 个人助理

---

### 3. OpenClaw 中文翻译版 ⭐ 3,031

> 全中文界面

| 属性 | 值 |
|------|-----|
| GitHub | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) |
| Stars | 3,031 |

**✅ 优点**
- 全流程中文
- 详细中文教程
- 每月同步更新

**❌ 缺点**
- 同步可能有延迟

**🎯 适用场景**
- 中文用户入门
- 不想看英文文档

---

## 🎯 垂直领域变种

### 1. OpenClaw-RL ⭐ 1,730

> 强化学习训练 agent

| 属性 | 值 |
|------|-----|
| GitHub | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) |
| Stars | 1,730 |

**简介**
通过对话训练 agent 的强化学习框架。

**✅ 优点**
- 支持 RL 训练
- 可定制训练流程

**🎯 适用场景**
- AI 研究
- 自定义 agent 训练

---

### 2. OpenClaw Medical Skills ⭐ 1,004

> 医疗领域技能库

| 属性 | 值 |
|------|-----|
| GitHub | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) |
| Stars | 1,004 |

**简介**
最大的开源医疗 AI 技能库。

**🎯 适用场景**
- 医疗辅助
- 健康咨询

---

### 3. nof1.ai ⭐ 569

> AI 交易系统

| 属性 | 值 |
|------|-----|
| GitHub | [195440/nof1.ai](https://github.com/195440/nof1.ai) |
| Stars | 569 |

**简介**
自主 AI 交易系统。

**🎯 适用场景**
- 量化交易
- 金融分析

---

## 🛠️ 工具与仪表板

### 1. ClawX ⭐ 3,772

> 桌面客户端

| 属性 | 值 |
|------|-----|
| GitHub | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) |
| Stars | 3,693 |

**简介**
OpenClaw 的桌面应用图形界面，不需要命令行。

**✅ 优点**
- 图形界面友好
- 跨平台 (Windows/macOS)
- 中国区有独立网站

**🎯 适用场景**
- 不习惯命令行的用户
- 桌面办公场景

---

### 2. OpenClaw Studio ⭐ 1,570

> Web 仪表板

| 属性 | 值 |
|------|-----|
| GitHub | [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) |
| Stars | 1,570 |

**简介**
简洁的 OpenClaw Web 管理面板。

**✅ 优点**
-界面清爽
- 功能全面

---

### 3. OpenClaw Mission Control ⭐ 2,028

> 多 agent 编排

| 属性 | 值 |
|------|-----|
| GitHub | [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) |
| Stars | 2,028 |

**简介**
AI Agent 编排仪表板，管理多 agent 协作。

**✅ 优点**
- 多 agent 管理
- 任务分配
- 协调协作

**🎯 适用场景**
- 团队使用
- 多任务处理

---

### 4. MemOS ⭐ 13,900

> 记忆操作系统

| 属性 | 值 |
|------|-----|
| GitHub | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) |
| Stars | 6,654 |

**简介**
为 LLM 和 Agent 系统提供持久记忆，支持跨任务技能复用和进化。

**✅ 优点**
- 长期记忆
- 技能进化
- 多 agent 共享

---

### 5. memU ⭐ 12,900

> 记忆系统

| 属性 | 值 |
|------|-----|
| GitHub | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) |
| Stars | 12,844 |

**简介**
为 24/7 主动 agent 提供记忆系统。

---

## 📦 记忆与存储

| 项目 | Stars | 描述 |
|------|-------|------|
| memU | 12,844 | 记忆系统 |
| MemOS | 6,654 | 记忆 OS |
| openclaw-supermemory | 584 | 长期记忆 |

---

## 🚀 自动化变种 (AutoClaw 系列)

### 1. AutoClaw ⭐ 40

> 超轻量级自动化 Agent

| 属性 | 值 |
|------|-----|
| GitHub | [tsingliuwin/autoclaw](https://github.com/tsingliuwin/autoclaw) |
| Stars | 40 |

**简介**
超轻量级 AI Agent，设计运行在 Docker 容器内。与重量级 GUI 依赖的 Agent 不同，AutoClaw 为无头、大规模并发而构建。

**✅ 优点**
- 超轻量级
- 容器化运行
- 适合大规模并发
- 无 GUI 依赖

**❌ 缺点**
- Stars 较低，社区较小
- 功能可能较基础

**🎯 适用场景**
- 服务器部署
- 大规模自动化任务
- 资源敏感环境

---

### 2. AutoClaw Web ⭐ 3

> Web 安装助手

| 属性 | 值 |
|------|-----|
| GitHub | [my3rdstory/autoclaw-web](https://github.com/my3rdstory/autoclaw-web) |
| Stars | 3 |

**简介**
在网页界面中帮助安装 OpenClaw 的工具。

---

### 3. AutoClawD ⭐ 2

> macOS  ambient AI

| 属性 | 值 |
|------|-----|
| GitHub | [sameeeeeeep/autoclawd](https://github.com/sameeeeeeep/autoclawd) |
| Stars | 2 |

**简介**
macOS 上的环境 AI，无需提示词即可持续工作。持续监听对话，理解你的世界，在工作和生活中自主完成任务。

---

### 4. AutoClaw Browser ⭐ 0

> 浏览器自动化

| 属性 | 值 |
|------|-----|
| GitHub | [hasd52636-a11y/autoclaw-browser](https://github.com/hasd52636-a11y/autoclaw-browser) |
| Stars | 0 |

**简介**
OpenClaw 浏览器自动化技能，支持 MCP 协议。

---

### 5. AutoClaw Skills ⭐ 0

> 技能扩展

| 属性 | 值 |
|------|-----|
| GitHub | [gula00/autoclaw-skills](https://github.com/gula00/autoclaw-skills) |
| Stars | 0 |

**简介**
AutoClaw 技能扩展。

---

## 🔧 其他有趣变种

### 1. Edict ⭐ 8,169

> 三省六部制 · OpenClaw 多 Agent 编排系统

| 属性 | 值 |
|------|-----|
| GitHub | [cft0808/edict](https://github.com/cft0808/edict) |
| Stars | 8,169 |

**简介**
🏛️ 三省六部制 · OpenClaw 多 Agent 编排系统 — 9 个专业 AI agents，配备实时仪表板、模型配置和完整审计追踪。

**✅ 优点**
- 9 个专业化 Agent 协作
- 实时仪表板
- 完整审计日志
- 中国古代官制风格

**🎯 适用场景**
- 多 Agent 复杂任务
- 企业级编排
- 需要审计的工作流

---

### 2. LangBot ⭐ 15,532

> 生产级多平台智能机器人开发平台

| 属性 | 值 |
|------|-----|
| GitHub | [langbot-app/LangBot](https://github.com/langbot-app/LangBot) |
| Stars | 15,530 |

**简介**
生产级多平台智能机器人开发平台。提供 Agent、知识库编排、插件系统。支持 Discord / Slack / LINE / Telegram / WeChat / 飞书 / 钉钉 / QQ 等。

**✅ 优点**
- 支持 10+ 平台
- 集成 DeepSeek, Claude, Gemini 等
- 知识库编排
- 插件系统

**🎯 适用场景**
- 企业级机器人
- 多平台运营
- 需要知识库的场景

---

### 3. Nocturne Memory ⭐ 619

> 轻量级可回滚的长期记忆服务器

| 属性 | 值 |
|------|-----|
| GitHub | [Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory) |
| Stars | 619 |

**简介**
轻量级、可回滚、可视化的 MCP Agents 长期记忆服务器。

**✅ 优点**
- 图结构持久记忆
- 可回滚
- 即插即用

---

### 4. Claw Empire ⭐ 613

> AI Agent 办公室模拟器

| 属性 | 值 |
|------|-----|
| GitHub | [GreenSheep01201/claw-empire](https://github.com/GreenSheep01201/claw-empire) |
| Stars | 613 |

**简介**
从 CEO 办公桌指挥你的 AI Agent 帝国。

---

### 5. Overture ⭐ 596

> MCP 可视化流程图

| 属性 | 值 |
|------|-----|
| GitHub | [SixHq/Overture](https://github.com/SixHq/Overture) |
| Stars | 596 |

**简介**
将 AI 编码 Agent 的执行计划映射为交互式流程图。

---

### 6. AI Maesto ⭐ 523

> AI Agent 编排器

| 属性 | 值 |
|------|-----|
| GitHub | [23blocks-OS/ai-maestro](https://github.com/23blocks-OS/ai-maestro) |
| Stars | 523 |

---

### 7. OpenClaw Dashboard ⭐ 386

> 安全实时监控仪表板

| 属性 | 值 |
|------|-----|
| GitHub | [tugcantopaloglu/openclaw-dashboard](https://github.com/tugcantopaloglu/openclaw-dashboard) |
| Stars | 386 |

---

### 8. Agents Radar ⭐ 378

> AI 生态动态追踪

| 属性 | 值 |
|------|-----|
| GitHub | [duanyytop/agents-radar](https://github.com/duanyytop/agents-radar) |
| Stars | 378 |

---

### 9. OpenClaw Zero Token ⭐ 1,658

> 无需 API Key

| 属性 | 值 |
|------|-----|
| GitHub | [linuxhsj/openclaw-zero-token](https://github.com/linuxhsj/openclaw-zero-token) |

**简介**
支持所有主流 AI 模型，无需 API Token。

**支持模型**
Claude / ChatGPT / Gemini / DeepSeek / Doubao / Grok / Qwen / Manus / Kimi

---

### 2. Poco-Claw ⭐ 1,139

> 更美观的替代方案

| 属性 | 值 |
|------|-----|
| GitHub | [poco-ai/poco-claw](https://github.com/poco-ai/poco-claw) |
| Stars | 1,139 |

**简介**
更美观、更易用的 OpenClaw 替代品。拥有更漂亮的 Web UI、内置 IM 支持，以及沙箱运行时提高安全性。底层由 Claude Code 驱动。

**✅ 优点**
- Web UI 更美观
- 内置 IM 支持
- 沙箱运行时更安全

**❌ 缺点**
- 依赖 Claude Code

**🎯 适用场景**
- 追求美观 UI 的用户
- 需要内置 IM 功能

---

### 3. Antfarm ⭐ 2,120

> 一命令构建 Agent 团队

| 属性 | 值 |
|------|-----|
| GitHub | [snarktank/antfarm](https://github.com/snarktank/antfarm) |
| Stars | 2,120 |

**简介**
在 OpenClaw 中用一条命令构建你的 Agent 团队。

**✅ 优点**
- 快速构建多 Agent 团队
- 简化协作配置

**🎯 适用场景**
- 多 Agent 协作任务
- 复杂工作流

---

### 4. Lobster ⭐ 802

> 原生工作流引擎

| 属性 | 值 |
|------|-----|
| GitHub | [openclaw/lobster](https://github.com/openclaw/lobster) |
| Stars | 802 |

**简介**
OpenClaw 原生工作流 Shell：类型化、本地优先的"宏引擎"，将技能/工具转换为可组合的管道和安全自动化——一步调用这些工作流。

**✅ 优点**
- 类型化工作流
- 本地优先
- 安全自动化

**🎯 适用场景**
- 工作流自动化
- 复杂任务编排

---

### 5. Crabwalk ⭐ 859

> 实时伴侣监控

| 属性 | 值 |
|------|-----|
| GitHub | [crabwise-ai/crabwalk](https://github.com/crabwise-ai/crabwalk) |
| Stars | 859 |

**简介**
🦀 OpenClaw Agent 的实时伴侣监控器。

**✅ 优点**
- 实时监控
- 可视化展示

**🎯 适用场景**
- 调试 Agent
- 实时观察 Agent 行为

---

### 6. MicroClaw ⭐ 546

> Rust 实现

| 属性 | 值 |
|------|-----|
| GitHub | [microclaw/microclaw](https://github.com/microclaw/microclaw) |

**简介**
受 nanoclaw 启发的轻量级 AI 助手，使用 Rust 编写。

---

### 3. Clawra ⭐ 2,031

> AI 伴侣

| 属性 | 值 |
|------|-----|
| GitHub | [SumeLabs/clawra](https://github.com/SumeLabs/clawra) |

**简介**
作为伴侣的 OpenClaw。

---

### 4. AIRI ⭐ 32,660

> 虚拟偶像伴侣

| 属性 | 值 |
|------|-----|
| GitHub | [moeru-ai/airi](https://github.com/moeru-ai/airi) |

**简介**
自托管的 Grok 伴侣，虚拟偶像容器。支持实时语音聊天、MC 游戏、Factorio。

---

### 5. ClawHub ⭐ 5,459

> 技能目录

| 属性 | 值 |
|------|-----|
| GitHub | [openclaw/clawhub](https://github.com/openclaw/clawhub) |

**简介**
OpenClaw 官方技能目录。

---

### 6. Cloud-Claw ⭐ 239

> 一键 Cloudflare 部署

| 属性 | 值 |
|------|-----|
| GitHub | [miantiaome/cloud-claw](https://github.com/miantiao-me/cloud-claw) |

**简介**
一键在 Cloudflare Containers 部署。

---

## 📊 变种对比表

| 项目 | Stars | 轻量 | 中国支持 | 桌面端 | 记忆 | 安全 |
|------|-------|------|----------|--------|------|------|
| **NanoClaw** | 21,782 | ✅ | ❌ | ❌ | ✅ | ✅ |
| **MoltWorker** | 9,573 | ✅ | ❌ | ❌ | ❌ | ✅ |
| **OpenClaw China** | 2,878 | ❌ | ✅ | ❌ | ❌ | ❌ |
| **ClawX** | 3,693 | ❌ | ✅ | ✅ | ❌ | ❌ |
| **MemOS** | 6,654 | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Secure OpenClaw** | 1,362 | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Zero Token** | 1,658 | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## 🆚 选择指南

### 我该选哪个？

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

## 📝 如何贡献

欢迎提交 PR 添加新的 OpenClaw 变种！

1. Fork 本项目
2. 添加变种信息到对应章节
3. 提交 Pull Request

---

## 📚 参考链接

- [OpenClaw 官方](https://github.com/openclaw/openclaw)
- [OpenClaw 文档](https://docs.openclaw.ai)
- [ClawHub 技能市场](https://clawhub.com)

---

## 🚀 部署教程汇总

### Docker 部署

| 教程 | 来源 | 推荐度 |
|------|------|--------|
| NanoClaw Docker 部署 | [官方 Wiki](https://github.com/qwibitai/nanoclaw) | ⭐⭐⭐⭐⭐ |
| OpenClaw Docker 全指南 | [OpenClaw Docs](https://docs.openclaw.ai) | ⭐⭐⭐⭐⭐ |
| Cloudflare Workers 部署 | [MoltWorker README](https://github.com/cloudflare/moltworker) | ⭐⭐⭐⭐ |

### 一键部署

| 项目 | 命令/链接 |
|------|-----------|
| NanoClaw | `docker run -d --name nanoclaw -v ~/.openclaw:/home/openclaw/.openclaw qwibitai/nanoclaw` |
| Cloud-Claw | [GitHub](https://github.com/miantiao-me/cloud-claw) |

### 平台特定教程

- **macOS**: [OpenClaw macOS 安装指南](https://docs.openclaw.ai)
- **Linux**: [Ubuntu/Debian 安装](https://docs.openclaw.ai)
- **Windows**: [WSL2 部署方案](https://docs.openclaw.ai)

---

## 💬 社区与资源

### 中文社区

| 社区 | 链接 | 描述 |
|------|------|------|
| OpenClaw 中文社区 | [Discord #中文](https://discord.com/invite/clawd) | 中文用户交流 |
| OpenClaw China | [GitHub](https://github.com/BytePioneer-AI/openclaw-china) | 国内变种维护 |

### 英文社区

| 社区 | 链接 | 描述 |
|------|------|------|
| OpenClaw Discord | [discord.gg/clawd](https://discord.com/invite/clawd) | 官方社区 |
| OpenClaw Reddit | [reddit.com/r/openclaw](https://reddit.com/r/openclaw) | 讨论区 |
| OpenClaw Discord | [Discord](https://discord.gg/openaiclaw) | AI Agents |

### 学习资源

| 资源 | 链接 | 描述 |
|------|------|------|
| Awesome OpenClaw | [GitHub](https://github.com/vincentkoc/awesome-openclaw) | 精选资源列表 |
| OpenClaw 官方文档 | [docs.openclaw.ai](https://docs.openclaw.ai) | 完整文档 |
| OpenClaw YouTube | [YouTube](https://youtube.com/@openclaw) | 视频教程 |

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

### Q5: 如何保障安全？

**答**: 
- 使用 Docker 容器隔离运行
- 使用 `Secure OpenClaw` 加强安全
- 不要在生产环境保存敏感信息
- 定期更新版本

### Q6: 微信/飞书机器人会被封吗？

**答**: 
- 企业微信/飞书/钉钉：官方支持，风险低
- 个人微信：存在风控风险，建议小号测试
- QQ：机器人协议相对宽松

---

## 🆕 更多变种项目

### 新兴变种

| 项目 | Stars | 特点 |
|------|-------|------|
| AIRI ⭐32,660 | 虚拟偶像伴侣 | 实时语音聊天、游戏集成 |
| ClawHub ⭐5,459 | 技能市场 | 官方认证技能目录 |
| Clawra ⭐2,031 | AI 伴侣 | 情感陪伴 |
| ClawWork ⭐- | 工作流 | AI 工作流自动化 |

### 研究项目

| 项目 | Stars | 领域 |
|------|-------|------|
| OpenClaw-RL ⭐1,730 | 强化学习 | Agent 训练 |
| OpenClaw-Medical ⭐1,004 | 医疗 | 医疗技能库 |

### 轻量级变种

| 项目 | Stars | 特点 |
|------|-------|------|
| MicroClaw ⭐546 | Rust 实现 | 高性能 |
| mini-claw ⭐- | 极简 | 最少依赖 |

---

## 📈 项目统计

> 截至 2026-03-12

| 分类 | 项目数 | 最高 Stars |
|------|--------|------------|
| 热门变种 | 10 | 35,862 (awesome-openclaw-skills) |
| 核心变种 | 4 | 26,298 (ZeroClaw) |
| 中国特色 | 3 | 15,532 (LangBot) |
| AutoClaw 系列 | 5 | 40 |
| 垂直领域 | 3 | 1,730 |
| 工具仪表板 | 7 | 13,900 (MemOS) |
| 记忆系统 | 3 | 12,900 (memU) |

---

## 🙏 致谢

感谢所有为 OpenClaw 生态贡献的开发者！

- NanoClaw - 轻量级替代
- MoltWorker - Serverless 部署
- OpenClaw China - 国内生态
- ClawHub - 技能市场
- 所有变种维护者

---

*🦞 Last updated: 2026-03-12 | ClawDen - OpenClaw 变种收集站*

