# Agent Skills (Macnversion Fork)

本项目是 Anthropic Agent Skills 的 Fork 版本，旨在收集和管理适用于 AI Agent 的各种能力（Skills）。

Skills 是指一组指令、脚本和资源的集合，AI 模型（如 Claude）可以动态加载这些 Skills 来完成特定领域的任务，例如文档处理、代码生成或创意设计。

## 1. 目录结构规范

每个 Skill 都必须是一个独立的文件夹，并包含核心的描述文件。

### 标准结构示例
```text
skills/
└── my-skill-name/          <-- Skill 文件夹 (名称必须为小写, 用连字符分隔)
    ├── SKILL.md            <-- [必须] 核心定义文件 (包含 YAML 头信息和 Markdown 指令)
    ├── scripts/            <-- [可选] 辅助脚本 (Python, Node.js 等)
    └── resources/          <-- [可选] 静态资源文件 (模板, 图片等)
```

### SKILL.md 格式要求
`SKILL.md` 文件必须以 YAML frontmatter 开头：
```markdown
---
name: my-skill-name        # 必须与文件夹名称一致
description: 简短描述这个 Skill 的功能和适用场景
---

# My Skill Name

[详细的 Prompt 指令内容...]
```

---

## 2. 安装与使用指南

本项目支持两种主流的使用场景：**Claude Code** (命令行工具) 和 **Open Code** (开源环境)。

### 场景 A: Claude Code (Marketplace 模式)

在 Claude Code 中，Skills 是通过 Marketplace 插件的形式加载的。

#### 核心机制：白名单
本项目根目录下的 `.claude-plugin/marketplace.json` 文件充当了 **白名单**。
*   **注意**：在 `skills/` 目录下添加新文件夹 **不会** 自动对 Claude Code 可见。
*   **必须**：您必须在 `marketplace.json` 的 `plugins` 列表中显式添加该 Skill 的配置，Claude Code 才能识别和安装它。

#### 安装步骤
1.  **注册 Marketplace**:
    在 Claude Code 终端运行：
    ```bash
    /plugin marketplace add src  # 如果是在当前目录运行
    # 或者指定绝对路径
    /plugin marketplace add /path/to/this/repo
    ```

2.  **安装 Skill**:
    ```bash
    /plugin install docx      # 安装单个 Skill
    /plugin install pdf       # 安装单个 Skill
    ```
    *提示：运行 `/plugin list` 可以查看当前已安装的 Skill。*

---

### 场景 B: Open Code (独立环境)

Open Code 等开源工具通常通过读取本地特定的配置文件目录来加载 Skills。本项目提供了一个自动化脚本，方便您将 Skills 同步到 Open Code 的配置环境中。

#### 安装脚本
我们提供了一个功能完备的 Python 脚本 `opencode-installer/manage_skills.py`，它不仅可以安装 Skill，还支持查看列表和删除。

该脚本执行 **安装** 操作时，采用 **全量覆盖** 模式（先删除目标文件夹，再复制新文件），以确保您的环境始终是最新的。

#### 使用方法

1.  **安装/更新 Skill** (覆盖模式):
    ```bash
    # 安装/更新单个 Skill
    python3 opencode-installer/manage_skills.py install pdf
    
    # 安装/更新所有 Skills
    python3 opencode-installer/manage_skills.py install --all
    ```
    *这将把 `skills/pdf` 同步到 `~/.config/opencode/skills/pdf`。*

2.  **查看已安装列表**:
    ```bash
    python3 opencode-installer/manage_skills.py list
    ```

3.  **删除 Skill**:
    ```bash
    python3 opencode-installer/manage_skills.py remove pdf
    ```

4.  **查看帮助**:
    ```bash
    python3 opencode-installer/manage_skills.py --help
    ```

---

## 3. 开发须知

如果您想添加一个新的 Skill：

1.  在 `skills/` 下创建一个新文件夹（例如 `my-new-tool`）。
2.  在该文件夹内创建 `SKILL.md`，并按照规范编写。
3.  **(针对 Open Code)**: 直接运行 `python3 opencode-installer/install.py my-new-tool` 即可测试。
4.  **(针对 Claude Code)**: 编辑 `.claude-plugin/marketplace.json`，在 `plugins` 数组中添加一项：
    ```json
    {
      "name": "my-new-tool",
      "description": "Your description here",
      "source": "./skills/my-new-tool"
    }
    ```

## 4. 常见问题

**Q: 我在 skills 目录下加了文件，为什么 Claude Code 看不到？**
A: 请检查 `.claude-plugin/marketplace.json`。Claude Code 只加载该文件中列出的插件。这是为了防止未完成的草稿代码意外被加载。

**Q: opencode-installer 会覆盖我的修改吗？**
A: **是的**。为了保持版本一致性，该脚本在安装时会先删除目标目录中的旧版本。请始终在本项目 (`skills/` 目录) 中进行修改，然后使用脚本发布到 Open Code 环境。
