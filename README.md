# project_name

To get started, rename all instances of `project_name` in the codebase to the name of your project, and delete this line.

## Development Environment Setup

To set up your development environment, use the provided Docker Compose config in the base directory.

1. Duplicate the `.env.example` file and name the new file `.env`.

2. Run `docker compose up` to start the Flask app in a Docker container.

3. To set up pre-commit hooks, ensure that `pre-commit` is installed. You can install it using:

   ```bash
   pip install pre-commit
   ```

4. To install the hooks defined in `.pre-commit-config.yml`, run:

   ```bash
   pre-commit install
   ```
   This ensures that code is properly formatted and passes linting checks before commits are made.
