**Website**

This is a proxy which interacts with the catalog api. Since catalog api has a strict ratelimit, i tried to bypass
by making a database which stores the response each day (This way preventing you from spamming the api). It's not perfect
so sometimes my proxy gets ratelimited (only if u send requests to two endpoints)
