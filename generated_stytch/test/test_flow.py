from stytch import Client


def test_stytch():
    client = Client(project_id='', secret='')
    resp = client.Users.create_user({ "email": "nathan-test6@stytch.com", "first_name": "Nathan", "last_name": "Chiu"})
    client.Users.get_user_by_id(resp.user_id)
    client.Users.delete_user(resp.user_id)