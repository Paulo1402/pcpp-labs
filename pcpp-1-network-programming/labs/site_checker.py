import sys
import argparse

from sitechecker.factory import SiteCheckerFactory
from sitechecker.exception import (
    SiteCheckerInsufficientParametersError,
    SiteCheckerBadParameterError,
    SiteCheckerTimeoutError,
    SiteCheckerNotFoundError,
    SiteCheckerError,
)

if __name__ == "__main__":
    error_map = {
        SiteCheckerInsufficientParametersError: 1,
        SiteCheckerBadParameterError: 2,
        SiteCheckerTimeoutError: 3,
        SiteCheckerError: 4,
        SiteCheckerNotFoundError: 5,
    }

    parser = argparse.ArgumentParser()

    parser.add_argument("server")
    parser.add_argument("port", type=int)
    parser.add_argument("--backend", default="socket")

    args = parser.parse_args()

    try:
        factory = SiteCheckerFactory()
        checker = factory.get_site_checker(backend=args.backend)
        sys.exit(checker.check(args.server, args.port))
    except SiteCheckerError as e:
        for error, code in error_map.items():
            if isinstance(e, error):
                print(e)
                exit(code)
        else:
            print(e)
            exit(6)
