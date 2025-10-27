# Zazu - The South African Voice Translator Assistant

Zazu is a conversational AI assistant that acts as a real-time voice translator for South African languages. It's designed to be used over a phone call, where it can listen to a user speaking in one of South Africa's languages, translate it to a target language (defaulting to English), and speak the translation back to the user.

## How it works

The assistant is built with Python and uses a combination of services to function:

*   **Twilio:** Manages the phone call and streams the user's voice audio.
*   **Deepgram:** Provides real-time speech-to-text (STT) to transcribe the user's speech and text-to-speech (TTS) to generate the translated audio. The configuration also suggests that an AI provider like OpenAI is intended to be used for the translation logic, but the current implementation in `zazu.py` does not yet include this integration.

The application is built using `asyncio` and `websockets` to handle the real-time streaming of audio and data between these services.

## Key Features

*   **Real-time Voice Translation:** Translates between various South African languages and English.
*   **Natural Conversation:** Features a warm, local, and culturally aware personality.
*   **Barge-in Support:** Allows users to interrupt the assistant for a more fluid conversation.
*   **Powered by a Modern AI Stack:** Utilizes Twilio and Deepgram to create a powerful and responsive voice AI.

## Getting Started

### Prerequisites

*   Python 3.7+
*   A Twilio account with a configured phone number.
*   A Deepgram API key.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Zazu_Ai_Assistant.git
    cd Zazu_Ai_Assistant
    ```
2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install websockets python-dotenv
    ```
3.  **Configure your environment variables:**
    Create a `.env` file in the project root and add your Deepgram API key:
    ```
    DEEPGRAM_API_KEY=your_deepgram_api_key
    ```
4.  **Review the assistant's configuration:**
    The `config.json` file contains the detailed configuration for the assistant's voice, language, and personality. You can modify this file to change the assistant's behavior.

### Running the Assistant

To start the WebSocket server, run the following command:

```bash
python zazu.py
```

The server will start on `ws://localhost:5000`. You will need to configure your Twilio phone number to send a stream to this WebSocket URL.