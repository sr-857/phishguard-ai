from pypdf import PdfReader

try:
    reader = PdfReader("document.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    print(text[:2000]) # Print first 2000 chars to inspect
    
    # Search for 'Roney'
    if "Roney" in text or "RONEY" in text:
        print("\n--- FOUND USER NAME ---")
        print("Found 'Roney' in document.")
    else:
        print("\n--- User Name Not Found ---")
        
except Exception as e:
    print(f"Error reading PDF: {e}")
