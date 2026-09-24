# Cybersecurity Projects

A collection of cybersecurity coursework and hands-on projects completed for school. This repository brings together systems programming exercises, operating-systems/security research, and web-application security demonstrations.

> **Educational use only:** The proof-of-concept files in this repository are intended for authorized labs, coursework, and controlled environments. Do not use them against systems or accounts without explicit permission.

## Repository Contents

```text
.
├── OSE/
│   └── Final Technical Report.pdf
├── Scripting/
│   ├── L6P1.c
│   └── L6P2.c
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

### `WebApp/`
Web-application security coursework, including the **ITSC-302 Final Project – Web Application Security Audit** report.

The `PoCs/` directory contains controlled HTML demonstrations of cross-site request forgery (CSRF) scenarios:

- **`CSRF_LockAccount.html`** submits a hidden request intended to demonstrate an account-locking action.
- **`CSRF_MILLIONAIR.html`** demonstrates how a deceptive link could trigger an unauthorized transfer request in a deliberately vulnerable training application.

## Languages

- **C** — file I/O, parsing, binary inspection, and formatted output
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

### Review the web-security materials

The PDF report can be opened with any PDF viewer. The HTML proof-of-concept files can be reviewed as source or opened only within an authorized, isolated lab environment configured for the related training application. The embedded endpoints are lab-specific and are not expected to work outside that environment.

## Learning Focus

This repository is intended to document practical experience with:

- Secure and defensive analysis of web applications
- CSRF attack mechanics and the importance of request validation and anti-CSRF protections
- File formats, magic numbers, hexadecimal inspection, and text/binary classification
- C file handling, parsing, output formatting, and error handling
- Technical reporting and communicating security findings

## Responsible Disclosure and Usage

Use these materials only for education, testing systems you own, or environments where you have written authorization. When adapting the examples, replace lab endpoints with local mock services and avoid real credentials, accounts, or financial systems.

## Author

**Abdul040722**

This repository will continue to grow as additional cybersecurity projects and school assignments are completed.
