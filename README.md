# Django NFL Simulation Web App

This Django web app allows users to select their favorite NFL team after logging in or creating an account. Users can then simulate their team's games, track their record within the division, and reset the simulation at any point. After 17 games, users can proceed to a screen displaying playoff standings.

## App Structure

The app is structured into five distinct Django apps:

1. **core**: This is the standard app, typically named after the project. It houses the models for both teams and users, as these models are utilized across multiple screens. Besides handling these models, it also manages its usual responsibilities.

2. **custom_auth**: This app extends the standard user profile to associate a favorite team with each user. It contains the logic for managing login and registration in the views, and also houses the necessary forms for these processes.

3. **team**: This app organizes the NFL teams by division and populates the template to display them visually. It provides the interface for users to select their favorite team.

4. **my_team**: After a user selects their team in the team app, they are directed to this app. It shows the weekly matchups for the selected team and tracks their standings within the division.

5. **results**: This app displays the playoff standings, showing which teams made the playoffs after the regular season simulations.

## Installation Instructions

To set up and run this Django web app, follow these steps:

### Clone or Download the Repository

Visit the [GitHub repository](https://github.com/seandifatta1/Django_demo).

Clone the repository using Git:

```bash
git clone https://github.com/seandifatta1/Django_demo.git
```

Or download the repository as a ZIP file and extract it.

Set Up Virtual Environment
Ensure you have Python installed. If not, download and install it from python.org.

Navigate to the project directory:

```bash
# Windows
chdir path\to\app\Django_demo

# MacOs/Linux
cd /path/to/app/Django_demo
```
Install venv if you haven't already:

```bash
python -m ensurepip --upgrade
python -m pip install --user virtualenv
```
Create a virtual environment:

```bash
python -m venv venv
```
Activate the virtual environment:

```bash

# Windows 
venv\Scripts\activate

# MacOs/Linux
source venv/bin/activate
```
Install the required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

Run the Django App
Apply the database migrations:

```bash
python manage.py migrate
```
Create a superuser to access the admin interface:

```bash
python manage.py createsuperuser
```
Run the development server:

```bash
python manage.py runserver
```
Open a web browser and go to http://127.0.0.1:8000 to access the app.