# Python Command Line Tools course

In this course you'll go through all the basics to learn how to build Python command line tools. You'll go from the very basics (and fastest ways) to create them, to more involved with frameworks that can handle complex cases.

The full course is available on the [O'Reilly platform](https://learning.oreilly.com/videos/python-command-line/50131VIDEOPAIML/).

**Building a CLI is the foundation for automation in your daily work**

By the end of the course you should feel confident in creating a tool, and the following:

- packaging
- testing and linting
- CI/CD for testing before a PR
- CI/CD for cutting a release and automatically uploading the project

We'll cover 3 different ways to create tools, from the very basic (with `sys.argv`) to using a framework that comes with Python (`argparse`), and finally the more involved, by using an external library like [Click](https://click.palletsprojects.com/en/latest/).

## Repository structure

Since this repository is used as the basis for the course and working with 3 different flavours of the same tool, the [examples](examples/) directory has the `sys.argv` and `argparse` code, while the rest of the repository contains all the files for automation, packaging, testing, and code using the Click framework.

## Next steps

Now that you are comfortable building tools in Python. Try creating them and pushing the code to a repository online. Follow the best-practices in this course to maintain it and improve it with more and better tests and automation.

Start finding manual processes that could get automated with a command line tool. Use any of the 3 variants discussed in the course: from simplest, to more involved.

## Questions and followups

If you find and issue in this repo or in the course, feel free to create one in this repo. I'm most active on [LinkedIn](https://www.linkedin.com/in/alfredodeza/) where you can also follow me as I continue to produce more content.
