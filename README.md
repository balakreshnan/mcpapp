# MCPApp

MCP Based Apps to show Existing MCP servers - A voice-enabled conversational AI application powered by Azure OpenAI and Microsoft Learn documentation.

## 📋 Architecture

For detailed system architecture, component diagrams, and technical specifications, see [ARCHITECTURE.md](ARCHITECTURE.md).

## 🚀 Quick Start

### Development Setup

- Install python debugger
- Install Azure App Service
- Install Functions
- Create a python virtual Environment
- install python 3.12

### Environment Configuration

Copy `sample.env` to `.env` and configure your Azure OpenAI credentials:

```bash
cp sample.env .env
# Edit .env with your Azure OpenAI settings
```

### Local Development

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Azure App Service Deployment

```bash
bash streamlit.sh
```

## 🎯 Features

- **Voice-First Interface**: Natural language voice input and audio responses
- **Intelligent Context Retrieval**: Real-time Microsoft Learn documentation access via MCP
- **Conversational Memory**: Multi-turn conversations with session management
- **Azure Cloud Integration**: Scalable deployment with Azure OpenAI services

## 🛠 Technology Stack

- **Frontend**: Streamlit Web UI
- **AI Services**: Azure OpenAI (Whisper + GPT)
- **Integration**: Model Context Protocol (MCP)
- **External APIs**: Microsoft Learn API, Google Text-to-Speech
- **Deployment**: Azure App Service