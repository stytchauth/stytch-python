# Stytch Python API Client
---

## Requirements:
Stytch python supports Python 3.4+

## Installation:
`pip install stytch`

## Usage:

```python
from stytch import Client

# Initialize client
stytch_client = Client(
    project_id="***YOUR PROJECT ID***",
    secret="***YOUR PROJECT SECRET***",
    environment="test",
)

# Create a user
resp = stytch_client.Users.create(email="person@app.com")

# Send magic link to user
stytch_client.MagicLink.send(
    method_id=resp.user_id, 
    email=resp.email_id, 
    magic_link_url="https://my-app.com/login"
)

# Authenticate magic link
stytch_client.MagicLink.authenticate(token="*** EMAILED TOKEN ****")
```

### Login Or Create User
```python
stytch_client.MagicLink.login_or_create(
    email="person@app.com", 
    login_magic_link_url="https://my-app.com/login",
    signup_magic_link_url="https://my-app.com/signup"
)
```

### Login Or Invite By Email
```python
stytch_client.MagicLink.login_or_invite_by_email(
    email="person@app.com", 
    login_magic_link_url="https://my-app.com/login",
    invite_magic_link_url="https://my-app.com/invite"
)
```

### Handling exceptions:
Handle Stytch exceptions with StytchErrors
```python
from stytch.api.error import StytchError 

try: 
    stytch_client.MagicLink.authenticate(token="token")
except StytchError as error:
    # Handle stytch errors here
    pass
except Exception as error:
    # Handle error here
    pass
```

### Testing:
Unit tests are run via `pytest tests/api`

Integration tests accept a project_id + secret via command line
```
pytest tests/integration/test_integration.py --project_id="***YOUR PROJECT ID***" --secret="***YOUR SECRET KEY***"
```

### Documentation:

docs.stytch.com

### More information:

Visit https://stytch.com/ for more information