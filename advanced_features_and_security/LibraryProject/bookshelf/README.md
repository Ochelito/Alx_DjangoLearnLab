# Permissions and Groups

## Groups:
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: all permissions

## Notes:
Permissions are checked using Django’s @permission_required decorator. 
If a user lacks permission, they will receive a 403 Forbidden response.