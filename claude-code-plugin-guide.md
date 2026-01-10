# Claude Code 插件与技能管理完整指南

本文档介绍 Claude Code 中插件（Plugin）、技能（Skill）和市场（Marketplace）的完整管理命令。

---

## 目录

- [概念说明](#概念说明)
- [市场管理](#市场管理)
- [插件管理](#插件管理)
- [技能管理](#技能管理)
- [命令速查表](#命令速查表)

---

## 概念说明

### 三层关系

```
市场 (Marketplace)
  └── 插件 (Plugin)
      └── 技能 (Skill) / 命令 (Command) / 代理 (Agent) / 钩子 (Hook)
```

| 概念 | 说明 | 示例 |
|------|------|------|
| **市场** | 插件的目录/仓库 | `claude-plugins-official`, `mac-agent-skills` |
| **插件** | 功能包，包含技能/命令等 | `frontend-design`, `pdf` |
| **技能** | 用户可调用的具体功能 | `/commit`, `/review` |

---

## 市场管理

市场是插件的目录。添加市场后，您可以浏览并安装其中的插件。

### 添加市场

```bash
# 从 GitHub 添加 (推荐)
/plugin marketplace add owner/repo

# 示例
/plugin marketplace add anthropics/claude-code

# 从 Git URL 添加 (GitLab, Bitbucket 等)
/plugin marketplace add https://gitlab.com/company/plugins.git

# 从本地路径添加
/plugin marketplace add ./my-marketplace

# 从远程 JSON 文件添加
/plugin marketplace add https://example.com/marketplace.json
```

### 查看市场

```bash
# 列出所有已配置的市场
/plugin marketplace list

# 打开交互式界面
/plugin
# 然后按 Tab 切换到 "市场" 选项卡
```

### 更新市场

```bash
# 更新指定市场（刷新插件列表）
/plugin marketplace update marketplace-name

# 示例
/plugin marketplace update claude-plugins-official
```

### 删除市场

```bash
# 删除指定市场
/plugin marketplace remove marketplace-name

# 示例
/plugin marketplace remove mac-agent-skills
```

> ⚠️ **注意**: 删除市场会自动卸载从该市场安装的所有插件！

### 市场自动更新

```bash
# 通过 UI 配置：
/plugin
# -> 市场 -> 选择市场 -> 启用/禁用自动更新
```

官方市场默认启用自动更新，第三方市场默认禁用。

---

## 插件管理

### 安装插件

```bash
# 基本语法（默认安装到用户范围）
/plugin install plugin-name@marketplace-name

# 示例
/plugin install frontend-design@claude-plugins-official
/plugin install pdf@mac-agent-skills

# 指定安装范围
claude plugin install plugin-name@marketplace-name --scope user     # 用户范围（默认）
claude plugin install plugin-name@marketplace-name --scope project  # 项目范围
claude plugin install plugin-name@marketplace-name --scope local    # 本地范围
```

#### 安装范围说明

| 范围 | 说明 | 存储位置 |
|------|------|----------|
| `user` | 所有项目可用，仅自己可见 | `~/.claude/` |
| `project` | 项目内所有协作者可用 | 项目 `.claude/settings.json` |
| `local` | 仅本项目对自己可用 | 项目 `.claude/local.json` |

### 查看插件

```bash
# 打开交互式界面（推荐）
/plugin
# 然后按 Tab 切换到 "已安装" 选项卡
```

### 禁用插件（不删除）

```bash
/plugin disable plugin-name@marketplace-name

# 示例
/plugin disable frontend-design@claude-plugins-official
```

### 重新启用插件

```bash
/plugin enable plugin-name@marketplace-name

# 示例
/plugin enable frontend-design@claude-plugins-official
```

### 卸载插件

```bash
# 基本卸载命令
/plugin uninstall plugin-name@marketplace-name

# 指定范围卸载
claude plugin uninstall plugin-name@marketplace-name --scope project

# 示例
/plugin uninstall pdf@mac-agent-skills
```

### 验证插件

```bash
# 验证插件配置
claude plugin validate .

# 或在 Claude Code 中
/plugin validate .
```

---

## 技能管理

技能是插件提供的可调用功能，通常以 `/` 开头（如 `/commit`, `/review`）。

### 查看可用技能

```bash
# 方法1: 通过 /plugin 界面
/plugin
# -> 发现 -> 浏览插件及其技能

# 方法2: 通过 /skills 界面
/skills
```

### 使用技能

```bash
# 直接调用技能
/skill-name arguments

# 示例
/commit --all
/review "检查这段代码"
/frontend-design "创建一个登录页面"
```

### 技能命名空间

插件提供的技能通常带有插件名前缀：

```bash
# 格式
/plugin-name:skill-name

# 示例
/commit-commands:commit
/commit-commands:push
```

### 技能缓存问题

如果技能安装后未出现，清除缓存：

```bash
# 清除插件缓存
rm -rf ~/.claude/plugins/cache

# 然后重启 Claude Code 并重新安装插件
```

---

## 命令速查表

### 市场命令

| 操作 | 命令 | 快捷方式 |
|------|------|----------|
| 添加市场 | `/plugin marketplace add <source>` | `/plugin market add <source>` |
| 列出市场 | `/plugin marketplace list` | `/plugin market list` |
| 更新市场 | `/plugin marketplace update <name>` | `/plugin market update <name>` |
| 删除市场 | `/plugin marketplace remove <name>` | `/plugin market rm <name>` |

### 插件命令

| 操作 | 命令 | 说明 |
|------|------|------|
| 安装插件 | `/plugin install <plugin>@<market>` | 默认用户范围 |
| 卸载插件 | `/plugin uninstall <plugin>@<market>` | |
| 禁用插件 | `/plugin disable <plugin>@<market>` | 保留安装但停用 |
| 启用插件 | `/plugin enable <plugin>@<market>` | 重新启用已停用的插件 |
| 验证插件 | `/plugin validate .` | 检查配置 |

### 交互式界面

```bash
/plugin    # 插件管理界面
/skills    # 技能浏览界面
```

**界面选项卡**（使用 `Tab` 或 `Shift+Tab` 切换）：

| 选项卡 | 功能 |
|--------|------|
| 发现 | 浏览所有市场的可用插件 |
| 已安装 | 管理/启用/禁用/卸载已安装插件 |
| 市场 | 添加/删除/更新市场 |
| 错误 | 查看插件加载错误 |

---

## 常见操作场景

### 场景1: 从零开始安装插件

```bash
# 1. 添加市场
/plugin marketplace add anthropics/claude-code

# 2. 查看可用插件
/plugin
# -> 发现 -> 浏览插件

# 3. 安装插件
/plugin install commit-commands@anthropics-claude-code

# 4. 使用技能
/commit-commands:commit
```

### 场景2: 完全移除插件和市场

```bash
# 1. 卸载插件
/plugin uninstall plugin-name@marketplace-name

# 2. 删除市场（可选，会自动卸载该市场的所有插件）
/plugin marketplace remove marketplace-name
```

### 场景3: 临时禁用某个插件

```bash
# 禁用插件
/plugin disable plugin-name@marketplace-name

# 需要时重新启用
/plugin enable plugin-name@marketplace-name
```

### 场景4: 团队共享插件配置

在项目的 `.claude/settings.json` 中配置：

```json
{
  "extraKnownMarketplaces": {
    "company-tools": {
      "source": {
        "source": "github",
        "repo": "your-org/claude-plugins"
      }
    }
  },
  "enabledPlugins": {
    "code-formatter@company-tools": true,
    "deployment-tools@company-tools": true
  }
}
```

---

## 故障排除

### 插件技能未出现

```bash
# 1. 清除缓存
rm -rf ~/.claude/plugins/cache

# 2. 重启 Claude Code

# 3. 重新安装插件
/plugin uninstall plugin-name@marketplace-name
/plugin install plugin-name@marketplace-name
```

### 市场无法加载

- 验证 URL 可访问性
- 检查 `.claude-plugin/marketplace.json` 是否存在
- 对于私有仓库，确认访问权限

### /plugin 命令无法识别

```bash
# 检查版本
claude --version

# 更新 Claude Code
brew upgrade claude-code    # Homebrew
npm update -g @anthropic-ai/claude-code    # npm
```

---

## 官方市场插件参考

### claude-plugins-official (官方市场)

自动可用，包含以下类别：

| 类别 | 插件示例 |
|------|----------|
| **代码智能** | `clangd-lsp`, `gopls-lsp`, `pyright-lsp`, `rust-analyzer-lsp` |
| **外部集成** | `github`, `gitlab`, `figma`, `notion`, `slack` |
| **开发工作流** | `commit-commands`, `pr-review-toolkit`, `plugin-dev` |
| **输出样式** | `explanatory-output-style`, `learning-output-style` |

### anthropics/claude-code (演示市场)

包含示例插件，展示插件系统功能：

```bash
/plugin marketplace add anthropics/claude-code
```

---

## 更多信息

- [创建和分发插件市场](https://code.claude.com/docs/zh-CN/plugin-marketplaces)
- [发现和安装预构建插件](https://code.claude.com/docs/zh-CN/discover-plugins)
- [插件参考](https://code.claude.com/docs/zh-CN/plugins-reference)
- [插件设置](https://code.claude.com/docs/zh-CN/settings#plugin-settings)
