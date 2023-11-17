# parliament-agent
  It summarizes Italian parliamentary debates for efficient access to legislative insights in Italy.
  ## Installation
  To install all dependencies run :
  ```bash
    pip install -r requirements.txt
  ```
  # Configuration
  Please update necessary variables in .env file.
  ## Run
  You can run your application using the command
  ```bash
    uvicorn main:app --reload
  ```
  Access it at `http://localhost:7000` (HOST=localhost and PORT=7000 as defined in .env file)
  
