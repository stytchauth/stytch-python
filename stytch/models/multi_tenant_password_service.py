#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class MultitenantpasswordstrengthcheckResponse(ResponseBase):
    request_id: str
    valid_password: bool
    score: TODO
    breached_password: bool
    luds_feedback: TODO
    strength_policy: str
    breach_detection_on_create: bool
    zxcvbn_feedback: TODO


class MultitenantpasswordmigrateResponse(ResponseBase):
    request_id: str
    member_id: str
    member_created: bool
    member: TODO
    organization: TODO


class MultitenantpasswordauthenticateResponse(ResponseBase):
    request_id: str
    member_id: str
    organization_id: str
    member: TODO
    session_token: str
    session_jwt: str
    member_session: TODO
    organization: TODO


class MultitenantpasswordemailresetstartResponse(ResponseBase):
    request_id: str
    member_id: str
    member_email_id: str


class MultitenantpasswordemailresetResponse(ResponseBase):
    request_id: str
    member_id: str
    member_email_id: str
    organization_id: str
    member: TODO
    session_token: str
    session_jwt: str
    member_session: TODO
    organization: TODO


class MultitenantpasswordsessionresetResponse(ResponseBase):
    request_id: str
    member_id: str
    member_session: TODO
    member: TODO
    organization: TODO


class MultitenantpasswordexistingpasswordresetResponse(ResponseBase):
    request_id: str
    member_id: str
    member_session: TODO
    member: TODO
    session_token: str
    session_jwt: str
    organization: TODO
