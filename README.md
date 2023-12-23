
# Speech Emotion Recognition Project

## Overview
This project is a web-based application for recognizing emotions from speech. It uses a deep learning model to analyze the emotional tone in spoken words. The backend is built with FastAPI, providing robust and efficient handling of requests, and the frontend is developed using React, offering a dynamic and responsive user interface.

## Features
- **Emotion Recognition**: Analyze spoken words and identify emotions like happiness, sadness, anger, etc.
- **User-Friendly Interface**: Easy-to-use web interface for uploading audio files.
- **Real-Time Analysis**: Quick processing and visualization of emotional tones.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.8 or later
- Node.js 12.x or later
- npm or yarn

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/1sharkguy/Speech-Emotion-Recognition.git
   cd Speech-Emotion-Recognition
   ```

2. **Set Up the Backend**
   - Navigate to the backend directory:
     ```bash
     cd backend
     ```
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Start the FastAPI server:
     ```bash
     uvicorn main:app --reload
     ```

3. **Set Up the Frontend**
   - Navigate to the frontend directory from the root of the project:
     ```bash
     cd ../frontend
     ```
   - Install the required npm packages:
     ```bash
     npm install
     ```
   - Start the React development server:
     ```bash
     npm start
     ```

4. **Access the Application**
   - Open your web browser and navigate to `http://localhost:3000`.

## Usage
- Record or upload an audio file through the web interface.
- Submit the audio file for processing.
- View the emotional analysis results displayed on the interface.

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Your Name - [divyanshgarg404@gmail.com](mailto:divyanshgarg404@gmail.com)

Project Link: [https://github.com/1sharkguy/Speech-Emotion-Recognition](https://github.com/1sharkguy/Speech-Emotion-Recognition)
