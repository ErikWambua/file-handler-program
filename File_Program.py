"""
File Handler Program
Reads a file, modifies its content, and writes to a new file
with comprehensive error handling.
"""

import os
import sys

def read_file(filename):
    """
    Read content from a file with error handling
    
    Args:
        filename (str): Path to the file to read
        
    Returns:
        str: Content of the file if successful, None if error occurs
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"✓ Successfully read {filename}")
        return content
        
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
        return None
    except PermissionError:
        print(f"❌ Error: Permission denied to read '{filename}'.")
        return None
    except UnicodeDecodeError:
        print(f"❌ Error: Cannot decode the file '{filename}'. It might be a binary file.")
        return None
    except IOError as e:
        print(f"❌ Error: Unable to read file '{filename}': {e}")
        return None

def modify_content(content, modification_type="upper"):
    """
    Modify the content based on the specified modification type
    
    Args:
        content (str): Original content to modify
        modification_type (str): Type of modification to apply
        
    Returns:
        str: Modified content
    """
    if not content:
        return content
        
    modification_types = {
        "upper": content.upper(),
        "lower": content.lower(),
        "title": content.title(),
        "reverse": content[::-1],
        "double": content * 2,
        "remove_spaces": ' '.join(content.split()),
        "default": content
    }
    
    return modification_types.get(modification_type, content)

def write_file(filename, content):
    """
    Write content to a file with error handling
    
    Args:
        filename (str): Path to the file to write
        content (str): Content to write to the file
        
    Returns:
        bool: True if successful, False if error occurs
    """
    try:
        # Check if file already exists
        if os.path.exists(filename):
            overwrite = input(f"⚠️  File '{filename}' already exists. Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                print("Operation cancelled.")
                return False
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✓ Successfully wrote to {filename}")
        return True
        
    except PermissionError:
        print(f"❌ Error: Permission denied to write to '{filename}'.")
        return False
    except IOError as e:
        print(f"❌ Error: Unable to write to file '{filename}': {e}")
        return False

def get_modification_choice():
    """
    Get user choice for content modification
    
    Returns:
        str: Modification type
    """
    print("\nChoose modification type:")
    print("1. Convert to UPPERCASE")
    print("2. Convert to lowercase")
    print("3. Convert to Title Case")
    print("4. Reverse content")
    print("5. Double content")
    print("6. Remove extra spaces")
    print("7. No modification")
    
    while True:
        try:
            choice = input("Enter your choice (1-7): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                modification_map = {
                    '1': 'upper',
                    '2': 'lower',
                    '3': 'title',
                    '4': 'reverse',
                    '5': 'double',
                    '6': 'remove_spaces',
                    '7': 'default'
                }
                return modification_map[choice]
            else:
                print("Please enter a number between 1 and 7.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            sys.exit(0)

def main():
    """Main function to run the file handler program"""
    print("=" * 50)
    print("📁 FILE HANDLER PROGRAM")
    print("=" * 50)
    
    # Get input filename
    while True:
        input_filename = input("\nEnter the filename to read: ").strip()
        if not input_filename:
            print("Please enter a valid filename.")
            continue
            
        content = read_file(input_filename)
        if content is not None:
            break
        else:
            retry = input("Would you like to try another file? (y/n): ").lower()
            if retry != 'y':
                print("Goodbye!")
                return
    
    # Get modification choice
    modification_type = get_modification_choice()
    
    # Modify content
    modified_content = modify_content(content, modification_type)
    
    # Get output filename
    while True:
        output_filename = input("\nEnter output filename: ").strip()
        if not output_filename:
            print("Please enter a valid filename.")
            continue
            
        if write_file(output_filename, modified_content):
            break
        else:
            retry = input("Would you like to try another filename? (y/n): ").lower()
            if retry != 'y':
                print("Operation cancelled.")
                return
    
    # Show preview
    print("\n" + "=" * 50)
    print("📊 PREVIEW")
    print("=" * 50)
    print(f"Original length: {len(content)} characters")
    print(f"Modified length: {len(modified_content)} characters")
    
    preview = modified_content[:200] + ("..." if len(modified_content) > 200 else "")
    print(f"\nPreview:\n{preview}")
    
    print(f"\n✅ Operation completed successfully!")
    print(f"📁 Output saved to: {output_filename}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")