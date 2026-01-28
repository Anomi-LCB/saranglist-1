
import pandas as pd
import json
import re
import os

INPUT_FILE = r'c:\Users\user\Desktop\AG\명부검색\26.1.25 목포사랑의교회 명부 10개팀.xlsx'
OUTPUT_DIR = r'c:\Users\user\Desktop\AG\명부검색\src'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'data.json')

def clean_phone(val):
    if pd.isna(val): return ""
    return re.sub(r'[^0-9]', '', str(val))

def clean_date(val):
    if pd.isna(val): return ""
    s = str(val)
    # If it's a timestamp, pandas might have read it as such
    if isinstance(val, pd.Timestamp):
        return val.strftime('%Y%m%d')
    # Remove non-digits
    return re.sub(r'[^0-9]', '', s)

def process_names(val):
    if pd.isna(val): return [], ""
    original_name = str(val).strip()
    # Split by 'OR', 'or', ',', '/' just in case
    # The user specifically mentioned "OR"
    parts = re.split(r'\s+OR\s+|\s+or\s+|\s*,\s*|\s*/\s*', original_name)
    search_names = [p.replace(" ", "") for p in parts] # Remove internal spaces for search
    return search_names, original_name

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    df = pd.read_excel(INPUT_FILE)
    
    # Map expected columns
    # We found: '이름', '생년월일', '휴대전화', '팀'
    # Let's be safe and strip whitespace from columns
    df.columns = df.columns.str.strip()
    
    records = []
    
    for _, row in df.iterrows():
        name_val = row.get('이름')
        dob_val = row.get('생년월일')
        phone_val = row.get('휴대전화')
        team_val = row.get('팀')
        
        # Skip empty rows if name is missing
        if pd.isna(name_val):
            continue
            
        # Split names and process
        # Using the same regex logic as before to split
        original_name_str = str(name_val).strip()
        parts = re.split(r'\s+OR\s+|\s+or\s+|\s*,\s*|\s*/\s*', original_name_str)
        
        phone_clean = clean_phone(phone_val)
        dob_clean = clean_date(dob_val)
        team_str = str(team_val).strip() if not pd.isna(team_val) else ""
        
        for part in parts:
            part = part.strip()
            if not part: continue
            
            # Clean name for search (remove spaces)
            search_name = part.replace(" ", "")
            
            records.append({
                "id": len(records) + 1, # Simple auto-increment ID
                "display_name": part,
                "search_names": [search_name], # Still keeping list format for compatibility
                "birthdate": dob_clean,
                "phone": phone_clean,
                "team": team_str
            })
        
    print(f"Extracted {len(records)} records.")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
