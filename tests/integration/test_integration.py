import stytch
import pytest


class TestIntegration:
    """
    This tests runs through available api calls in the API

    Pass in your project id and secret to run this.
    """

    @pytest.mark.unit
    def test_full_user_flow(self, project_id, secret, email):
        # Instantiate stytch client with command line args
        stytch_client = stytch.Client(
            project_id=project_id,
            secret=secret,
            environment="test",
        )

        # Create a Stytch user.
        # curl -X POST https://api.stytch.com/v1/users -u project_id:secret
        # -d '{ email: "user@test.com", name : { first_name: "Nathan", last_name: "Chiu" } }'
        resp = stytch_client.users.create(
            email=email, first_name="Nathan", last_name="Chiu"
        )
        assert resp.status_code == 201
        created_user_id = resp.json()["user_id"]

        # Get that recently created user.
        # curl -X GET https://api.stytch.com/v1/users/<user_id> -u project_id:secret
        resp = stytch_client.users.get(created_user_id)
        assert resp.status_code == 200
        user_id = resp.json()["user_id"]

        # Update that user's middle name.
        # curl -X PUT https://api.stytch.com/v1/users/<user_id> -u project_id:secret
        # -d '{ name: { middle_name: "Big" } }'
        stytch_client.users.update(user_id=user_id, middle_name="Middle")
        assert resp.status_code == 200

        # Check that update worked
        resp = stytch_client.users.get(user_id)
        assert resp.status_code == 200
        user_data = resp.json()
        assert user_data["name"]["middle_name"] == "Middle"

        # Get Pending Users
        # curl -X POST https://api.stytch.com/v1/users/pending -u projectId:secret
        resp = stytch_client.users.get_pending(limit=1)
        assert resp.status_code == 200

        """
        Magic Link routes
        """
        user_id = user_data["user_id"]
        email_id = user_data["emails"][0]["email_id"]
        assert email_id

        # Send magic link to email
        # curl -X POST https://api.stytch.com/v1/magic_links/email/send -u projectId:secret
        # -d { email: "sandbox@stytch.com",
        #     signup_magic_link_url: "https://test.com/signup",
        #     login_magic_link_url: "https://test.com/login"}
        resp = stytch_client.magic_links.email.send(
            email=email,
            login_magic_link_url="https://test.com/login",
            signup_magic_link_url="https://test.com/signup",
            attributes={
                "ip_address": "1.1.1.1",
                "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                + "(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            },
        )
        assert resp.status_code == 200

        # Login or Create User
        # curl -X POST https://api.stytch.com/v1/magic_links/email/login_or_create -u projectId:secret
        # -d { email: "sandbox@stytch.com",
        #     signup_magic_link_url: "https://test.com/signup",
        #     login_magic_link_url: "https://test.com/login"}
        resp = stytch_client.magic_links.email.login_or_create(
            email="sandbox@stytch.com",
            login_magic_link_url="https://test.com/login",
            signup_magic_link_url="https://test.com/signup",
        )
        assert resp.status_code == 200

        # Invite By Email
        # curl -X POST https://api.stytch.com/v1/magic_links/email/invite -u projectId:secret
        # -d { email: "sandbox+1@stytch.com",
        #     magic_link_url: "https://test.com/invite"}
        resp = stytch_client.magic_links.email.invite(
            email="sandbox+1@stytch.com",
            invite_magic_link_url="https://test.com/invite",
        )
        assert resp.status_code == 200

        # Revoke Invite By Email
        # curl -X POST https://api.stytch.com/v1/magic_links/email/revoke_invite -u projectId:secret
        # -d { email: "sandbox+1@stytch.com"}
        resp = stytch_client.magic_links.email.revoke_invite(
            email="sandbox+1@stytch.com",
        )
        assert resp.status_code == 200

        # TODO: Test this
        #  Authenticate that token
        # curl -X POST https://api.stytch.com/v1/magic_links/authenticate -u project_id:secret
        # -d '{ email: "user@test.com", name : { first_name: "Nathan", last_name: "Chiu" } }'
        # stytch_client.MagicLinks.authenticate()
        # stytch_client.MagicLinks.authenticate(token=token)

        # Delete the created test user.
        # curl -X DELETE https://api.stytch.com/v1/users/<user_id> -u project_id:secret
        resp = stytch_client.users.delete(user_data["user_id"])
        assert resp.status_code == 200
