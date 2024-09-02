# MyCodeBlog

**MyCodeBlog** is a blogging platform built with Django. It allows users to create, view, edit, and delete blog posts. Users must sign up and log in to access certain features such as creating, editing, or deleting posts. 

## Features

- **User Authentication:** Users can sign up, log in, and log out.
- **Post Management:** Users can create, view, edit, and delete posts.
- **User Permissions:** Only the author of a post can edit or delete it.
- **Security:** Forms are protected against CSRF attacks, and user permissions are enforced to ensure data security.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/goldenjeffempire/MyCodeBlog.git
    cd MyCodeBlog
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

- **Sign Up:** Visit `/signup/` to create a new account.
- **Log In:** Visit `/login/` to log in to your account.
- **Create Post:** After logging in, visit `/create/` to create a new post.
- **Edit/Delete Post:** Only the author of a post can edit or delete it. Visit `/edit_post/<post_id>/` to edit and `/delete_post/<post_id>/` to delete.

## Security

- Ensure CSRF protection is enabled for all forms.
- Use HTTPS to encrypt data between the user and server. Configure your web server and obtain an SSL certificate.
- Restrict admin access to specific IP addresses where possible.

## Author
  **Author**
- **Jeffery Emuodafevware**  
  [GitHub](https://github.com/goldenjeffempire)  
  [Twitter](https://twitter.com/goldenjeffemp)  
  [LinkedIn](https://linkedin.com/in/jeffery-emuodafevware)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

