# Health

Types:

```python
from bountylab.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/bountylab/resources/health.py">check</a>() -> <a href="./src/bountylab/types/health_check_response.py">HealthCheckResponse</a></code>

# API

Types:

```python
from bountylab.types import (
    APIRetrieveExampleResponse,
    APIRetrieveRawDataResponse,
    APISearchResponse,
)
```

Methods:

- <code title="get /api/example">client.api.<a href="./src/bountylab/resources/api.py">retrieve_example</a>() -> <a href="./src/bountylab/types/api_retrieve_example_response.py">APIRetrieveExampleResponse</a></code>
- <code title="get /api/raw">client.api.<a href="./src/bountylab/resources/api.py">retrieve_raw_data</a>() -> <a href="./src/bountylab/types/api_retrieve_raw_data_response.py">APIRetrieveRawDataResponse</a></code>
- <code title="get /api/search">client.api.<a href="./src/bountylab/resources/api.py">search</a>() -> <a href="./src/bountylab/types/api_search_response.py">APISearchResponse</a></code>
