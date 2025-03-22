# Matepanion

[![GitHub stars](https://img.shields.io/github/stars/kkviper1/matepanion.svg)](https://github.com/kkviper1/matepanion/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/kkviper1/matepanion.svg)](https://github.com/kkviper1/matepanion/network)
[![GitHub issues](https://img.shields.io/github/issues/kkviper1/matepanion.svg)](https://github.com/kkviper1/matepanion/issues)

## Description

Matepanion is a Django project for a companion AI Chatbot that uses Twilio's whatsapp API and Krutrim's APIs to communicate.

## Features

- Personalized Behaviour
- Ease of use
- (TODO) Voice note conversations

## Installation

To install the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/kkviper1/matepanion.git
    ```
2. Change into the project directory:
    ```bash
    cd matepanion
    ```
3. (Optional) Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the project, follow these steps:

1. Create a .env file with your Krutrim API Key
2. Share the callback URL to your Twilio console
3. Chat

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request
