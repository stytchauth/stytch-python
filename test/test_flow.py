import stytch


configuration = stytch.Configuration(
    username = 'project-test-9d426430-e7a7-4f4c-86c3-819f499cd19d',
    password = 'secret-test-_WEsPmDcCtfh6twRLbdAtGtNlfBLAZP4g5w='
)

def test_stytch():
    stytch_client = stytch.ApiClient(configuration)
    api_instance = stytch.UsersApi(stytch_client)

    resp = api_instance.create_user({ "email": "nathan-test6@stytch.com", "first_name": "Nathan", "last_name": "Chiu"})
    created_user_id = resp.user_id
    assert created_user_id 
    resp = api_instance.get_user_by_id(created_user_id)
    assert resp
    resp = api_instance.delete_user(created_user_id)
