from src.utils.temp_db import temp_data


def is_execution_abort():
  if not temp_data["isExecutionContinue"]:
    print("Abort due to request")
    raise SystemExit(0)
