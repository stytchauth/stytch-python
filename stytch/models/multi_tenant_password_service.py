#!/usr/bin/env python3


from stytch.core.models import ResponseBase


class MultitenantpasswordstrengthcheckResponse(ResponseBase):
    request_id: str
    valid_password: bool
    score: None
    breached_password: bool
    luds_feedback: None
    strength_policy: str
    breach_detection_on_create: bool
    zxcvbn_feedback: None


class MultitenantpasswordmigrateResponse(ResponseBase):
    request_id: str
    member_id: str
    member_created: bool
    member: None
    organization: None


class MultitenantpasswordauthenticateResponse(ResponseBase):
    request_id: str
    member_id: str
    organization_id: str
    member: None
    session_token: str
    session_jwt: str
    member_session: None
    organization: None


class MultitenantpasswordemailresetstartResponse(ResponseBase):
    request_id: str
    member_id: str
    member_email_id: str


class MultitenantpasswordemailresetResponse(ResponseBase):
    request_id: str
    member_id: str
    member_email_id: str
    organization_id: str
    member: None
    session_token: str
    session_jwt: str
    member_session: None
    organization: None


class MultitenantpasswordsessionresetResponse(ResponseBase):
    request_id: str
    member_id: str
    member_session: None
    member: None
    organization: None


class MultitenantpasswordexistingpasswordresetResponse(ResponseBase):
    request_id: str
    member_id: str
    member_session: None
    member: None
    session_token: str
    session_jwt: str
    organization: None
