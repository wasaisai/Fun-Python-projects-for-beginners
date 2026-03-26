import json
import os
import datetime
import uuid

def recorder(user_input: str, ai_response: str, cov_id: str, title: str = "新对话"):
    file_name = 'history.json'
    history = []
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r', encoding='utf-8') as f:
            try:
                history = json.load(f)
            except Exception:
                history = []
                                    
    formatted_message = [
        {"role": "user", "content": user_input},
        {"role": "assisant", "content": ai_response}
    ]
    
    new_entry={
        "id": str(uuid.uuid4()),
        "title": title,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message":formatted_message
    }
    
    if len(history) == 0:
        history.append(new_entry)
    else:
        found = False
        for item in history:
            if item.get('id') == cov_id:
                item['message'].extend(formatted_message)
                found = True
                break

            if not found:
                history.append(new_entry)
    
            
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4, ensure_ascii=False)
        
    