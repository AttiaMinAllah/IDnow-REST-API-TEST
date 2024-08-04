# IDNOW REST API Test Framework

This project is a test framework for testing the REST API provided by IDNOW. The primary focus is on validating the `autoident` browser matrix support for web, ensuring the minimum version supported for each platform. The framework will support making requests for GET, POST, PUT and DELETE calls, example functions added in the api_client.py

The structure according to Page Object Model and following is the description of the project 

### `api_testing_utils/`
- **`__init__.py`**: Marks the directory as a Python package.
- **`api_client.py`**: Contains the `APIClient` class to interact with the REST API.
- **`settings.py`**: Configuration settings such as the API base URL and endpoint.

### `tests/`
- **`__init__.py`**: Marks the directory as a Python package.
- **`test_autoident_browser_matrix.py`**: Contains test cases for validating the `autoident` browser matrix.

### Root Directory
- **`venv/`**: Virtual environment directory (ignored by `.gitignore`).
- **`.gitignore`**: Specifies intentionally untracked files to ignore.
- **`pytest.ini`**: Configuration file for pytest.
- **`README.md`**: Project overview and instructions (this file).
- **`requirements.txt`**: Lists dependencies required to run the tests.
- **`setup.py`**: Setup script to install the project as a package.

## Setup

```bash
# 1. Clone the Repository
git clone <repository_url>
cd IDNOW-REST-API-TEST

# 2. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Install the Project in Editable Mode
pip install -e .

# 5. Run Tests
pytest
