#!/usr/bin/env python3

from typing import Dict, List

from stytch.b2b.core.models import Member, Organization
from stytch.core.models import ResponseBase, SearchResultsMetadata


class CreateResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `organization`: The Organization object.
    """  # noqa

    organization: Organization


class GetResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `organization`: The Organization object.
    """  # noqa

    organization: Organization


class UpdateResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `organization`: The Organization object.
    """  # noqa

    organization: Organization


class DeleteResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.
    """  # noqa

    organization_id: str


class GetMemberResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_id`: The UUID of the Member.

    - `member`: The Member object.

    - `organization`: The Organization object.
    """  # noqa

    member_id: str
    member: Member
    organization: Organization


class CreateMemberResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_id`: The UUID of the Member.

    - `member`: The Member object.

    - `organization`: The Organization object.
    """  # noqa

    member_id: str
    member: Member
    organization: Organization


class UpdateMemberResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_id`: The UUID of the Member.

    - `member`: The Member object.

    - `organization`: The Organization object.
    """  # noqa

    member_id: str
    member: Member
    organization: Organization


class DeleteMemberResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_id`: Globally unique UUID that identifies a specific Member in the Stytch API. The member_id is critical to perform operations on a Member, so be sure to preserve this value.
    """  # noqa

    member_id: str


class DeleteMemberPasswordResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `member_id`: Globally unique UUID that identifies a specific Member in the Stytch API. The member_id is critical to perform operations on a Member, so be sure to preserve this value.

    - `member`: The Member object.

    - `organization`: The Organization object.
    """  # noqa

    member_id: str
    member: Member
    organization: Organization


class SearchResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `organizations`: An array of Organization objects.

    - `results_metadata`: Metadata relevant to your search query.
    """  # noqa

    organizations: List[Organization]
    results_metadata: SearchResultsMetadata


class SearchMembersResponse(ResponseBase):
    """Response fields beyond those defined in `ResponseBase`:

    - `members`: An array of Member objects.

    - `results_metadata`: Metadata relevant to your search query.
    """  # noqa

    members: List[Member]
    organizations: Dict[str, Organization]
    results_metadata: SearchResultsMetadata
