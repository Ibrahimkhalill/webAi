# webAi

A small Django web app with user registration, login/logout and a data submission endpoint.

## Routes

Defined in `webAi/urls.py`:

| Path | View | Purpose |
|---|---|---|
| `/` | `Home` | Landing page |
| `/submit_data` | `submit` | Handles the submitted form |
| `/login/` | `Login` | Sign in |
| `/register/` | `Register` | Create an account |
| `/logout/` | `logoutUser` | Sign out |

The Django admin is at `/admin/`.

## Project layout

```
mainapp/         # settings, root urls, wsgi
webAi/           # views, urls, app logic
templates/       # base.html and page templates
manage.py
```

Note the naming: the *settings* package is `mainapp/`, and the *app* is `webAi/` — the reverse of the usual Django convention.

## Getting started

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/.

## Notes

- The app defines no models of its own; it relies on Django's built-in user model.
- No `requirements.txt` is checked in. `db.sqlite3` is committed.
