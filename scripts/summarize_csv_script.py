# summarize_csv_script.py

from envtest import summarize_csv

def main():
    file_path = 'scripts/data.csv'  
    summary = summarize_csv(file_path)
    print("Summary of CSV:")
    print(summary)

if __name__ == "__main__":
    main()
