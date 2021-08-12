from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
import boto3
import mysql.connector

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="SENTRY_DSN",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/")
def index():
    db = mysql.connector.connect(
        host = 'RDS_HOST',
        user = 'admin',
        passwd = 'asdf1234',
        database = 'mysql',
        connection_timeout = 3
    )
    cursor = db.cursor()
    db.close()

    s3 = boto3.client('s3')
    response = s3.list_buckets()

    return 'index page'    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)