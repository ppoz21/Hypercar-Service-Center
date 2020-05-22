IS_RELEASE_SERVER = bool(input().lower() == 'true')

DEBUG = not IS_RELEASE_SERVER
