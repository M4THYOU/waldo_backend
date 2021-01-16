# Setup

1. Make sure you have Python 3.9.1 installed on your machine.
2. Do `git clone https://github.com/M4THYOU/waldo_backend.git`.
3. Do `cd waldo` or whatever this project is called to enter the base directory of the project. You're in the right spot if and only if `manage.py` is in your immediate directory. If not, go to the directory where it is.
4. Run `mkvirtualenv venv` to make a virtual environment.
5. I think it will automatically enter you into the virtual environment, but run `source venv/bin/activate` just to make sure.
6. Run `python -m pip install -r requirements.txt` to install all the required packages for the project.
7. Ask Matthew for the `secrets.py` file. Put it in the same directory as `settings.py`. I.e. the path from base of the project is `waldo/secrets.py`.
8. Run `python manage.py runserver` to start the server. It should work, you can verify this by going to http://localhost:8000/. If it doesn't work, well just fix what's broken. Use your critical thinking skills for this.

# Development Process
* Create your own dev branch with the following command `git checkout -b dev-<you name here>`. Obviously, replace `<you name here>` with your actual name.
* Never ever commit to master branch. Work on the branch above and make a pull request when you want changes to be merged.
* Message Matthew when you make a pull request, and he will merge it in.
* We are using Bootstrap 4.1 as a frontend ~~framework~~ library: https://getbootstrap.com/docs/4.1/getting-started/introduction/ 