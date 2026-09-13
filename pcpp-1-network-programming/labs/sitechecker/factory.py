from sitechecker.site_checker import HTTPSiteChecker, SocketSiteChecker
from sitechecker.exception import SiteCheckerNotFoundError


class SiteCheckerFactory:
    SITE_CHECKER_BACKEND = {
        "requests": HTTPSiteChecker,
        "socket": SocketSiteChecker,
    }

    @classmethod
    def get_site_checker(cls, backend):
        checker = cls.SITE_CHECKER_BACKEND.get(backend)

        if not checker:
            raise SiteCheckerNotFoundError(
                f"Site checker backend {backend} not available"
            )

        return checker()
