import os 

ERROR_KEYWORDS = ["ERROR", "WARN", "EXCEPTION", "TRACEBACK","TIMEOUT", "FAILED", "FAILURE"]

SUPPORTED_EXTENSIONS = (".log", ".txt",".py",".js",".java",".rb")

def scan_repo(repo_path: str):
    """
    Scan a repository and extracts error related log lines 
    """

    collected_logs = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(SUPPORTED_EXTENSIONS):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", errors="ignore") as f:
                        for line in f:
                            if any(keyword in line for keyword in ERROR_KEYWORDS):
                                enriched_log = f"{file_path}: {line.strip()}"
                                collected_logs.append(enriched_log)
                except Exception as e:
                    # in=gnore unreadable files
                    print(f"⚠️ Could not read file {file_path}: {e}")
                    continue 

    return collected_logs
