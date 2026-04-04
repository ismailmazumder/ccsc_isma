import os
import re
from pathlib import Path


def extract_match(pattern, data, default="", flags=0):
    match = re.search(pattern, data, flags)
    return match.group(1).strip() if match else default


def extract_section(data, start_label, end_label=None):
    if end_label:
        pattern = rf'{re.escape(start_label)}([\s\S]*?){re.escape(end_label)}'
    else:
        pattern = rf'{re.escape(start_label)}([\s\S]*)'
    match = re.search(pattern, data)
    return match.group(1) if match else ""


def format_profile(data):
    profile = {
        'ID No': extract_match(r'ID No\.?\s*(\d+)', data),
        'Name': extract_match(r'Name:\s*(.+?)\s+Father\'s Name:', data),
        "Father's Name": extract_match(r"Father's Name:\s*(.+?)\s+Mother's Name:", data),
        "Mother's Name": extract_match(r"Mother's Name:\s*(.+?)\s+Gender:", data),
        'Gender': extract_match(r'Gender:\s*(\w+)', data),
        'Religion': extract_match(r'Religion:\s*(\w+)', data),
        'Date of Birth': extract_match(r'Date of birth:\s*([\d/]+)', data),
        'Academic Qualification': extract_match(r'Academic Qualification:\s*(.+?)\s+Type:', data),
        'Type': extract_match(r'Type:\s*(.+?)\s+Designation:', data),
        'Designation': extract_match(r'Designation:\s*(.+?)\s+Subject', data),
        'Subject': extract_match(r'Subject\s*:\s*(.*?)\s+Date of Joining:', data),
        'Date of Joining': extract_match(r'Date of Joining:\s*([\d/+-]+)', data),
        'Blood Group': extract_match(r'Blood:\s*([\w\+\-]+)', data),
    }

    present_section = extract_section(data, 'Present Address', 'Permanent Address')
    permanent_section = extract_section(data, 'Permanent Address')

    present_address = {
        'Village/Holding No': extract_match(r'Village/Holding No:\s*(.+?)\s+Post:', present_section),
        'Post': extract_match(r'Post:\s*(.+?)\s+Word/ Union:', present_section),
        'Word/ Union': extract_match(r'Word/ Union:\s*(.+?)\s+Upazilla/ Thana:', present_section),
        'Upazilla/ Thana': extract_match(r'Upazilla/ Thana:\s*(.+?)\s+Zilla:', present_section),
        'Zilla': extract_match(r'Zilla:\s*(.+)', present_section),
    }

    permanent_address = {
        'Village/Holding No': extract_match(r'Village/Holding No:\s*(.+?)\s+Post:', permanent_section),
        'Post': extract_match(r'Post:\s*(.+?)\s+Word/ Union:', permanent_section),
        'Word/ Union': extract_match(r'Word/ Union:\s*(.+?)\s+Upazilla/ Thana:', permanent_section),
        'Upazilla/ Thana': extract_match(r'Upazilla/ Thana:\s*(.+?)\s+Zilla:', permanent_section),
        'Zilla': extract_match(r'Zilla:\s*(.+)', permanent_section),
    }

    return {
        'Basic Information': profile,
        'Present Address': present_address,
        'Permanent Address': permanent_address,
    }


def iter_info_files(base_dir):
    for root, _, files in os.walk(base_dir):
        if 'info.txt' in files:
            yield os.path.join(root, 'info.txt')


def main():
    script_dir = Path(__file__).resolve().parent
    default_base = script_dir / 'ccsc_love_pre_test'
    path_base = default_base if default_base.exists() else Path(r'D:\Users\im087\OneDrive\Desktop\All\ccsc\all_files')

    if not path_base.exists():
        raise FileNotFoundError(f'Base directory not found: {path_base}')

    search_term = input('Enter victim name or search term: ').strip()
    if not search_term:
        print('Search term is required.')
        return

    matches = 0
    for path in iter_info_files(path_base):
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                file_content = file.read()
        except OSError:
            continue

        if search_term.lower() not in file_content.lower():
            continue

        matches += 1
        print(f'--- Match {matches} ({path}) ---')
        formatted_profile = format_profile(file_content)
        for section, info in formatted_profile.items():
            print(section + ':')
            for key, value in info.items():
                print(f'  {key}: {value}')
            print()

    if matches == 0:
        print('No matches found.')


if __name__ == '__main__':
    main()
