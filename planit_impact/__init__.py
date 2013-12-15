from flask import Flask

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)

import settings, models, routes
