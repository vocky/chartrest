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
    exchange = {'2001-01-31': 1.064, '2002-01-31': 1.1305,
                '2003-01-31': 0.9417, '2004-01-31': 0.7937,
                '2005-01-31': 0.7609, '2006-01-31': 0.827,
                '2007-01-31': 0.7692, '2008-01-31': 0.6801,
                '2009-01-31': 0.7491, '2010-01-31': 0.7002,
                '2011-01-31': 0.7489, '2012-01-31': 0.7755,
                '2013-01-31': 0.7531
                }

    browser_stats = [['Chrome', 52.9], ['Firefox', 27.7], ['Opera', 1.6],
                     ['Internet Explorer', 12.6], ['Safari', 4]]

    temperature = [{'data': {  '2012-00-01 00:00:00 -0700': 7,
                                '2012-01-01 00:00:00 -0700': 6.9,
                                '2012-02-01 00:00:00 -0700': 9.5,
                                '2012-03-01 00:00:00 -0700': 14.5,
                                '2012-04-01 00:00:00 -0700': 18.2,
                                '2012-05-01 00:00:00 -0700': 21.5,
                                '2012-06-01 00:00:00 -0700': 25.2,
                                '2012-07-01 00:00:00 -0700': 26.5,
                                '2012-08-01 00:00:00 -0700': 23.3,
                                '2012-09-01 00:00:00 -0700': 18.3,
                                '2012-10-01 00:00:00 -0700': 13.9,
                                '2012-11-01 00:00:00 -0700': 9.6},
                    'name': 'Tokyo', 'color': 'red'},
                    {'data': { '2012-00-01 00:00:00 -0700': -0.2,
                                '2012-01-01 00:00:00 -0700': 0.8,
                                '2012-02-01 00:00:00 -0700': 5.7,
                                '2012-03-01 00:00:00 -0700': 11.3,
                                '2012-04-01 00:00:00 -0700': 17,
                                '2012-05-01 00:00:00 -0700': 22,
                                '2012-06-01 00:00:00 -0700': 24.8,
                                '2012-07-01 00:00:00 -0700': 24.1,
                                '2012-08-01 00:00:00 -0700': 20.1,
                                '2012-09-01 00:00:00 -0700': 14.1,
                                '2012-10-01 00:00:00 -0700': 8.6,
                                '2012-11-01 00:00:00 -0700': 2.5},
                    'name': 'New York'},
                    {'data': { '2012-00-01 00:00:00 -0700': -0.9,
                                '2012-01-01 00:00:00 -0700': 0.6,
                                '2012-02-01 00:00:00 -0700': 3.5,
                                '2012-03-01 00:00:00 -0700': 8.4,
                                '2012-04-01 00:00:00 -0700': 13.5,
                                '2012-05-01 00:00:00 -0700': 17,
                                '2012-06-01 00:00:00 -0700': 18.6,
                                '2012-07-01 00:00:00 -0700': 17.9,
                                '2012-08-01 00:00:00 -0700': 14.3,
                                '2012-09-01 00:00:00 -0700': 9,
                                '2012-10-01 00:00:00 -0700': 3.9,
                                '2012-11-01 00:00:00 -0700': 1},
                    'name': 'Berlin'},
                    {'data': { '2012-00-01 00:00:00 -0700': 3.9,
                                '2012-01-01 00:00:00 -0700': 4.2,
                                '2012-02-01 00:00:00 -0700': 5.7,
                                '2012-03-01 00:00:00 -0700': 8.5,
                                '2012-04-01 00:00:00 -0700': 11.9,
                                '2012-05-01 00:00:00 -0700': 15.2,
                                '2012-06-01 00:00:00 -0700': 17,
                                '2012-07-01 00:00:00 -0700': 16.6,
                                '2012-08-01 00:00:00 -0700': 14.2,
                                '2012-09-01 00:00:00 -0700': 10.3,
                                '2012-10-01 00:00:00 -0700': 6.6,
                                '2012-11-01 00:00:00 -0700': 4.8},
                    'name': 'London'}]

    sizes = [['X-Small', 5], ['Small', 27], ['Medium', 10],
             ['Large', 14], ['X-Large', 10]]

    areas = {'2013-07-27 07:08:00 UTC': 4, '2013-07-27 07:09:00 UTC': 3,
             '2013-07-27 07:10:00 UTC': 2, '2013-07-27 07:04:00 UTC': 2,
             '2013-07-27 07:02:00 UTC': 3, '2013-07-27 07:00:00 UTC': 2,
             '2013-07-27 07:06:00 UTC': 1, '2013-07-27 07:01:00 UTC': 5,
             '2013-07-27 07:05:00 UTC': 5, '2013-07-27 07:03:00 UTC': 3,
             '2013-07-27 07:07:00 UTC': 3}   
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
