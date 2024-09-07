import redis  # type: ignore


class RateLimit:

    def __init__(self, upper_limit, ttl) -> None:
        self.upper_limit = upper_limit
        self.ttl = ttl
        self.remainingTries = 0

    def get_rate_limit(self, userToken):
        r = redis.Redis()
        if r.get(userToken) is None:
            self.remainingTries = self.upper_limit - 1
            r.setex(userToken, self.ttl, value=self.remainingTries)
        else:
            self.remainingTries = int(r.get(userToken)) - 1
            r.setex(userToken, r.ttl(userToken), value=self.remainingTries)
            self.ttl = r.ttl(userToken)


def api(request):

    authHeader = request.header.get("Authorization").split(" ")

    rate_limit = RateLimit(5, 60)

    rate_limit.get_rate_limit(authHeader[1])

    ttl = rate_limit.ttl

    remaining_tries = int(rate_limit.remainingTries)

    if remaining_tries > 1:
        return Respose(
            {"status_code": 429, "message": f"to many request try after {ttl} seconds"}
        )
    else:
        pass
