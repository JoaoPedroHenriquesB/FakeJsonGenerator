# JsonGenerator

## Overview

**JsonGenerator** is a Python-based automation tool designed to generate large volumes of mock user data in JSON format.

The main intent of this project is to **automate the creation of realistic datasets for testing, database population, and analysis**. It solves the problem of having to manually write or copy-paste sample data by programmatically generating thousands of user records with realistic attributes like names, emails, and employment details.

## Features

Here are the core functionalities implemented in the project:

* **Bulk Data Generation:** Capable of generating thousands of records (default is 10,000) in seconds.
* **Realistic Mock Data:** Uses the `Faker` library to create authentic-looking names, emails, and dates.
* **Structured JSON Output:** Exports data to a clean, indented `bigjson.json` file.
* **Randomized Attributes:** Automatically randomizes fields such as Salary, Department, Active Status, and Subscription Plan.

## Tech Stack/Libraries

The project was built using **Python 3** and the key libraries are:

* **Faker:** For generating fake data (names, emails, dates).
* **json:** Standard library for JSON serialization.
* **random:** Standard library for random number generation and choices.

## Images

!Terminal Execution
*Figure 1: Running the script in the terminal.*

!Generated JSON File
*Figure 2: The resulting bigjson.json file structure.*

## Installation and Setup

Follow these simple steps to get JsonGenerator running locally on your machine.

### Prerequisites

Ensure you have the following installed:

* **Python 3.6+**
* **pip** (Python package installer)

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/JsonGenerator.git
    cd JsonGenerator
    ```

2. **Install Dependencies**
    Run the following command to install the necessary packages:

    ```bash
    pip install faker
    ```

3. **Run the Script**
    Execute the main script to generate the data:

    ```bash
    python main.py
    ```

4. **Check Output**
    A file named `bigjson.json` will be created in the project directory containing the generated data.
