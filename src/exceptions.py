# Author: Albert Esteve <aesteve@redhat.com>
#
# This file is licensed under the GNU General Public License.
# Please see the LICENSE file

"""
Centralized exception handling for the entire package.
"""


from functools import wraps

from github.GithubException import GithubException

from . import log


def exception_handler(func):
    """
    Can be used as a decorator for CLI functions to handle all posible
    exceptions.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except GithubException as exc:
            log.critical('Failed to connect to GitHub: %s', exc)

    return wrapper
