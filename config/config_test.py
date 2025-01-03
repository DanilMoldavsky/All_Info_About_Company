from typing import Dict


class ConfigTest:
    links_search_test: str = 'https://synapsenet.ru/organizacii'
    params_search_test: Dict[str, str] = {
        'regmindate': '01.01.2002',
        'regmaxdate': '03.01.2025',
        'query': 'си%20мобайл',
        'operating': 'true',
        'changing': 'true',
        'liquidated': 'true'
    }
