# 🛡️ Hacksudo VulnScan

**Hacksudo VulnScan** is a powerful, containerized **Web Vulnerability Assessment and Security Testing platform** designed for penetration testers, security researchers, and cybersecurity professionals.

It combines an easy-to-use web dashboard with industry-standard security tools such as **Nmap, Nikto, SSLScan, and TestSSL.sh**, along with built-in HTTP interception and request-analysis capabilities.

The complete application can be deployed using a **pre-built Docker image**, making installation fast and eliminating the need to manually build the application or install individual security tools.

🔗 **GitHub Repository:**
https://github.com/hacksudo/VulnScan

---

# ✨ Features

* 🐳 Fully containerized Docker deployment
* 🌐 Web-based security testing dashboard
* 🎯 Target management
* 🕷️ Automated web vulnerability scanning
* 🔍 Nmap port and service discovery
* 🛡️ Nikto web server scanning
* 🔒 SSL/TLS security analysis
* 🔁 HTTP/HTTPS interception proxy
* 🚀 Intruder-style automated payload testing
* 🔄 Repeater for manual HTTP request manipulation
* 🕵️ Technology detection
* 🔑 JWT and token analysis
* 🍪 Cookie security analysis
* 🛡️ HTTP security header analysis
* 🧩 Encoding/decoding utilities
* 🎣 CSRF Proof-of-Concept generation
* 🌐 CORS testing
* 🏠 Host Header testing
* 🔗 Collaborator/OAST support
* 📊 Global vulnerability analytics
* 👤 User-specific scan tracking
* 🗄️ Pre-seeded SQLite database
* ⚡ Offline Docker image deployment

---

# 🧭 Navigation Buttons & Features

## 🏠 Dashboard — Global Analytics

Provides a bird's-eye view of vulnerabilities detected across scans and targets.

### Highlights

* Interactive vulnerability charts
* Severity breakdown
* Critical / High / Medium / Low statistics
* Scan activity overview
* Target statistics
* User-specific tracking

---

## 🎯 Target

Allows users to define and manage the URLs, domains, and IP addresses they want to test.

### Highlights

* Add and manage targets
* Organize testing scope
* Reuse previously configured targets
* Run security tools against specific targets
* Avoid repeatedly entering target URLs

---

## 🕷️ Web Scanner

The primary automated vulnerability scanning module.

### Highlights

The scanner integrates security tools such as:

* Nmap
* Nikto
* Web reconnaissance components

It can assist with identifying:

* Open ports
* Running services
* Outdated servers
* Known vulnerabilities
* Common web-server misconfigurations
* Potential CVEs
* Exposed services

---

## 🔒 SSL Scan

Provides dedicated SSL/TLS security analysis.

### Powered By

* `sslscan`
* `testssl.sh`

### Highlights

Checks for security issues such as:

* Obsolete TLS versions
* TLS 1.0 / TLS 1.1
* Weak cipher suites
* Certificate issues
* Certificate expiration
* Heartbleed
* Ticketbleed
* Cryptographic configuration weaknesses

---

## 🔁 Proxy

An HTTP/HTTPS interception proxy designed for interactive web application testing.

### Highlights

* Capture HTTP/HTTPS traffic
* Inspect request and response headers
* Modify requests
* Modify parameters
* Modify payloads
* Inspect cookies
* Forward modified requests
* Analyze captured traffic

The workflow is similar to an intercepting proxy used during professional web application penetration testing.

---

## 🚀 Intruder

Automated payload injection and fuzzing functionality.

### Highlights

Capture a request and select a parameter to test with a wordlist or payload set.

Useful for authorized testing of:

* SQL Injection
* XSS
* Input validation
* Authentication parameters
* Parameter manipulation
* Fuzzing scenarios

---

## 🔄 Repeater

Manual HTTP request manipulation and replay functionality.

### Highlights

* Send captured requests to Repeater
* Modify headers
* Modify cookies
* Modify request body
* Modify parameters
* Replay requests
* Compare server responses

This is useful when manually validating application behavior and vulnerability findings.

---

## ⚙️ Settings

Provides account and application configuration functionality.

---

## 🚪 Logout

Safely terminates the current application session and returns the user to the login screen.

---

# 🧠 Built-in Analyzer Modules

When a request is captured through the **Interceptor/Proxy**, additional analysis modules become available.

---

## 🕵️‍♂️ Tech Analyzer

Automatically analyzes the target's technology stack.

### Can help identify

* Web server technologies
* Frameworks
* Application technologies
* Technology versions exposed through headers
* Potentially outdated components

Example technologies may include:

```text
PHP
IIS
ASP.NET
Nginx
Apache
Node.js
```

---

## 🔑 Token Analyzer

