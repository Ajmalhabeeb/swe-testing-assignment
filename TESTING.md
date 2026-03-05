Testing Strategy for Quick-Calc



This document explains the testing approach used for the Quick-Calc calculator application. The purpose of the testing strategy is to ensure that the calculator performs arithmetic operations correctly, handles unusual inputs safely, and that the graphical interface works properly with the underlying calculation logic.



The testing approach used in this project includes both unit testing and integration testing. This multi-layered strategy helps verify the correctness of individual components as well as the interaction between different parts of the application.



Testing Strategy



The Quick-Calc application was tested using two main types of testing: unit testing and integration testing.



Unit testing focuses on verifying that individual functions work correctly in isolation. In this project, the calculation logic located in core.py was tested using several unit tests. These tests verify that each arithmetic operation returns the correct result. The following operations were tested: addition, subtraction, multiplication, and division.



Edge cases were also included to ensure the application behaves correctly in unusual situations. Examples of edge cases tested include division by zero, negative numbers, decimal numbers, and very large numbers. Testing these cases ensures the calculator remains stable and reliable even when unexpected input values are provided.



Integration testing verifies that different parts of the system work together correctly. In this project, integration tests were used to confirm that the graphical user interface interacts properly with the calculation logic. Instead of manually clicking buttons, the tests simulate user input through the application interface.



For example, one integration test simulates a user entering “5 + 3 =” and verifies that the result shown on the calculator display is “8”. Another integration test verifies that pressing the Clear button after performing a calculation resets the display to “0”. These tests ensure that the interface and calculation engine function together correctly.



Lecture Concepts Applied



The testing strategy implemented in this project reflects several key software testing concepts discussed in Lecture 3.



The first concept is the Testing Pyramid. The test suite follows the pyramid structure where the majority of tests are unit tests and a smaller number are integration tests. In this project there are eight unit tests and two integration tests. Unit tests are faster and easier to run, which makes them ideal for testing small pieces of logic. Integration tests are fewer in number but ensure that the system components work together correctly.



Another concept applied is the difference between black-box testing and white-box testing. Unit tests in this project are considered white-box tests because they test the internal calculation functions directly and are written with knowledge of how the code works internally. Integration tests represent black-box testing because they simulate user interactions with the system without focusing on the internal implementation details.



Functional testing is also demonstrated in this project. The main goal of functional testing is to verify that the software behaves according to its expected functionality. The tests confirm that the calculator performs arithmetic operations correctly, handles division by zero safely, and resets the display properly when the Clear button is pressed. Non-functional aspects such as performance or usability design were not tested in this project because the assignment focuses mainly on verifying functional correctness.



Regression testing is another important concept supported by this test suite. Regression testing ensures that previously working features continue to function after changes are made to the code. Because the tests are automated, they can be executed quickly using a single command. If future modifications introduce a bug, the tests will fail and alert the developer that a previously working feature has broken. This helps maintain the reliability of the software over time.



Test Results Summary



The following  summarises the tests included in the project and their results.



Test Name: test\_addition  

Type: Unit Test  

Result: Pass



Test Name: test\_subtraction  

Type: Unit Test  

Result: Pass



Test Name: test\_multiplication  

Type: Unit Test  

Result: Pass



Test Name: test\_division  

Type: Unit Test  

Result: Pass



Test Name: test\_division\_by\_zero  

Type: Unit Test  

Result: Pass



Test Name: test\_negative\_numbers  

Type: Unit Test  

Result: Pass



Test Name: test\_decimal\_numbers  

Type: Unit Test  

Result: Pass



Test Name: test\_large\_numbers  

Type: Unit Test  

Result: Pass



Test Name: test\_full\_user\_interaction\_addition  

Type: Integration Test  

Result: Pass



Test Name: test\_clear\_resets\_display  

Type: Integration Test  

Result: Pass



All tests passed successfully when the test suite was executed.



Running the Tests



All tests in the project can be executed using the following command:



python -m pytest



This command runs both the unit tests and the integration tests and provides a summary of the results.

