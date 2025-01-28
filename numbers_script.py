import subprocess
from config import NUMBERS_DOC_NAME

class NumbersUpdater:
    def __init__(self):
        self.doc_name = NUMBERS_DOC_NAME
        
    def update_sheet(self, headers, data):
        """Update Numbers sheet with the provided data"""
        script = f'''
        tell application "Numbers"
            activate
            if not (exists document "{self.doc_name}") then
                make new document
                save document 1 as "{self.doc_name}"
            end if
            
            tell document "{self.doc_name}"
                tell active sheet
                    tell table 1
                        delete every row
                        
                        -- Add headers
                        set values of row 1 to {{"{'", "'.join(headers)}"}}
                        
                        -- Add data rows
                        {self._generate_data_rows(data)}
                    end tell
                end tell
            end tell
        end tell
        '''
        
        self._run_applescript(script)
    
    def _generate_data_rows(self, data):
        script_rows = []
        for row_index, row in enumerate(data, start=2):
            values = [str(row.get(header, '')) for header in headers]
            script_rows.append(f'set values of row {row_index} to {{"{'", "'.join(values)}"}}')
        return '\n'.join(script_rows)
    
    def _run_applescript(self, script):
        """Execute the AppleScript"""
        process = subprocess.Popen(['osascript', '-e', script],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            raise Exception(f"AppleScript error: {stderr.decode()}") 