# 🦞 ClawDen - OpenClaw 变种收集站

> 收集基于 OpenClaw 开发的各种变种项目，了解它们的优缺点和适用场景

---

## 📋 目录

- [项目地图](#项目地图)
- [核心变种](#核心变种)
- [中国特色变种](#中国特色变种)
- [轻量级变种](#轻量级变种)
- [垂直领域变种](#垂直领域变种)
- [工具与周边](#工具与周边)
- [变种对比表](#变种对比表)

---

## 🗺️ 项目地图

```
OpenClaw (原 Clawdbot / Moltbot)
    │
    ├── 🔥 核心变种
    │   ├── nanoclaw         (轻量化替代)
    │   ├── moltworker       (Cloudflare Workers)
    │   └── secure-openclaw  (安全强化)
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
    │   └── tenacitOS        (Mission Control)
    │
    └── 📦 记忆与存储
        ├── memU             (记忆系统)
        ├── MemOS            (记忆 OS)
        └── openclaw-supermemory (长期记忆)
```

---

## 🔥 核心变种

### 1. NanoClaw ⭐ 21,782

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

### 1. OpenClaw China ⭐ 2,878

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

### 1. ClawX ⭐ 3,693

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

### 4. MemOS ⭐ 6,654

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

### 5. memU ⭐ 12,844

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

## 🔧 其他有趣变种

### 1. OpenClaw Zero Token ⭐ 1,658

> 无需 API Key

| 属性 | 值 |
|------|-----|
| GitHub | [linuxhsj/openclaw-zero-token](https://github.com/linuxhsj/openclaw-zero-token) |

**简介**
支持所有主流 AI 模型，无需 API Token。

**支持模型**
Claude / ChatGPT / Gemini / DeepSeek / Doubao / Grok / Qwen / Manus / Kimi

---

### 2. MicroClaw ⭐ 546

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

*🦞 Last updated: 2026-01-19 | ClawDen - OpenClaw 变种收集站*

---

---

## 🔥 热门变种项目 (自动更新于 2026-03-12)

> 通过 Tavily 自动搜索收录

### memUBot).

| 属性 | 值 |
|------|-----|
| GitHub | [memUBot).](https://github.com/NevaMind-AI/memUBot).) |
| 分类 | 记忆系统 |


### openclaw-china

| 属性 | 值 |
|------|-----|
| GitHub | [openclaw-china](https://github.com/BytePioneer-AI/openclaw-china/issues).) |
| 分类 | 中国特色 |


### memUBot

| 属性 | 值 |
|------|-----|
| GitHub | [memUBot](https://github.com/NevaMind-AI/memUBot#-why-memubot)) |
| 分类 | 记忆系统 |


### mini-claw

| 属性 | 值 |
|------|-----|
| GitHub | [mini-claw](https://github.com/htlin222/mini-claw) |
| 分类 | 轻量级 |


### moltw...

| 属性 | 值 |
|------|-----|
| GitHub | [moltw...](https://github.com/cloudflare/moltw...) |
| 分类 | 其他 |


### MemOS

| 属性 | 值 |
|------|-----|
| GitHub | [MemOS](https://github.com/MemTensor/MemOS) |
| 分类 | 记忆系统 |


### moltworker

| 属性 | 值 |
|------|-----|
| GitHub | [moltworker](https://github.com/cloudflare/moltworker/actions).) |
| 分类 | 轻量级 |


### openclaw-plugin-feishu

| 属性 | 值 |
|------|-----|
| GitHub | [openclaw-plugin-feishu](https://github.com/xzq-xu/openclaw-plugin-feishu/tree/main/scripts) |
| 分类 | 中国特色 |


### ClawWork

| 属性 | 值 |
|------|-----|
| GitHub | [ClawWork](https://github.com/HKUDS/ClawWork/actions).) |
| 分类 | 其他 |


### memUBot

| 属性 | 值 |
|------|-----|
| GitHub | [memUBot](https://github.com/NevaMind-AI/memUBot) |
| 分类 | 记忆系统 |


### openclaw-plugin-feishu

| 属性 | 值 |
|------|-----|
| GitHub | [openclaw-plugin-feishu](https://github.com/xzq-xu/openclaw-plugin-feishu/...) |
| 分类 | 中国特色 |


### moltworker

| 属性 | 值 |
|------|-----|
| GitHub | [moltworker](https://github.com/cloudflare/moltworker/blob/main/start-openclaw.sh) |
| 分类 | 轻量级 |


### openclaw-china).

| 属性 | 值 |
|------|-----|
| GitHub | [openclaw-china).](https://github.com/BytePioneer-AI/openclaw-china).) |
| 分类 | 中国特色 |


### ClawX)

| 属性 | 值 |
|------|-----|
| GitHub | [ClawX)](https://github.com/ValueCell-ai/ClawX)) |
| 分类 | 工具仪表板 |


### openclaw-china)

| 属性 | 值 |
|------|-----|
| GitHub | [openclaw-china)](https://github.com/BytePioneer-AI/openclaw-china)) |
| 分类 | 中国特色 |


### moltworker

| 属性 | 值 |
|------|-----|
| GitHub | [moltworker](https://github.com/cloudflare/moltworker) |
| 分类 | 轻量级 |


### ClawWork

| 属性 | 值 |
|------|-----|
| GitHub | [ClawWork](https://github.com/HKUDS/ClawWork) |
| 分类 | 其他 |


### explain-openclaw

| 属性 | 值 |
|------|-----|
| GitHub | [explain-openclaw](https://github.com/centminmod/explain-openclaw/blob/master/03-deploy/cloudflare-moltworker.md) |
| 分类 | 工具仪表板 |


### awesome-openclaw

| 属性 | 值 |
|------|-----|
| GitHub | [awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw) |
| 分类 | 其他 |


### openclaw-plugin-feishu

| 属性 | 值 |
|------|-----|
| GitHub | [openclaw-plugin-feishu](https://github.com/xzq-xu/openclaw-plugin-feishu) |
| 分类 | 中国特色 |


---

