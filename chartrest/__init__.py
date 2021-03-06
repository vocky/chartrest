# -*- encoding: utf-8 -*-
# We'll render HTML templates and access data sent by POST
# using the request object from flask
import flask
import chartkick
import os
# Initialize the Flask application

VERSION = (0,0,1)
__version__ = '.'.join(map(str, VERSION))
       

def describe(app):
    """get general descriptions of the current instance"""
    rtn = dict(
        version=__version__,
        flask=flask.__version__,
        # XXX: no flask-restful info
        config=dict((k, v) for k, v in app.config.items()\
                    if k.startswith('CHARTREST')),
    )
    return rtn

def description():
    return flask.jsonify(**flask.current_app.description)

def index():
    dq_Tokyo = {'2015-07-14': 0.72, '2015-07-15': 0.75,
                '2015-07-16': 0.85, '2015-07-17': 0.81,
                '2015-07-18': 0.65, '2015-07-19': 0.61,
                '2015-07-20': 0.76, '2015-07-21': 0.87,
                '2015-07-22': 0.84, '2015-07-23': 0.89,
                '2015-07-24': 0.74, '2015-07-25': 0.76,
                '2015-07-26': 0.75
                }
    dq_Average = {'2015-07-14': 0.77, '2015-07-15': 0.77,
                  '2015-07-16': 0.81, '2015-07-17': 0.81,
                  '2015-07-18': 0.64, '2015-07-19': 0.65,
                  '2015-07-20': 0.79, '2015-07-21': 0.88,
                  '2015-07-22': 0.81, '2015-07-23': 0.85,
                  '2015-07-24': 0.79, '2015-07-25': 0.78,
                  '2015-07-26': 0.71
                }
    dq_Fukuoka = {'2015-07-14': 0.71, '2015-07-15': 0.74,
                  '2015-07-16': 0.87, '2015-07-17': 0.87,
                  '2015-07-18': 0.64, '2015-07-19': 0.66,
                  '2015-07-20': 0.73, '2015-07-21': 0.89,
                  '2015-07-22': 0.87, '2015-07-23': 0.84,
                  '2015-07-24': 0.73, '2015-07-25': 0.72,
                  '2015-07-26': 0.78
                }
    dq_string = 'string'
    
    dm_users = [['2015-07-14', 5000], ['2015-07-15', 8000], ['2015-07-16', 7000],
                     ['2015-07-17', 7500], ['2015-07-18', 8500], ['2015-07-19', 8700],
                     ['2015-07-20', 8200], ['2015-07-21', 8000], ['2015-07-22', 8800],
                     ['2015-07-23', 7500], ['2015-07-24', 7800], ['2015-07-25', 8400],
                     ['2015-07-26', 8200]]
    
    tp = [{'data': {'2015-07-27 05:00:00': 1.0, '2015-07-27 06:00:00': 0.9, '2015-07-27 07:00:00': 0.8, 
                    '2015-07-27 08:00:00': 0.7, '2015-07-27 09:00:00': 0.65, '2015-07-27 10:00:00': 0.75, 
                    '2015-07-27 11:00:00': 0.79, '2015-07-27 12:00:00': 0.85, '2015-07-27 13:00:00': 0.95, 
                    '2015-07-27 14:00:00': 1.1, '2015-07-27 15:00:00': 1.2, '2015-07-27 16:00:00': 1.0, 
                    '2015-07-27 17:00:00': 0.9, '2015-07-27 18:00:00': 0.85, 
                    '2015-07-27 19:00:00': 0.80, '2015-07-27 20:00:00': 0.79},
           'name': 'Sunday', 'color': 'navy'},
          {'data': {'2015-07-27 05:00:00': 1.5, '2015-07-27 06:00:00': 2.1, '2015-07-27 07:00:00': 3.6, 
                    '2015-07-27 08:00:00': 5.8, '2015-07-27 09:00:00': 6.3, '2015-07-27 10:00:00': 6.2, 
                    '2015-07-27 11:00:00': 3.8, '2015-07-27 12:00:00': 3.6, '2015-07-27 13:00:00': 3.7, 
                    '2015-07-27 14:00:00': 3.8, '2015-07-27 15:00:00': 4.2, '2015-07-27 16:00:00': 5.4, 
                    '2015-07-27 17:00:00': 7.4, '2015-07-27 18:00:00': 7.9, 
                    '2015-07-27 19:00:00': 6.5, '2015-07-27 20:00:00': 3.8},
           'name': 'Monday', 'color': 'red'},
          {'data': {'2015-07-27 05:00:00': 1.6, '2015-07-27 06:00:00': 2.4, '2015-07-27 07:00:00': 4.2, 
                    '2015-07-27 08:00:00': 7.0, '2015-07-27 09:00:00': 7.8, '2015-07-27 10:00:00': 6.5, 
                    '2015-07-27 11:00:00': 4.4, '2015-07-27 12:00:00': 4.1, '2015-07-27 13:00:00': 4.0, 
                    '2015-07-27 14:00:00': 4.1, '2015-07-27 15:00:00': 4.7, '2015-07-27 16:00:00': 6.2, 
                    '2015-07-27 17:00:00': 8.9, '2015-07-27 18:00:00': 9.8, 
                    '2015-07-27 19:00:00': 8.2, '2015-07-27 20:00:00': 4.9},
           'name': 'Tuesday', 'color': 'lime'},
          {'data': {'2015-07-27 05:00:00': 1.7, '2015-07-27 06:00:00': 2.5, '2015-07-27 07:00:00': 4.3, 
                    '2015-07-27 08:00:00': 7.0, '2015-07-27 09:00:00': 7.8, '2015-07-27 10:00:00': 6.4, 
                    '2015-07-27 11:00:00': 4.4, '2015-07-27 12:00:00': 3.9, '2015-07-27 13:00:00': 4.0, 
                    '2015-07-27 14:00:00': 4.2, '2015-07-27 15:00:00': 4.9, '2015-07-27 16:00:00': 6.4, 
                    '2015-07-27 17:00:00': 9.2, '2015-07-27 18:00:00': 10.2, 
                    '2015-07-27 19:00:00': 8.4, '2015-07-27 20:00:00': 4.9},
           'name': 'Wednesday', 'color': 'purple'},
          {'data': {'2015-07-27 05:00:00': 1.6, '2015-07-27 06:00:00': 2.4, '2015-07-27 07:00:00': 4.0, 
                    '2015-07-27 08:00:00': 6.5, '2015-07-27 09:00:00': 7.3, '2015-07-27 10:00:00': 6.2, 
                    '2015-07-27 11:00:00': 4.4, '2015-07-27 12:00:00': 4.1, '2015-07-27 13:00:00': 4.0, 
                    '2015-07-27 14:00:00': 4.4, '2015-07-27 15:00:00': 5.2, '2015-07-27 16:00:00': 7.1, 
                    '2015-07-27 17:00:00': 10.3, '2015-07-27 18:00:00': 11.4, 
                    '2015-07-27 19:00:00': 9.4, '2015-07-27 20:00:00': 5.5},
           'name': 'Thursday', 'color': 'royalblue'},
          {'data': {'2015-07-27 05:00:00': 1.7, '2015-07-27 06:00:00': 2.1, '2015-07-27 07:00:00': 3.1, 
                    '2015-07-27 08:00:00': 4.6, '2015-07-27 09:00:00': 5.1, '2015-07-27 10:00:00': 4.7, 
                    '2015-07-27 11:00:00': 4.0, '2015-07-27 12:00:00': 4.2, '2015-07-27 13:00:00': 4.7, 
                    '2015-07-27 14:00:00': 5.3, '2015-07-27 15:00:00': 6.7, '2015-07-27 16:00:00': 9.1, 
                    '2015-07-27 17:00:00': 11.9, '2015-07-27 18:00:00': 12.1, 
                    '2015-07-27 19:00:00': 9.5, '2015-07-27 20:00:00': 5.7},
           'name': 'Friday', 'color': '#FFA042'},
          {'data': {'2015-07-27 05:00:00':1.5, '2015-07-27 06:00:00': 1.5, '2015-07-27 07:00:00': 1.4, 
                    '2015-07-27 08:00:00': 1.6, '2015-07-27 09:00:00': 1.9, '2015-07-27 10:00:00': 2.3, 
                    '2015-07-27 11:00:00': 2.9, '2015-07-27 12:00:00': 3.6, '2015-07-27 13:00:00': 4.1, 
                    '2015-07-27 14:00:00': 4.3, '2015-07-27 15:00:00': 4.3, '2015-07-27 16:00:00': 4.0, 
                    '2015-07-27 17:00:00': 3.9, '2015-07-27 18:00:00': 3.7, 
                    '2015-07-27 19:00:00': 3.4, '2015-07-27 20:00:00': 3.0},
           'name': 'Saturday', 'color': '#97CBFF'},
          ]

    ti_city = [['Sapporo', 7.5], ['Tokyo', 6.5], ['Nagoya', 3.5],
             ['Fukuoka', 2.0], ['Nara', 1.2]]

    dm_volume = {'2015-07-27 07:05:00 UTC': 100000, '2015-07-27 07:10:00 UTC': 120050,
             '2015-07-27 07:15:00 UTC': 95000, '2015-07-27 07:20:00 UTC': 90000,
             '2015-07-27 07:25:00 UTC': 98000, '2015-07-27 07:30:00 UTC': 109000,
             '2015-07-27 07:35:00 UTC': 118000, '2015-07-27 07:40:00 UTC': 104000,
             '2015-07-27 07:45:00 UTC': 89100, '2015-07-27 07:50:00 UTC': 105000,
             '2015-07-27 07:55:00 UTC': 140000}   
    return flask.render_template('index.html', **locals())  

def create_app(config=None):
    """Create timorest application
    Config tries the following:
    1. 'config' parameter
    2. 'TIMO_APP_SETTINGS' from the environment variable
    3. 'settings.cfg' file in current path
    
    All config prefixed with 'TIMO_' can be overridden by direct envvar
    """
    app = flask.Flask(__name__)
    ck = flask.Blueprint('ck_page', __name__, static_folder=chartkick.js(), static_url_path='/static')
    app.register_blueprint(ck, url_prefix='/ck')
    app.jinja_env.add_extension("chartkick.ext.charts")    
    
    app.config.from_object('chartrest.default_settings')
    
    if config:
        if isinstance(config, dict):
            app.config.update(config)
        else:
            app.config.from_pyfile(config)
    else:
        app.config.from_envvar('CHART_APP_SETTINGS', silent=True)
        
    env_override = dict((k, v) for k, v in os.environ.items() \
                        if k.startswith('CHARTREST_'))
    app.config.update(env_override)

    app.add_url_rule('/', 'index', index)
    app.description = describe(app)
    app.add_url_rule('/describe', 'describe', description)
    app.add_url_rule('/health_check', 'describe')  # alias
    return app
