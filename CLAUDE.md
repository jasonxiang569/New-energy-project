# CLAUDE.md - AI Assistant Guide

**Repository**: New-energy-project
**Last Updated**: 2026-01-17
**Status**: New Repository (Initializing)

## Overview

This is a new energy-related software project currently in its initialization phase. This document provides guidance for AI assistants (like Claude) working on this codebase.

## Repository Status

**Current State**: Empty repository
**Branch**: `claude/claude-md-mki338ntdduolkw6-E7mIj`
**Remote**: http://local_proxy@127.0.0.1:59966/git/jasonxiang569/New-energy-project

This repository has been initialized but does not yet contain any code or project structure. When working on this project, AI assistants should help establish appropriate project foundations.

## Project Initialization Guidelines

### When Setting Up This Project

If asked to initialize or scaffold this project, consider:

1. **Technology Stack Selection**
   - Clarify with the user what technology stack is needed
   - Common options for energy projects:
     - Python (data analysis, ML, scientific computing)
     - JavaScript/TypeScript (web dashboards, visualization)
     - Java/Kotlin (enterprise systems)
     - C++ (embedded systems, performance-critical applications)

2. **Essential Initial Files**
   - `.gitignore` - appropriate for chosen technology
   - `README.md` - project overview and setup instructions
   - License file (if applicable)
   - Configuration files (package.json, requirements.txt, etc.)
   - Directory structure (src/, tests/, docs/, etc.)

3. **Development Environment Setup**
   - Document required dependencies
   - Provide setup instructions
   - Include environment configuration templates

## Development Workflows

### Git Workflow

**Branch Naming Convention**:
- Feature branches: `feature/<description>`
- Bug fixes: `fix/<description>`
- Documentation: `docs/<description>`
- Claude branches: `claude/claude-md-<session-id>`

**Commit Guidelines**:
- Use clear, descriptive commit messages
- Follow conventional commits format when possible:
  - `feat:` new features
  - `fix:` bug fixes
  - `docs:` documentation changes
  - `refactor:` code refactoring
  - `test:` test additions/changes
  - `chore:` maintenance tasks

**Push Requirements**:
- Always use: `git push -u origin <branch-name>`
- Branch names must start with 'claude/' for AI assistant work
- Retry up to 4 times with exponential backoff on network errors

### Code Quality Standards

When writing code for this project:

1. **Security First**
   - Never introduce common vulnerabilities (XSS, SQL injection, command injection)
   - Validate input at system boundaries
   - Follow OWASP best practices

2. **Simplicity Over Complexity**
   - Avoid over-engineering
   - Only implement what's explicitly requested
   - Don't add "future-proofing" for hypothetical requirements
   - Three similar lines are better than premature abstraction

3. **Code Style**
   - Follow language-specific conventions
   - Use consistent formatting
   - Add comments only where logic isn't self-evident
   - Delete unused code completely (no commented-out code)

4. **Testing**
   - Write tests for new functionality when applicable
   - Ensure existing tests pass before committing
   - Document test requirements and coverage goals

## Project Structure (To Be Established)

This section will be updated once the project structure is defined. Typical structures include:

```
/
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation
├── config/        # Configuration files
├── scripts/       # Build and utility scripts
└── README.md      # Project documentation
```

## Key Conventions

### File Operations

**Reading Files**:
- Always read existing files before modifying
- Use Read tool for file contents
- Never propose changes to unread code

**Editing Files**:
- Prefer editing existing files over creating new ones
- Use Edit tool for modifications
- Preserve existing indentation and formatting

**Creating Files**:
- Only create files when absolutely necessary
- Avoid creating documentation files unless explicitly requested
- No emoji usage unless explicitly requested

### Task Management

When working on multi-step tasks:

1. **Use TodoWrite Tool**
   - Break down complex tasks into actionable steps
   - Track progress with pending/in_progress/completed states
   - Only ONE task should be in_progress at a time
   - Mark tasks complete immediately after finishing

2. **Task Breakdown Example**:
   ```
   - Research existing implementation
   - Design solution approach
   - Implement core functionality
   - Add tests
   - Update documentation
   ```

### Communication Style

- Be concise and technical
- Focus on facts over validation
- No unnecessary emojis or superlatives
- Provide objective guidance
- Disagree when necessary for technical accuracy

## Technology-Specific Guidelines

*This section will be populated once the technology stack is determined.*

### [Language/Framework Name]

- Coding conventions
- Build commands
- Test commands
- Deployment process
- Common patterns

## Common Commands

*To be documented based on chosen technology stack.*

```bash
# Setup
# [To be added]

# Development
# [To be added]

# Testing
# [To be added]

# Build
# [To be added]
```

## Dependencies

*No dependencies currently defined. This will be updated as the project develops.*

## Architecture Decisions

*Architecture decisions will be documented here as the project evolves.*

### ADR Format

When making significant architectural decisions, document:
- **Context**: What is the issue we're addressing?
- **Decision**: What is the change we're proposing?
- **Consequences**: What becomes easier or more difficult?

## Troubleshooting

*Common issues and solutions will be documented here.*

## External Resources

*Links to relevant documentation, APIs, and resources will be added.*

## Energy Domain Considerations

Given this is a new energy project, consider these domain-specific aspects:

1. **Data Handling**
   - Energy consumption/generation data often requires high precision
   - Time-series data handling may be critical
   - Units and conversions must be accurate (kWh, MW, etc.)

2. **Compliance & Standards**
   - Energy sector may have regulatory requirements
   - Data privacy considerations for consumption data
   - Industry standards (IEC, IEEE, etc.)

3. **Performance**
   - Real-time data processing may be required
   - Scalability for large datasets
   - Efficient algorithms for energy optimization

4. **Integration Points**
   - Smart meter APIs
   - Grid management systems
   - Weather data services
   - Energy market APIs

## Next Steps

For AI assistants beginning work on this project:

1. **If scaffolding the project**:
   - Ask the user about technology preferences
   - Establish basic project structure
   - Add essential configuration files
   - Create initial README.md

2. **If implementing features**:
   - Read this document first
   - Understand the project context
   - Follow established conventions
   - Update this document as patterns emerge

3. **If fixing issues**:
   - Understand the codebase first
   - Make minimal, focused changes
   - Test thoroughly
   - Document any new patterns

## Document Maintenance

This document should be updated when:
- Project structure changes significantly
- New conventions are established
- Technology stack is modified
- Common patterns emerge
- New team members provide feedback

---

**Note for AI Assistants**: This is a living document. As you work on the project and discover patterns, conventions, or important details, update this file to help future AI assistants work more effectively.
