# FILE-INTEGRITY-CHECKER-
*Company*:- Codtech it solutions
*Name*:- Satish Shalse 
*Intern id*:- CTIS5896
*Domain*:- Cyber Security & Ethical Hacking 
*Duration*:- 4 weeks
*Mentor*:- Neela Santosh

*Description of given task*:- File Integrity Checker 

The File Integrity Checker is a security-focused tool developed using Python to monitor and detect changes in files within a specified directory. The primary objective of this tool is to ensure that files remain unaltered and secure by identifying any unauthorized modifications, deletions, or additions. This is achieved through the use of cryptographic hash functions, specifically the SHA-256 algorithm provided by Python’s built-in hashlib library.

In modern computing environments, maintaining the integrity of files is critical, especially in systems that store sensitive data such as configuration files, system logs, or user information. Even a small, unnoticed change in a file can lead to serious security vulnerabilities or system failures. Therefore, the File Integrity Checker acts as a protective mechanism by continuously verifying the consistency of files over time.

The working principle of this tool is based on the concept of hashing. A hash function takes an input (in this case, file content) and produces a fixed-length string known as a hash value or digest. This hash value acts like a digital fingerprint of the file. If the file content is altered even slightly, the resulting hash value changes significantly. This property makes hash functions highly effective for integrity verification.

The tool operates in two main phases: baseline creation and integrity verification. During the first phase, the user specifies a directory to monitor. The tool scans all files within this directory and calculates their SHA-256 hash values. These values are then stored in a file (commonly in JSON format) known as the baseline. This baseline serves as a reference point representing the original, trusted state of the files.

In the second phase, the tool performs integrity checks by recalculating the hash values of the current files in the directory and comparing them with the previously stored baseline values. Based on this comparison, the tool identifies three types of changes. If a file exists in both the baseline and the current scan but has a different hash value, it is marked as modified. If a file from the baseline is missing in the current scan, it is flagged as deleted. Conversely, if a file appears in the current scan but not in the baseline, it is identified as a new file.

The implementation of this tool uses Python’s os module to traverse directories and access file paths, while the hashlib module is used to compute secure hash values. The baseline data is stored and retrieved using the json module, ensuring easy readability and structured storage.

One of the key advantages of this File Integrity Checker is its simplicity and efficiency. It does not require any external dependencies beyond Python’s standard libraries, making it lightweight and easy to deploy. Additionally, it can be extended with advanced features such as real-time monitoring using file system watchers, logging mechanisms for audit trails, email notifications for alerts, and graphical user interfaces for better usability.

In conclusion, the File Integrity Checker is a practical and effective tool for ensuring data security and system reliability. By leveraging cryptographic hashing techniques, it provides a reliable way to detect unauthorized changes in files. This project demonstrates fundamental concepts of cybersecurity, file handling, and automation, making it highly valuable for learning and real-world applications.
