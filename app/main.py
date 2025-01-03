from internal.links import Links_test
from config.config_test import ConfigTest
import requests


links = Links_test.Links(
    links_search_test=(ConfigTest.links_search_test, ConfigTest.params_search_test)
)

response = requests.get(*links.links_search_test)
print(response)
