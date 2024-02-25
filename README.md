
# Speech Emotion Recognition

## Overview
This repository contains the code for a Speech Emotion Recognition (SER) application. The application is designed to identify emotions from speech using a deep learning model.

## Features
- Audio recording and upload functionality.
- Real-time emotion detection from speech.
- Responsive UI for a seamless user experience.

## Technology Stack
- **Backend**: FastAPI
- **Frontend**: React
- **Deployment**: GCP (Backend), Vercel (Frontend)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.8+
- Node.js and npm

### Installing
A step-by-step guide to get a development environment running.

1. **Clone the Repository**
   ```bash
   git clone https://github.com/1sharkguy/Speech-Emotion-Recognition.git
   cd Speech-Emotion-Recognition
   ```

2. **Set Up the Backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

3. **Set Up the Frontend**
   ```bash
   cd frontend
   npm install
   npm start
   ```


This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments
- Mention any inspirations, code snippets, etc.