Analyzes tokens found in intercepted requests.

### Highlights

* Detect JWT tokens
* Decode JWT payloads
* Inspect token structure
* Identify signature algorithms
* Analyze token claims
* Inspect session-token patterns

> Token decoding does not automatically mean a token is vulnerable. Security findings should be validated against the application's actual authentication controls.

---

## 🍪 Cookie Analyzer

Analyzes cookies present in intercepted HTTP requests/responses.

### Checks for

* `HttpOnly`
* `Secure`
* `SameSite`
* Session cookie configuration
* Potential session-management weaknesses

This helps identify cookie configurations that may increase session-related security risks.

---

## 🛡️ Header Checker

Audits HTTP security headers.

### Examples

```text
Strict-Transport-Security
Content-Security-Policy
X-Frame-Options
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
```

The module identifies missing or potentially weak security protections.

---

## 🧩 Smart Decoder

Provides quick encoding and decoding functionality directly from intercepted requests.

### Supported formats

* Base64
* URL Encoding
* Hex
* HTML Encoding

Example:

```text
Encoded Data
     ↓
Smart Decoder
     ↓
Decoded Value
```

It can also be used to encode modified values before sending a request.

---

## 🎣 CSRF PoC Generator

Generates an HTML Proof of Concept from a captured request to assist with authorized CSRF testing.

The generated PoC can be used in a controlled testing environment to determine whether a request is susceptible to Cross-Site Request Forgery.

---

## 🌐 CORS Tester

Tests Cross-Origin Resource Sharing configurations by sending controlled `Origin` headers.

### Helps assess

* Allowed origins
* Origin reflection
* CORS configuration
* Credential-related CORS behavior
* Potential cross-origin security weaknesses

---

## 🏠 Host Header Injector

Provides quick testing of Host Header behavior.

### Supports headers such as

```http
Host:
X-Forwarded-Host:
```

Useful for authorized testing of potential:

* Host Header Injection
* Host Header Poisoning
* Proxy trust issues
* Routing inconsistencies

---

## 🔗 Collaborator / OAST

Supports out-of-band security testing using external interaction endpoints.

This functionality can assist with identifying blind vulnerabilities such as:

* Blind SSRF
* Blind command execution
* Out-of-band interactions

> Use only OAST endpoints and infrastructure that you are authorized to use.

---

## 🔒 SSL/TLS Scanner

Launches a dedicated SSL/TLS security scan against the intercepted target.

Powered by:

```text
testssl.sh
```

Can assist with identifying:

* Weak cipher suites
* Deprecated protocols
* TLS configuration issues
* Certificate problems
* Heartbleed-related exposure

---

## 🗺️ Nmap Port Scanner

Provides one-click Nmap scanning against an authorized target.

Can identify:

* Open ports
* Services
* Service versions
* Network exposure
* Available protocols

Example underlying tool:

```bash
nmap
```

---

## 🕷️ Nikto Web Scanner

Provides one-click Nikto scanning against an authorized web target.

Can help identify:

* Default files
* Known web-server issues
* Outdated server software
* Common web-server misconfigurations
* Potentially exposed resources

Example underlying tool:

```bash
nikto
```

---

# 🏗️ Architecture

```text
                    ┌──────────────────────────┐
                    │     Web Browser          │
                    │                          │
                    │  Hacksudo VulnScan UI    │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │    VulnScan Application  │
                    │                          │
                    │ Dashboard / Target       │
                    │ Proxy / Scanner          │
                    │ Intruder / Repeater      │
                    └────────────┬─────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
          ┌────────┐         ┌────────┐        ┌──────────┐
          │  Nmap  │         │ Nikto  │        │ SSLScan  │
          └────────┘         └────────┘        └──────────┘
                                                    │
                                                    ▼
                                               ┌──────────┐
                                               │TestSSL.sh│
                                               └──────────┘

                         ┌─────────────────┐
                         │ SQLite Database  │
                         └─────────────────┘
```

---

# 📦 Quick Install via Release

The recommended installation method is to download the pre-built release package.

The release contains:

* Pre-built Docker image
* Application
* Security tools
* Database
* Deployment script

**You do not need to build the Docker image from source.**

---

# 🚀 Step 1 — Download the Release

Go to the GitHub Releases page:

**https://github.com/hacksudo/VulnScan/releases**

Download the latest:

```text
finalhacksudoscan.zip
```

---

# 📂 Step 2 — Extract the Release

Extract the ZIP file:

```bash
unzip finalhacksudoscan.zip
```

Enter the extracted directory:

```bash
cd finalhacksudoscan
```

---

# 🐳 Step 3 — Deploy

Run the automated deployment script:

```bash
python3 deploy_vulnscan.py
```

The deployment script automatically:

