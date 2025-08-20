Social Media API Documentation (Posts & Comments)
1. Authentication

All endpoints require token authentication except /register/ and /login/.

Header Example:

Authorization: Token <your_token_here>

2. User Endpoints
Endpoint	Method	Description
/register/	POST	Register a new user
/login/	POST	Obtain authentication token
/profile/	GET	Placeholder for profile info
3. Posts Endpoints
Endpoint	Method	Description
/posts/	GET	List all posts (paginated, filterable)
/posts/	POST	Create a new post
/posts/<id>/	GET	Retrieve a specific post
/posts/<id>/	PUT/PATCH	Update a post (author only)
/posts/<id>/	DELETE	Delete a post (author only)

Example Requests:

Create Post:

POST /posts/
{
    "content": "This is my first post!"
}


List Posts with Filter & Pagination:

GET /posts/?search=first&page=1&page_size=5


Response:

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "john",
            "content": "This is my first post!",
            "created_at": "2025-08-20T08:00:00Z",
            "updated_at": "2025-08-20T08:00:00Z",
            "comments": []
        }
    ]
}

4. Comments Endpoints
Endpoint	Method	Description
/comments/	GET	List all comments (paginated, filterable)
/comments/	POST	Create a new comment
/comments/<id>/	GET	Retrieve a specific comment
/comments/<id>/	PUT/PATCH	Update a comment (author only)
/comments/<id>/	DELETE	Delete a comment (author only)

Example Requests:

Create Comment:

POST /comments/
{
    "post": 1,
    "content": "Great post!"
}


Response:

{
    "id": 1,
    "post": 1,
    "author": "alice",
    "content": "Great post!",
    "created_at": "2025-08-20T08:05:00Z"
}


List Comments with Filter & Pagination:

GET /comments/?search=Great&page=1&page_size=5

5. Notes

Permissions:

Only the author of a post/comment can update or delete it.

All other users receive a 403 Permission Denied.

Pagination:

Default page size: 10

Query param page_size can be used to adjust (max 50)

Filtering:

Use ?search=<keyword> to filter posts/comments by content.

Token Authentication:

All CRUD operations require Authorization: Token <token> header.