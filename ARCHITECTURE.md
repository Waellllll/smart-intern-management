# Architecture

```text
Browser
  ↓
Angular :4200
  ↓ HTTP/JSON
Spring Boot REST :8080
  ├── JPA → MySQL :3306
  └── HTTP/JSON → Python FastAPI :8000
                         ↓
                 recommendation engine
```
