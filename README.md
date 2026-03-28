# Smart Hustle Finder 🚀

Smart Hustle Finder is an AI-powered platform designed to help students and aspiring developers discover the most in-demand tech skills based on real-time market trends.

## Features
- **Skill Analysis**: Input your current skill and get an AI-driven report on market demand.
- **Top In-Demand Skills**: Discover related skills that are currently trending in job listings.
- **Skill Gap Analyzer**: Identify specifically what you're missing and how to learn it.
- **Market Summary**: A concise overview of the current landscape for your expertise.
- **Modern UI**: A sleek, dark-themed dashboard built with vanilla CSS.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML5, Vanilla CSS
- **Configuration**: python-decouple for environment variables
- **AI (Prototype)**: Simulated AI responses based on common tech job trends.

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory:
   ```bash
   cd smart-hustle-finder
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```

### Running the App
Start the development server:
```bash
python manage.py runserver
```
Visit the app at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Project Structure
- `core/`: Django project configuration.
- `analyzer/`: Main application logic including views and services.
- `templates/`: HTML templates for the UI.
- `static/`: CSS and other static assets.
- `.env`: Environment variables (API keys, Debug mode, etc).
