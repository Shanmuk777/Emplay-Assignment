import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

# Step 1: Web Scraping
def webscrap(url):
    try:
        # Send an HTTP request to the URL
        a= requests.get(url)
        a.raise_for_status()
        
        # Parse the HTML content of the page using BeautifulSoup
        b = BeautifulSoup(response.text, 'html.parser')
        
        return b
    except Exception as e:
        print(f"Error while scraping: {e}")
        return None

# Step 2: Extract Headings and Sections
def extract(b):
    c = []

    # Find all headings (e.g., h1, h2, h3, etc.)
    headings = b.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    for heading in headings:
        section_title = heading.get_text(strip=True)
        section_content = []
        
        # Extract text content under the heading until the next heading
        sibling = heading.find_next_sibling()
        while sibling and sibling.name not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if sibling.name == 'p':
                section_content.append(sibling.get_text())
            sibling = sibling.find_next_sibling()

        headings_and_sections.append({
            'title': section_title,
            'content': ' '.join(section_content),
        })

    return headings_and_sections

# Step 3: Summarization
def summary(headings_and_sections):
    summarized_sections = []

    for section in headings_and_sections:
        section_title = section['title']
        section_content = section['content']

        # Summarize each section's content
        section_summary = summarize(section_content, ratio=0.3)  # Adjust the ratio as needed

        summarized_sections.append({
            'title': section_title,
            'summary': section_summary,
        })

    return summarized_sections

# Step 4: Main Pipeline
def main(url):
    # Step 1: Web Scraping
    soup = scrape_web_page(url)

    if soup is not None:
        # Step 2: Extract Headings and Sections
        headings_and_sections = extract_headings_and_sections(soup)

        if headings_and_sections:
            # Step 3: Summarization
            summarized_sections = summarize_sections(headings_and_sections)

            # Step 4: Display or further process the summarized sections
            for section in summarized_sections:
                print(f"Section Title: {section['title']}")
                print(f"Section Summary: {section['summary']}\n")

# Provide the URL of the web page to be scraped and summarized
web_page_url = 'https://en.wikipedia.org/wiki/Alexander_the_Great'
main(web_page_url)
