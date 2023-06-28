# SocialNet-API

SocialNet-API is an API for a social networking platform, designed to provide users with features for creating posts, following other users, and interacting with the platform's social features. This repository contains the code and resources for the SocialNet-API.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

SocialNet-API is built to serve as the backend for a social networking platform. It provides a range of functionalities, including creating and managing user accounts, posting content, following other users, and interacting with the social aspects of the platform.

The API is designed to be scalable and customizable, allowing developers to build upon it and extend its functionality as needed. It provides a foundation for creating social networking applications or integrating social features into existing projects.

This repository has all the necessary functionality implemted for testing the socialNet API using python pytest. Create your tests in the tests folder and run pytest.

It also CI/CD integrated to it using github actions, where a push into github will automatically invoke the github action and the code will be tested against the test cases defined in the the tests folder on a ubuntu machine. If the build is successful, the code will be created as a docker image and pushed to the dockerhub automatically.

## Features

- User registration and authentication
- Creating, editing, and deleting posts
- Liking on posts
- User profiles creation.
- Pagination creation endpoint.
- Continuous integration using GitHub actions
- Continuous delivery

## Getting Started

To get started with the SocialNet-API, follow these steps:

- Clone the repository: git clone https://github.com/Nandangonchikar/SocialNet-API
- Install the project dependencies: pip install -r requirements.txt
- [Set up](#env) the PostgreSQL database and configure the database connection in the code. 
- Run the application: uvicorn main:app --reload
- Access the API endpoints through the provided URLs.

  ## Setting up PostgresDB connection
   - Create a .env file in the root directory and add the below environment variables details.
        DATABASE_HOSTNAME =localhost #default  
        DATABASE_PORT=5432 #default  
        DATABASE_PASSWORD=#your db pswd#  
        DATABASE_NAME=#DB Name#  
        DATABASE_USERNAME=postgres #default  
        SECRET_KEY=#secret key for password hashing algorithm#  
        ALGORITHM = HS256 #Type of the algorithm for hashing  
        ACCESS_TOKEN_EXPIRE_MINUTES = 30  #Number of minutes after which the access token will expire  

## API Endpoints
 Below you will find details on each endpoint, including their functionality, request/response models, and any required dependencies.

    ## Table of Contents

- [Posts](#posts)
  - [Get All Posts](#get-all-posts-get-posts)
  - [Create Post](#create-post-post-posts)
  - [Get Post](#get-post-get-postid)
  - [Update Post](#update-post-put-postid)
  - [Delete Post](#delete-post-delete-postid)

- [Users](#users)
  - [Create User](#create-user-post-users)
  - [Get User](#get-user-get-userid)

- [Vote](#vote)
  - [Vote on Post](#vote-post-vote)

## Posts

### Get All Posts [GET /posts]

This endpoint retrieves all posts.

#### Request

- Method: GET
- Path: /posts
- Query Parameters:
  - `limit` (optional): The maximum number of posts to retrieve (default: 10).
  - `skip` (optional): The number of posts to skip (default: 0).
  - `search` (optional): A search query to filter posts by title (default: "").

#### Response

- Status Code: 200 OK
- Response Model: List[schemas.PostResponseVotes]

### Create Post [POST /posts]

This endpoint creates a new post.

#### Request

- Method: POST
- Path: /posts
- Body:
  - `title` (string): The title of the post.
  - `content` (string): The content of the post.
  - `published` (bool): Whether the post is published or not.
- Headers:
  - Authorization: Bearer {access_token}

#### Response

- Status Code: 201 Created
- Response Model: schemas.PostResponse

### Get Post [GET /posts/{id}]

This endpoint retrieves a specific post by its ID.

#### Request

- Method: GET
- Path: /posts/{id}
- Path Parameters:
  - `id` (integer): The ID of the post.

#### Response

- Status Code: 200 OK
- Response Model: schemas.PostResponseVotes

### Update Post [PUT /posts/{id}]

This endpoint updates a specific post.

#### Request

- Method: PUT
- Path: /posts/{id}
- Path Parameters:
  - `id` (integer): The ID of the post to update.
- Body:
  - `title` (string): The updated title of the post.
  - `content` (string): The updated content of the post.
  - `published` (bool): The updated published status of the post.
- Headers:
  - Authorization: Bearer {access_token}

#### Response

- Status Code: 200 OK
- Response Model: schemas.PostResponse

### Delete Post [DELETE /posts/{id}]

This endpoint deletes a specific post.

#### Request

- Method: DELETE
- Path: /posts/{id}
- Path Parameters:
  - `id` (integer): The ID of the post to delete.
- Headers:
  - Authorization: Bearer {access_token}

#### Response

- Status Code: 204 No Content

## Users

### Create User [POST /users]

This endpoint creates a new user.

#### Request

- Method: POST
- Path: /users
- Body:
  - `username` (string): The username of the user.
  - `password` (string): The password of the user.

#### Response

- Status Code: 201 Created
- Response Model:

## Technologies

The SocialNet-API is built using the following technologies:

- Python: The backend language used for implementing the API logic.
- fastAPI: A powerful framework used for building the API and handling requests.
- PostgreSQL: A robust relational database management system used for data storage.
- Docker: A containerization platform used for containerizing the application and its dependencies.
- Postman: For API testing purposes

## Contributing
Contributions to the SocialNet-API are welcome! If you'd like to contribute, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your modifications or add new features.
Commit your changes and push the branch to your forked repository.
Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code as per the terms of the license.

## Contact
If you have any questions or suggestions regarding the SocialNet-API, please feel free to reach out:

Email: nandangonchikar97@gmail.com