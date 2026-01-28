
import pandas as pd

file_path = r'c:\Users\user\Desktop\AG\명부검색\26.1.25 목포사랑의교회 명부 10개팀.xlsx'

try:
    df = pd.read_excel(file_path)
    print("--- COLUMNS ---")
    for col in df.columns:
        print(f"'{col}'")
    print("\n--- FIRST ROW ---")
    print(df.iloc[0].to_dict())
except Exception as e:
    print(f"Error: {e}")
