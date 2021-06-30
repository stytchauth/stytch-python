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
resp = stytch_client.users.create(email="person@app.com")

# Set MagicLinkURLs on the dashboard
Set them [here](https://stytch.com/dashboard/magic-link-urls)

# Send magic link to user
stytch_client.magic_links.email.send(
    email=resp.email_id,
    login_magic_link_url="https://my-app.com/login",
    signup_magic_link_url="https://my-app.com/signup",
)

# Authenticate magic link
stytch_client.magic_links.authenticate(token="*** EMAILED TOKEN ****")
```

### Login Or Create User
```python
stytch_client.magic_links.email.login_or_create(
    email="person@app.com",
    login_magic_link_url="https://my-app.com/login",
    signup_magic_link_url="https://my-app.com/signup",
)
```

### Handling exceptions:
Handle Stytch exceptions with StytchErrors
```python
from stytch.api.error import StytchError

try:
    stytch_client.magic_links.authenticate(token="token")
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
pytest tests/integration/test_integration.py --project_id="***YOUR PROJECT ID***" --secret="***YOUR SECRET KEY***" --email="***YOUR EMAIL***" --phone_number="***YOUR PHONE NUMBER***"
```

### Documentation:

https://stytch.com/docs/api

### More information:

Visit https://stytch.com/ for more information
