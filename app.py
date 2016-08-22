from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TEAM_NAME = "Zappa"
SLACK_TOKEN = "xoxp-Z4PP4Z4PP4-Z4PP4Z4PP4-Z4PP4Z4PP4-Z4PP4Z4PP4"
SLACK_DOMAIN = "zappateam.slack.com"

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':

        email = request.form['email']
        data = {
            'email': email,
            'token': SLACK_TOKEN,
            'set_active': True
        }
        url = 'https://' + SLACK_DOMAIN + '/api/users.admin.invite'

        resp = requests.post(url, data=data)
        if resp.status_code == 200:
            return render_template('success.html', 
                    team_name=TEAM_NAME,
                )
        else:
            return render_template('failure.html', 
                    team_name=TEAM_NAME,
                )

    else:
        return render_template('hello.html', 
                team_name=TEAM_NAME,

            )
