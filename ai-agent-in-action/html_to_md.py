import re
from bs4 import BeautifulSoup

def html_to_markdown(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    markdown_output = []

    # Find the main content div
    main_content_div = soup.find('div', class_='cp bi gq gr gs gt')
    if not main_content_div:
        return ""

    # Extract title
    title_tag = main_content_div.find('h1', class_='pw-post-title')
    if title_tag:
        markdown_output.append(f"# {title_tag.get_text(strip=True)}\n\n")
        # Remove the title tag to avoid re-processing it later
        title_tag.extract()

    # Remove author/date information and subscription section
    for unwanted_class in ['speechify-ignore', 'ac cw jl jm jn jo jp jq jr js jt ju jv jw jx jy jz ka', 'vx vy vz wa ac r cv']:
        for tag in main_content_div.find_all(class_=unwanted_class):
            tag.extract()

    # Remove any img tags that are not part of the main content (e.g., author image)
    for img_tag in main_content_div.find_all('img'):
        if 'data-testid' in img_tag.attrs and img_tag['data-testid'] == 'authorPhoto':
            img_tag.extract()

    # Process remaining content
    for element in main_content_div.find_all(['h1', 'h2', 'h3', 'p', 'ul', 'ol', 'pre', 'img']):
        if element.name.startswith('h'):
            level = int(element.name[1])
            markdown_output.append(f"{'#' * level} {element.get_text(strip=True).strip()}\n\n")
        elif element.name == 'p':
            paragraph_text = str(element)
            paragraph_text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', paragraph_text)
            clean_paragraph = BeautifulSoup(paragraph_text, 'html.parser').get_text(strip=True).strip()
            if clean_paragraph:
                markdown_output.append(f"{clean_paragraph}\n\n")
        elif element.name == 'ul':
            for li in element.find_all('li'):
                li_text = str(li)
                li_text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', li_text)
                clean_li = BeautifulSoup(li_text, 'html.parser').get_text(strip=True).strip()
                if clean_li:
                    markdown_output.append(f"- {clean_li}\n")
            markdown_output.append("\n") # Add a newline after a list
        elif element.name == 'ol':
            for i, li in enumerate(element.find_all('li')):
                li_text = str(li)
                li_text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', li_text)
                clean_li = BeautifulSoup(li_text, 'html.parser').get_text(strip=True).strip()
                if clean_li:
                    markdown_output.append(f"{i+1}. {clean_li}\n")
            markdown_output.append("\n") # Add a newline after a list
        elif element.name == 'pre':
            # Extract code content, preserving internal newlines and indentation
            code_content = element.get_text(separator='\n', strip=True)
            markdown_output.append(f"```python\n{code_content}\n```\n\n")
        elif element.name == 'img':
            img_src = element.get('src')
            img_alt = element.get('alt', '').strip()
            if img_src:
                markdown_output.append(f"![{img_alt}]({img_src})\n\n")

    # Filter out excessive blank lines and ensure single newlines between blocks
    final_output = []
    previous_line_was_empty = False
    for line in markdown_output:
        stripped_line = line.strip()
        if stripped_line:
            final_output.append(line)
            previous_line_was_empty = False
        elif not previous_line_was_empty:
            final_output.append("\n") # Keep only one blank line
            previous_line_was_empty = True

    return "".join(final_output).strip()

if __name__ == "__main__":
    html_file_path = 'articles/unlocking-tool-calling-for-any-llm-using-microagents-framework.html'
    output_markdown_file = 'articles/unlocking-tool-calling-for-any-llm-using-microagents-framework.md'

    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    markdown_content = html_to_markdown(html_content)

    with open(output_markdown_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Successfully converted {html_file_path} to {output_markdown_file}")