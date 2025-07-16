# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Package Management (uv only)
- Install dependencies: `uv sync`
- Add package: `uv add package`
- Add dev package: `uv add --dev package`
- Upgrade package: `uv add --dev package --upgrade-package package`
- FORBIDDEN: `uv pip install`, `@latest` syntax

### Application 
- Start server: `uv run python src/chat_app/main.py`
- Server will run on: http://localhost:8000
- Playground: http://localhost:8000/translate/playground/

### Testing & Quality
- Run tests: `uv run --frozen pytest`
- Format code: `uv run --frozen ruff format .`
- Check linting: `uv run --frozen ruff check .`
- Auto-fix linting: `uv run --frozen ruff check . --fix`
- Install pre-commit: `uv run pre-commit install`

### Docker Development
- Build: `./docker/build.sh` or `docker compose build`
- Run: `./docker/run.sh` or `docker compose up`

## Architecture

This is a LangChain-based translation API service using Google Gemini AI:

### Core Components
- **FastAPI Application** (`src/chat_app/main.py`): Entry point and server setup
- **Translation Chain** (`src/chat_app/chains/translation_chain.py`): LangChain pipeline (Prompt → Model → Parser)
- **Model Factory** (`src/chat_app/models/model_factory.py`): Creates Gemini AI model instances
- **Translation API** (`src/chat_app/api/translation_api.py`): LangServe route setup at `/translate`
- **Environment Loader** (`src/chat_app/environment/env_loader.py`): Handles API key setup with interactive prompts

### Request Flow
1. POST `/translate` receives `{"input": {"text": "Hello", "language": "日本語"}}`
2. LangServe routes to translation chain
3. Chain executes: Translation prompt → Gemini model → String parser
4. Returns `{"output": "translated text"}`

### Environment Variables
Required in `.env` file:
- `GOOGLE_API_KEY`: Google Gemini AI API key
- `LANGSMITH_API_KEY`: Optional LangSmith tracing
- `LANGSMITH_PROJECT`: Optional LangSmith project name

## Code Standards

### Mandatory Requirements
- Type hints for all functions and variables
- Google-style docstrings
- Ruff formatting and linting compliance
- Follow existing patterns exactly

### Commit Messages
Use Conventional Commits format with English:
- `feat:` New features
- `fix:` Bug fixes  
- `docs:` Documentation changes
- `style:` Formatting changes
- `refactor:` Code restructuring
- `test:` Test additions/fixes
- `chore:` Build/tooling changes

### Pre-commit Hooks
Automatically run on commit:
- `uv-lock`: Updates lockfile
- `ruff-check --fix`: Linting with auto-fix
- `ruff-format`: Code formatting