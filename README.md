# 🏈 NFL Prospect API

## Description
This project is a full-stack application that provides information about NFL prospects and drafted players. It consists of a React TypeScript frontend and a Flask (Python) backend, leveraging the NFL v5 Sportradar US API to fetch player data.

The application allows users to input a player's name and the year they were either drafted or considered an NFL prospect. It then retrieves and displays key information about the player, including:

- Position
- Height
- Weight
- Year
- Place of birth
- University
- Conference

This tool can be particularly useful for sports analysts, fantasy football enthusiasts, or anyone interested in NFL player statistics and background information.

## ✨ Features
- User-friendly React TypeScript frontend
- Flask (Python) backend for API interactions
- Integration with NFL v5 Sportradar US API
- Retrieval of comprehensive player information

## 🚀 Installation

### Prerequisites
- Node.js and npm (for the frontend)
- Python 3.x (for the backend)
- NFL v5 Sportradar US API key

### Frontend Setup
1. Clone the repository:
2. Install dependencies:
3. Start the development server:
   
### Backend Setup
1. Navigate to the backend directory:
2. Create a virtual environment (optional but recommended):
3. Install required Python packages:
4. Set up your API key:
   Create a `.env` file in the backend directory and add your NFL v5 Sportradar US API key:
   
### Backend Setup

1. Navigate to the backend directory:
2. Create a virtual environment (optional but recommended):
3. Install required Python packages:
4. Set up your API key:
  Create a `.env` file in the backend directory and add your NFL v5 Sportradar US API key: API_KEY={your_api_key}
5. Start the Flask server:
## Usage

1. Open your web browser and go to `http://localhost:5173` (or the port where your React app is running).
2. Enter the player's name and the year of interest in the provided fields.
3. Click the submit button to retrieve and display the player's information.



