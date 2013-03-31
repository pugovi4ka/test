from mycatalog.models import Statistic


class Statistics(object):
    def process_response(self, request, response):
        Statistic.objects.create(
            url=request.get_full_path(),
            method=request.method,
            response_status_code=response.status_code
        )

        return response