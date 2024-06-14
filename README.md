# scrape_data-from-event-adobe-summit
scrape_data from event adobe summit
# Adobe Summit Web Scraping

This project scrapes event details from the Adobe Summit website and saves the data into a CSV file. The data includes information such as event name, dates, location, description, key speakers, agenda, registration details, pricing, categories, and audience type.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone this repository or download the script file `scrape_adobe_summit.py`.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Install the required Python libraries using pip:

    ```bash
    pip install requests beautifulsoup4 pandas
    ```

## Usage

1. Run the Python script to scrape the data from the Adobe Summit website:

    ```bash
    python scrape_adobe_summit.py
    ```

2. The script will create a CSV file named `adobe_summit_2024.csv` in the same directory. This file contains the scraped data in a structured format.

## Files

- `scrape_adobe_summit.py`: The main script file for scraping the Adobe Summit website.
- `README.md`: This README file with instructions.

## Data Fields

The script extracts and saves the following data fields:

- Event Name
- Event Date(s)
- Location
- Website URL
- Description
- Key Speakers
- Agenda/Schedule
- Registration Details
- Pricing
- Categories
- Audience type

## Example Output

The resulting CSV file will have the following structure:

| Event Name   | Event Date(s)  | Location          | Website URL        | Description | Key Speakers                  | Agenda/Schedule                               | Registration Details                    | Pricing                                | Categories                               | Audience type                            |
|--------------|----------------|-------------------|--------------------|-------------|-------------------------------|----------------------------------------------|----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|
| Adobe Summit | March 25-28, 2024 | Las Vegas, NV & Virtual | [Adobe Summit](https://summit.adobe.com) | N/A         | Anil Chakravarthy, Ed Bastian, Mary Barra | Refer to the website for detailed agenda and schedule. | Refer to the website for registration details. | Refer to the website for current pricing details. | Digital marketing, Customer experience, Technology | Marketers, Advertisers, IT professionals |

## Troubleshooting

- Ensure you have an active internet connection.
- Verify the URL of the Adobe Summit is correct and accessible.
- If the website structure changes, update the selectors in the script accordingly.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a pull request or open an issue.

## License

This project is licensed under the MIT License.
