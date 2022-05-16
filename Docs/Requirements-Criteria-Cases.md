## Requirements

### **Software Requirements**.
#### **Functional Requirements**
* The system must convert Arabic numbers to roman numbers.
* The system must ask to an Arabic Number.
* The system must show the Roman number as the requested Arabic one.
#### **Non-functional Requirements**.
##### **Performance requirements**.
* The system must run in an interval of [0.001, 1.5] seconds.
* The console must bear Roman characters.
##### **Reliability Requirements**.
* The system must be built as a university work requirement.
##### **Usability Requirements**.
* The system must be coded in a console program context.
##### **Maintainability Requirements**.
* The system must be uploaded to GitHub due to possible future upgrades or modifications.
## **Test cases**
### **Unit tests**
* Test case 1: check invalid input number.
* Test case 2: check valid input number.
* Test case 3: check out range Arabic input number.
* Test case 4: check in range Arabic input number.
### **End-To-End tests**
* Test case 5: check happy party program flow.
* Test case 6: check entire program with an error in the input range.
* Test case 7: check entire program with an error in the input format (not an Arabic number).
## **Acceptance Criteria**
### **Basic Acceptance Criteria**
* The user needs to localize cursor to the correct space to type an Arabic number.
* The user needs to indicate when the program stops, following the format well indicated in the console.
* The system should indicated correctly the step-by-step user experience.
### **Scenarios**
#### **Scenario: Valid number**
* Given: The user navigates to the program file location.
* When: The user runs the program.
* Add: Enters a valid input.
* Then: The system converts the Arabic number to a Roman number. 
* When: The system conversion is ready.
* Then: The user sees the appropriate conversion in his console.
	
#### **Scenario: Invalid number**
* Given: The user navigates to the program file location.
* When: The user runs the program.
* Add: Enters an invalid input.
* Then: The system validates input given is incorrect. 
* When: The system validation is ready.
* Then: The user sees a message in his console indication the given input is invalid.



