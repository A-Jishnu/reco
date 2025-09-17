#!/usr/bin/env python3
"""
Music Recommendation Using Facial Expressions
Entry point script to run the application with different interface options
"""

import sys
import os
import subprocess

def main():
    print("🎵 Music Recommendation Using Facial Expressions 🎵")
    print("=" * 50)
    print("Choose an interface option:")
    print("1. CLI Mode (Terminal-based)")
    print("2. Streamlit Web App")
    print("3. PySimpleGUI Desktop App")
    print("4. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                print("\n🖥️  Starting CLI Mode...")
                subprocess.run([
                    sys.executable, 
                    "Music-Recommendation-Using-Facial-Expressions-contribution/Music-Recommendation-Using-Facial-Expressions-contribution/code/ui_interfaces/cli_main.py"
                ])
                break
                
            elif choice == "2":
                print("\n🌐 Starting Streamlit Web App...")
                subprocess.run([
                    "streamlit", "run",
                    "Music-Recommendation-Using-Facial-Expressions-contribution/Music-Recommendation-Using-Facial-Expressions-contribution/code/ui_interfaces/app_local_streamlit.py"
                ])
                break
                
            elif choice == "3":
                print("\n🖼️  Starting PySimpleGUI Desktop App...")
                subprocess.run([
                    sys.executable,
                    "Music-Recommendation-Using-Facial-Expressions-contribution/Music-Recommendation-Using-Facial-Expressions-contribution/code/ui_interfaces/app_PySimpleGUI.py"
                ])
                break
                
            elif choice == "4":
                print("👋 Goodbye!")
                sys.exit(0)
                
            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()