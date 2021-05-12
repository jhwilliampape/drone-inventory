import os

basedir = os.path.abspath(os.path.dirname(__file__))


# Gives us access to the project in any Operating System
# Allows outside files/folders to be added to the project from the base directory


class Config():
    """
    Set config variables for the flask app here
    using any variables where available
    otherwise create them if not done already
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False  # Turns off notifications from database - can get annoying
    
