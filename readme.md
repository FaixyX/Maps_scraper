# Google Maps Business Scraper

A Python-based web scraping tool that extracts comprehensive business information from Google Maps search results using Selenium WebDriver. This tool is designed for market research, lead generation, and business intelligence gathering.

# Demo Video
https://www.loom.com/share/3f311684e8474f85a0b7e449ec8cc4c6?sid=a7a4aa29-c452-4311-ae8a-9c3ab4ae083e

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [File Structure](#file-structure)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Output Format](#output-format)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Legal and Ethical Considerations](#legal-and-ethical-considerations)
- [License](#license)

## Project Overview

This project is a web scraping automation tool that leverages Google Maps' search functionality to collect detailed business information. It's built with Python and Selenium WebDriver to handle dynamic content loading and user interactions.

### Key Capabilities

- **Interactive Search**: Accepts user-defined search terms and locations
- **Comprehensive Data Extraction**: Captures business names, ratings, reviews, contact information, and detailed attributes
- **Scalable Results**: Configurable scrolling to load more search results
- **Robust Error Handling**: Graceful handling of missing data and network issues
- **Structured Output**: Exports data in JSON format for easy analysis

### Architecture

The scraper follows a simple but effective architecture:

```
User Input → Search Execution → Results Scraping → Data Processing → JSON Export
```

- **Input Layer**: Interactive prompts for search terms and scroll count
- **Browser Automation**: Selenium WebDriver with Chrome for web interaction
- **Data Extraction**: CSS selectors and XPath for targeted element selection
- **Output Layer**: JSON serialization with UTF-8 encoding support

## Features

### Core Functionality

- **Dynamic Search**: Search for any business type or niche in any location
- **Multi-Data Extraction**: 
  - Business name and category
  - Rating and total review count
  - Physical address
  - Website URL
  - Phone number
  - Detailed "About" section information
- **Configurable Depth**: Adjustable scroll count to control result volume
- **Real-time Progress**: Console output showing extraction progress
- **Error Resilience**: Continues processing even if individual businesses fail

### Data Quality Features

- **Graceful Degradation**: Handles missing data with "N/A" placeholders
- **UTF-8 Support**: Proper encoding for international business names
- **Structured Output**: Consistent JSON format for easy parsing
- **Comprehensive Coverage**: Extracts both basic and detailed business information

## File Structure

```
maps-business/
├── maps_scraper.py          # Main scraping script
├── businesses_data.json     # Output file with scraped data
├── .gitignore              # Git ignore rules
├── venv/                   # Python virtual environment
└── readme.md              # This documentation file
```

### File Descriptions

- **`maps_scraper.py`**: The main Python script containing all scraping logic
- **`businesses_data.json`**: Generated output file containing all scraped business data
- **`.gitignore`**: Excludes virtual environment and environment files from version control
- **`venv/`**: Python virtual environment directory (excluded from git)

## Prerequisites

Before running this scraper, ensure you have the following installed:

### System Requirements

- **Python 3.7+**: Required for modern Python features and Selenium compatibility
- **Chrome Browser**: Latest version recommended for optimal compatibility
- **ChromeDriver**: Must match your Chrome browser version

### Python Dependencies

The following Python packages are required:

- `selenium`: Web automation and browser control
- `json`: Built-in JSON handling (no installation needed)
- `time`: Built-in time utilities (no installation needed)

## Installation and Setup

### Step 1: Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd maps-business

# Or download and extract the project files
```

### Step 2: Set Up Python Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Install Selenium
pip install selenium

# Verify installation
python -c "import selenium; print('Selenium installed successfully')"
```

### Step 4: Install ChromeDriver

#### Option A: Using Homebrew (macOS)
```bash
brew install chromedriver
```

#### Option B: Manual Installation
1. Check your Chrome version: `chrome://version/` in Chrome browser
2. Download matching ChromeDriver from: https://chromedriver.chromium.org/
3. Extract and add to your system PATH or place in project directory

#### Option C: Using pip (Alternative)
```bash
pip install webdriver-manager
```

### Step 5: Verify Setup

```bash
# Test ChromeDriver installation
python -c "from selenium import webdriver; driver = webdriver.Chrome(); driver.quit(); print('Setup successful!')"
```

## Usage

### Basic Usage

1. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate     # Windows
   ```

2. **Run the scraper**:
   ```bash
   python maps_scraper.py
   ```

3. **Follow the prompts**:
   - Enter your search term (e.g., "restaurants in California")
   - Specify number of scrolls (default: 5)

### Usage Examples

#### Example 1: Local Restaurant Search
```
Enter the niche or search term: restaurants in Indianapolis
Enter number of scrolls for more results: 3
```

#### Example 2: Industry-Specific Search
```
Enter the niche or search term: coffee shops in Seattle
Enter number of scrolls for more results: 10
```

#### Example 3: Service-Based Search
```
Enter the niche or search term: dental clinics in New York
Enter number of scrolls for more results: 5
```

### Advanced Usage

#### Customizing Scroll Count
- **Low (1-3)**: Quick results, fewer businesses
- **Medium (4-7)**: Balanced speed and coverage
- **High (8-15)**: Maximum coverage, longer runtime

#### Search Term Optimization
- **Be Specific**: "Italian restaurants in downtown Chicago" vs "restaurants"
- **Use Location**: Include city, state, or neighborhood for targeted results
- **Industry Terms**: Use specific business categories for better results

## Output Format

The scraper generates a JSON file (`businesses_data.json`) with the following structure:

```json
[
  {
    "name": "Business Name",
    "rating": "4.5",
    "total_reviews": "1,234",
    "category": "Business Category",
    "address": "Full Address",
    "website": "https://website.com",
    "phone": "+1-555-123-4567",
    "about": {
      "Offerings": ["Service 1", "Service 2"],
      "Amenities": ["Amenity 1", "Amenity 2"],
      "Payments": ["Payment Method 1", "Payment Method 2"],
      "Accessibility": ["Accessibility Feature 1"]
    }
  }
]
```

### Data Fields Explained

- **`name`**: Business name as displayed on Google Maps
- **`rating`**: Average rating (1.0-5.0 scale)
- **`total_reviews`**: Number of reviews in parentheses
- **`category`**: Primary business category
- **`address`**: Full physical address
- **`website`**: Business website URL (if available)
- **`phone`**: Contact phone number
- **`about`**: Detailed business attributes organized by category

## Configuration

### Chrome Options

The scraper uses the following Chrome configuration for optimal performance:

```python
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
```

### Timing Configuration

- **Search Wait**: 5 seconds for initial results
- **Scroll Wait**: 2 seconds between scrolls
- **Detail Wait**: 3 seconds for business details to load
- **Element Wait**: 5-10 seconds for dynamic content

### CSS Selectors

The scraper uses specific CSS selectors for data extraction:

- **Business Name**: `h1.DUwDvf`
- **Rating**: `div.F7nice > span:nth-child(1) > span:nth-child(1)`
- **Total Reviews**: `span:nth-child(2) > span > span`
- **Category**: `button.DkEaL`
- **Address**: `button[data-item-id='address']`
- **Website**: `a[data-item-id='authority']`
- **Phone**: `button[data-item-id^='phone']`

## Troubleshooting

### Common Issues and Solutions

#### Issue: ChromeDriver Not Found
**Error**: `selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Chrome binary`

**Solution**:
```bash
# Ensure Chrome is installed and in PATH
# Or specify Chrome path explicitly in the script
chrome_options.binary_location = "/path/to/chrome"
```

#### Issue: Element Not Found
**Error**: `selenium.common.exceptions.NoSuchElementException`

**Solution**:
- Google Maps may have updated their interface
- Check if CSS selectors need updating
- Increase wait times for slower connections

#### Issue: Rate Limiting
**Symptoms**: Fewer results than expected, timeouts

**Solutions**:
- Reduce scroll count
- Add delays between requests
- Use different IP addresses (VPN)
- Respect robots.txt and terms of service

#### Issue: Memory Issues
**Symptoms**: Script crashes with large datasets

**Solutions**:
- Reduce scroll count
- Process data in batches
- Close browser between sessions

### Performance Optimization

#### For Large Datasets
1. **Batch Processing**: Process results in smaller chunks
2. **Memory Management**: Clear variables periodically
3. **Connection Management**: Use stable internet connection

#### For Faster Execution
1. **Reduce Wait Times**: Adjust timing variables (may cause errors)
2. **Optimize Selectors**: Use more specific CSS selectors
3. **Parallel Processing**: Run multiple instances (use with caution)

### Debug Mode

To enable debug output, add logging to the script:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

### Development Workflow

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Make changes**: Follow the coding standards below
4. **Test thoroughly**: Ensure the scraper works with your changes
5. **Submit a pull request**: Include detailed description of changes

### Coding Standards

- **Python Style**: Follow PEP 8 guidelines
- **Error Handling**: Always include try-except blocks for web scraping
- **Documentation**: Add comments for complex logic
- **Testing**: Test with different search terms and locations

### Areas for Improvement

- **API Integration**: Consider using Google Places API for more reliable data
- **Database Storage**: Add database support for large datasets
- **GUI Interface**: Create a web-based interface
- **Export Formats**: Add CSV, Excel, and other export options
- **Scheduling**: Add automated scheduling capabilities

## Legal and Ethical Considerations

### Terms of Service Compliance

- **Google Maps Terms**: Review and comply with Google Maps Terms of Service
- **Rate Limiting**: Implement reasonable delays between requests
- **Data Usage**: Use scraped data responsibly and legally
- **Respect Robots.txt**: Check and respect website robots.txt files

### Best Practices

- **Respectful Scraping**: Don't overwhelm servers with requests
- **Data Privacy**: Handle business data responsibly
- **Attribution**: Credit Google Maps as data source when appropriate
- **Commercial Use**: Verify commercial usage rights

### Limitations

- **Data Accuracy**: Scraped data may not be 100% accurate or current
- **Service Changes**: Google may change their interface, breaking the scraper
- **Legal Risks**: Web scraping may have legal implications in some jurisdictions
- **Rate Limits**: Google may implement rate limiting or blocking

## License

This project is provided as-is for educational and research purposes. Users are responsible for ensuring compliance with applicable laws and terms of service.

### Disclaimer

This tool is for educational purposes only. Users are responsible for:
- Complying with Google Maps Terms of Service
- Respecting website robots.txt files
- Using scraped data legally and ethically
- Understanding local laws regarding web scraping

### Support

For issues and questions:
1. Check the troubleshooting section above
2. Review Google Maps Terms of Service
3. Consider using official APIs for production use

---

**Note**: This scraper is designed for educational and research purposes. For commercial applications, consider using Google's official Places API which provides more reliable and legally compliant access to business data.
