#!/usr/bin/env python3
"""
OpenClaw 变种项目每日维护脚本
自动收集 GitHub 上基于 OpenClaw 的变种项目，更新文档并提交
"""

import os
import json
import subprocess
from datetime import datetime
import urllib.request
import urllib.parse

# 项目路径
REPO_PATH = "/Users/caisd1/code/ClawDen"
README_PATH = os.path.join(REPO_PATH, "README.md")

# GitHub API 配置
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

def search_github_repos(query, per_page=50):
    """搜索 GitHub 仓库"""
    url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(query)}&sort=stars&per_page={per_page}"
    
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode())
            return data.get("items", [])
    except Exception as e:
        print(f"Error searching: {e}")
        return []

def get_openclaw_forks():
    """获取 OpenClaw 的 forks 和相关项目"""
    repos = []
    
    # 搜索关键词
    queries = [
        "openclaw",
        "autoclaw",
        "clawdbot",
        "nanoclaw",
        "claude+agent+orchestration",
    ]
    
    for query in queries:
        print(f"Searching: {query}")
        results = search_github_repos(query)
        repos.extend(results)
    
    # 去重
    seen = set()
    unique_repos = []
    for repo in repos:
        if repo["full_name"] not in seen:
            seen.add(repo["full_name"])
            unique_repos.append(repo)
    
    # 按 stars 排序
    unique_repos.sort(key=lambda x: x.get("stargazers_count", 0), reverse=True)
    
    return unique_repos[:100]

def generate_markdown_table(repos):
    """生成变种对比表"""
    header = """| 项目 | Stars | 描述 |
|------|-------|------|
"""
    
    rows = []
    for repo in repos[:30]:
        name = repo.get("full_name", "").split("/")[-1]
        stars = repo.get("stargazers_count", 0)
        desc = repo.get("description", "")[:60] or "暂无描述"
        rows.append(f"| [{name}]({repo.get('html_url', '')}) | {stars} | {desc} |")
    
    return header + "\n".join(rows)

def update_readme(repos):
    """更新 README"""
    # 读取现有 README
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 更新日期
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 在"最后更新"处添加新内容（如果存在）
    update_marker = "## 📝 最后更新"
    
    if update_marker in content:
        # 更新现有表格
        pass
    else:
        # 添加更新部分
        content += f"\n\n{update_marker}\n{today}\n"
    
    # 生成新表格
    new_table = generate_markdown_table(repos)
    
    # 简单的插入逻辑 - 在"变种对比表"之后插入新表格
    table_marker = "## 📊 变种对比表"
    if table_marker in content:
        content = content.replace(
            table_marker,
            f"{table_marker}\n\n### 🔥 热门项目排行 ({today})\n{new_table}"
        )
    
    # 写回
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    
    return content

def commit_and_push():
    """提交并推送"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # git add
    subprocess.run(["git", "add", "-A"], cwd=REPO_PATH, check=True)
    
    # git commit
    commit_msg = f"chore: 每日更新 - {today}"
    result = subprocess.run(
        ["git", "commit", "-m", commit_msg],
        cwd=REPO_PATH,
        capture_output=True
    )
    
    if result.returncode != 0:
        if "nothing to commit" in result.stderr.decode():
            print("没有变化需要提交")
            return False
        print(f"Commit error: {result.stderr.decode()}")
        return False
    
    # git push
    subprocess.run(["git", "push"], cwd=REPO_PATH, check=True)
    
    return True

def main():
    print(f"🚀 开始每日维护 - {datetime.now()}")
    
    # 1. 收集项目
    print("📡 收集 OpenClaw 变种项目...")
    repos = get_openclaw_forks()
    print(f"   找到 {len(repos)} 个相关项目")
    
    # 2. 更新 README
    print("📝 更新文档...")
    update_readme(repos)
    
    # 3. 提交
    print("📤 提交更改...")
    if commit_and_push():
        print("✅ 每日维护完成!")
    else:
        print("ℹ️ 没有需要提交的更改")

if __name__ == "__main__":
    main()
