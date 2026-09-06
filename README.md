# Astra-AI
My Ai Website
# Astra AI Website — Project Documentation

## 1. Project Overview

### Project Name

**Astra AI**

### Project Type

AI-powered web application

### Purpose

The purpose of this project is to build a personal AI chat website that allows users to interact with an AI model through a web interface.

The application consists of:

* Frontend user interface
* Flask backend
* AI API integration
* Environment-based API key management
* AI model selection
* Chat request/response handling
* Future image-generation support

The project is being developed and tested locally using Kali Linux.

---

# 2. Project Architecture

The basic architecture is:

```text
User
  |
  v
Astra Web Interface
(index.html)
  |
  | POST /chat
  v
Flask Backend
(app.py)
  |
  | API Request
  v
Experiential Labs Gateway
  |
  v
Selected AI Model
```

### Components

| Component            | Purpose                 |
| -------------------- | ----------------------- |
| HTML/CSS/JavaScript  | Frontend interface      |
| Flask                | Backend web server      |
| Python               | Backend programming     |
| Experiential Labs    | AI API gateway          |
| AI Model             | Generates responses     |
| Environment Variable | Stores API key securely |
| Kali Linux           | Development environment |

---

# 3. Development Environment

The project was developed in:

* Operating System: Kali Linux
* Backend: Python
* Web Framework: Flask
* Frontend: HTML, CSS, JavaScript
* API Style: OpenAI-compatible API
* API Gateway: Experiential Labs

Project directory:

```text
~/my-ai-website
```

Python virtual environment:

```text
~/astra-test/venv
```

---

# 4. Project Files

The initial project structure was:

```text
my-ai-website/
│
├── app.py
└── index.html
```

### app.py

This file contains the Flask backend.

Responsibilities:

* Start the web server
* Receive messages from the frontend
* Send messages to the AI API
* Receive the AI response
* Return the response to the frontend

### index.html

This file contains the frontend.

Responsibilities:

* Display the Astra interface
* Accept user messages
* Send messages to Flask
* Display AI responses
* Provide the ChatGPT-like interface

---

# 5. Creating the Flask Backend

Flask was selected as the backend framework because it is lightweight and easy to use for creating APIs.

The backend exposes a chat endpoint:

```text
POST /chat
```

The frontend sends a JSON request similar to:

```json
{
    "message": "Hello"
}
```

The Flask backend receives the message and sends it to the AI provider.

The response is then returned to the browser.

---

# 6. Connecting the AI API

Experiential Labs was selected as the AI gateway.

The API uses an OpenAI-compatible interface.

The base URL used by the project is:

```text
https://api.experientiallabs.ai/v1
```

The API requires authentication using an API key.

The official documentation specifies the authentication format as:

```text
Authorization: Bearer <API_KEY>
```

The same key can be used for inference through the `/v1` API.

---

# 7. API Key Security

The API key was not hard-coded directly into the application.

Instead, an environment variable was used:

```text
EXPLABS_API_KEY
```

This is important because placing an API key directly inside source code could expose the credential if the project is uploaded to GitHub.

The application therefore reads the key from the environment.

Conceptually:

```text
Environment
     |
     v
EXPLABS_API_KEY
     |
     v
Flask Backend
     |
     v
Experiential Labs API
```

The API key must never be published in the GitHub repository.

---

# 8. Testing API Authentication

Before using an AI model, the API connection was tested using:

```text
GET /v1/models
```

The request was successful.

This confirmed that:

1. The API key was valid.
2. The API endpoint was reachable.
3. The account was authenticated.
4. The account could access the model catalog.

Experiential Labs documentation also recommends `/v1/models` as the way to verify which models an API key can call.

---

# 9. Discovering Available Models

The `/v1/models` endpoint returned a large model catalog.

Among the available models were:

```text
gpt-5-mini
gpt-5-image
gpt-5-image-mini
gemini-2.5-flash-image
gemini-3-pro-image
gemini-3.1-flash-image
gpt-5.6-luna
gpt-6-astra
```

The important concept discovered here is that the application does not need to directly integrate separately with every AI provider.

Instead:

