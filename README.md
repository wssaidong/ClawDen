# OpenClaw 版本收集 (ClawDen 🦞)

> 收集 GitHub 上各个版本的 OpenClaw 内容，分析优缺点和使用场景

## 项目简介

OpenClaw 是一个本地运行的个人 AI 助手，可以在各种平台上运行（WhatsApp、Telegram、Slack、Discord、Google Chat、Signal、iMessage 等）。它的核心理念是"Any OS. Any Platform. The lobster way."

## 版本发布策略

OpenClaw 采用三个发布通道：

| 通道 | 标签格式 | npm dist-tag | 说明 |
|------|----------|--------------|------|
| **Stable** | vYYYY.M.D | latest | 正式发布版本 |
| **Beta** | vYYYY.M.D-beta.N | beta | 预发布版本 |
| **Dev** | main 分支最新 | dev | 开发版本 |

---

## 版本时间线

### 2026年3月

| 版本 | 发布日期 | 类型 | 主要特性 |
|------|----------|------|----------|
| [v2026.3.8](#v2026.3.8) | 2026-03-09 | Stable | CLI/backup、Talk mode 静默超时、远程 Gateway token |
| [v2026.3.8-beta.1](#v2026.3.8-beta1) | 2026-03-09 | Beta | 2026.3.8 beta 测试版 |
| [v2026.3.7](#v2026.3.7) | 2026-03-08 | Stable | 构建准备版本 |
| [v2026.3.7-beta.1](#v2026.3.7-beta1) | 2026-03-08 | Beta | 2026.3.7 beta 测试版 |
| [v2026.3.2](#v2026.3.2) | 2026-03-03 | Stable | 月度稳定版 |
| [v2026.3.2-beta.1](#v2026.3.2-beta1) | 2026-03-03 | Beta | 2026.3.2 beta 测试版 |
| [v2026.3.1](#v2026.3.1) | 2026-03-02 | Stable | 文档更新版本 |

### 2026年2月

| 版本 | 发布日期 | 类型 | 主要特性 |
|------|----------|------|----------|
| [v2026.2.26](#v2026.2.26) | 2026-02-26 | Stable | 月末稳定版 |
| [v2026.2.26-beta.1](#v2026.2.26-beta1) | 2026-02-26 | Beta | 2026.2.26 beta 测试版 |
| [v2026.2.25](#v2026.2.25) | 2026-02-26 | Stable | 月度稳定版 |

---

## 详细版本记录

### v2026.3.8

**发布日期：** 2026-03-09  
**类型：** Stable (Immutable)  
**Commit:** 3caab92

#### 新增功能

| 功能 | 描述 |
|------|------|
| **CLI/backup** | 新增 `openclaw backup create` 和 `openclaw backup verify` 命令，支持本地状态归档，包括 `--only-config`、`--no-include-workspace`、清单/负载验证 |
| **macOS onboarding** | 新增远程 Gateway token 字段，保留现有非明文 `gateway.remote.token` 配置值 |
| **Talk mode** | 新增 `talk.silenceTimeoutMs` 配置项，可设置自动发送前的静默等待时间 |
| **TUI** | 从当前工作区推断活动 agent，支持显式 agent 会话目标 |
| **Brave web search** | 新增 `tools.web.search.brave.mode: "llm-context"` 选项，支持 LLM Context 端点 |
| **CLI/install** | `openclaw --version` 输出包含短 git commit hash |
| **ACP/Provenance** | 新增可选 ACP 入口溯源元数据和可见收据注入 |

#### 修复内容

- macOS launchd 重启：重新启用已禁用的 LaunchAgent 服务
- macOS 聊天 UI：路由浏览器代理、保留纯文本粘贴语义
- Android Play 分发：移除自更新后台位置等
- Telegram DM 路由：去重
- Matrix DM 路由：修复 homeserver 检测
- 浏览器扩展中继：支持 WSL2 跨命名空间
- TUI 主题：检测浅色终端背景
- 模型切换：清除过期的 cached contextTokens

#### 优缺点分析

**优点：**
- ✅ 备份功能增强，数据安全更有保障
- ✅ Talk mode 静默超时设置，语音交互更自然
- ✅ 远程 Gateway token 支持，部署更灵活
- ✅ 多平台 DM 路由修复

**缺点：**
- ❌ macOS 相关功能依赖 Apple 生态
- ❌ 部分功能配置复杂

**适用场景：**
- 需要数据备份的企业用户
- 远程部署场景
- 语音交互需求强的用户

---

### v2026.3.7

**发布日期：** 2026-03-08  
**类型：** Stable (Immutable)  
**Commit:** 42a1394

#### 主要内容

构建准备版本，包含底层优化和测试改进。

#### 优缺点分析

**优点：**
- ✅ 稳定的基础版本
- ✅ 适合追求稳定的用户

**缺点：**
- ❌ 无重大新功能

**适用场景：**
- 日常使用
- 追求稳定不需要最新功能的用户

---

### v2026.3.2

**发布日期：** 2026-03-03  
**类型：** Stable (Immutable)  
**Commit:** 85377a2

#### 主要内容

月度稳定版本，包含多项改进。

#### 优缺点分析

**优点：**
- ✅ 月度例行更新
- ✅ 稳定性有保障

**适用场景：**
- 常规使用
- 长期稳定运行需求

---

### v2026.2.26

**发布日期：** 2026-02-26  
**类型：** Stable (Immutable)  
**Commit:** bc50708

#### 主要内容

月末稳定版本。

#### 优缺点分析

**优点：**
- ✅ 月末例行更新

**适用场景：**
- 定期更新用户

---

### v2026.2.25

**发布日期：** 2026-02-26  
**类型：** Stable (Immutable)  
**Commit:** 4b5d4a4

#### 主要内容

月度稳定版本，完成发布说明和 appcast 更新。

#### 优缺点分析

**优点：**
- ✅ 月度大版本
- ✅ 完整的发布文档

**适用场景：**
- 需要完整功能集的用户

---

## Beta 版本说明

Beta 版本（vYYYY.M.D-beta.N）是预发布版本，包含即将在稳定版中发布的新功能。

**特点：**
- 🧪 测试新功能
- ⚠️ 可能存在不稳定因素
- 📋 适合愿意尝试新功能的用户

**建议：**
- 生产环境使用 Stable 版本
- 测试环境可以使用 Beta 版本

---

## 各版本对比

| 特性 | v2026.2.25 | v2026.3.x | Beta |
|------|-------------|-----------|------|
| 备份功能 | ❌ | ✅ | ✅ |
| 远程 Gateway token | ❌ | ✅ | ✅ |
| Talk 静默超时 | ❌ | ✅ | ✅ |
| Brave LLM Context | ❌ | ✅ | ✅ |
| 稳定性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## 安装指南

### 稳定版（推荐）

```bash
npm install -g openclaw@latest
# 或
pnpm add -g openclaw@latest
```

### Beta 版

```bash
npm install -g openclaw@beta
```

### Dev 版

```bash
npm install -g openclaw@dev
```

### 从源码构建

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm ui:build
pnpm build
pnpm openclaw onboard --install-daemon
```

---

## 核心功能一览

| 功能 | 描述 | 成熟度 |
|------|------|--------|
| **多渠道接入** | WhatsApp, Telegram, Slack, Discord, Signal, iMessage 等 20+ 平台 | ⭐⭐⭐⭐⭐ |
| **Voice Wake** | macOS/iOS 语音唤醒 | ⭐⭐⭐⭐ |
| **Talk Mode** | 连续语音对话（Android） | ⭐⭐⭐⭐ |
| **Live Canvas** | 代理驱动的可视化工作区 | ⭐⭐⭐⭐ |
| **多 Agent 路由** | 按渠道/账号路由到独立 Agent | ⭐⭐⭐⭐⭐ |
| **浏览器控制** | Chrome 扩展中继、CDP 控制 | ⭐⭐⭐⭐ |
| **定时任务** | Cron 作业和唤醒事件 | ⭐⭐⭐⭐⭐ |
| **记忆系统** | 会话记忆、长期记忆 | ⭐⭐⭐⭐ |

---

## 选择版本建议

### 🏠 个人用户
- 使用 `latest` 稳定版
- 足够满足日常需求

### 🏢 企业用户
- 使用 `latest` 稳定版
- 建议配置备份功能

### 🧪 测试/开发
- 可以尝试 Beta 版本
- 体验新功能

### 🔧 贡献者
- 使用 Dev 版本
- 参与功能测试

---

## 相关链接

- [OpenClaw 官网](https://openclaw.ai)
- [官方文档](https://docs.openclaw.ai)
- [GitHub Releases](https://github.com/openclaw/openclaw/releases)
- [Discord 社区](https://discord.gg/clawd)
- [更新指南](https://docs.openclaw.ai/install/updating)

---

*本文档由 ClawDen 自动生成*