1. Checks the Docker environment
2. Verifies that Docker is running
3. Loads the offline Docker `.tar` image
4. Creates the VulnScan container
5. Starts the application

---

# 🌐 Step 4 — Access the Dashboard

After successful deployment, open:

```text
http://localhost:3000
```

You should now see the **Hacksudo VulnScan login/dashboard interface**.

---

# ⚙️ Prerequisites

Before deployment, install:

* Python 3.x
* Docker

### Windows

Install Docker Desktop and make sure Docker is running.

### macOS

You can use either:

* Docker Desktop
* Colima

For Colima:

```bash
colima start
```

Verify Docker:

```bash
docker --version
```

Verify the Docker daemon:

```bash
docker ps
```

---

# 🛠️ Server Management

The included deployment script provides simple container-management commands.

## 🛑 Stop the Server

```bash
python3 deploy_vulnscan.py stop
```

---

## 🗑️ Remove the Container

```bash
python3 deploy_vulnscan.py remove
```

> **Note:** Removing the container does not delete the Docker image from your local Docker cache.

---

# 🔍 Included Security Tools

| Tool           | Purpose                             |
| -------------- | ----------------------------------- |
| **Nmap**       | Port, service and network discovery |
| **Nikto**      | Web server vulnerability scanning   |
| **SSLScan**    | SSL/TLS configuration analysis      |
| **TestSSL.sh** | Advanced SSL/TLS security testing   |

---

# 🗄️ Embedded Database

The pre-built Docker image contains a pre-seeded SQLite database.

This means the application does not require a separate database server or database download during deployment.

The release is designed to minimize setup requirements and provide a ready-to-run environment.

---

# 📁 Release Package Structure

A typical release package contains:

```text
finalhacksudoscan/
│
├── deploy_vulnscan.py
├── hacksudo-vulnscan.tar
└── ...
```

### `deploy_vulnscan.py`

Automates:

* Docker verification
* Docker image loading
* Container creation
* Application startup
* Container management

### `hacksudo-vulnscan.tar`

Contains the pre-built Docker image with the application environment and required security tooling.

---

# 🔄 Common Commands

### Deploy

```bash
python3 deploy_vulnscan.py
```

### Stop

```bash
python3 deploy_vulnscan.py stop
```

### Remove

```bash
python3 deploy_vulnscan.py remove
```

### Check Running Containers

```bash
docker ps
```

### Check Docker Images

```bash
docker images
```

---

# 🔐 Security Testing Workflow

A typical authorized assessment workflow can look like:

```text
        Target
          │
          ▼
   ┌─────────────┐
   │    Target   │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │ Web Scanner │
   └──────┬──────┘
          │
     ┌────┴────┐
     ▼         ▼
   Nmap      Nikto
     │         │
     └────┬────┘
          ▼
    SSL/TLS Scan
          │
          ▼
      Proxy / Interceptor
          │
    ┌─────┼───────────────┐
    ▼     ▼       ▼       ▼
  Token Cookie  Header   Tech
 Analyzer Analyzer Checker Analyzer
    │
    ▼
 Intruder / Repeater
    │
    ▼
 Vulnerability Validation
    │
    ▼
 Dashboard & Reports
```

---

# 📊 Vulnerability Dashboard

The dashboard provides centralized visibility into security testing activity.

Example severity categories:

```text
Critical
High
Medium
Low
Informational
```

Users can review findings across multiple targets and scans from a centralized interface.

---

# 🎯 Supported Testing Areas

Hacksudo VulnScan can assist with authorized testing of areas including:

* Web application security
* Network exposure
* Port and service discovery
* SSL/TLS configuration
* HTTP security headers
* Cookie security
* JWT/token analysis
* CORS configuration
* Host Header behavior
* CSRF testing
* Technology fingerprinting
* Web-server configuration
* Input fuzzing
* Manual request manipulation
* Out-of-band testing

---

# ⚠️ Responsible Use

Hacksudo VulnScan is intended for **authorized security testing and security research only**.

Use this tool only against:

* Systems you own
* Applications you are authorized to test
* Dedicated penetration-testing environments
* CTF/lab environments
* Security research environments where testing is explicitly permitted

**Do not scan or attack systems without authorization.**

The user is responsible for ensuring that all testing performed with Hacksudo VulnScan complies with applicable laws, regulations, contracts, and authorization requirements.

---

# 🔗 Links

### GitHub Repository

https://github.com/hacksudo/VulnScan

### Releases

https://github.com/hacksudo/VulnScan/releases

---

# 👨‍💻 Hacksudo

**Hacksudo — Learn. Build. Hack. Secure.**

Built for penetration testers, cybersecurity professionals, security researchers, and cybersecurity learners.
