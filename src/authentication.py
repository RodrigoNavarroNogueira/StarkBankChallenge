import starkbank

from src.utils.settings import PRIVATE_KEY, USER_ID

private_key_content = f"""
-----BEGIN EC PARAMETERS-----
BgUrgQQACg==
-----END EC PARAMETERS-----
{PRIVATE_KEY}
"""

user = starkbank.Project(
    environment="sandbox",
    id=USER_ID,
    private_key=private_key_content
)
