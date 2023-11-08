# Layered Pattern Generator

This project includes a simple Python program that generates a pattern based on the number of layers specified. The pattern starts with 'A' as the innermost layer and expands outward with subsequent letters of the alphabet.

## Structure

- `layers.py`: Contains the `create_layers` function that generates the pattern.
- `layers_test.py`: Contains unit tests for the `create_layers` function using `pytest`.
- `main.py`: A command-line interface to interact with the `create_layers` function.

## Prerequisites

- Python 3
- pip
- virtualenv (optional but recommended)

## Setup

To set up the project environment, follow these steps:

1. Clone the repository:

```bash
git clone git@github.com:juusoi/layers.git
cd layers
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On Unix or MacOS:

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the main program:

```bash
python main.py
```

Follow the on-screen prompts to generate a pattern with your desired number of layers.

## Testing

To run the tests:

```bash
pytest layers_test.py
```

Make sure all tests pass to verify the correct behavior of the `create_layers` function.

## Exiting the Application

To exit the application, enter `0` when prompted for the number of layers.

## License

This project is licensed under the [MIT License](LICENSE).
