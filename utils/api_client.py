import requests
from time import sleep
from requests.exceptions import RequestException

def call_api_with_retries(url, method='GET', auth=None, headers=None, payload=None, retries=3):
    for attempt in range(retries):
        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                auth=auth,
                headers=headers or {},
                json=payload if method.upper() != 'GET' else None,
                params=payload if method.upper() == 'GET' else None
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            if attempt == retries - 1:
                raise e
            sleep(2 ** attempt)
    return None