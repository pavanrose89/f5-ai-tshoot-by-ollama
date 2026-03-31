def validate_file_upload(file):
    """
    Validates the uploaded file based on extension and size.
    """
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
    max_file_size = 5 * 1024 * 1024  # 5MB

    if '.' in file.filename:
        extension = file.filename.rsplit('.', 1)[1].lower()
        if extension not in allowed_extensions:
            return False, "Invalid file extension."
    else:
        return False, "No file extension found."

    if file.content_length > max_file_size:
        return False, "File is too large. Maximum size is 5MB."

    return True, "File is valid."


def validate_text_input(text):
    """
    Validates user input to prevent injection attacks.
    """
    # Basic validation: ensuring input is not empty and doesn't contain malicious scripts.
    if not text or "<script>" in text or "' OR '1'='1" in text:
        return False, "Invalid text input."
    return True, "Text input is valid."


def sanitize_prompt(prompt):
    """
    Sanitizes the prompt to remove potentially harmful characters.
    """
    sanitized_prompt = prompt.replace("<", "&lt;").replace(">", "&gt;")
    sanitized_prompt = sanitized_prompt.replace("'", "&apos;").replace("&", "&amp;")
    return sanitized_prompt
