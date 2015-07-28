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
    
    dm_users = {'2015-07-14': 5000, '2015-07-15': 8000,
                  '2015-07-16': 7000, '2015-07-17': 7500,
                  '2015-07-18': 8500, '2015-07-19': 8700,
                  '2015-07-20': 8200, '2015-07-21': 8000,
                  '2015-07-22': 8800, '2015-07-23': 7500,
                  '2015-07-24': 7800, '2015-07-25': 8400,
                  '2015-07-26': 8200
                }
    browser_stats = [['2015-07-14', 5000], ['2015-07-15', 8000], ['2015-07-16', 7000],
                     ['2015-07-17', 7500], ['2015-07-18', 8500], ['2015-07-19', 8700],
                     ['2015-07-20', 8200], ['2015-07-21', 8000], ['2015-07-22', 8800],
                     ['2015-07-23', 7500], ['2015-07-24', 7800], ['2015-07-25', 8400],
                     ['2015-07-26', 8200]]

    temperature = [{'data': {   '2015-07-15': 0.72,
                                '2015-07-16': 0.75,
                                '2015-07-17': 0.85,
                                '2015-07-18': 0.81,
                                '2015-07-19': 0.65,
                                '2015-07-20': 0.61,
                                '2015-07-21': 0.76,
                                '2015-07-22': 0.87,
                                '2015-07-23': 0.84,
                                '2015-07-24': 0.89,
                                '2015-07-25': 0.74,
                                '2015-07-26': 0.76},
                    'name': 'Tokyo'},
                    {'data': { '2015-07-15': 0.71,
                                '2015-07-16': 0.79,
                                '2015-07-17': 0.81,
                                '2015-07-18': 0.89,
                                '2015-07-19': 0.61,
                                '2015-07-20': 0.65,
                                '2015-07-21': 0.79,
                                '2015-07-22': 0.81,
                                '2015-07-23': 0.84,
                                '2015-07-24': 0.85,
                                '2015-07-25': 0.71,
                                '2015-07-26': 0.78},
                    'name': 'Average', 'color':'red'},
                    {'data': { '2015-07-15': 0.77,
                                '2015-07-16': 0.71,
                                '2015-07-17': 0.85,
                                '2015-07-18': 0.84,
                                '2015-07-19': 0.64,
                                '2015-07-20': 0.61,
                                '2015-07-21': 0.77,
                                '2015-07-22': 0.86,
                                '2015-07-23': 0.81,
                                '2015-07-24': 0.89,
                                '2015-07-25': 0.75,
                                '2015-07-26': 0.71},
                    'name': 'Sapporo'},
                    {'data': { '2015-07-15': 0.74,
                                '2015-07-16': 0.77,
                                '2015-07-17': 0.81,
                                '2015-07-18': 0.88,
                                '2015-07-19': 0.61,
                                '2015-07-20': 0.67,
                                '2015-07-21': 0.74,
                                '2015-07-22': 0.81,
                                '2015-07-23': 0.88,
                                '2015-07-24': 0.81,
                                '2015-07-25': 0.78,
                                '2015-07-26': 0.79},
                    'name': 'Fukuoka'}]

    sizes = [['X-Small', 5], ['Small', 27], ['Medium', 10],
             ['Large', 14], ['X-Large', 10]]

    areas = {'2015-07-27 07:05:00 UTC': 100000, '2015-07-27 07:10:00 UTC': 120050,
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
