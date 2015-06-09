DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "e5016461-ae6a-4667-b783-ed336bfe5066f81aaa7c-17ed-48ff-9c4d-05deae02c774b2b13b82-28ec-4c4d-b483-c0f1b8b5888d"
NEVERCACHE_KEY = "a1571c58-2a07-4aac-9b4c-943a80c671657ed2f039-c58f-4305-900d-c15066f925208d8b8411-0c47-4328-b70a-8c7fd5997c22"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