```text
Astra
  |
  v
Experiential Labs
  |
  +---- Model A
  |
  +---- Model B
  |
  +---- Model C
```

The model is selected using its model slug.

Experiential Labs describes its catalog as a collection of model slugs with information including modalities and pricing.

---

# 10. Selecting the AI Model

The first model tested for Astra was:

```text
gpt-6-astra
```

However, the API returned a `429` error indicating that this model's promotional/free access required account verification involving a small payment.

This demonstrated an important lesson:

> A model appearing in the catalog does not necessarily mean it can be used under the current account's free-access conditions.

The model catalog and actual account access/credit conditions must therefore be checked separately.

---

# 11. Free Model Investigation

The account contained platform credits.

The project therefore investigated which models could be used without making the $1 verification payment.

The goal was to avoid unnecessary spending while developing the application.

The important distinction discovered was:

```text
Model available in catalog
        ≠
Model available for free under current account conditions
```

Experiential Labs supports both platform-funded deployments and BYOK deployments. Platform-funded deployments use platform credits, while BYOK deployments use the user's own provider credentials.

---

# 12. Frontend Development

The frontend was developed to resemble a modern AI chat application.

The interface contains:

* Sidebar
* Astra branding
* Model information
* Welcome screen
* Suggestion cards
* Chat messages
* User message bubbles
* AI response bubbles
* Message input box
* Send button
* Responsive layout

The objective was to create a professional interface rather than a simple HTML form.

---

# 13. Frontend-to-Backend Communication

JavaScript was used to communicate with Flask.

The process is:

```text
User types message
        |
        v
JavaScript captures message
        |
        v
POST /chat
        |
        v
Flask receives message
        |
        v
AI API request
        |
        v
AI response
        |
        v
Flask returns JSON
        |
        v
JavaScript displays response
```

The frontend therefore does not directly expose the Experiential Labs API key.

This is an important security design decision.

---

# 14. Running the Application

The Flask server was started locally.

The application was accessed through:

```text
http://127.0.0.1:5000
```

The browser communicates with the local Flask server, while Flask communicates with the external AI gateway.

---

# 15. First Chat API Test

A chat request was sent from the application.

Initially, the backend returned an HTTP `500` error.

The investigation showed that the problem was not necessarily the frontend.

The backend was calling:

```text
gpt-6-astra
```

The API responded with a `429` error because of the model's free-tier verification requirement.

This was an important debugging step.

---

# 16. Backend Error Handling

The Flask backend was improved to catch API exceptions.

Instead of allowing the application to crash with an unclear `500` error, the backend was modified to:

1. Receive the request.
2. Validate the message.
3. Call the AI API.
4. Catch API errors.
5. Print the actual error in the terminal.
6. Return a controlled JSON error to the frontend.

Conceptually:

```text
Frontend
   |
   v
Flask
   |
   +---- Success ----> AI response
   |
   +---- Error ------> Controlled error message
```

This makes debugging much easier.

---

# 17. Image Generation Investigation

A new requirement was introduced:

> When the user asks Astra to generate an image, the website should actually generate an image instead of only returning an image prompt.

For example:

```text
Generate an image of Lord Krishna.
```

The desired behavior is:

```text
User
 |
 v
Astra
 |
 v
Image Generation Model
 |
 v
Generated Image
 |
 v
Browser
```

---

# 18. First Image Generation Test

The model:

```text
gpt-5-image
```

was tested.

Initially, an OpenAI-style endpoint was attempted:

```text
/v1/images/generations
```

The gateway returned:

```text
Unsupported serving path: /v1/images/generations
```

This showed that the Experiential Labs gateway did not expose that particular image-generation endpoint.

Therefore, the image endpoint could not simply be assumed from the model name.

---

# 19. Testing the Responses API

The next test used:

```text
POST /v1/responses
```

with:

```text
model: gpt-5-image
```

The request was accepted.

The API returned:

```text
status: completed
```

and:

```text
error: null
```

This confirmed that `gpt-5-image` was recognized by the Responses API.

However, the returned response contained:

```text
output: []
```

No actual image data was returned.

Therefore, the investigation is not finished.

---

# 20. Important Lesson From Image Testing

