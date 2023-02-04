#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import OAuthSession, ResponseBase, StytchSession, User


class OauthattachResponse(ResponseBase):
    request_id: str
    oauth_attach_token: str


class OauthgoogleonetapstartResponse(ResponseBase):
    request_id: str
    google_client_id: str
    stytch_csrf_token: str
    oauth_callback_id: str


class OauthgooglestartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthgoogleidtokenauthenticateResponse(ResponseBase):
    request_id: str
    user_id: str
    provider_subject: str
    session: Optional[StytchSession]
    session_token: str
    session_jwt: str
    user: User
    reset_sessions: bool


class OauthmicrosoftstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthapplestartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthappleidtokenauthenticateResponse(ResponseBase):
    request_id: str
    user_id: str
    provider_subject: str
    session: Optional[StytchSession]
    session_token: str
    session_jwt: str
    user: User
    reset_sessions: bool


class OauthgithubstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthfacebookstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthamazonstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthbitbucketstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthcoinbasestartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthdiscordstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthfigmastartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthgitlabstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthinstagramstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthlinkedinstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthshopifystartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthslackstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthsnapchatstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthspotifystartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthsteamstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthtiktokstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthtwitchstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthtwitterstartResponse(ResponseBase):
    request_id: str
    redirect_url: str
    oauth_state: str
    cname_domain: str


class OauthauthenticateResponse(ResponseBase):
    request_id: str
    user_id: str
    provider_subject: str
    provider_type: str
    session: OAuthSession
    session_token: str
    session_jwt: str
    provider_values: None
    user: User
    reset_sessions: bool
    oauth_user_registration_id: str
