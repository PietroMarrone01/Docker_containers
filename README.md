In this exercise, you need to develop a containerized application and deploy it. The web application shows to the end user an "hello world" landing page along with your name, retrieved from a database.

The exercise must met the following acceptance criteria (the more, the merrier):

1. Front end
    - A web server that displays an "hello world, {name}" page with the {name} token should be replaced with a value taken from the database
    - Dockerfile to build the front end container
2. Database
    - A database with a simple schema containing a table with a row having at least a "name" column and a row with your name on it.
    - Dockerfile to build the database container
3. Use one of the following container orchestration approaches:
    - docker-compose
    - kubernetes yaml
    - helm
    - kustomize
4. Instruction file with list of instructions to build and run the proposed solution