The following assumptions were proven incorrect:

```text
Image model exists
        ↓
Therefore /images/generations works
```

This is not necessarily true.

Instead, the correct process is:

```text
Identify model
      ↓
Check supported modalities
      ↓
Check supported API route
      ↓
Check request format
      ↓
Test response format
      ↓
Implement image handling
```

This is an important API integration lesson.

---

# 21. Current Image Generation Status

Current status:

```text
Text chat              → Working / being integrated
API authentication     → Working
Model discovery        → Working
Flask backend          → Working
Frontend               → Working
Image model discovery  → Working
Image endpoint         → Not yet confirmed
Actual image output    → Not yet implemented
```

The image-generation implementation should therefore not be considered complete.

---

# 22. Security Considerations

The project follows several basic security principles.

### API Key Protection

The API key is stored in an environment variable rather than frontend JavaScript.

### Frontend Isolation

The browser communicates with:

```text
Flask
```

rather than directly communicating with the AI provider.

### Error Handling

API errors are handled by the backend.

### GitHub Protection

The API key must not be committed to Git.

A `.gitignore` file should eventually include sensitive files such as:

```text
.env
__pycache__/
venv/
```

---

# 23. Current Architecture

The current architecture can be represented as:

```text
                 ┌─────────────────────┐
                 │       User          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Astra Frontend    │
                 │ HTML/CSS/JavaScript │
                 └──────────┬──────────┘
                            │
                       POST /chat
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Flask Backend    │
                 │      app.py         │
                 └──────────┬──────────┘
                            │
                    Bearer API Key
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Experiential Labs   │
                 │       Gateway       │
                 └──────────┬──────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
       Text AI Models              Image Models
              │                           │
              ▼                           ▼
       AI Text Response            Image Response
              │                           │
              └─────────────┬─────────────┘
                            ▼
                      Astra Website
```

---

# 24. Current Project Status

### Completed

* [x] Created project directory
* [x] Created Flask backend
* [x] Created frontend
* [x] Created Astra-style interface
* [x] Configured Python environment
* [x] Created Experiential Labs API key
* [x] Stored API key in environment variable
* [x] Tested API authentication
* [x] Retrieved available models
* [x] Tested AI model access
* [x] Identified free/promotion restrictions
* [x] Implemented frontend/backend communication
* [x] Investigated image-generation models
* [x] Tested Responses API
* [x] Investigated API errors

### In Progress

* [ ] Select the best free/low-cost text model
* [ ] Finalize normal chat functionality
* [ ] Determine correct image-generation API format
* [ ] Implement actual image generation
* [ ] Display generated images in Astra
* [ ] Add conversation history
* [ ] Improve error messages
* [ ] Add security protections
* [ ] Prepare GitHub repository
* [ ] Write final project report

---

# 25. Future Improvements

Possible future features include:

### Chat

* Conversation history
* New-chat button
* Delete conversation
* Model selector
* Streaming responses

### AI

* Multiple AI models
* Image generation
* Image analysis
* File upload
* Document analysis

### Security

* Input validation
* Rate limiting
* API key protection
* Authentication
* Secure session management
* Logging and monitoring

### UI

* Dark/light mode
* Mobile optimization
* Markdown rendering
* Code blocks
* Copy response button
* Regenerate response button

---

# 26. Key Technical Lessons Learned

During development, several important concepts were learned.

### Lesson 1 — API keys must be protected

Never place an API key directly inside frontend JavaScript.

### Lesson 2 — Test authentication first

The `/v1/models` endpoint is useful for verifying whether the API key works before making inference requests.

### Lesson 3 — HTTP errors need investigation

A frontend message such as:

```text
Could not connect to server
```

does not necessarily mean the server is offline.

The actual cause may be:

```text
Frontend
   ↓
Flask
   ↓
API
   ↓
429 / 401 / 500
```

Therefore backend logs must be checked.

### Lesson 4 — Model availability and free access are different

A model can appear in the catalog while still having account-specific pricing or access requirements.

### Lesson 5 — Never assume an API endpoint

A model called `gpt-5-image` does not automatically mean that:

```text
/v1/images/generations
```

is supported.

The provider's actual API contract must be checked first.

---

# 27. Conclusion

The Astra AI project successfully established the foundation of a full-stack AI web application.

The current system contains:

```text
Frontend
   +
Flask Backend
   +
Secure API Authentication
   +
AI Model Gateway
```

The next major development task is completing image generation and connecting the generated image response to the Astra frontend.

The project is being developed incrementally, with each API integration tested before being incorporated into the final application.






# Astra AI — AI Assistant Website

A Flask-based AI assistant website developed as a learning project to understand how a frontend, Python backend, and external AI API work together.

The project focuses on building a simple chat application, securely connecting to an AI provider, testing API authentication, discovering available models, and investigating image-generation capabilities.

## Project Overview

Astra AI is a web-based AI assistant that allows users to enter questions and receive AI-generated responses through a browser interface.

The application was developed using **HTML, CSS, JavaScript, Python, and Flask**. The Flask backend acts as an intermediary between the frontend and the external AI API. This architecture keeps the API key on the server side instead of exposing it in the browser.

The project was developed as a practical learning exercise to understand API integration, backend development, frontend-to-backend communication, authentication testing, and troubleshooting.

## Features

* AI chat interface
* Flask backend
* External AI API integration
* Environment-variable-based API key configuration
* Available model discovery
* Model selection
* Frontend-to-backend communication
* API authentication testing
* Backend error handling
* Image-generation capability investigation
* Project documentation and screenshots

## Project Architecture

The application follows a simple three-layer architecture:

```text
User
  │
  ▼
Frontend (HTML / CSS / JavaScript)
  │
  │ POST /chat
  ▼
Flask Backend (app.py)
  │
  │ Authenticated API Request
  ▼
External AI API
  │
  ▼
AI Model Response
  │
  ▼
Flask Backend
  │
  ▼
Frontend
  │
  ▼
User
```

The frontend collects the user's message and sends it to the Flask backend. The backend validates the request, sends it to the external AI API using the configured API key, and returns the AI-generated response to the frontend.

## Technologies Used

| Technology                 | Purpose                                    |
| -------------------------- | ------------------------------------------ |
| Python                     | Backend programming                        |
| Flask                      | Web framework                              |
| HTML                       | Frontend structure                         |
| CSS                        | Frontend styling                           |
| JavaScript                 | Frontend interaction and API communication |
| OpenAI Python SDK          | AI API integration                         |
| External AI API            | AI model access                            |
| Kali Linux                 | Development environment                    |
| Python virtual environment | Dependency isolation                       |
| Git                        | Version control                            |
| GitHub                     | Project hosting                            |

## Project Structure

```text
my-ai-website/
│
├── app.py
├── index.html
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│   └── project-documentation.md
│
├── screenshots/
│   ├── 01-project-files.png
│   ├── 02-flask-backend.png
│   ├── 03-flask-server.png
│   ├── 04-frontend.png
│   ├── 05-backend-error.png
│   └── 06-successful-chat.png
│
└── venv/                 # Not uploaded to GitHub
```

## Development Environment

The project was developed in **Kali Linux** using Python and a virtual environment.

The virtual environment was created to keep the project's dependencies separate from the system Python installation.

### Create the virtual environment

```bash
python3 -m venv venv
```

### Activate the virtual environment

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install flask openai
```

## Creating the Flask Backend

The Flask backend is implemented in `app.py`.

Its main responsibilities are:

1. Initialize the Flask application.
2. Serve the frontend.
3. Receive chat messages.
4. Validate incoming requests.
5. Send requests to the external AI API.
6. Return the AI response to the frontend.
7. Handle errors when the request cannot be completed.

The backend provides a `/chat` endpoint that accepts a user message and returns a response.

## Connecting the AI API

The application uses the OpenAI Python SDK to communicate with the external AI API.

The backend configures the client using the provider's API key and base URL.

Example:

```python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("EXPLABS_API_KEY"),
    base_url="https://api.experientiallabs.ai/v1"
)
```

The API request is sent from the backend rather than directly from the browser.

This approach helps protect the API key and keeps the integration logic in one place.

## API Key Security

The API key is stored in an environment variable:

```bash
export EXPLABS_API_KEY="your_api_key_here"
```

The application reads the key using:

```python
os.environ.get("EXPLABS_API_KEY")
```

The actual API key should **never be committed to GitHub**.

The `.gitignore` file is used to prevent environment files and unnecessary Python files from being uploaded.

Example `.gitignore`:

```gitignore
venv/
__pycache__/
*.pyc
.env
.env.*
!.env.example
```

> **Security note:** If an API key is accidentally exposed, it should be revoked and replaced immediately.

## Testing API Authentication

API authentication was tested using the terminal and the configured environment variable.

Example request:

```bash
curl -s https://api.experientiallabs.ai/v1/models \
  -H "Authorization: Bearer $EXPLABS_API_KEY"
