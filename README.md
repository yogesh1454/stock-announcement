# Virtual Environment
## Create a new virtual environment
Go to your project’s directory and run the following command. This will create a new virtual environment in a local folder named .venv:

> python3 -m venv .venv

## Activate a virtual environment
Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

>Mac: source .venv/bin/activate
> Window: source .venv/Scripts/activate

## Verify
To confirm the virtual environment is activated, check the location of your Python interpreter:

`which python`
> .venv/bin/python

## Deactivate a virtual environment
> deactivate


# Prepare pip
python3 -m pip install --upgrade pip
python3 -m pip --version

# PIP Install Depended Modules
>pip install -r requirements.txt -t .
>pip install -r requirements.txt

# Run Python script

full_memory_file_path ='/d/ws/stock-announcement/data/memory-stock-events.txt'
>python3 corporate_announcements.py <telegram_chat_id> <full_memory_file_path>

# Window Activate a virtual environment

