# TabloLang

**TabloLang** is a simple backend programming language designed to extract and store data in tabular form from HTML web pages.

## Features
- Load HTML files and extract data.
- Save extracted data in a CSV format.
- Simple syntax for web data extraction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/TabloLang.git

2. Navigate to the project directory:
   ```bash
   cd TabloLang

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

Example Command File
Create a command file sample.tl with the following contents:

   ```vbnet
   LOAD_HTML "form.html"
   SELECT "input"
   EXTRACT "name" TO user_data
   EXTRACT "value" TO user_data
   SAVE_TABLE user_data TO "user_data.csv"
   DISPLAY_TABLE user_data



