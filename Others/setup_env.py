import subprocess
import sys
import os

def create_virtualenv(env_name):
    if not os.path.exists(env_name):
        print(f"Creating virtual environment '{env_name}'...")
        subprocess.check_call([sys.executable, '-m', 'venv', env_name])
    else:
        print(f"Virtual environment '{env_name}' already exists.")

def install_requirements(env_name, requirements_file):
    pip_executable = os.path.join(env_name, 'Scripts', 'pip') if os.name == 'nt' else os.path.join(env_name, 'bin', 'pip')
    
    print(f"Installing packages from {requirements_file}...")
    subprocess.check_call([pip_executable, 'install', '-r', requirements_file])

def main():
    env_name = 'venv'
    requirements_file = 'requirements.txt'
    
    create_virtualenv(env_name)
    install_requirements(env_name, requirements_file)
    print("Setup complete!")

if __name__ == "__main__":
    main()
