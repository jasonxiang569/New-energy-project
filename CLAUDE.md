# CLAUDE.md - AI Assistant Guide

**Repository**: New-energy-project
**Last Updated**: 2026-01-18
**Status**: Active Development

## Overview

This is an AI Intelligence Analysis System (AI情报系统) that provides intelligent information processing, analysis, and insight generation capabilities using artificial intelligence.

## Repository Status

**Current State**: Fully implemented AI intelligence system
**Branch**: `claude/claude-md-mki338ntdduolkw6-E7mIj`
**Remote**: http://local_proxy@127.0.0.1:59966/git/jasonxiang569/New-energy-project
**Tech Stack**: Python + FastAPI + React + TypeScript + SQLite

The system includes a complete backend API, AI analysis engine, and React-based frontend interface.

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

## Project Structure

```
New-energy-project/
├── backend/                    # Python FastAPI Backend
│   ├── app/
│   │   ├── api/               # API route handlers
│   │   │   ├── intelligence.py  # Intelligence & analysis endpoints
│   │   │   └── stats.py         # Statistics endpoints
│   │   ├── core/              # Core configuration
│   │   │   └── config.py        # Settings management
│   │   ├── db/                # Database layer
│   │   │   ├── database.py      # Database connection
│   │   │   └── init_db.py       # DB initialization script
│   │   ├── models/            # Data models
│   │   │   ├── intelligence.py  # SQLAlchemy models
│   │   │   └── schemas.py       # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   │   ├── ai_service.py           # AI analysis service
│   │   │   └── intelligence_service.py # Data service
│   │   └── main.py            # Application entry point
│   ├── tests/                 # Backend tests
│   ├── requirements.txt       # Python dependencies
│   └── .env.example          # Environment template
│
├── frontend/                  # React TypeScript Frontend
│   ├── src/
│   │   ├── components/       # Reusable components
│   │   ├── pages/           # Page components
│   │   │   ├── Dashboard.tsx        # Statistics dashboard
│   │   │   ├── IntelligenceList.tsx # Intelligence management
│   │   │   └── QuickAnalysis.tsx    # Quick analysis tool
│   │   ├── services/        # API integration
│   │   │   └── api.ts              # API client
│   │   ├── types/           # TypeScript definitions
│   │   │   └── index.ts            # Type definitions
│   │   ├── styles/          # CSS styles
│   │   │   └── App.css
│   │   ├── App.tsx          # Main app component
│   │   └── main.tsx         # Application entry
│   ├── public/              # Static assets
│   ├── index.html           # HTML template
│   ├── package.json         # Node dependencies
│   ├── vite.config.ts       # Vite configuration
│   └── tsconfig.json        # TypeScript config
│
├── docs/                    # Documentation
│   ├── api.md              # API documentation
│   └── deployment.md       # Deployment guide
│
├── scripts/                # Utility scripts
│   ├── start_backend.sh   # Backend startup (Linux/Mac)
│   ├── start_frontend.sh  # Frontend startup (Linux/Mac)
│   ├── start_backend.bat  # Backend startup (Windows)
│   └── start_frontend.bat # Frontend startup (Windows)
│
├── .gitignore             # Git ignore rules
├── README.md              # Project overview
└── CLAUDE.md             # AI assistant guide
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

### Backend (Python + FastAPI)

**Coding Conventions**:
- Follow PEP 8 style guide
- Use type hints for all functions
- Async/await for I/O operations
- Pydantic for data validation

**Key Files**:
- `app/main.py`: Application entry, routes registration
- `app/services/ai_service.py`: Core AI analysis logic
- `app/models/intelligence.py`: SQLAlchemy ORM models
- `app/models/schemas.py`: Pydantic request/response models

**Database**:
- SQLite for single-machine deployment
- SQLAlchemy ORM for database operations
- Alembic for migrations (if needed)

### Frontend (React + TypeScript)

**Coding Conventions**:
- Functional components with hooks
- TypeScript strict mode
- Ant Design component library
- Axios for API calls

**Key Files**:
- `src/App.tsx`: Main application component
- `src/services/api.ts`: API client and endpoints
- `src/types/index.ts`: TypeScript type definitions
- `src/pages/`: Page-level components

**State Management**:
- React hooks (useState, useEffect)
- Local component state (no global state library needed for this scale)

### AI Integration

**Model Used**: Claude 3 Sonnet (via Anthropic API)

**Analysis Features**:
- Text summarization
- Sentiment analysis (-100 to 100 scale)
- Entity recognition (PERSON, ORGANIZATION, LOCATION, DATE)
- Keyword extraction
- Topic identification
- Risk level assessment (low/medium/high/critical)
- Insight generation

## Common Commands

### Quick Start

**Linux/Mac**:
```bash
# Backend (Terminal 1)
./scripts/start_backend.sh

