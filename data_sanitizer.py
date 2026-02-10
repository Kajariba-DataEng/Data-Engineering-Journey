def sanitize_data_list(data_list):
    """
    Standardizes a list of strings by removing whitespace 
    and converting to uppercase for database consistency.
    """
    clean_list = []
    
    for item in data_list:
        # The logic: Strip spaces and capitalize
        clean_item = item.strip().upper()
        clean_list.append(clean_item)
        
    return clean_list

# --- Testing the Utility ---
if __name__ == "__main__":
    messy_input = ["  internet_pro  ", " mobile_5g ", "TV_LIGHT  ", "  fiber_optic"]
    result = sanitize_data_list(messy_input)
    
    print(f"Original: {messy_input}")
    print(f"Sanitized: {result}")
