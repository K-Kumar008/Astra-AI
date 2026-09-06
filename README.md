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