# Frontend (Terminal 2)
./scripts/start_frontend.sh
```

**Windows**:
```bash
# Backend (Terminal 1)
scripts\start_backend.bat

# Frontend (Terminal 2)
scripts\start_frontend.bat
```

### Backend Commands

```bash
cd backend

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python -m app.db.init_db

# Run development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run tests
pytest

# Production server
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend Commands

```bash
cd frontend

# Install dependencies
npm install

# Development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint
```

### Database Commands

```bash
cd backend

# Initialize new database
python -m app.db.init_db

# Create migration (if using Alembic)
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### API Testing

```bash
# Health check
curl http://localhost:8000/health

# Create intelligence
curl -X POST http://localhost:8000/api/intelligence/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","content":"Test content"}'

# Quick analysis
curl -X POST http://localhost:8000/api/intelligence/quick-analyze \
  -H "Content-Type: application/json" \
  -d '{"content":"要分析的文本内容..."}'

# Get stats
curl http://localhost:8000/api/stats/
```

## Dependencies

### Backend Dependencies (Python)

**Core Framework**:
- `fastapi==0.109.0` - Web framework
- `uvicorn==0.27.0` - ASGI server
- `pydantic==2.5.3` - Data validation

**Database**:
- `sqlalchemy==2.0.25` - ORM
- `alembic==1.13.1` - Database migrations

**AI/ML**:
- `anthropic==0.18.1` - Claude API client
- `openai==1.12.0` - OpenAI API client
- `langchain==0.1.6` - LLM framework
- `jieba==0.42.1` - Chinese text segmentation

**Utilities**:
- `python-dotenv==1.0.0` - Environment variables
- `httpx==0.26.0` - HTTP client

### Frontend Dependencies (Node.js)

**Core**:
- `react@18.2.0` - UI library
- `react-dom@18.2.0` - React DOM rendering
- `react-router-dom@6.21.3` - Routing

**UI Framework**:
- `antd@5.13.3` - Ant Design components
- `@ant-design/icons@5.2.6` - Icons

**Data & State**:
- `axios@1.6.5` - HTTP client
- `zustand@4.5.0` - State management
- `recharts@2.10.4` - Charts

**Build Tools**:
- `vite@5.0.11` - Build tool
- `typescript@5.3.3` - TypeScript compiler
- `@vitejs/plugin-react@4.2.1` - React plugin

### System Requirements

- Python 3.9+
- Node.js 18+
- 2GB RAM minimum
- 1GB disk space

## Architecture Decisions

*Architecture decisions will be documented here as the project evolves.*

### ADR Format

When making significant architectural decisions, document:
- **Context**: What is the issue we're addressing?
- **Decision**: What is the change we're proposing?
- **Consequences**: What becomes easier or more difficult?

## Troubleshooting

### Backend Issues

**"ANTHROPIC_API_KEY not configured"**
- Edit `backend/.env` file
- Add your Anthropic API key: `ANTHROPIC_API_KEY=sk-ant-xxx`
- Restart the backend server

**"Module not found" errors**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`
- Check Python version (requires 3.9+)

**Database errors**
- Delete `backend/intelligence.db` if corrupted
- Run `python -m app.db.init_db` to recreate
- Check file permissions

**Port 8000 already in use**
- Find process: `lsof -i :8000` (Linux/Mac) or `netstat -ano | findstr :8000` (Windows)
- Kill process or use different port: `--port 8001`

### Frontend Issues

**"Cannot connect to backend"**
- Ensure backend is running on port 8000
- Check `frontend/vite.config.ts` proxy settings
- Verify CORS settings in `backend/app/core/config.py`

