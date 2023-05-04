# django_colab
# My Django CRUD App

A web application built with Django to manage blog posts and user profiles, featuring a responsive design and search functionality.



## Features

- User authentication and registration
- Blog post creation, editing, and deletion
- User profile management with profile picture uploads
- Search functionality with autocomplete
- Responsive design with a left and right background image
- File upload functionality for various formats (e.g., PDF, DOCX)

## Installation and Setup

1. Clone the repository

2. Install the required dependencies:

cd my-django-crud-app
pip install -r requirements.txt

3. Apply migrations and create the database:

python manage.py migrate

4. Start the development server:

python manage.py runserver

5. Access the app in your browser at `http://127.0.0.1:8000/`.

## Usage

- Register a new user or log in with an existing account.
- Create, edit, and delete blog posts.
- Update your user profile and upload a profile picture.
- Search for blog posts using the search bar with autocomplete suggestions.
- Upload files in various formats (e.g., PDF, DOCX).

## Contributing

We welcome contributions to improve the project. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them to your branch.
4. Submit a pull request for your changes to be reviewed and merged.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.


## Acknowledgments

- Django web framework
- Bootstrap CSS library
- jQuery and autocomplete.js
- Mammoth.js for file conversion
