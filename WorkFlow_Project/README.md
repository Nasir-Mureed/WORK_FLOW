WorkFlow

A simple project management app for freelancers. Track projects, clients, budgets, sprints, and user stories in one place—without the complexity of big tools.
What is WorkFlow?

WorkFlow helps freelancers stay on top of their work:

    Projects — Create projects with a title, description, budget, amount paid, and deadline. Link each project to a client.
    Clients — Store client names and emails. Attach clients to projects when you create or edit a project.
    Sprints — Break a project into time-boxed sprints (e.g. “Sprint 1”, “Week 1–2”). Each sprint has a start and end date.
    User stories — Inside each sprint, add user stories: short descriptions of what to build (e.g. “As a user I can log in”, “Add payment form”).

You get a dashboard with totals (number of projects, clients, total budget, paid, remaining) and quick links. Everything is scoped to your account—you only see your own projects and clients.
Features

    Sign up & log in — Create an account with username and password. Your profile stores first and last name.
    Dashboard — See how many projects and clients you have, total budget, total paid, and remaining amount. Quick actions to add a project or client.
    Projects — List, add, edit, delete, and search projects. Each project shows budget, paid, client, and due date. Open a project to manage its sprints.
    Project detail — View full project info and all sprints. Create sprints and open any sprint to add or view user stories.
    Clients — List, add, edit, and delete clients. Use them in the project form when creating or editing a project.
    Sprints — Create sprints for a project (name, start date, end date). Sprints are where you add user stories.
    User stories — Per sprint, add and view user stories. Each story is a short description of a task or feature to deliver.
    Responsive UI — Layout works on desktop and mobile. Tailwind CSS is loaded via CDN; no build step required for the default setup.
    Clear flow — Breadcrumbs and short explanations on each page so you always know where you are: Projects → Project detail → Sprints → User stories.

Tech stack

    Backend: Django 6.x
    Database: SQLite3 (file-based; no separate DB server)
    Frontend: HTML templates + Tailwind CSS (CDN)
    Auth: Django’s built-in user system + a simple Profile model (first name, last name)

Project structure

WorkFlow/
├── README.md                 # This file
├── requirements.txt         # Python dependencies
├── context.md                # Technical architecture notes (optional read)
└── WorkFlow_Project/        # Django project
    ├── manage.py             # Django CLI
    ├── WorkFlow_Project/     # Project settings
    │   ├── settings.py
    │   ├── urls.py           # Root URL config
    │   ├── wsgi.py
    │   └── asgi.py
    ├── templates/            # Global templates (e.g. base layout)
    │   └── base.html
    ├── static/               # Static files (if any)
    ├── accounts/             # Sign up, login, logout, profile
    ├── clients/              # Client CRUD
    ├── dashboard/            # Home, dashboard, about, contact, profile page
    ├── projects/             # Project CRUD, detail, search
    ├── sprints/              # Create sprint (per project)
    ├── userStories/          # List and create user stories (per sprint)
    └── theme/                # Optional Tailwind theme app (can be used for build)

How to run the project
1. Prerequisites

    Python 3.10+ (or 3.11, 3.12)
    A terminal (or IDE terminal) in the project folder

2. Create and activate a virtual environment (recommended)

# From the WorkFlow folder (where this README lives)
python3 -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

3. Install dependencies

pip install -r requirements.txt

4. Go into the Django project and run migrations

cd WorkFlow_Project
python manage.py migrate

This creates the SQLite database and tables (users, profiles, clients, projects, sprints, user stories).
5. Start the development server

python manage.py runserver

You should see something like: Starting development server at http://127.0.0.1:8000/
6. Open the app

In your browser go to: http://127.0.0.1:8000/

    Use Sign up to create an account.
    After logging in, you’ll land on the Dashboard. From there you can add clients and projects, then open a project to add sprints and user stories.

Quick start (first use)

    Sign up — Click “Sign up”, enter first name, last name, username, and password.
    Dashboard — You’ll see zeros at first. Use “New project” or “Add client” to get started.
    Add a client (optional) — Go to Clients → Add client. Enter name and email. You can link this client to a project later.
    Add a project — Go to Projects → Add project. Fill in title, description, budget, amount paid, optional client, and dates.
    Open the project — On the projects list, click View details & sprints for your project.
    Create a sprint — On the project page, click Create sprint. Give it a name and start/end dates.
    Add user stories — Click View user stories on the sprint. Then Add user story and type a short description (e.g. “As a user I can log in”).

That’s the full loop: Project → Sprints → User stories.
Main URLs (for reference)
URL 	What it does
/ 	Home (landing)
/accounts/signup/ 	Create account (Sign up)
/accounts/login/ 	Log in
/accounts/logout/ 	Log out
/dashboard/ 	Dashboard (after login)
/profile/ 	Your profile
/projects/ 	List projects
/projects/add/ 	Add project
/projects/detail/<id>/ 	Project detail + sprints
/projects/edit/<id>/ 	Edit project
/clients/ 	List clients
/clients/add 	Add client
/clients/edit/<id>/ 	Edit client
/sprints/create/<project_id>/ 	Create sprint for a project
/userStories/userStories/<sprint_id>/ 	User stories for a sprint
/userStories/create/<sprint_id>/ 	Add user story to a sprint
/admin/ 	Django admin (superuser only)
Optional: Create a superuser (admin)

To use Django’s admin site at /admin/:

cd WorkFlow_Project
python manage.py createsuperuser

Follow the prompts (email can be left blank). Then log in at http://127.0.0.1:8000/admin/ with that account.
Database

    The app uses SQLite3. The database file is created at WorkFlow_Project/db.sqlite3 after you run migrate.
    Your data (users, projects, clients, sprints, user stories) is stored in that file. Keep a backup of db.sqlite3 if you need to preserve data.

Troubleshooting

    “No module named 'django'” — Activate your virtual environment and run pip install -r requirements.txt again from the WorkFlow folder (where requirements.txt is).
    “tailwind_tags is not a registered tag library” — The app is set up to use Tailwind via CDN in the base template. You don’t need the django-tailwind package to run the app. If you removed tailwind or theme from INSTALLED_APPS in settings.py, that’s fine.
    Blank or broken styles — Make sure you’re online; Tailwind is loaded from a CDN. If you’re offline, the layout may still work but styling can be missing.
    404 on login — After login you’re redirected to /dashboard/. If that page errors, run python manage.py migrate and try again.

License and contribution

This project is built for freelancers who want a straightforward way to track projects, clients, sprints, and user stories. Feel free to adapt it for your own use or to contribute improvements (e.g. via pull requests or issues, if the repo is hosted on GitHub or similar).

Enjoy using WorkFlow.
