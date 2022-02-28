from rest_framework.throttling import SimpleRateThrottle

class PostCreateThrottle(SimpleRateThrottle):
    scope = "postCreateThrottle"
    def get_cache_key(self, request, view) :
        if request.method=="GET":
            return None
        return self.cache_format
