# FastAPI Render App

This project is a simple FastAPI application that provides an endpoint to count the number of characters in a given string. It is designed to be deployed on Render.

## Project Structure

```
fastapi-render-app
├── app
│   ├── main.py
│   ├── routers
│   │   └── string_utils.py
│   └── __init__.py
├── requirements.txt
├── render.yaml
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-render-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the FastAPI application locally, use the following command:
```
uvicorn app.main:app --reload
```

You can then access the application at `http://127.0.0.1:8000`.

### Endpoint

- **POST /count-characters**
  - Request Body: JSON object with a key `input_string` containing the string to be processed.
  - Response: JSON object with a key `character_count` indicating the number of characters in the input string.

## Deployment

To deploy the application on Render, ensure you have a `render.yaml` file configured with the necessary build and start commands. Follow the instructions on the Render documentation for deploying a FastAPI application.

## License

This project is licensed under the MIT License.