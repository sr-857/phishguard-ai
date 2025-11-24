# Contributing to PhishGuard AI

First off, thank you for considering contributing to PhishGuard AI! It's people like you that make PhishGuard AI such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots and animated GIFs** if possible

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior** and **explain which behavior you expected to see instead**
* **Explain why this enhancement would be useful**

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Follow the Python and JavaScript styleguides
* Include thoughtfully-worded, well-structured tests
* Document new code
* End all files with a newline

## Development Process

### Setup Development Environment

1. Fork the repo
2. Clone your fork
```bash
git clone https://github.com/YOUR_USERNAME/phishguard-ai.git
cd phishguard-ai
```

3. Install dependencies
```bash
# Backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

4. Create a branch
```bash
git checkout -b feature/your-feature-name
```

### Coding Standards

#### Python
* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* Use type hints where appropriate
* Write docstrings for all functions and classes
* Maximum line length: 100 characters

#### JavaScript/React
* Use ES6+ features
* Follow [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
* Use functional components with hooks
* Keep components small and focused

#### Git Commit Messages
* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Testing

* Write tests for new features
* Ensure all tests pass before submitting PR
* Maintain or improve code coverage

```bash
# Run Python tests
pytest

# Run frontend tests
cd frontend
npm test
```

### Documentation

* Update README.md if needed
* Add JSDoc comments for JavaScript functions
* Update API documentation for new endpoints

## Project Structure

```
phishguard-ai/
├── frontend/          # React application
├── src/              # Backend & ML code
├── models/           # Trained models
├── .github/          # GitHub assets
└── docs/             # Additional documentation
```

## Recognition

Contributors will be recognized in:
* README.md contributors section
* Release notes
* Project documentation

## Questions?

Feel free to contact the maintainer:
* Email: subhajitroy857@gmail.com
* LinkedIn: [linkedin.com/in/sr857](https://linkedin.com/in/sr857)

Thank you for contributing! 🎉
