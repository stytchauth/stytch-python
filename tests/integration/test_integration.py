import stytch
import pytest


class TestIntegration:
    """
    This tests runs through available api calls in the API

    Pass in your project id and secret to run this.
    """

    @pytest.mark.unit
    def test_full_user_flow(self, project_id, secret):
        # Instantiate stytch client with command line args
        stytch_client = stytch.Client(
            project_id=project_id,
            secret=secret,
            environment="test",
        )

        # Create a Stytch user.
        # curl -X POST https://api.stytch.com/v1/users -u project_id:secret
        # -d '{ email: "user@test.com", name : { first_name: "Nathan", last_name: "Chiu" } }'
        resp = stytch_client.Users.create(
            email="nathan-chiu+15@stytch.com", first_name="Nathan", last_name="Chiu"
        )
        assert resp.status_code == 200
        created_user_id = resp.json()["user_id"]

        # Get that recently created user.
        # curl -X GET https://api.stytch.com/v1/users/<user_id> -u project_id:secret
        resp = stytch_client.Users.get(created_user_id)
        assert resp.status_code == 200
        user_id = resp.json()["user_id"]

        # Update that user's middle name.
        # curl -X PUT https://api.stytch.com/v1/users/<user_id> -u project_id:secret
        # -d '{ name: { middle_name: "Big" } }'
        stytch_client.Users.update(user_id=user_id, middle_name="Middle")
        assert resp.status_code == 200

        # Check that update worked
        resp = stytch_client.Users.get(user_id)
        assert resp.status_code == 200
        user_data = resp.json()
        assert user_data["name"]["middle_name"] == "Middle"

        """
        Magic Link routes
        """
        user_id = user_data["user_id"]
        email_id = user_data["emails"][0]["email_id"]
        assert email_id
        # TODO: Implement without sending email
        # stytch_client.MagicLinks.send(
        #     method_id=email_id, user_id=user_id, magic_link_url="https://test.com/login"
        # )

        """
        Email routes
        """
        # send user email verification
        # stytch_client.Emails.send_email_verification(
        #     email_id=email_id,
        #     user_id=user_id,
        #     magic_link_url="https://hello.com",
        # )

        # Delete email of user
        # curl -X DELETE https://api.stytch.com/v1/emails/<email_id>/users/<user_id>
        resp = stytch_client.Emails.delete_email(user_id=user_id, email_id=email_id)
        assert resp.status_code == 200
        resp = stytch_client.Users.get(created_user_id)
        assert resp.status_code == 200
        assert resp.json()["emails"] == []

        # Delete the created test user.
        # curl -X PUT https://api.stytch.com/v1/users/<user_id> -u project_id:secret
        # -d '{ name: { middle_name: "Big" } }'
        resp = stytch_client.Users.delete(user_data["user_id"])
        assert resp
