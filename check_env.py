"""
Loose script from a developer to quickly check environment variables
before starting the project locally.

It doesn't follow any project convention, isn't imported by any other
module, and should probably be removed or moved to scripts/.
"""

import os

REQUIRED_VARS = ["DATABASE_URL", "ENVIRONMENT"]

for var in REQUIRED_VARS:
    value = os.getenv(var)
    print(f"{var}: {'OK' if value else 'NOT SET'}")
