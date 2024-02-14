# EVENT PLANNER

**EVENT PLANNER** is your go-to web application for organizing gatherings of any kind. Built with Flask, it simplifies event creation, RSVPs, and guest management, making it perfect for parties, networking events, and dog-centric celebrations.

## Core Features

- **Event Creation**: Effortlessly set up events with essential details such as title, description, date, and time.
- **RSVP Management**: Guests can confirm their attendance with a simple RSVP, ensuring you know who's coming.
- **Guest Information**: Collect guests' names, email addresses, and phone numbers for easy communication and management.

## Quick Start Guide

1. **Clone and Navigate**:
    ```bash
    git clone https://github.com/your-username/event-planner.git
    cd event-planner
    ```

2. **Set Up Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Initialize Database**:
    ```bash
    flask db upgrade
    ```

5. **Run the Application**:
    ```bash
    flask run
    ```
    Visit `http://127.0.0.1:5000/` in your browser.

## How to Use

- **Create Events**: Click on "+ New Event" and fill in the details to create a new event.
- **RSVP**: Guests can RSVP to events by providing their name, email, and phone number, ensuring you have all the info you need for your guest list.
- **Manage Guests**: Review guest details to keep track of who's attending which event.

## Contributing

Your contributions are welcome! Feel free to fork the repo, make improvements, and submit a pull request.

## Note

Remember, EVENT PLANNER is designed to add a touch of ease and fun to your event planning process. Whether it's a formal gathering or a dog party, let's make every event memorable!