# Forum App - Message Service

A Flask-based microservice for handling message management.

## Features

- **Send Messages**: Create new forum messages with user information
- **View Messages**: Retrieve all messages or specific messages by ID

## Project Structure

```
fa-message/
├── controllers/
│   ├── __init__.py
│   └── message_controller.py
├── models/
│   ├── __init__.py
│   └── message_models.py
├── routes/
│   ├── __init__.py
│   └── message_routes.py
├── config/
│   └── config.py
├── app.py
├── seed.py
├── .env
├── .flaskenv
└── README.md
```

## API Endpoints

| Method | Endpoint             | Description        |
| ------ | -------------------- | ------------------ |
| `POST` | `/api/messages`      | Send a new message |
| `GET`  | `/api/messages`      | Get all messages   |
| `GET`  | `/api/messages/<id>` | Get message by ID  |

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/forum-app-team/fa-message.git
   cd fa-message
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Environment Setup

Create a `.env` file in the project root with the following variables:

```env
# Database Configuration
DATABASE_URI=your-db-uri-here

# Flask Configuration
FLASK_CONFIG=development
SECRET_KEY=your-secret-key-here
```

## Running the Application

### 1. Initialize Database

Create tables and populate with mock data:

```bash
python seed.py
```

### 2. Start the Application

```bash
python app.py
```

Or using Flask CLI:

```bash
flask run
```

The application will be available at `http://localhost:5000`

## Database Schema

### Message Table

| Field         | Type        | Description                        |
| ------------- | ----------- | ---------------------------------- |
| `messageId`   | Integer     | Primary key (auto-increment)       |
| `userId`      | Integer     | User identifier                    |
| `email`       | String(255) | User email address                 |
| `message`     | Text        | Message content                    |
| `dateCreated` | DateTime    | Creation timestamp                 |
| `status`      | String(20)  | Message status (default: 'active') |
