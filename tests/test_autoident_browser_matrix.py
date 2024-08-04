import pytest
from api_testing_utils.api_client import APIClient
from api_testing_utils.settings import BASE_URL, ENDPOINT

# Expected browser matrix support for web
expected_browser_matrix_web = {
    "desktop": {
        "default": ["chrome"],
        "linux": ["chrome"],
        "macintosh": ["safari", "chrome"],
        "windows": ["edge", "chrome", "firefox"]
    }
}

@pytest.fixture(scope="module")
def api_client():
    return APIClient(BASE_URL)

def test_autoident_browser_matrix(api_client: APIClient):
    response = api_client.get(ENDPOINT)
    
    # Extract the 'autoident' dictionary
    autoident_dict = response.get('settings', {}).get('idnow', {}).get('autoident', None)
    assert autoident_dict is not None, "'autoident' key is not in the response"
    
    browser_matrix = autoident_dict["web"]["browserSupportMatrix"]["desktop"]

    # Validate each expected browser in the desktop browser matrix
    for platform, browsers in expected_browser_matrix_web["desktop"].items():
        assert platform in browser_matrix, f"{platform} is not in the browser matrix"
        for browser in browsers:
            assert browser in browser_matrix[platform], f"{browser} is not in the browser matrix for {platform}"
            assert "min" in browser_matrix[platform][browser], f"'min' key is missing for {browser} on {platform}"
            assert browser_matrix[platform][browser]["min"] != "-1", f"{browser} is not supported on {platform}"
