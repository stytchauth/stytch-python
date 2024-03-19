# Development

Thanks for contributing to Stytch's Python library! If you run into trouble, find us in [Slack].

## Setup

1. Install [Python](https://www.python.org/) version 3.8 or greater.
2. (Recommended, but optional) Create a new [virtualenv](https://docs.python.org/3/tutorial/venv.html).
3. `pip install -r requirements_dev.txt`

## Generating (and regenerating) the API

If you create, update, or delete an API method, you should rerun the codegen to keep this module up-to-date. There is a
script at `bin/generate-api.sh` that will run the default codegen with sane options (applying default formatters, not
overwriting existing manual implementation methods). This is the recommended way to allow the client to hit a new
endpoint.

### Adding a new manual implementation method

If you are adding a new **manual** method, first check if you need to add any new `additional_imports` within
the spec file. Add your input and create the stub for your manual method. Run `bin/generate-api.sh`. The script will
generate the new method stub, but your import may be missing -- this is because the auto-formatter determined that the
method was not used. You can now write your manual method, and add a test in `api/test/`

You should be able to call `bin/generate.sh` again to ensure you've added all necessary imports. Verify the correctness
of your changes by remembering to [run the unit tests][#testing].

## Testing

Run the tests with the `unittest` module. To test everything, run `python -m unittest` from the project root directory.

Run the **core** unit tests with `python -m unittest discover -s stytch/ -t .`.

Run the **codegen** unit tests with `python -m unittest discover -s codegen/ -t .`

Run the **integration** tests with `python -m unittest discover -s test/ -t .`

The integration tests call the test API of Stytch to ensure you can call all methods. It requires setting up the following environment variables:

- `STYTCH_PYTHON_RUN_INTEGRATION_TESTS=1`
- `STYTCH_PROJECT_ID=your-stytch-project-id`
- `STYTCH_SECRET=your-stytch-secret`

You can check test coverage with the following command:

```
coverage run -m unittest  && coverage report --omit="*test/*" --sort=cover
```

Note that if you _didn't_ enable the integration tests that coverage will be much lower. If you have your
`STYTCH_PROJECT_ID` and `STYTCH_SECRET` in your env, this command may be useful:

```
env STYTCH_PYTHON_RUN_INTEGRATION_TESTS=1 coverage run -m unittest && coverage html --omit="*test/*"
```

The above is also available as a convenience script at `bin/generate-coverage.sh`

You can run that and then see the exact coverage in a useful HTML page with line-by-line coverage.

## Issues and Pull Requests

Please file issues in this repo. We don't have an issue template yet, but for now, say whatever you think is important!

If you have non-trivial changes you'd like us to incorporate, please open an issue first so we can discuss the changes before starting on a pull request. (It's fine to start with the PR for a typo or simple bug.) If we think the changes align with the direction of the project, we'll either ask you to open the PR or assign someone on the Stytch team to make the changes.

When you're ready for someone to look at your issue or PR, assign `@stytchauth/client-libraries` (GitHub should do this automatically). If we don't acknowledge it within one business day, please escalate it by tagging `@stytchauth/engineering` in a comment or letting us know in [Slack].

[slack]: https://stytch.slack.com/join/shared_invite/zt-2f0fi1ruu-ub~HGouWRmPARM1MTwPESA
