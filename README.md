> **Note:** For information about the Agent Skills standard, see [agentskills.io](https://agentskills.io).

# Agent Skills Plugin Marketplace

A curated collection of Agent Skills plugins for Claude Code, organized as independent plugins that can be installed individually. Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.

## What Are Skills?

Skills teach Claude how to complete specific tasks in a repeatable way—creating documents with brand guidelines, analyzing data using specific workflows, automating personal tasks, or building web applications.

For more information, check out:
- [Agent Skills Documentation](https://code.claude.com/docs/en/skills)
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

## Available Skills

This marketplace provides 17 individual plugins organized into three categories:

### Creative Skills
Skills for creative and design work:
- **algorithmic-art** - Creating generative art using p5.js with seeded randomness and interactive parameter exploration
- **brand-guidelines** - Applies official brand colors and typography to artifacts
- **canvas-design** - Create beautiful visual art in PNG and PDF documents using design philosophy
- **frontend-design** - Create distinctive, production-grade frontend interfaces with high design quality
- **slack-gif-creator** - Knowledge and utilities for creating animated GIFs optimized for Slack
- **theme-factory** - Toolkit for styling artifacts with professional font and color themes

### Document Skills
Comprehensive document processing skills:
- **docx** - Word document creation, editing, and analysis with support for tracked changes and comments
- **pdf** - PDF manipulation toolkit for text extraction, form filling, merging, and splitting
- **pptx** - Presentation creation, editing, and analysis for PowerPoint slides
- **video-analysis** - AI-powered video content analysis using Volces ARK API
- **xlsx** - Excel spreadsheet creation, editing, and analysis with formulas and formatting

### Development Skills
Skills for development workflows:
- **doc-coauthoring** - Structured workflow for co-authoring documentation
- **internal-comms** - Resources for writing internal communications (status reports, newsletters, etc.)
- **mcp-builder** - Guide for creating MCP (Model Context Protocol) servers in Python or Node/TypeScript
- **skill-creator** - Guide for creating effective skills
- **web-artifacts-builder** - Suite of tools for creating multi-component HTML artifacts with React, Tailwind CSS, and shadcn/ui
- **webapp-testing** - Toolkit for testing local web applications using Playwright

## Installation in Claude Code

### Step 1: Add the Marketplace

```bash
/plugin marketplace add macnversion/skills
```

### Step 2: Install Individual Skills

Each skill can be installed independently based on your needs:

```bash
# Install specific skills
/plugin install algorithmic-art@skills
/plugin install frontend-design@skills
/plugin install pdf@skills
/plugin install mcp-builder@skills
```

Or use the interactive menu:
1. Run `/plugin` to open the plugin manager
2. Navigate to the **Discover** tab (or press Tab)
3. Browse the available skills from the `skills` marketplace
4. Select a skill to view its details
5. Choose your installation scope (User, Project, or Local)
6. Press Enter to install

### Step 3: Use the Skills

After installation, Claude automatically activates relevant skills based on your request. For example:
- "Use the PDF skill to extract text from this file"
- "Create a presentation about our Q4 results"
- "Build a React dashboard with shadcn components"

## Directory Structure

```
skills/
├── .claude-plugin/
│   └── marketplace.json       # Plugin marketplace configuration (17 plugins)
├── plugins/
│   ├── creative/               # Creative & Design plugins
│   │   ├── algorithmic-art/
│   │   │   └── .claude-plugin/
│   │   │       └── plugin.json
│   │   ├── brand-guidelines/
│   │   │   └── .claude-plugin/
│   │   │       └── plugin.json
│   │   ├── canvas-design/
│   │   │   └── .claude-plugin/
│   │   │       └── plugin.json
│   │   ├── frontend-design/
│   │   │   └── .claude-plugin/
│   │   │       └── plugin.json
│   │   ├── slack-gif-creator/
│   │   │   └── .claude-plugin/
│   │   │       └── plugin.json
│   │   └── theme-factory/
│   │       └── .claude-plugin/
│   │           └── plugin.json
│   ├── document/               # Document processing plugins
│   │   ├── docx/
│   │   │   └── .claude-plugin/
│   │   │       └── plugin.json
│   │   ├── pdf/
│   │   │   └── .claude-plugin/
│   │   │       └── plugin.json
│   │   ├── pptx/
│   │   │   └── .claude-plugin/
│   │   │       └── plugin.json
│   │   ├── video-analysis/
│   │   │   └── .claude-plugin/
│   │   │       └── plugin.json
│   │   └── xlsx/
│   │       └── .claude-plugin/
│   │           └── plugin.json
│   └── development/            # Development workflow plugins
│       ├── doc-coauthoring/
│       │   └── .claude-plugin/
│       │       └── plugin.json
│       ├── internal-comms/
│       │   └── .claude-plugin/
│       │       └── plugin.json
│       ├── mcp-builder/
│       │   └── .claude-plugin/
│       │       └── plugin.json
│       ├── skill-creator/
│       │   └── .claude-plugin/
│       │       └── plugin.json
│       ├── web-artifacts-builder/
│       │   └── .claude-plugin/
│       │       └── plugin.json
│       └── webapp-testing/
│           └── .claude-plugin/
│               └── plugin.json
├── spec/                      # Agent Skills specification
└── template/                  # Skill template
```

## Managing Skills

### View Installed Skills
```bash
/plugin
# Navigate to "Installed" tab
```

### Disable/Enable Skills
```bash
/plugin disable algorithmic-art@skills
/plugin enable algorithmic-art@skills
```

### Uninstall Skills
```bash
/plugin uninstall algorithmic-art@skills
```

### Update Marketplace
```bash
/plugin marketplace update skills
```

### Remove Marketplace
```bash
/plugin marketplace remove skills
```

## Creating Your Own Skills

Skills are simple to create—just a folder with a `SKILL.md` file:

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here]

## Examples
- Example usage 1

## Guidelines
- Guideline 1
```

Use the [`template/`](./template) folder as a starting point.

## Resources

- [Agent Skills Specification](https://agentskills.io/specification)
- [Claude Code Skills Docs](https://code.claude.com/docs/en/skills)
- [Plugin Marketplaces Docs](https://code.claude.com/docs/zh-CN/plugin-marketplaces)
- [Best Practices Guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

## License

Each skill may have its own license. Please check individual skill folders for specific licensing information.

---

**Note:** These skills are provided for demonstration and educational purposes. Always test skills thoroughly in your own environment before relying on them for critical tasks.
