import sqlite3
import os

# ---------- 1. SQL Injection ----------
def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # ❌ Vulnerable: SQL Injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# ---------- 2. Command Injection ----------
def ping_server(host):
    # ❌ Vulnerable: Command Injection
    os.system(f"ping -c 1 {host}")

# ---------- 3. Hardcoded Credentials ----------
def connect_to_service():
    # ❌ Vulnerable: Hardcoded credentials
    username = "admin"
    password = "12345"
    print(f"Connecting to service with username={username} and password={password}")
    # ... connection logic ...

# ----------- Example Usage -----------
if __name__ == "__main__":
    # SQL Injection Example
    print("[SQLi] Login attempt")
    print(login("' OR '1'='1", "anything"))  # bypass authentication

    # Command Injection Example
    print("[Command Injection] Pinging host")
    ping_server("127.0.0.1; echo HACKED")

    # Hardcoded credentials Example
    print("[Hardcoded Credentials]")
    connect_to_service()
