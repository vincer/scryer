import urllib

from flask import Flask, render_template, request

from pyicloud import PyiCloudService

from auth import requires_auth

app = Flask(__name__)

app.config.from_pyfile('config.py')

accounts_config = app.config['ACCOUNTS_CONFIG']


@app.route('/js')
@requires_auth
def js():
    return render_template('simple.js', **app.config)

@app.route('/accounts')
@requires_auth
def accounts():
    return render_template('accounts.html', accounts=accounts_config)


@app.route('/accounts/<account_id>/')
@requires_auth
def account(account_id):
    name = accounts_config[account_id]['name']
    return render_template('account.html', **locals())


@app.route('/accounts/<account_id>/devices')
@requires_auth
def devices(account_id):
    devices = get_devices_by_account_id(account_id)
    return render_template('devices.html', **locals())


# use "path:" in annotation, otherwise flask will still interpret urlencoded '%2F' as an actual '/'
@app.route('/accounts/<account_id>/devices/<path:device_id>')
@requires_auth
def device(account_id, device_id):
    d = get_devices_by_account_id(account_id)[urllib.unquote(device_id)]
    status = d.status()
    device_status = d['deviceStatus']
    battery = int(status['batteryLevel'] * 100)
    name = status['name']
    location = d.location()
    return render_template('device.html', **locals())


@app.route('/accounts/<account_id>/devices/<path:device_id>/sound', methods=['GET', 'PUT'])
@requires_auth
def sound(account_id, device_id):
    d = get_devices_by_account_id(account_id)[urllib.unquote(device_id)]
    name = d.status()['name']
    if request.method == 'PUT':
        d.play_sound()
        sound_playing = True
        return render_template('sound.html', **locals())
    else:
        sound_playing = False
        return render_template('sound.html', **locals())


def get_devices_by_account_id(account_id):
    user = accounts_config[account_id]
    return get_devices_by_apple_credentials(user['apple_id'], user['apple_password'])


def get_devices_by_apple_credentials(apple_id, apple_password):
    api = PyiCloudService(apple_id, apple_password)
    return api.devices


@app.template_filter('urlencode2')
def urlencode2_filter(s):
    """
    Jinja2's urlencode does not encode '/' as %2F much like the default behavior or urllib.quote,
    and there's no option to make it do so.
    So, this filter will do that.
    :param s: string to urlencode
    :return: fully urlencoded string, including the '/'s
    """
    return urllib.quote(s, safe='')


if __name__ == '__main__':
    app.run(debug=True)
