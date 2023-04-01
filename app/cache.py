from pymemcache.client import base
from pymemcache import fallback

# Set `ignore_exc=True` so it is possible to shut down
# the old cache and migrate to the new for back up 
old_cache = base.Client(('localhost', 11211), ignore_exc=True)
new_cache = base.Client(('localhost', 11212))

# this allow us to fail safe
client = fallback.FallbackClient((new_cache, old_cache))

# This allow us to leverage cache to store action process score map, use RAM for fast accessing
# also allow us to fail safe
def on_visit(userId, client):
    while True:
        result, cas = client.gets(userId)
        if result is None:
            result = 1
        else:
            result += 1
        if client.cas(userId, result, cas):
            break