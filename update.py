#!/usr/bin/env python3
"""
ClawDen 自动更新脚本
使用 Tavily API 搜索 GitHub 上的 OpenClaw 变种项目
"""

import subprocess
import json
import re
import os
from datetime import datetime

TAVILY_KEY = os.environ.get("TAVILY_API_KEY", "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")
TAVILY_SCRIPT = "/Users/caisd1/.openclaw/workspace/skills/tavily-search/scripts/search.mjs"

# 搜索查询
SEARCH_QUERIES = [
    "github openclaw fork nanoclaw moltworker",
    "github openclaw variant MemOS memU", 
    "github openclaw China wechat feishu",
    "github openclaw clawX studio desktop",
    "github openclaw alternative microclaw clawra"
]

def tavily_search(query: str, count: int = 10) -> list:
    """使用 Tavily 搜索"""
    try:
        result = subprocess.run(
            ["node", TAVILY_SCRIPT, query, "-n", str(count)],
            capture_output=True, text=True, timeout=60,
            env={**os.environ, "TAVILY_API_KEY": TAVILY_KEY}
        )
        output = result.stdout
        
        # 解析结果 - 提取 GitHub 链接
        github_repos = []
        github_pattern = re.compile(r'https://github\.com/([^\s]+)')
        
        for match in github_pattern.finditer(output):
            repo = match.group(1).rstrip('/')
            # 清理
            if repo.endswith('#'):
                repo = repo[:-1]
            # 排除非仓库链接
            if '/' in repo and not repo.startswith('github.com'):
                github_repos.append(f"https://github.com/{repo}")
        
        return list(set(github_repos))
    except Exception as e:
        print(f"搜索失败: {e}")
    return []

def get_repo_info(url: str) -> dict:
    """从 GitHub URL 获取仓库信息"""
    # 使用 GitHub API (需要 token) 或简单解析
    match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
    if not match:
        return {}
    
    owner, repo = match.groups()
    repo = repo.split('#')[0].split('?')[0]  # 清理
    
    return {
        "url": url,
        "owner": owner,
        "repo": repo,
        "full_name": f"{owner}/{repo}"
    }

def update_readme(projects: list):
    """更新 README.md"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 解析项目信息
    project_cards = []
    for url in projects[:20]:
        info = get_repo_info(url)
        if info:
            name = info["repo"]
            # 简单分类
            cat = "其他"
            n = name.lower()
            if any(x in n for x in ["china", "wechat", "qq", "ding", "feishu"]):
                cat = "中国特色"
            elif any(x in n for x in ["nano", "micro", "lite", "worker", "mini"]):
                cat = "轻量级"
            elif any(x in n for x in ["mem", "memory", "super"]):
                cat = "记忆系统"
            elif any(x in n for x in ["studio", "x", "ui", "dash"]):
                cat = "工具仪表板"
            elif any(x in n for x in ["medical", "health", "rl"]):
                cat = "垂直领域"
            elif any(x in n for x in ["secure", "safe", "zero"]):
                cat = "安全"
            
            project_cards.append(f"""### {name}

| 属性 | 值 |
|------|-----|
| GitHub | [{name}]({url}) |
| 分类 | {cat} |

""")
    
    # 读取现有文件
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
    except:
        content = ""
    
    # 更新最后时间
    content = re.sub(r'\*Last updated: \d{4}-\d{2}-\d{2}', f'*Last updated: {today}', content)
    
    # 新章节
    new_section = f"""---

## 🔥 热门变种项目 (自动更新于 {today})

> 通过 Tavily 自动搜索收录

"""
    new_section += "\n".join(project_cards)
    
    # 替换
    if "## 🔥 热门变种项目" in content:
        pattern = r'## 🔥 热门变种项目.*?(?=\n## |\n---|\n\*Last|$)'
        content = re.sub(pattern, new_section + "\n---\n", content, flags=re.DOTALL)
    else:
        content = content + "\n" + new_section
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"已更新 {len(project_cards)} 个项目")

def git_commit_push():
    """提交到 GitHub"""
    try:
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd="/Users/caisd1/code/ClawDen")
        if not result.stdout.strip():
            print("没有更改")
            return
        
        subprocess.run(["git", "add", "README.md"], cwd="/Users/caisd1/code/ClawDen", check=True)
        subprocess.run(
            ["git", "commit", "-m", f"docs: 更新 OpenClaw 变种列表 - {datetime.now().strftime('%Y-%m-%d')}"],
            cwd="/Users/caisd1/code/ClawDen", check=True
        )
        subprocess.run(["git", "push"], cwd="/Users/caisd1/code/ClawDen", check=True)
        print("✅ 已提交到 GitHub")
    except Exception as e:
        print(f"Git 失败: {e}")

def main():
    print("🔍 搜索 OpenClaw 变种项目...")
    
    all_urls = []
    for query in SEARCH_QUERIES:
        print(f"  查询: {query}")
        urls = tavily_search(query)
        all_urls.extend(urls)
    
    # 去重
    all_urls = list(set(all_urls))
    # 排除官方
    all_urls = [u for u in all_urls if 'openclaw/openclaw' not in u]
    
    print(f"\n找到 {len(all_urls)} 个项目")
    
    update_readme(all_urls)
    git_commit_push()
    print("✨ 完成!")

if __name__ == "__main__":
    main()
