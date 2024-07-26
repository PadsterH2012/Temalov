# Temalov

Temalov is a comprehensive role-playing game (RPG) content creation and management system. It allows users to generate, manage, and store various RPG elements such as characters, quests, and game settings using AI-powered tools and a user-friendly web interface.

## Features
- AI-powered character generation and details
- Quest creation and management
- Game settings storage and retrieval
- User authentication and management
- PDF content extraction and parsing
- RESTful API for content management
- Web-based user interface

## Project Structure
The project is divided into several microservices:

1. `rpg_content_api`: RESTful API for managing RPG content
2. `rpg_content_creator`: Service for generating and processing RPG content
3. `rpg_database`: PostgreSQL database for storing all RPG data
4. `rpg_web_frontend`: Web interface for users to interact with the system

## Installation

### Prerequisites
- Docker and Docker Compose
- Git

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project_root
   ```

2. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

This will start all the necessary services.

## Usage

After starting the services, you can access the web interface at `http://localhost:5000`. From there, you can:

- Register a new account or log in
- Generate new characters
- Create and manage quests
- Upload PDFs for content extraction
- Manage game settings

The API can be accessed at `http://localhost:5001/api/v1/`.

## Development

To set up the development environment:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the services individually for development:
   ```bash
   # In separate terminal windows:
   python rpg_content_api/run.py
   python rpg_content_creator/run.py
   python rpg_web_frontend/run.py
   ```

## Testing

To run the tests:

```bash
python -m pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

Project Link: [https://github.com/yourusername/temalov](https://github.com/yourusername/temalov)
