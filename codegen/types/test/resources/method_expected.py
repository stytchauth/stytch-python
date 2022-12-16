def create(
  self,
  email: Optional[str] = None,
  phone_number: Optional[str] = None,
  name: Optional[Name] = None,
  create_user_as_pending: bool = False,
  attributes: Optional[Dict[str, str]] = None,
  trusted_metadata: Optional[Dict[str, Any]] = None,
  untrusted_metadata: Optional[Dict[str, Any]] = None,
) -> CreateResponse:
    payload: Dict[str, Any] = {
        "create_user_as_pending": create_user_as_pending,
    }

    if email is not None:
        payload["email"] = email
    if phone_number is not None:
        payload["phone_number"] = phone_number
    if name is not None:
        payload["name"] = name.dict()
    if attributes is not None:
        payload["attributes"] = attributes
    if trusted_metadata is not None:
        payload["trusted_metadata"] = trusted_metadata
    if untrusted_metadata is not None:
        payload["untrusted_metadata"] = untrusted_metadata

    url = self.api_base.route_with_sub_url(self.sub_url, None)

    resp = self.sync_client.post(url, json=payload)
    return CreateResponse.from_json(resp.json())

async def create_async(
  self,
  email: Optional[str] = None,
  phone_number: Optional[str] = None,
  name: Optional[Name] = None,
  create_user_as_pending: bool = False,
  attributes: Optional[Dict[str, str]] = None,
  trusted_metadata: Optional[Dict[str, Any]] = None,
  untrusted_metadata: Optional[Dict[str, Any]] = None,
) -> CreateResponse:
    payload: Dict[str, Any] = {
        "create_user_as_pending": create_user_as_pending,
    }

    if email is not None:
        payload["email"] = email
    if phone_number is not None:
        payload["phone_number"] = phone_number
    if name is not None:
        payload["name"] = name.dict()
    if attributes is not None:
        payload["attributes"] = attributes
    if trusted_metadata is not None:
        payload["trusted_metadata"] = trusted_metadata
    if untrusted_metadata is not None:
        payload["untrusted_metadata"] = untrusted_metadata

    url = self.api_base.route_with_sub_url(self.sub_url, None)

    resp = await self.async_client.post(url, json=payload)
    return CreateResponse.from_json(await resp.json())
