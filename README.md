# 📊 Notion to Numbers Sync

A Python tool that automatically syncs your Notion database tables to Apple Numbers spreadsheets. Perfect for keeping your Numbers documents in sync with your Notion workspace!

## ✨ Features

- 🔄 Automatic sync from Notion database to Numbers spreadsheet
- 📝 Supports multiple Notion property types (text, numbers, select)
- 🔧 Creates new Numbers document if it doesn't exist
- 🎯 Easy configuration using environment variables
- 🚀 Simple to set up and run

## 🛠️ Prerequisites

- macOS with Numbers installed
- Python 3.7+
- A Notion account with API access
- A Notion database to sync from

## 📦 Installation

1. Clone this repository:

bash pip install -r requirements.txt

## ⚙️ Configuration

1. **Set up Notion API Access**
   - Go to [Notion Integrations](https://www.notion.so/my-integrations)
   - Create a new integration
   - Copy the integration token

2. **Share Your Notion Database**
   - Open your Notion database
   - Click `Share` in the top right
   - Add your integration to the share list
   - Copy the database ID from the URL (it's the part after the workspace name and before the '?')

3. **Configure Environment Variables**
   - Copy the `.env.example` file to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Fill in your details in the `.env` file:
     ```
     NOTION_TOKEN=your_notion_integration_token
     NOTION_DATABASE_ID=your_database_id
     NUMBERS_DOC_NAME=Your Document.numbers
     ```

4. **Configure macOS Permissions**
   - Open System Preferences > Security & Privacy > Privacy
   - Select "Automation" from the left sidebar
   - Ensure Python/your terminal app has permission to control Numbers
   - You may need to add Terminal/iTerm to the list if it's not there
   - Check the box next to "Numbers" for your terminal application

## 🚀 Usage

Run the sync script:
bash python main.py

The script will:
1. Connect to your Notion database
2. Fetch all data
3. Create or update a Numbers document
4. Populate the spreadsheet with your Notion data

## 📋 Supported Notion Property Types

- ✅ Title
- ✅ Rich Text
- ✅ Number
- ✅ Select

## ⚠️ Important Notes

1. **First Run**
   - The first time you run the script, macOS may prompt you to allow Terminal/iTerm to control Numbers
   - You must accept this prompt for the script to work

2. **Numbers Document Location**
   - By default, the script will create/update the Numbers document in your home directory
   - You can specify a different location by providing the full path in `NUMBERS_DOC_NAME`

3. **AppleScript Permissions**
   - If you get permission errors, try running Numbers manually first
   - Make sure Numbers is not in full-screen mode
   - If issues persist, try quitting and reopening Numbers

4. **Data Handling**
   - The script will overwrite existing data in the Numbers document
   - Make sure to backup important spreadsheets before running the sync
   - Empty cells in Notion will be converted to empty strings or 0 for numbers

## 🤔 Troubleshooting

**Numbers document isn't updating?**
- Make sure Numbers is installed and running
- Check if you have permission to create/edit files
- Verify the document name in your `.env` file
- Check System Preferences > Security & Privacy > Privacy > Automation settings

**No data appearing?**
- Confirm your Notion integration has access to the database
- Verify your database ID is correct
- Check your integration token permissions
- Make sure the database has at least one row of data

**AppleScript errors?**
- Quit Numbers completely and reopen it
- Check if Numbers is in full-screen mode (exit if it is)
- Verify automation permissions in System Preferences
- Try running the script with sudo (not recommended for regular use)

## 🛡️ Security Note

Keep your `.env` file secure and never commit it to version control. The `.gitignore` file is configured to exclude it.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Notion API](https://developers.notion.com/)
- [Python Notion Client](https://github.com/ramnes/notion-sdk-py)
- Apple Numbers and AppleScript documentation

---

Made with ❤️ by Daniel Kioko