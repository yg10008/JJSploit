def parsing_the_logFile(log_file_path):
    try:
        with open(log_file_path, 'r') as f:
            lines = f.readlines()

        with open('parsed.log', 'w') as output:  
            for line in lines:
                parts = line.strip().split(' / ')
                if len(parts) == 3:
                    timestamp, level, message = parts
                    if level in ['DEBUG', 'ERROR', 'CRITICAL']:
                        output.write(f"[{level}] at {timestamp}: {message}\n")
    except FileNotFoundError:
        print(f"File not found: {log_file_path}")
