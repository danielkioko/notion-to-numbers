from notion_client import Client
from config import NOTION_TOKEN, NOTION_DATABASE_ID

class NotionDataFetcher:
    def __init__(self):
        self.client = Client(auth=NOTION_TOKEN)
        
    def fetch_database_data(self):
        """Fetch all rows from the Notion database"""
        response = self.client.databases.query(
            database_id=NOTION_DATABASE_ID
        )
        
        rows = []
        for page in response['results']:
            row_data = {}
            properties = page['properties']
            
            for prop_name, prop_data in properties.items():
                prop_type = prop_data['type']
                if prop_type == 'title':
                    row_data[prop_name] = prop_data['title'][0]['text']['content'] if prop_data['title'] else ''
                elif prop_type == 'rich_text':
                    row_data[prop_name] = prop_data['rich_text'][0]['text']['content'] if prop_data['rich_text'] else ''
                elif prop_type == 'number':
                    row_data[prop_name] = prop_data['number'] if prop_data['number'] else 0
                elif prop_type == 'select':
                    row_data[prop_name] = prop_data['select']['name'] if prop_data['select'] else ''
                
            rows.append(row_data)
            
        return rows 