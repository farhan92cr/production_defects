 
Application Summary: Production Defects Management System
Overview
The Production Defects Management System is a comprehensive tool designed to streamline the process of tracking and managing defects in a production environment. This system is built using a Flask backend and a MongoDB database, with plans to extend its functionality to mobile devices through a mobile app.

Features
Defect Management:

Add Defect: Users can add new defects, selecting from predefined models and defect types or manually entering new ones. The system automatically records the entry time and date.
Delete Defect: Users can delete existing defects from the system.
Search Defect: Users can search for defects by IMEI, model, defect type, or date, allowing for easy tracking and resolution.
Dropdown Menus:

Model Dropdown: Includes options like X6528, X6526, X6836, and more, with an option to manually enter other models.
Defect Type Dropdown: Includes options like S.N not complete, SIM TRAY MISS, Factory Reset, and more, with an option to manually enter other defect types.
Line Selection: Users can select the production line (P01, P02, P03, P04) when adding a defect.

IMEI Check: The system ensures that no duplicate IMEI entries are saved, maintaining data integrity.

User Authentication: The system includes a secure login/logout functionality to protect sensitive data.

Deployment
The application is containerized using Docker for easy deployment and scalability. It is also integrated with GitHub for version control and continuous integration/continuous deployment (CI/CD) setup.

Mobile App
A mobile app version is planned to provide users with the convenience of managing defects on-the-go. This app will be developed using a cross-platform framework such as React Native or Flutter and will seamlessly integrate with the existing Flask backend.

Technology Stack
Backend: Flask
Database: MongoDB
Frontend: HTML, CSS, JavaScript (for web interface)
Mobile App: React Native/Flutter (planned)
Containerization: Docker
Version Control: GitHub
CI/CD: GitHub Actions (planned)
This system aims to improve the efficiency of defect tracking and management in a production environment, ensuring that issues are quickly identified and resolved to maintain high product quality.
