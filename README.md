Here is your updated `README.md` with the new TLS Client-Server project seamlessly integrated. I have added a new directory (`socket_programming/`), updated the repository tree, added a section explaining the project, and updated the languages, getting started, and learning focus sections to match your existing style.


# Cybersecurity Projects

A collection of cybersecurity coursework and hands-on projects completed for school. This repository brings together systems programming exercises, operating-systems/security research, network security applications, and web-application security demonstrations.

> **Educational use only:** The proof-of-concept files in this repository are intended for authorized labs, coursework, and controlled environments. Do not use them against systems or accounts without explicit permission.

## Repository Contents

```text
.
├── OSE/
│   └── Final Technical Report.pdf
├── Scripting/
│   ├── L6P1.c
│   └── L6P2.c
├── socket_programming/
│   ├── generate_cert.py
│   ├── tls_chat_client.py
│   ├── tls_chat_server.py
│   └── Building TLS Client-Server Applications with Sockets.pdf
├── WebApp/
│   ├── ITSC-302 Final Project – Web Application Security Audit.pdf
│   └── PoCs/
│       ├── CSRF_LockAccount.html
│       └── CSRF_MILLIONAIR.html
└── README.md
```

### `OSE/`
Operating-systems/security coursework documentation. The directory currently contains the **Final Technical Report** in PDF format.

### `Scripting/`
C programming exercises focused on file processing and binary analysis:

- **`L6P1.c`** reads grade-style records from `numbers.txt`, separates values into `below60.txt` and `above60.txt`, and prints processing totals.
- **`L6P2.c`** produces a hexadecimal/character view of a file, reports its first four bytes as a magic number, and estimates whether the file is text or binary based on printable ASCII content.

### `TLS_Chat/`
A multi-threaded, encrypted client-server messaging application built in Python. This project demonstrates the practical implementation of TLS over TCP sockets.

- **`generate_cert.py`** uses the `cryptography` library to generate a self-signed RSA 2048-bit private key (`server.key`) and X.509 certificate (`server.crt`).
- **`tls_chat_server.py`** establishes a TLS-wrapped socket, manages concurrent clients via threading, and routes encrypted messages based on a username dictionary.
- **`tls_chat_client.py`** wraps a raw TCP socket in a TLS context, handles user input, and continuously listens for incoming encrypted messages on a separate thread.
- **`TLS_Chat_Report.pdf`** contains a detailed step-by-step explanation of the interaction, Wireshark packet captures of the TLS handshake, and an analysis of the security trade-offs between TCP and TLS.

*Note: The client is configured with `verify_mode = ssl.CERT_NONE` for local testing with self-signed certificates. See the report for a discussion on enabling full certificate verification in production.*

### `WebApp/`
Web-application security coursework, including the **ITSC-302 Final Project – Web Application Security Audit** report.

The `PoCs/` directory contains controlled HTML demonstrations of cross-site request forgery (CSRF) scenarios:

- **`CSRF_LockAccount.html`** submits a hidden request intended to demonstrate an account-locking action.
- **`CSRF_MILLIONAIR.html`** demonstrates how a deceptive link could trigger an unauthorized transfer request in a deliberately vulnerable training application.

## Languages

- **C** — file I/O, parsing, binary inspection, and formatted output
- **Python** — socket programming, multithreading, TLS/SSL encryption, and cryptography
- **HTML** — web-security proof-of-concept pages

## Getting Started

Clone the repository and move into the project directory:

```bash
git clone https://github.com/Abdul040722/Cybersecurity-Projects.git
cd Cybersecurity-Projects
```

### Compile the C exercises

A C compiler such as GCC or Clang is required:

```bash
gcc Scripting/L6P1.c -o Scripting/L6P1
gcc Scripting/L6P2.c -o Scripting/L6P2
```

Run the grade-processing exercise from a directory containing a compatible `numbers.txt` file. It creates or overwrites `below60.txt` and `above60.txt` in the current working directory:

```bash
cd Scripting
./L6P1
```

Run the file-inspection exercise and provide the path to a file when prompted:

```bash
./L6P2
```

### Run the Python TLS Chat Application

A Python 3 environment is required. Install the necessary cryptography library:

```bash
pip install cryptography
```

Navigate to the TLS_Chat directory, generate the self-signed certificate, and start the server:

```bash
cd TLS_Chat
python generate_cert.py
python tls_chat_server.py
```

In a separate terminal, start the client and register a username:

```bash
cd TLS_Chat
python tls_chat_client.py
```

To test the direct messaging, open a third terminal and run the client again with a different username. Send a message using the format `recipient_username: message`.

### Review the web-security materials

The PDF report can be opened with any PDF viewer. The HTML proof-of-concept files can be reviewed as source or opened only within an authorized, isolated lab environment configured for the related training application. The embedded endpoints are lab-specific and are not expected to work outside that environment.

## Learning Focus

This repository is intended to document practical experience with:

- Secure and defensive analysis of web applications
- CSRF attack mechanics and the importance of request validation and anti-CSRF protections
- File formats, magic numbers, hexadecimal inspection, and text/binary classification
- C file handling, parsing, output formatting, and error handling
- Network socket programming, multithreading, and concurrency control
- TLS handshakes, X.509 certificate generation, and encrypted data transport
- Packet analysis using Wireshark for both plaintext (TCP) and encrypted (TLS) traffic
- Technical reporting and communicating security findings

## Responsible Disclosure and Usage

Use these materials only for education, testing systems you own, or environments where you have written authorization. When adapting the examples, replace lab endpoints with local mock services and avoid real credentials, accounts, or financial systems. The TLS chat application uses self-signed certificates for educational purposes and intentionally disables strict certificate verification; do not deploy this configuration in a production environment.

## Author

**Abdul040722**

This repository will continue to grow as additional cybersecurity projects and school assignments are completed.
