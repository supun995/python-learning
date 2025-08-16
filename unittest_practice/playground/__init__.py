from .effects import blur, mode, save, InvalidImageError
from .userman import UserManagement

__all__ = [
    'blur',
    'mode',
    'save',
    'fix_lab_path',
    'UserManagement',
    'InvalidImageError',
]


###############################################################################
''' This application is served via a reverse proxy to allow it to become
    accessible from the browser on /app/

    This is required solely for the lab environment to ensure the /app/ URL path
    is prepended to the URL.

    Remove this code if this application is run outside of the lab environment.
'''
import os
import re
# Capture group 1 contains the link type: href, action, src.
# Capture group 2 contains the local URL path.
# E.g: href="/login"
#   1: href
#   2: /login
app_urls = re.compile(r'''([href|action|src]){1}=['"](/.*?)['"].*?''', re.I)

def fix_lab_path(response):
    if os.environ.get('APP_UNDER_TEST', False):
        return response
    # Adjust the URL for redirects.
    if response.location:
        response.location = '/'.join(['/app', response.location.lstrip('/')])
    # Adjust URLs found in HTML.
    if 'html' in response.content_type:
        response.data = app_urls.sub(r'\1="/app\2"',response.data.decode())
    return response

###############################################################################