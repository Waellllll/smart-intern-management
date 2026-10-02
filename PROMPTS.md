# Prompt Engineering Dossier

## 1. Ideation
Act as a software architect and Prompt Engineering instructor. Propose web application ideas suitable for a 3-student university project. Each must have a modern frontend, REST backend, relational database and AI feature.

## 2. Architecture
We selected Smart Internship Hub. Design a manageable architecture using Angular, Spring Boot REST, MySQL and Python FastAPI. Explain responsibilities and data flow.

## 3. Requirements
Act as a senior requirements engineer. Generate functional and non-functional requirements for students, companies, supervisors and administrators. Separate MVP from future features.

## 4. Database
Design a MySQL schema for students, companies, offers, applications and evaluations. Give keys, relationships and constraints.

## 5. Spring Boot API
Act as a senior Java developer. Generate a Java 17 Spring Boot REST API using Controller, Service, Repository and Entity layers, with JSON examples and validation.

## 6. Angular
Act as a senior Angular developer. Create a responsive Angular frontend consuming the Spring Boot REST API. Include dashboard, students, offers and AI recommendations.

## 7. Python AI
Act as a Python AI engineer. Create a FastAPI POST /recommend endpoint receiving a student and offers and returning offer ID, score 0-100 and explanation.

## 8. Explainable recommendation
Design an explainable baseline: 70 points for skill overlap and 30 for preferred-domain match. Tokenize skills robustly, sort by score and explain limitations.

## 9. Java/Python integration
Implement Spring Boot communication with FastAPI using an HTTP client. Include error handling when the AI service is unavailable.

## 10. Testing
Generate tests for REST endpoints, validation, empty skills, no matching skills and unavailable AI service.

## 11. Prompt refinement
Weak prompt: “Create an AI recommendation system.” Improve it using role, context, inputs, constraints, output schema, edge cases and evaluation criteria.

## 12. Code review
Review the supplied project as a senior developer. Report only bugs and risks supported by the code, with severity and fixes.

## 13. Security
Extend the project with JWT authentication and role-based authorization for STUDENT, COMPANY, SUPERVISOR and ADMIN. Explain the flow before coding.

## 14. CV matching
Design a Python endpoint that compares CV text with an internship description and returns matched skills, missing skills and a match score without inventing information.

## 15. Chatbot
Design an internship assistant that answers using only available application data and explicitly says when information is missing.

## 16. Validation
For every AI-generated artifact, identify what the developers must manually verify: correctness, security, requirements, maintainability and tests.

## 17. Presentation
Create a 7-minute presentation for three students covering problem, requirements, architecture, implementation, AI, Prompt Engineering and demo.

## 18. Evaluation
Create a rubric evaluating prompt clarity, role, context, constraints, output format, iteration, validation and traceability.
