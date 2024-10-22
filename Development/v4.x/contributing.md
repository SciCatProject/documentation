# Contributing

There are many to get involved with the SciCat project:

1. Documentation - Fixing errors, covering weaker areas, adding examples. Documentation
   is divided between the
   [homepage](https://github.com/SciCatProject/scicatproject.github.io),
   [documentation pages](https://github.com/SciCatProject/documentation), and READMEs in
   the repositories.
2. Github Issues - This should be the first area to focus on for those that want to
   amend the code. To see how the project is developed, see the [Git Workflow
   page.](./Development_Methods.md)
3. [Testing](./testing.md) - Most repositories contain unit tests. Integration between
   components is tested with [scicatlive](https://github.com/SciCatProject/scicatlive),
   which is also the easiest way to run and develop SciCat locally.
4. Development - Check individual repositories for more information on how to contribute
   code ([frontend](https://github.com/SciCatProject/frontend),
   [backend](https://github.com/SciCatProject/scicat-backend-next)).

Communication is done through github issues, a slack channel, and a biweekly developer
meeting. Please [contact](https://scicatproject.github.io/#team) the project leader, Max
Novelli, for more information on getting involved.

## Issues

Issues are handled within the Github Issue tracker. Please follow the provided template
for each repository.

## Merge Requests

There should be **no** pushing directly to the `main`, `master` or `develop` branches.
To implement a fix, fork the repository and create a branch (eg `fix/ISSUE-NAME`)
complete all work there. When it is complete, open a Pull Request, which will be
reviewed and merged by the core developers.
