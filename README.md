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
stytch_client.MagicLink.send_by_id(method_id=resp.user_id)

# Authenticate magic link
stytch_client.MagicLink.authenticate(token="*** EMAILED TOKEN ****")
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


### Documentation:

TBI

### More information:

Visit https://stytch.com/ for more information