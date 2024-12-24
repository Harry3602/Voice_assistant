# Voice Assistant

This is a simple voice assistant application runs on console that can recognize speech, respond with text-to-speech, and perform various tasks such as taking screenshots, performing Google searches, and managing tasks.

## Features

- Speech recognition using Google Speech Recognition API
- Text-to-speech responses
- Task management
- Take screenshots
- Perform Google searches

## Requirements

- Python 3.x
- Internet connection for speech recognition

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Harry3602/Voice_assistant.git
    cd Voice_assistant
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the voice assistant:
    ```sh
    python voice_assistant.py
    ```

2. Follow the prompts and speak your commands.

## Commands

- **Greeting**: "hello", "hi", "hey", "good morning", "good afternoon", "good evening"
- **Farewell**: "bye", "stop", "exit", "quit", "goodbye"
- **Time**: "time", "what's the time", "tell me the time"
- **Date**: "date", "what's the date", "tell me the date"
- **Google Search**: "search for", "google", "find"
- **Tasks**: "add task", "show tasks", "list tasks"
- **Screenshot**: "take a screenshot", "capture screen"
- **Browser**: "open chrome", "launch chrome", "open browser"
- **Joke**: "tell me a joke", "joke", "make me laugh"
- **Thank**: "thank you", "thanks"

## License

This project is licensed under the MIT License.