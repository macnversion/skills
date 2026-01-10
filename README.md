> **Note:** For information about the Agent Skills standard, see [agentskills.io](https://agentskills.io).

# Agent Skills Collection

A curated collection of Agent Skills organized into skill sets for Claude Code. Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.

## What Are Skills?

Skills teach Claude how to complete specific tasks in a repeatable way—creating documents with brand guidelines, analyzing data using specific workflows, automating personal tasks, or building web applications.

For more information, check out:
- [Agent Skills Documentation](https://code.claude.com/docs/en/skills)
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

## Skill Sets

This repository organizes skills into four skill sets:

### Creative Skills (`creative-skills`)
Skills for creative and design work:
- **algorithmic-art** - Creating generative art using p5.js with seeded randomness
- **brand-guidelines** - Applies official brand colors and typography
- **canvas-design** - Create beautiful visual art in PNG and PDF documents
- **frontend-design** - Create distinctive, production-grade frontend interfaces
- **slack-gif-creator** - Create animated GIFs optimized for Slack
- **theme-factory** - Apply professional font and color themes to artifacts

### Document Skills (`document-skills`)
Comprehensive document processing skills:
- **docx** - Word document creation, editing with tracked changes
- **pdf** - PDF text extraction, form filling, merging
- **pptx** - PowerPoint slide generation and editing
- **xlsx** - Excel spreadsheet manipulation with formulas

### Development Skills (`development-skills`)
Skills for development workflows:
- **mcp-builder** - Guide for creating MCP (Model Context Protocol) servers
- **web-artifacts-builder** - Create web artifacts using React/Tailwind/shadcn
- **webapp-testing** - Test local web applications using Playwright
- **skill-creator** - Guide for creating effective skills
- **doc-coauthoring** - Structured workflow for co-authoring documentation
- **internal-comms** - Write internal communications (status reports, newsletters)

### Video Analysis Skills (`video-analysis-skills`)
AI-powered video content analysis:
- **video-analysis** - Video content analysis using Volces ARK API with support for general analysis, product/functionality analysis, and key node identification

## Installation in Claude Code

### Step 1: Add the Marketplace

```bash
/plugin marketplace add macnversion/skills
```

### Step 2: Install Skill Sets

Install individual skill sets based on your needs:

```bash
# Install creative skills
/plugin install creative-skills@mac-agent-skills

# Install document skills
/plugin install document-skills@mac-agent-skills

# Install development skills
/plugin install development-skills@mac-agent-skills

# Install video analysis skills
/plugin install video-analysis-skills@mac-agent-skills
```

Or use the interactive menu:
1. Select `Browse and install plugins`
2. Select `mac-agent-skills`
3. Select the skill set you want to install
4. Select `Install now`

### Step 3: Use the Skills

After installation, Claude automatically activates relevant skills based on your request. For example:
- "Use the PDF skill to extract text from this file"
- "Create a presentation about our Q4 results"
- "Build a React dashboard with shadcn components"

## Directory Structure

```
skills/
├── .claude-plugin/
│   └── marketplace.json    # Plugin marketplace configuration
├── skills/
│   ├── creative/           # Creative & Design skills
│   │   ├── algorithmic-art/
│   │   ├── brand-guidelines/
│   │   ├── canvas-design/
│   │   ├── frontend-design/
│   │   ├── slack-gif-creator/
│   │   └── theme-factory/
│   ├── document/           # Document processing skills
│   │   ├── docx/
│   │   ├── pdf/
│   │   ├── pptx/
│   │   └── xlsx/
│   └── development/        # Development workflow skills
│       ├── doc-coauthoring/
│       ├── internal-comms/
│       ├── mcp-builder/
│       ├── skill-creator/
│       ├── web-artifacts-builder/
│       └── webapp-testing/
│   └── video-analysis/      # Video content analysis skills
│       └── video-analysis/
├── spec/                   # Agent Skills specification
└── template/               # Skill template
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
- [Best Practices Guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

## License

Each skill may have its own license. Please check individual skill folders for specific licensing information.

---

**Note:** These skills are provided for demonstration and educational purposes. Always test skills thoroughly in your own environment before relying on them for critical tasks.
