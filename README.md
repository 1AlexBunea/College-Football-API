# NFL Prospect API

This repository contains the source code for the NFL Prospect API project. The project consists of a front end developed using React JS and a backend developed in Python. The application fetches detailed information about NFL prospects or drafted players based on user input.

## Overview

The front end accepts two parameters: a player's name and the year they were either drafted or were an NFL prospect. It then sends a request to a local server. The backend processes the request, accesses the NFL v5 Sportradar US API, and returns comprehensive data about the player. This data is then displayed on the React JS front end.

## Features

- **Player Information**: Fetches and displays detailed information about NFL players, including:
  - Position
  - Height
  - Weight
  - Year
  - Place of birth
  - University
  - Conference

- **Responsive Design**: The front end is optimized for various screen sizes, providing a seamless experience on both desktop and mobile devices.

## Installation

To run the NFL Prospect API project locally, follow these steps:

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/NFL-Prospect-API.git
   cd NFL-Prospect-API/backend
