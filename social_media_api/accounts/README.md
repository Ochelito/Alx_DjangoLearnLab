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

Social Media API – Follows and Feed Documentation
1. Follow/Unfollow Users
Endpoint
POST /accounts/follow/<user_id>/

Description

Toggles the follow status between the authenticated user and the target user:

If already following → unfollow

If not following → follow

Authentication

Required: Token authentication

Request Headers
Authorization: Token <user-token>
Content-Type: application/json

URL Parameters
Parameter	Type	Description
user_id	int	ID of the user to follow/unfollow
Sample Request
POST /accounts/follow/2/
Authorization: Token 123abc456def

Sample Response

Followed user:

{
  "detail": "followed bob"
}


Unfollowed user:

{
  "detail": "unfollowed bob"
}

2. User Feed
Endpoint
GET /posts/feed/

Description

Retrieves posts from users that the authenticated user follows, ordered by newest first.

Authentication

Required: Token authentication

Request Headers
Authorization: Token <user-token>

Sample Request
GET /posts/feed/
Authorization: Token 123abc456def

Sample Response
[
  {
    "id": 5,
    "author": "bob",
    "title": "Bob Post 2",
    "content": "Content 2",
    "created_at": "2025-08-19T10:30:00Z",
    "updated_at": "2025-08-19T10:30:00Z"
  },
  {
    "id": 4,
    "author": "bob",
    "title": "Bob Post 1",
    "content": "Content 1",
    "created_at": "2025-08-19T09:45:00Z",
    "updated_at": "2025-08-19T09:45:00Z"
  }
]

3. User Model Changes

The CustomUser model now includes:

Field	Type	Description
followers	ManyToManyField (self)	Users who follow this user
following	ManyToManyField (self)	Users that this user follows

These fields are asymmetrical: following a user does not automatically make them follow you.

4. Notes

All follow and feed operations require authenticated users.

Feed only displays posts from users the authenticated user is following.

The follow endpoint is idempotent: calling it multiple times toggles the follow status.


📖 API Documentation: Likes & Notifications
🔹 Likes System
1. Like a Post

Endpoint:
POST /posts/posts/<int:pk>/like/

Authentication: Required

Description: Allows an authenticated user to like a post. If the user already liked the post, they cannot like it again.

Request Example:

POST /posts/posts/5/like/
Authorization: Bearer <token>


Response Example (201 Created):

{
  "message": "Post liked."
}


Response Example (400 Bad Request):

{
  "message": "You have already liked this post."
}

2. Unlike a Post

Endpoint:
POST /posts/posts/<int:pk>/unlike/

Authentication: Required

Description: Allows an authenticated user to remove their like from a post.

Request Example:

POST /posts/posts/5/unlike/
Authorization: Bearer <token>


Response Example (200 OK):

{
  "message": "Post unliked."
}


Response Example (400 Bad Request):

{
  "message": "You have not liked this post."
}

🔹 Notifications System
3. Fetch Notifications

Endpoint:
GET /notifications/

Authentication: Required

Description: Returns a list of notifications for the logged-in user, with unread notifications shown prominently.

Request Example:

GET /notifications/
Authorization: Bearer <token>


Response Example (200 OK):

[
  {
    "id": 1,
    "actor": "johndoe",
    "verb": "liked your post",
    "target": "My First Blog Post",
    "timestamp": "2025-08-20T10:30:00Z",
    "read": false
  },
  {
    "id": 2,
    "actor": "janedoe",
    "verb": "commented on your post",
    "target": "My First Blog Post",
    "timestamp": "2025-08-20T09:45:00Z",
    "read": true
  }
]

🔹 Benefits of These Features

Likes increase engagement by letting users show appreciation for posts.

Notifications improve interaction by keeping users informed when others engage with their content (likes, comments, followers).

Together, these features create a more dynamic and interactive platform.