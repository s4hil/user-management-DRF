## Features

- **User Registration**: Allows users to sign up with a username, email, and password.
- **User Login**: Users can log in and receive an authentication token.
- **Superuser Login**: Superusers can log in separately to manage users.
- **User Management by Superuser**:
  - View all users
  - Create new users
  - Update existing users
  - Delete users
- **Token-Based Authentication**: Secure API endpoints using Django REST Framework's token authentication.

## API Endpoints

| Method | Endpoint | Description | Requires Authentication? |
|--------|---------------------------|----------------------------------|--------------------------|
| `POST` | `/api/register/` | Register a new user | ❌ No |
| `POST` | `/api/login/` | User login and receive token | ❌ No |
| `POST` | `/api/superuser-login/` | Superuser login and receive token | ❌ No |
| `GET` | `/api/manage-users/` | Get list of all users (Superuser only) | ✅ Yes (Superuser) |
| `POST` | `/api/manage-users/` | Create a new user (Superuser only) | ✅ Yes (Superuser) |
| `PUT` | `/api/manage-users/{id}/` | Update a user by ID (Superuser only) | ✅ Yes (Superuser) |
| `DELETE` | `/api/manage-users/{id}/` | Delete a user by ID (Superuser only) | ✅ Yes (Superuser) |
