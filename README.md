# Banking App Testing Repository

This repository contains the testing assets for a simple web-based banking application. It is structured to organize test cases, bug reports, exploratory testing findings, and automation scripts in a clear and accessible manner.

## Repository Structure

The repository is organized into the following folders:

### 1. `/Test_Cases/`
Contains detailed test cases for each feature of the application. These test cases cover positive, negative, and edge cases to ensure thorough testing.

- **User_Login_Test_Cases.md:** Test cases for the user login functionality.
- **View_Account_Balance_Test_Cases.md:** Test cases for viewing account balances.
- **Money_Transfer_Test_Cases.md:** Test cases for transferring money between accounts.
- **View_Transaction_History_Test_Cases.md:** Test cases for viewing transaction history.

### 2. `/Bug_Reports/`
Contains detailed bug reports for any identified issues. Each report includes a description, steps to reproduce, expected vs. actual results, severity, and priority.

- **Bug_Report_001.md:** Report on negative balance display issue.
- **Bug_Report_002.md:** Report on money transfer page freezing.
- **Bug_Report_003.md:** Report on logout functionality issues.

### 3. `/Exploratory_Testing/`
Summarizes the findings from exploratory testing. This includes usability, security, performance, and edge case testing results.

- **Exploratory_Testing_Report.md:** Summary of issues found during exploratory testing with suggestions for improvements.

### 4. `/Automation/`
Contains automation scripts for testing certain functionalities, along with documentation on how to run them.

- **login_test.py:** A Selenium script to automate the login functionality.
- **README.md:** Instructions on setting up the environment and running the automation script.

## Getting Started

### Viewing Test Cases
Navigate to the `Test_Cases` folder to view the detailed test cases for each feature.

### Reviewing Bug Reports
Check the `Bug_Reports` folder for detailed reports on identified bugs.

### Exploratory Testing Insights
The `Exploratory_Testing` folder contains a summary of the exploratory testing conducted on the application.

### Running Automation Scripts
The `Automation` folder contains scripts for automating specific tests. Refer to the `README.md` in the `Automation` folder for instructions on how to run the scripts.
## Tools Used for Testing

### 1. **Manual Testing**
   - **Tools:** Excel or Google Sheets for documenting test cases and results.
   - **Purpose:** To manually verify the functionality of the application by following the test cases.

### 2. **Bug Tracking**
   - **Tools:** JIRA, Bugzilla, or GitHub Issues.
   - **Purpose:** To log, track, and manage bugs found during testing.

### 3. **Automation Testing**
   - **Tools:** Selenium WebDriver with Python.
   - **Purpose:** To automate the testing of the login functionality and potentially other repetitive tasks.

### 4. **Exploratory Testing**
   - **Tools:** The application itself, along with any required browser developer tools (e.g., Chrome DevTools) for inspecting elements, checking console errors, etc.
   - **Purpose:** To explore the application and identify usability, security, and performance issues without predefined test cases.

### 5. **Performance Testing (Optional)**
   - **Tools:** JMeter, LoadRunner, or browser-based performance profiling tools.
   - **Purpose:** To test the application’s response time under normal and heavy load conditions.

### 6. **Security Testing (Optional)**
   - **Tools:** OWASP ZAP, Burp Suite, or any browser security plugins.
   - **Purpose:** To identify potential security vulnerabilities in the application.

## Contributing

If you would like to contribute to this repository, please fork the repository and submit a pull request with your changes. Make sure to follow the existing structure and provide detailed descriptions for any new test cases or bug reports.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for more information.



