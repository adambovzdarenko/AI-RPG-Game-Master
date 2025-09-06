# RPG Game Master

## Overview
RPG Game Master is a web-based interactive chat application that allows users to communicate with an AI-powered bot to generate RPG-style game content. The application supports multiple languages, real-time streaming responses, and markdown formatting for rich-text messages.

## Features
- Multi-language selection.
- AI-powered bot that responds in real-time.
- Streamed responses with live typing effect.
- Markdown support for bold, italic, and inline formatting.
- Mobile-friendly design.
- Initial prompt from bot asking user to enter a description.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/adambovzdarenko/AI-RPG-Game-Master
cd rpg-game-master
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open the link displayed in the console (e.g., `http://127.0.0.1:5000`) in your browser or on a mobile device connected to the same network.

## Usage
- Select your preferred language.
- The bot will send a welcome message prompting you to enter a description.
- Type your messages in the input box and press Enter or click Send.
- The bot responds in real-time with formatted messages.

## Tech Stack
- **Python Flask** for backend.
- **Socket.IO** for real-time communication.
- **HTML/CSS/JavaScript** for frontend.
- **Marked.js** for markdown parsing.

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes.
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Open a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
Adam Bovzdarenko - [adambovzdarenko@gmail.com](mailto:adambovzdarenko@gmail.com)

