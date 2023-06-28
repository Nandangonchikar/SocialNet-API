# SocialNet-API

SocialNet-API is an API for a social networking platform, designed to provide users with features for creating posts, following other users, and interacting with the platform's social features. This repository contains the code and resources for the SocialNet-API.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

SocialNet-API is built to serve as the backend for a social networking platform. It provides a range of functionalities, including creating and managing user accounts, posting content, following other users, and interacting with the social aspects of the platform.

The API is designed to be scalable and customizable, allowing developers to build upon it and extend its functionality as needed. It provides a foundation for creating social networking applications or integrating social features into existing projects.

## Features

- User registration and authentication
- Creating, editing, and deleting posts
- Following and unfollowing other users
- Liking and commenting on posts
- News feed to view posts from followed users
- User profiles and user search functionality

## Technologies

The SocialNet-API is built using the following technologies:

- Python: The backend language used for implementing the API logic.
- fastAPI: A powerful framework used for building the API and handling requests.
- PostgreSQL: A robust relational database management system used for data storage.
- Docker: A containerization platform used for containerizing the application and its dependencies.

## Getting Started

To get started with the SocialNet-API, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/Nandangonchikar/SocialNet-API.git

2. API Endpoints
    The SocialNet-API provides the following main endpoints (base URL: http://localhost:8000/api/):

    /users/: Endpoints for user registration, login, profile details, and user search.
    /posts/: Endpoints for creating, retrieving, updating, and deleting posts.
    /posts/{post_id}/like/: Endpoint for liking a post.
    /posts/{post_id}/comment/: Endpoint for commenting on a post.
    /users/{user_id}/follow/: Endpoint for following a user.
    Please refer to the API documentation or explore the codebase for a complete list of available endpoints and their usage.

Authentication
The SocialNet-API uses token-based authentication. To make authenticated requests, you need to include the token in the request headers.

You can obtain an authentication token by making a POST request to /api/users/login/ with valid credentials. The response will include the authentication token, which you can then include in subsequent requests by adding an Authorization header with the value Token <token_value>.

Contributing
Contributions to the SocialNet-API are welcome! If you'd like to contribute, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your modifications or add new features.
Commit your changes and push the branch to your forked repository.
Submit a pull request with a clear description of your changes.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code as per the terms of the license.

Contact
If you have any questions or suggestions regarding the SocialNet-API, please feel free to reach out:

Email: nandangonchikar97@gmail.com