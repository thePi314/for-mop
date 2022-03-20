from django_redis.client import DefaultClient
# noinspection PyPackageRequirements
from rediscluster import RedisCluster


class ClusterRedisClient(DefaultClient):

    def connect(self, index=0):
        return RedisCluster.from_url(self._server[index], skip_full_coverage_check=True)