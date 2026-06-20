# Reflection

The **lint** stage protects code quality and consistency by catching formatting issues and style problems early. The **test** stage protects the application’s behavior by verifying that core API endpoints still work correctly and that failure cases are handled as expected. The **deploy** stage simulates releasing the app, so it should only happen after the code has already passed quality and correctness checks.

The order matters because deploying before testing could push broken code to production, which may cause downtime or incorrect API behavior for users. In a real production pipeline, one thing I would add is a **build and deployment to a staging environment** (or Docker image build) before production deployment, so changes can be validated in an environment closer to real use.
