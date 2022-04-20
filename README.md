# ReactDjango_JWT_StarterCode

Starter code for full stack React + Django applications using JWT for authentication/authorization and a fully working register/login system on the React side

## NOTE

"cars" app in Django backend for example purposes only. Study it closely and review provided resources to understand how to properly create protected endpoints that require a JWT token for authorization.

## For implementing user roles

- see comments in the following files in the order they are listed
  - backend/authentication/models.py
  - backend/authentication/serializers.py (note that there are several places needing modification in that file)
- If modifying the User class in authentication/serializers.py, make sure to drop your existing database,
  create it, and run migrations from scratch
- for a great reference, see the following article: https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
  - note that this article is from 2018 and dealing with a full stack Django application scenario with HTML/CSS templates. The principles of setting up the backend portion for User roles is still valid!
- once user roles are set up on your backend, you can now utilize them on the frontend. See the "Handling Multiple User Roles in React Router" video on your Online Portal!
