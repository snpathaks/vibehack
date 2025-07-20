# StudySprint - AI-Powered Study Group Platform

![Hero Image](static/img/hero-bg.png)

StudySprint is a dynamic web application designed to help students connect and form effective study groups. It features an AI-powered matching system, real-time group chat, and accountability tools to enhance the learning experience. The platform includes a main landing page and a feature-rich study group hub.

## ✨ Features

The platform is split into a landing page and the main study group application, with the following key features:

**Main Application (`/study-groups`):**
* **👤 User Profiles**: Students can create a profile with their name, university, subjects, and study preferences.
* **🎯 AI-Powered Matching**: The platform suggests study groups based on shared subjects, goals, and schedules.
* **👥 Group Management**: Users can browse existing groups, join them, or create their own.
* **💬 Real-Time Group Chat**: Integrated chat allows for seamless communication between group members.
* **📈 Progress Tracking**: An accountability section helps students track their study goals, streaks, and session attendance.
* **🤖 AI Assistant**: A helpful chatbot, powered by the Gemini API, provides study tips, book recommendations, and answers to academic questions.

**Landing Page (`/`):**
* **🚀 Modern Landing Page**: A visually appealing home page to attract and inform new users.
* **Responsive Design**: The entire site is built to work seamlessly across desktops and mobile devices.

## 🛠️ Tech Stack

This project is built with a modern set of technologies:

* **Backend**:
    * **Python**: The primary backend language.
    * **Flask**: A lightweight web framework used to build the web server and API.
    * **Flask-SocketIO**: Enables real-time, bidirectional communication for the chat feature.
    * **Gunicorn**: A robust WSGI server for running the application in production.
    * **Eventlet**: A concurrent networking library required for Flask-SocketIO with Gunicorn.
* **Frontend**:
    * **HTML5**: For the structure of the web pages.
    * **CSS3**: For custom styling and responsive design.
    * **JavaScript**: To handle interactive elements, page navigation, and communication with the backend.
* **External APIs**:
    * **Google Gemini API**: Powers the AI assistant for providing intelligent study support.

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

* Python 3.8+ and `pip`
* A virtual environment tool (`venv`)

### 2. Clone the Repository

First, clone the project to your local machine (if it's in a git repository).

```bash
git clone <your-repository-url>
cd vibehack
