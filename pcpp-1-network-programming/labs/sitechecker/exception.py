class SiteCheckerError(Exception):
    pass


class SiteCheckerBadParameterError(SiteCheckerError):
    pass


class SiteCheckerInsufficientParametersError(SiteCheckerError):
    pass


class SiteCheckerTimeoutError(SiteCheckerError):
    pass


class SiteCheckerNotFoundError(SiteCheckerError):
    pass