```

The API returned a list of available models, confirming that the configured key could authenticate successfully for that request.

A separate request to the Responses API returned an authentication error:

```text
A valid gateway Bearer key is required.
```

This demonstrated that **a key being set in the environment does not automatically mean every API request is valid**. The request format, endpoint, and provider requirements must also be correct.

## Discovering Available Models

The `/v1/models` endpoint was used to discover the models available through the provider.

The returned list included models from several model families, such as GPT, Claude, Gemini, DeepSeek, and others.

This investigation helped identify which model names could be used in API requests.

Example model identifiers discovered during testing included:

```text
gpt-5-mini
gpt-5-image
gpt-6-astra
claude-sonnet-4.5
gemini-2.5-flash
deepseek-r1
```

The actual model availability and access permissions depend on the provider's current configuration.

## Selecting the AI Model

The selected model is specified in the API request.

Example:

```python
response = client.responses.create(
    model="gpt-6-astra",
    input=message
)
```

Model selection is important because different models may support different capabilities, such as text generation, reasoning, coding, or image generation.

The project tested model availability before selecting a model for the chat application.

## Free Model Investigation

The provider dashboard showed a credit balance and information about platform-funded requests.

The project also investigated models with names containing `free`.

However, a model being listed as free does not necessarily mean that every request is free or that it is available for every API endpoint.

The actual cost and access depend on the provider's billing and model configuration.

## Frontend Development

The frontend was designed as a simple AI workspace.

It includes:

* Application branding
* Sidebar navigation
* Conversation area
* Message input
* Send button
* AI response display
* Error message display

The frontend was designed to provide a clean interface for interacting with the AI assistant.

## Frontend-to-Backend Communication

The frontend communicates with the Flask backend through an HTTP request.

The basic flow is:

```text
User enters message
        ↓
Frontend sends POST /chat
        ↓
Flask receives the request
        ↓
Flask sends the message to the AI API
        ↓
AI API returns a response
        ↓
Flask returns JSON
        ↓
