# MCPApp

MCP Based Apps to show Existing MCP servers - A voice-enabled conversational AI application powered by Azure OpenAI and Microsoft Learn documentation through enhanced MCP integration.

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

**Required Environment Variables:**
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI service endpoint
- `AZURE_OPENAI_KEY` - Azure OpenAI API key
- `AZURE_OPENAI_DEPLOYMENT` - Chat model deployment name
- `AZURE_OPENAI_ENDPOINT_TTS` - Azure OpenAI TTS endpoint (optional, falls back to Google TTS)
- `AZURE_OPENAI_KEY_TTS` - Azure OpenAI TTS API key (optional)

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

- **Voice-First Interface**: Natural language voice input with dual audio response options
- **Enhanced MCP Integration**: Direct Azure OpenAI MCP client for Microsoft Learn documentation access
- **Dual Text-to-Speech**: Azure OpenAI TTS (gpt-4o-mini-tts) with Google TTS fallback
- **Conversational Memory**: Multi-turn conversations with session management and audio playback
- **Microsoft Learn UI**: Specialized interface for Microsoft documentation queries
- **Azure Cloud Integration**: Scalable deployment with Azure OpenAI services

## 🛠 Technology Stack

- **Frontend**: Streamlit Web UI with wide layout
- **AI Services**: Azure OpenAI (Whisper STT + GPT Chat + TTS)
- **Integration**: Model Context Protocol (MCP) with Azure OpenAI MCP client
- **External APIs**: Microsoft Learn API, Azure OpenAI TTS, Google Text-to-Speech (fallback)
- **Deployment**: Azure App Service