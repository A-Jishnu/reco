#!/usr/bin/env python3
"""
Music Recommendation Using Facial Expressions
Main application launcher - WebContainer compatible version
"""

import sys
import os

def main():
    """Main function to run the music recommendation application"""
    print("🎵 Music Recommendation Using Facial Expressions 🎵")
    print("=" * 50)
    
    # Check if we're in WebContainer environment
    print("⚠️  Note: This application requires camera access and native Python modules")
    print("that are not available in the WebContainer environment.")
    print()
    print("To run this application properly, you would need to:")
    print("1. Download the project files to your local machine")
    print("2. Install Python 3.10+ with full standard library")
    print("3. Install the required dependencies: pip install -r requirements.txt")
    print("4. Run the application locally with camera access")
    print()
    
    # Show available interface options
    print("Available Interface Options:")
    print("1. CLI Mode - Terminal-based interface")
    print("2. Streamlit Web App - Browser-based interface") 
    print("3. PySimpleGUI Desktop App - Native desktop application")
    print()
    
    # Show project structure
    print("Project Structure:")
    try:
        base_path = "Music-Recommendation-Using-Facial-Expressions-contribution/Music-Recommendation-Using-Facial-Expressions-contribution"
        
        if os.path.exists(base_path):
            print(f"📁 Main project directory: {base_path}")
            
            # List key files
            key_files = [
                "code/ui_interfaces/cli_main.py",
                "code/ui_interfaces/app_local_streamlit.py", 
                "code/ui_interfaces/app_PySimpleGUI.py",
                "code/new_models/app_local_streamlit_ui_improved.py",
                "requirements.txt"
            ]
            
            for file_path in key_files:
                full_path = os.path.join(base_path, file_path)
                if os.path.exists(full_path):
                    print(f"  ✅ {file_path}")
                else:
                    print(f"  ❌ {file_path} (not found)")
        else:
            print(f"❌ Project directory not found: {base_path}")
            
    except Exception as e:
        print(f"Error checking project structure: {e}")
    
    print()
    print("For local execution, you would run one of these commands:")
    print("• python code/ui_interfaces/cli_main.py")
    print("• streamlit run code/ui_interfaces/app_local_streamlit.py")
    print("• python code/ui_interfaces/app_PySimpleGUI.py")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())