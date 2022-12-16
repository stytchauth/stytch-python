#!/usr/bin/env python3

from typing import Any, Dict, List, Optional


from stytch.core.models import (
  AuthenticationFactor,
  BiometricRegistration,
  CryptoWallet,
  Email,
  EmailFactor,
  Name,
  OAuthProvider,
  Operand,
  Password,
  PhoneNumber,
  ResponseBase,
  SearchQuery,
  SearchResultsMetadata,
  StytchSession,
  TOTPInstance,
  TOTPInstanceWithRecoveryCodes,
  User,
  WebAuthnRegistration,
)

class CreateResponse(ResponseBase):
  user_id: str
  user: User
  email_id: str
  phone_id: str
  status: str

class GetResponse(ResponseBase):
  user_id: str

class GetPendingResponse(ResponseBase):
  users: List[User]
  has_more: bool
  next_starting_after_id: str
  total: int

class SearchResponse(ResponseBase):
  results: List[User]
  results_metadata: SearchResultsMetadata

class DeleteResponse(ResponseBase):
  user_id: str

class UpdateResponse(ResponseBase):
  user_id: str
  user: User
  emails: List[Email]
  phone_numbers: List[PhoneNumber]
  crypto_wallets: List[CryptoWallet]

class DeleteEmailResponse(ResponseBase):
  user_id: str
  user: User

class DeletePhoneNumberResponse(ResponseBase):
  user_id: str
  user: User

class DeleteWebauthnRegistrationResponse(ResponseBase):
  user_id: str
  user: User

class DeleteTotpResponse(ResponseBase):
  user_id: str
  user: User

class DeleteCryptoWalletResponse(ResponseBase):
  user_id: str
  user: User

class DeletePasswordResponse(ResponseBase):
  user_id: str
  user: User

class DeleteBiometricRegistrationResponse(ResponseBase):
  user_id: str
  user: User

class DeleteOauthUserRegistrationResponse(ResponseBase):
  user_id: str
  user: User

