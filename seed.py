"""
    This script is intended to populate de database,
    first of all you must install all requirements, then
    create de database with the structure and finally run the script.

    python seed.py <int(default=150)>

    For unauthenticated requests, the rate
   limit allows for up to 60 requests per hour.
   Unauthenticated requests are associated with
   the originating IP address, and not the user making requests.
   More info:
   https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting
"""
import sys
import github_sdk as Github
from app.models import db
from app.models.user import User
from app.app_factory import create_app


def populate_db(users_amount):
    """
        :param users_amount: amount of desired users to be added to the database.
        :return:
    """
    print('Populating database...')
    app = create_app(register_blueprints=False)

    with app.app_context():
        users_per_page = 150  # Maximum 150
        last_user_id = 0
        _registers = 0
        while True:
            filters = {
                'per_page': users_per_page,
                'since': last_user_id
            }
            users = Github.Users.list(filters)
            for git_user in users:
                if _registers == users_amount:
                    print('Database populated')
                    return
                user = User(
                    username=git_user['login'],
                    image_url=git_user['avatar_url'],
                    profile_url=git_user['html_url'],
                    type=git_user['type'])

                db.session.add(user)
                try:
                    db.session.commit()
                    _registers += 1
                    last_user_id = git_user['id']
                except Exception:
                    print(user)
                    db.session.rollback()


if __name__ == '__main__':
    users_amount = 150
    try:
        users_amount = int(sys.argv[1])
    except ValueError:
        print('{} is not a valid number'.format(sys.argv[1]))
        exit()
    except IndexError:
        pass
    populate_db(users_amount)