**npm install fails**
- Clear cache: `npm cache clean --force`
- Delete `node_modules` and `package-lock.json`
- Run `npm install` again
- Check Node.js version (requires 18+)

**Page not updating**
- Hard refresh: Ctrl+Shift+R (or Cmd+Shift+R on Mac)
- Clear browser cache
- Check browser console for errors

### AI Analysis Issues

**Analysis returns generic results**
- Check API key validity and quota
- Verify network connectivity to Anthropic API
- Review prompt in `backend/app/services/ai_service.py`

**Analysis takes too long**
- Normal for large texts (30-60 seconds)
- Check timeout settings in API client
- Consider reducing text length

**"Analysis failed" errors**
- Check backend logs for detailed error
- Verify API key has sufficient quota
- Test API key with simple request

### Common Solutions

**Reset everything**
```bash
# Backend
cd backend
rm -rf venv intelligence.db
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m app.db.init_db

# Frontend
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**Check logs**
- Backend: Check terminal running uvicorn
- Frontend: Check browser console (F12)
- Network: Check browser Network tab (F12)

## External Resources

*Links to relevant documentation, APIs, and resources will be added.*

## AI Intelligence System Considerations

### System Design Principles

1. **AI Analysis Quality**
   - Prompt engineering in `ai_service.py` is critical
   - Temperature set to 0.3 for consistent analytical results
   - Structured JSON output for reliable parsing
   - Fallback mechanisms when AI response is malformed

2. **Data Management**
   - Intelligence data stored in SQLite for simplicity
   - Each analysis creates new record (history preserved)
   - Status workflow: pending → analyzing → completed/failed
   - Soft delete recommended (add deleted_at field) rather than hard delete

3. **Performance Optimization**
   - AI analysis is I/O bound (network call to Anthropic API)
   - Consider caching analysis results for identical content
   - Implement rate limiting to prevent API quota exhaustion
   - Use background tasks for batch analysis

4. **Security Considerations**
   - API keys stored in environment variables (never in code)
   - Input validation using Pydantic models
   - CORS properly configured for frontend access
   - No sensitive data in intelligence content (user responsibility)
   - Consider adding user authentication for multi-user scenarios

5. **Extensibility Points**
   - Easy to add new AI models (OpenAI, local models)
   - Analysis schema extensible via metadata field
   - Frontend components modular and reusable
   - API versioning ready (`/api/v1/...`)

6. **Monitoring & Analytics**
   - Track analysis success/failure rates
   - Monitor API usage and costs
   - Log analysis duration for performance tracking
   - Stats endpoint provides system overview

## Getting Started

### For Users

1. **Configure API Key**:
   ```bash
   cd backend
   cp .env.example .env
   # Edit .env and add your ANTHROPIC_API_KEY
   ```

2. **Start Backend**:
   ```bash
   ./scripts/start_backend.sh  # or start_backend.bat on Windows
   ```

3. **Start Frontend** (in new terminal):
   ```bash
   ./scripts/start_frontend.sh  # or start_frontend.bat on Windows
   ```

4. **Access Application**:
   - Frontend: http://localhost:5173
   - API Docs: http://localhost:8000/docs

### For AI Assistants

**When adding features**:
1. Read this document first
2. Understand existing architecture in `backend/app/` and `frontend/src/`
3. Follow established patterns (FastAPI routes, React hooks)
4. Update API documentation if adding endpoints
5. Test changes before committing
6. Update this document if patterns change

**When fixing bugs**:
1. Reproduce the issue
2. Check relevant logs (backend terminal, browser console)
3. Review related code in backend services or frontend components
4. Make minimal, focused changes
5. Test fix thoroughly
6. Document solution in Troubleshooting section if helpful

**When optimizing**:
1. Identify bottlenecks (database queries, API calls, render performance)
2. Consider caching strategies for AI results
3. Optimize database queries with proper indexing
4. Implement pagination for large datasets
5. Profile before and after changes

## Document Maintenance

This document should be updated when:
- Project structure changes significantly
- New conventions are established
- Technology stack is modified
- Common patterns emerge
- New team members provide feedback

---

**Note for AI Assistants**: This is a living document. As you work on the project and discover patterns, conventions, or important details, update this file to help future AI assistants work more effectively.
