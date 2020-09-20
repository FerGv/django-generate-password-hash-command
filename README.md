# django-generate-password-hash-command

Create a `generate_password_hash` command for Django shell to generate a hashed password with the provided argument using project configurations.

## Example
```
$ python manage.py generate_password_hash test
-> pbkdf2_sha256$180000$9BkvUiEaaphE$3NW0eA3UYf5ukezQhfSJhf0xGsPVl0pbwWN+9bbXLwU=
```
