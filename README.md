# project_name Backend

To get started, rename all instances of `project_name` in the codebase to the name of your project.

## Development Environment Setup

To set up your development environment, use the provided Docker Compose config in the base directory. Run `docker compose up` to start the Flask app in a Docker container.

To set up pre-commit hooks, ensure that `pre-commit` is installed. You can install it using `pip install pre-commit`. Run `pre-commit install` to install the hooks defined in `.pre-commit-config.yml`. This ensures that code is properly formatted and passes linting checks before commits are made.
