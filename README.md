
# Notes-api

Why use Django Rest Framework for this project?

Django Rest Framework (DRF) is a powerful and popular toolkit for building Web APIs using the Django framework. Here are some key reasons why developers choose to use Django Rest Framework for API development, presented in points:

1. Built on Django: DRF is built on top of the Django framework, leveraging its strengths and providing a seamless integration for building APIs. This means you can take advantage of Django's features like authentication, ORM, and other utilities while building your API.

2. Rapid Development: DRF simplifies and speeds up the process of building APIs by providing a set of reusable components, such as serializers and views, that handle common tasks. This allows developers to focus more on the business logic rather than boilerplate code.

3. Serialization: DRF provides a powerful serialization framework that allows you to easily convert complex data types, such as Django models, into Python data types that can be easily rendered into various content types like JSON or XML.

4. Authentication and Authorization: DRF offers robust authentication and authorization mechanisms out of the box. It supports various authentication methods, including token-based authentication, OAuth, and more. Authorization can be easily customized to control access to different parts of your API.
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`DB_HOST`

`DB_USERNAME`

`DB_PASSWORD`

`DB_NAME`

A .sample-env file has been added as an example.
## Setting Up PostgreSQL and Python Virtual Environment

This guide will walk you through the steps to set up PostgreSQL and a Python virtual environment for your project.

### Prerequisites

- [ ]  Ensure that you have Python installed. If not, download and install it from [Python Official Website](https://www.python.org/).
- [ ]  Make sure you have administrative privileges on your machine to install PostgreSQL.

### PostgreSQL Installation

1. **Download PostgreSQL:**
   - Visit the [PostgreSQL download page](https://www.postgresql.org/download/).
   - Choose the appropriate version for your operating system.
   - Follow the installation instructions for your specific OS.

2. **Installation Steps:**
   - During the installation process, you'll be prompted to set a password for the PostgreSQL superuser. Remember this password as you'll need it later.
   - Make a note of the port number used by PostgreSQL (default is `5432`).

3. **Verify Installation:**
   - Open a command prompt or terminal and run the following command to verify that PostgreSQL is installed:
     ```bash
     psql --version
     ```

### Python Virtual Environment

1. **Clone the Project Repository:**
   - Open a command prompt or terminal and run the following command to clone the project repository:
     ```bash
     git clone https://github.com/PallavMarwaha/notes-api
     ```

2. **Create Virtual Environment:**
   - Run the following command to create a virtual environment inside your project directory:
     ```bash
     python -m venv venv
     ```

3. **Activate Virtual Environment:**
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Dependencies:**
   - With the virtual environment activated, install project dependencies using `pip`:
     ```bash
     pip install -r requirements.txt
     ```

### Configuration


1. **Run Migrations:**
   - Run database migrations to create necessary tables and structures:
     ```bash
     python manage.py migrate
     ```
2. **Run the Django Development Server:**
- Start the Django development server:
```bash
python manage.py runserver
```

3. **Access Your Project:**
   - Open your web browser and navigate to [http://localhost:8000/](http://localhost:8000/) to see your project in action.

4. You can access the API documentation and interact with different API endpoints.

5. **Run the tests:**
```bash
python manage.py test
```
## Screenshots

![App Screenshot](https://i.imgur.com/c9ak0eK.jpeg)

