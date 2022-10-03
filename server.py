from email_app import app
from email_app.controllers import emails
app.secret_key = "secreto"


if __name__=="__main__":
    app.run(debug=True)