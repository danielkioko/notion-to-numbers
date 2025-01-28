from notion_client import NotionDataFetcher
from numbers_script import NumbersUpdater

def main():
    # Fetch data from Notion
    notion = NotionDataFetcher()
    data = notion.fetch_database_data()
    
    if not data:
        print("No data found in Notion database")
        return
    
    # Get headers from the first row
    headers = list(data[0].keys())
    
    # Update Numbers sheet
    numbers = NumbersUpdater()
    numbers.update_sheet(headers, data)
    print("Numbers sheet updated successfully!")

if __name__ == "__main__":
    main() 