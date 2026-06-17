# 🖥️ IT Help Desk Management System

A Python-based help desk ticketing system developed as part of the CompTIA IT Fundamentals (ITF+) Final Project.

## 🚀 Features

- User Registration
- Ticket Creation
- Ticket Tracking
- Ticket Status Updates
- File-Based Storage
- Command Line Interface

## 🛠 Technologies Used

- Python 3
- Visual Studio Code
- Text Files

## 📂 Project Structure

```text
IT-HelpDesk-Management-System
├── main.py
├── users.txt
├── tickets.txt
├── README.md
└── screenshots
    ├── menu.png
    ├── register_user.png
    ├── create_ticket.png
    ├── view_ticket.png
    └── update_ticket.png
```

## Installation

1. Install Python 3 on your computer.
2. Download or copy the project files.
3. Open the project folder in Visual Studio Code.
4. Open a terminal inside VS Code.

Run the program using:

```bash
python main.py
```

---

## How to Use

### Register a User

1. Select option 1 from the main menu.
2. Enter a username when prompted.
3. The user information will be saved to `users.txt`.

### Create a Ticket

1. Select option 2 from the main menu.
2. Enter the username who is reporting the issue.
3. Enter a detailed description of the technical issue.
4. A ticket will be created automatically with a unique ID.

### View Tickets

1. Select option 3 from the main menu.
2. All submitted tickets will be displayed with their current status.

### Update Ticket Status

1. Select option 4 from the main menu.
2. Enter the Ticket ID you wish to update.
3. Choose the new status:
   - **In Progress** - Ticket is being actively worked on
   - **Resolved** - Issue has been fixed

### Exit the Program

Select option 5 to close the application.

---

## 📸 Screenshots & Walkthrough

### Main Menu
![Main Menu](screenshots/menu.png)

**Description:** The main menu displays all available options for the help desk system:
- Option 1: Register a new user
- Option 2: Create a support ticket
- Option 3: View all tickets
- Option 4: Update ticket status
- Option 5: Exit the program

### Register User
![Register User](screenshots/register_user.png)

**Description:** User registration interface where new support staff or users can create an account. The system validates and stores user information in the `users.txt` file.

### Create Ticket
![Create Ticket](screenshots/create_ticket.png)

**Description:** Ticket creation form that collects:
- Username of the person reporting the issue
- Detailed description of the technical problem
- Auto-generates a unique Ticket ID and timestamp

### View Tickets
![View Tickets](screenshots/view_ticket.png)

**Description:** Displays all submitted tickets in a table format showing:
- Ticket ID (unique identifier)
- Username (who reported the issue)
- Issue description
- Current status (Open/In Progress/Resolved)
- Creation timestamp

### Update Ticket Status
![Update Ticket Status](screenshots/update_ticket.png)

**Description:** Status update interface allows support staff to:
- Search tickets by ID
- Change status from "Open" to "In Progress"
- Mark tickets as "Resolved" when the issue is fixed
- Track progress on support requests

---

## Skills Demonstrated

This project demonstrates:

* **IT Support Concepts** - Help desk workflows and ticket management
* **Troubleshooting Processes** - Systematic issue tracking and resolution
* **Data Management** - File I/O and data persistence
* **File Handling** - Reading and writing to text-based data files
* **Programming Fundamentals** - Python functions, loops, and conditionals
* **Problem Solving** - Creating practical solutions for real-world scenarios

---

## Future Improvements

* 🔐 User Authentication (login/password protection)
* 🎨 Graphical User Interface (GUI) with Tkinter or PyQt
* 💾 Database Integration (SQLite or PostgreSQL)
* 📧 Email Notifications (automated alerts for ticket updates)
* 📊 Reporting Dashboard (analytics and statistics)
* ⏱️ Priority Levels (urgent, high, medium, low)
* 📝 Ticket Comments (add updates without changing main description)
* 🔍 Search & Filter (find tickets by status, user, or date)

---

## Author
**Sharmeen Ahsan**

**Course:** CompTIA IT Fundamentals (ITF+)

---

## Conclusion

The IT Help Desk Management System successfully demonstrates the practical application of IT Fundamentals concepts. The project provides a simple but effective solution for managing technical support requests, showcasing core programming skills and IT support knowledge essential for entry-level IT professionals.

---

**Last Updated:** June 2026
