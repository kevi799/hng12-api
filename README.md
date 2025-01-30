# HNG12 API

This is a public API that returns the following information:

1. Your registered email address (used to register on the HNG12 Slack workspace).
2. The current datetime as an ISO 8601 formatted timestamp.
3. The GitHub URL of the project's codebase.

---

## Table of Content

1. [Project Description](#project-description)
2. [Setup Instructions] (#setup-instructions)
3. [API Documentation] (#api-documentation) -[Endpoint URL](#endpoint-url) -[Request Format](#request-format) -[Example Usage] (#example-usage)

## Project Dscription

This project is a FlaskAPI-based API serving the user details. It includes
-A root endpoint (`/`)returning a welcome message
-A `/api/info` endpoint returning the user details which include
-Email address.
-Github url.
-A Timestamp
-Proper CORS configuration allowing requests from specified origins.

---

## Setup Instructions

Follow these steps to run the proect locally.

### Prerequisites

-python3.7 or higher
`pip` (Python package manager).

### Steps

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/kevi799/hng12-api.git
    cd your-repo-name

    ```

2.  **Install the required dependencies**

        ```bash

    pip install flask flask cors jsonify gunicorn

3.  **Create a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate

    ```

4.  \*\*Run the application:

    ```bash
    gunicorn app:app
    ```

### Api Documentation

## EndPoint URL

`http://127.0.0.1:8000 `.

## Endpoint

1. Root Endpoint(`/`)
   -Method `GET`
   -Description ``Returns a welcome message`

2. Get User details(`/api/info`)
   -Method:`GET`
   -Description: Returns user ino such as
   -user email
   -Github URL
   -A Timestamp

### Example Usage

Using curl to Test the API

1. Access the root endpoint:
   curl -X GET http://127.0.0.1:8000/

_Response:_

{
"message": "Welcome"
}

2. Access the /get-details endpoint:
   curl -X GET http://127.0.0.1:8000/api/info

_Response:_

{
"email": "kelvinmulinge9702@gmail.com",
"local-time": "2023-10-05T14:30:45Z",
"github-url": "https://github.com"
}

## License

This project is licensed under the [MIT License](LICENSE).

```

```
