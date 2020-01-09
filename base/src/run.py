#!/usr/bin/env python
import json
import os
import sys
import time
import requests

ARGS = sys.argv


def _usage_and_exit():
    print("""
export SHIFTER_USER=username
export SHIFTER_PASS=password
export SHIFTER_SITE_ID=xxxx-xxxx-xxxxxx

run.py [start|stop]

- `start` sets SHIFTER_APP_URL as environment variable.
- `stop` terminates an app.
    """)

    exit(0)


class ShifterAPI:
    def __init__(self):
        self.user = os.getenv("SHIFTER_USER")
        self.password = os.getenv("SHIFTER_PASS")
        self.endpoint = os.getenv("SHIFTER_ENDPOINT", 'https://api.getshifter.io/latest')
        self.site_id = os.getenv("SHIFTER_SITE_ID")
        self.token = None

    def login(self):
        params = {}
        params['username'] = self.user
        params['password'] = self.password

        r = requests.post(self.endpoint + '/login', json=params)
        if not r.ok:
            print(r.status_code, r.text)
            exit(1)

        self.token = r.json()['AccessToken']
        return None

    def start(self):
        headers = {'Authorization': self.token}

        already_running = False
        r = requests.post(
            self. endpoint + '/sites/{site_id}/wordpress_site/start'.format(site_id=self.site_id),
            headers=headers
        )
        if r.status_code == 409:
            print('already running detected.')
            already_running = True
            print('::set-env name=SHIFTER_APP_KEEP::true')
        elif not r.ok:
            print(r.status_code, r.text)
            exit(1)

        if not already_running:
            notification_id = r.json()['notification_id']

            print('Success to start container, waiting for COMPLETE...')
            time.sleep(5)
            complete = False
            for x in range(1, 30):
                print('.', end='', flush=True)
                r = requests.get(
                    self. endpoint + '/sites/{site_id}/wordpress_site/check_wp_setup/{notification_id}'.format(site_id=self.site_id, notification_id=notification_id),
                    headers=headers
                )
                if os.getenv("DEBUG"):
                    print(r.json())
                if r.json() == 'COMPLETE':
                    complete = True
                    break
                elif r.json().startswith('ERROR_'):
                    print(r.json())
                    print('Please retry rater')
                    break
                time.sleep(5)
            print()

            if not complete:
                print('Timeout error!')
                print('send Stop container')
                self.stop()
                exit(1)

        r = requests.get(
            self.endpoint + '/sites/{site_id}'.format(site_id=self.site_id),
            headers=headers
        )
        wordpress_site_url = r.json()['wordpress_site_url']
        if r.json().get('subdir'):
            wordpress_site_url = ('/').join([wordpress_site_url, r.json().get('subdir')])

        return wordpress_site_url

    def stop(self):
        headers = {'Authorization': self.token}

        r = requests.post(
            self. endpoint + '/sites/{site_id}/wordpress_site/stop'.format(site_id=self.site_id),
            headers=headers
        )

        if r.ok:
            print('Container has been terminated')
            return None

        print(r.status_code, r.text)

        return None


def start():
    s = ShifterAPI()
    s.login()
    url = s.start()
    print('::set-output name=shifter_app_url::{s}'.format(s=url))
    print('::add-mask::{s}'.format(s=url))
    return None


def stop():
    if os.getenv("SHIFTER_APP_KEEP"):
        if os.getenv("SHIFTER_APP_KEEP") != 'false':
            print('Skipped stop container, due to env SHIFTER_APP_KEEP.')
            exit(0)

    s = ShifterAPI()
    s.login()
    s.stop()
    return None


# Initialize
if len(ARGS) < 2:
    _usage_and_exit()

if ARGS[1] == 'start':
    start()
elif ARGS[1] == 'stop':
    stop()


exit(0)
