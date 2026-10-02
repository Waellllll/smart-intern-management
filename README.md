# Smart Internship Platform

## Architecture
Angular frontend → Spring Boot REST API → MySQL → Python FastAPI AI service

### Start order
1. MySQL
2. Python AI service on :8000
3. Spring Boot API on :8080
4. Angular frontend on :4200

### MySQL
The backend expects root/root. Change `backend/src/main/resources/application.properties` if needed.

### Python
```bash
cd ai-service
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Spring Boot
```bash
cd backend
mvn spring-boot:run
```

### Angular
```bash
cd frontend
npm install
npm start
```
Then open http://localhost:4200

### End-to-end recommendation flow
Angular sends GET /api/recommendations/student/{id} → Spring Boot reads MySQL → Spring Boot sends POST /recommend to FastAPI → Python calculates scores → Spring Boot returns JSON → Angular displays cards.