Frontend displays the response
```

This separation allows the frontend to focus on user interaction while the backend handles API communication.

## Running the Application

The application is started using the Flask development server.

Example:

```bash
python app.py
```

The application can then be accessed through:

```text
http://127.0.0.1:5000
```

The Flask development server is suitable for local testing and learning. A production deployment would require a production WSGI server and additional security configuration.

## First Chat API Test

The first successful chat test confirmed that the application could receive a user message and return an AI-generated response.

A question about quantum computing was entered through the frontend, and the AI response was displayed in the conversation area.

This demonstrated that the basic frontend-to-backend-to-AI communication flow was working.

## Backend Error Handling

During testing, the frontend displayed an error message when it could not connect to the backend server.

This helped identify the importance of checking:

* Whether the Flask server is running
* Whether the frontend is using the correct endpoint
* Whether the backend is returning a valid response
* Whether the API request is being sent correctly

Error handling is important because it helps users understand when a request cannot be completed.

## Image Generation Investigation

The project also investigated whether the external AI API could generate images.

The investigation included:

1. Discovering image-capable model identifiers.
2. Testing the image-generation endpoint.
3. Testing the Responses API with an image-capable model.
4. Checking the returned response structure.
5. Comparing the expected API behavior with the actual provider response.

The investigation showed that **having an image-capable model listed does not automatically mean that the image-generation endpoint is supported**.

## First Image Generation Test

An image-generation request was attempted using the `/v1/images/generations` endpoint.

The provider returned:

```text
Unsupported serving path: /v1/images/generations
```

This indicated that the tested endpoint was not supported by the provider's gateway.

The test was useful because it demonstrated the importance of checking the provider's supported API paths instead of assuming that every OpenAI-compatible provider supports every endpoint.

## Testing the Responses API

The Responses API was also tested using an image-capable model.

The request returned a completed response object, but the response contained an empty output array:

```json
{
  "status": "completed",
  "output": []
}
```

The response also included usage information.

This showed that **a request can complete without producing the expected image output**. The response structure must be inspected to determine whether the requested capability was actually returned.

## Lesson From Image Testing

The image-generation investigation highlighted several important lessons:

* Model availability and endpoint availability are different.
* OpenAI-compatible APIs may not support every OpenAI endpoint.
* A successful HTTP response does not always mean the expected output was generated.
* The provider's documentation should be checked before implementing a new capability.
* Image generation should be tested separately from text chat functionality.

## Current Image Generation Status

The current project successfully demonstrates the **text chat workflow**.

Image generation remains an **investigated capability** rather than a completed feature.

The tested image-generation endpoint was unsupported, and the Responses API test did not return the expected image output.

Further implementation would require confirming the provider's supported image-generation API and response format.

## Security Considerations

The project follows basic API security practices:

* API keys are stored in environment variables.
* API keys are not included in frontend code.
* API keys should not be committed to GitHub.
* The virtual environment is excluded from version control.
* The application is tested locally before deployment.

Additional security improvements would be required before using the application in a production environment.

## Current Architecture

```text
Browser
   │
   ▼
Frontend
(index.html)
   │
   ▼
Flask Backend
(app.py)
   │
   ▼
External AI API
   │
   ▼
Selected AI Model
   │
   ▼
AI Response
   │
   ▼
Frontend Display
```

## Current Project Status

| Component                      | Status            |
| ------------------------------ | ----------------- |
| Flask backend                  | Completed         |
| Frontend interface             | Completed         |
| AI API integration             | Completed         |
| API key configuration          | Completed         |
| Model discovery                | Completed         |
| Chat testing                   | Completed         |
| Backend error handling         | Implemented       |
| Image-generation investigation | Completed         |
| Image-generation feature       | Not yet completed |
| GitHub documentation           | In progress       |

## Future Improvements

The project may later be expanded with:

* User authentication
* Conversation history
* Database integration
* Multiple model selection
* Better error handling
* Production deployment
* Image-generation support
* File upload support
* Improved frontend design
* API usage monitoring
* Rate limiting

## Key Technical Lessons Learned

This project helped develop practical understanding of:

* Flask application development
* REST API communication
* Environment variables
* API authentication
* Model discovery
* Frontend-to-backend communication
* HTTP request and response handling
* Error troubleshooting
* API endpoint compatibility
* Git and GitHub project organization

## Conclusion

Astra AI was developed as a practical project to understand how an AI-powered web application is built.

The project successfully demonstrates the integration of a Flask backend with an external AI API and provides a working text chat interface.

The image-generation investigation also provided valuable experience in testing API capabilities, understanding endpoint limitations, and troubleshooting unexpected responses.

The project documentation records the development process, testing results, and lessons learned throughout the implementation.

## Documentation

Detailed project documentation is available in:

```text
docs/project-documentation.md
```

The documentation includes:

* Project overview
* Architecture
* Development environment
* Project files
* Flask backend development
* AI API integration
* API key security
* Authentication testing
* Model discovery
* Model selection
* Free model investigation
* Frontend development
* Frontend-to-backend communication
* Application execution
* Chat testing
* Error handling
* Image-generation investigation
* API testing
* Current project status
* Future improvements
* Technical lessons learned

## Screenshots

Screenshots of the development process and application testing are available in:

```text
screenshots/
```

They include the project structure, backend code, running Flask server, frontend interface, error handling, and successful chat response.

## Author

**Krishna**

Cybersecurity Student | Python | Flask | API Integration | AI Projects

