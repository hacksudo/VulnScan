import os
import sys
import subprocess
import platform
import time

def run_cmd(cmd, check=True):
    print(f"[*] Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if check and result.returncode != 0:
        print(f"[!] Command failed: {cmd}")
        sys.exit(1)
    return result.returncode

def check_docker():
    print("[*] Checking if Docker is installed...")
    if subprocess.run("which docker", shell=True, capture_output=True).returncode != 0:
        print("[!] Docker is not installed! Please install Docker.")
        sys.exit(1)
    print("[+] Docker is installed.")

def ensure_daemon():
    print("[*] Checking if Docker daemon is running...")
    if subprocess.run("docker info", shell=True, capture_output=True).returncode == 0:
        print("[+] Docker daemon is already running.")
        return

    sys_platform = platform.system()
    if sys_platform == 'Darwin': # macOS
        print("[*] macOS detected. Checking for Colima...")
        if subprocess.run("which colima", shell=True, capture_output=True).returncode == 0:
            print("[*] Starting Colima...")
            run_cmd("colima start", check=False)
            time.sleep(2)
        else:
            print("[!] Docker daemon is not running and Colima is not installed.")
            print("[!] Please start Docker Desktop or install Colima (brew install colima).")
            sys.exit(1)
    elif sys_platform == 'Linux':
        print("[*] Linux detected. Trying to start docker service...")
        run_cmd("sudo systemctl start docker", check=False)
    
    # Wait for daemon
    for _ in range(15):
        if subprocess.run("docker info", shell=True, capture_output=True).returncode == 0:
            print("[+] Docker daemon is now running.")
            return
        time.sleep(1)
    
    print("[!] Failed to connect to Docker daemon. Please start Docker manually.")
    sys.exit(1)

def main():
    print("========================================")
    print(" Hacksudo VulnScan - Universal Deployer")
    print("========================================")
    
    check_docker()
    ensure_daemon()
    
    tar_file = "hacksudo-vulnscan.tar"
    if not os.path.exists(tar_file):
        print(f"[!] Error: {tar_file} not found in the current directory.")
        print("[!] Please make sure deploy_vulnscan.py and hacksudo-vulnscan.tar are in the same folder.")
        sys.exit(1)
        
    print(f"\n[*] Loading Docker image from {tar_file}...")
    run_cmd(f"docker load -i {tar_file}")
    
    print("\n[*] Checking for existing container 'hacksudo-vulnscan-app'...")
    existing = subprocess.run("docker ps -aq -f name=hacksudo-vulnscan-app", shell=True, capture_output=True, text=True).stdout.strip()
    if existing:
        print("[*] Found existing container. Removing it to deploy the new one...")
        run_cmd("docker rm -f hacksudo-vulnscan-app")
        
    print("\n[*] Starting new container...")
    run_cmd("docker run -d --name hacksudo-vulnscan-app -p 3000:3000 -p 8080:8080 hacksudo-vulnscan:latest")
    
    print("\n========================================")
    print(" [SUCCESS] Hacksudo VulnScan is running!")
    print(" -> Web UI:    http://localhost:3000")
    print(" -> Proxy:     http://localhost:8080")
    print("\n [MANAGEMENT]")
    print(" -> To stop:   docker stop hacksudo-vulnscan-app")
    print(" -> To remove: docker rm -f hacksudo-vulnscan-app")
    print("========================================\n")

if __name__ == "__main__":
    main()
