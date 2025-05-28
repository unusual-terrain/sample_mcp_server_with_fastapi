from typing import Dict, List

candidates: List[Dict] = [
    {
      "candidate_id": "CAND001",
      "name": "Aarav Mehta",
      "email": "aarav.mehta@example.com",
      "phone": "+919000000001",
      "applied_job_id": "JOB001",
      "experience": 3,
      "skills": ["Python", "Django", "REST APIs"]
    },
    {
      "candidate_id": "CAND002",
      "name": "Isha Roy",
      "email": "isha.roy@example.com",
      "phone": "+919000000002",
      "applied_job_id": "JOB002",
      "experience": 2,
      "skills": ["SQL", "Tableau", "Excel"]
    },
    {
      "candidate_id": "CAND003",
      "name": "Ravi Kumar",
      "email": "ravi.kumar@example.com",
      "phone": "+919000000003",
      "applied_job_id": "JOB001",
      "experience": 5,
      "skills": ["JavaScript", "React", "Node.js"]
    },
    {
      "candidate_id": "CAND004",
      "name": "Sneha Iyer",
      "email": "sneha.iyer@example.com",
      "phone": "+919000000004",
      "applied_job_id": "JOB004",
      "experience": 4,
      "skills": ["Figma", "Adobe XD", "Prototyping"]
    },
    {
      "candidate_id": "CAND005",
      "name": "Nikhil Sharma",
      "email": "nikhil.sharma@example.com",
      "phone": "+919000000005",
      "applied_job_id": "JOB005",
      "experience": 6,
      "skills": ["AWS", "Terraform", "CI/CD"]
    },
    {
      "candidate_id": "CAND006",
      "name": "Pooja Batra",
      "email": "pooja.batra@example.com",
      "phone": "+919000000006",
      "applied_job_id": "JOB003",
      "experience": 3,
      "skills": ["Roadmap Planning", "Agile", "Stakeholder Management"]
    },
    {
      "candidate_id": "CAND007",
      "name": "Manav Kapoor",
      "email": "manav.kapoor@example.com",
      "phone": "+919000000007",
      "applied_job_id": "JOB007",
      "experience": 2,
      "skills": ["HTML", "CSS", "Vue.js"]
    },
    {
      "candidate_id": "CAND008",
      "name": "Divya Deshmukh",
      "email": "divya.deshmukh@example.com",
      "phone": "+919000000008",
      "applied_job_id": "JOB008",
      "experience": 4,
      "skills": ["Selenium", "Postman", "Bugzilla"]
    },
    {
      "candidate_id": "CAND009",
      "name": "Rahul Sinha",
      "email": "rahul.sinha@example.com",
      "phone": "+919000000009",
      "applied_job_id": "JOB010",
      "experience": 3,
      "skills": ["Business Analysis", "JIRA", "Documentation"]
    },
    {
      "candidate_id": "CAND010",
      "name": "Tanya Joseph",
      "email": "tanya.joseph@example.com",
      "phone": "+919000000010",
      "applied_job_id": "JOB012",
      "experience": 1,
      "skills": ["Content Writing", "SEO", "Proofreading"]
    },
    {
      "candidate_id": "CAND011",
      "name": "Deepak Nair",
      "email": "deepak.nair@example.com",
      "phone": "+919000000011",
      "applied_job_id": "JOB006",
      "experience": 4,
      "skills": ["Flask", "Python", "SQLAlchemy"]
    },
    {
      "candidate_id": "CAND012",
      "name": "Ritika Sharma",
      "email": "ritika.sharma@example.com",
      "phone": "+919000000012",
      "applied_job_id": "JOB011",
      "experience": 2,
      "skills": ["TensorFlow", "Scikit-learn", "Python"]
    },
    {
      "candidate_id": "CAND013",
      "name": "Zaid Khan",
      "email": "zaid.khan@example.com",
      "phone": "+919000000013",
      "applied_job_id": "JOB013",
      "experience": 6,
      "skills": ["Azure", "Kubernetes", "Cloud Architecture"]
    },
    {
      "candidate_id": "CAND014",
      "name": "Aishwarya Patil",
      "email": "aishwarya.patil@example.com",
      "phone": "+919000000014",
      "applied_job_id": "JOB014",
      "experience": 5,
      "skills": ["Network Security", "SIEM", "Risk Analysis"]
    },
    {
      "candidate_id": "CAND015",
      "name": "Siddharth Menon",
      "email": "siddharth.menon@example.com",
      "phone": "+919000000015",
      "applied_job_id": "JOB009",
      "experience": 2,
      "skills": ["HRMS", "Recruitment", "Payroll"]
    },
    {
      "candidate_id": "CAND016",
      "name": "Megha Kapoor",
      "email": "megha.kapoor@example.com",
      "phone": "+919000000016",
      "applied_job_id": "JOB015",
      "experience": 3,
      "skills": ["Scrum", "Kanban", "Agile"]
    },
    {
      "candidate_id": "CAND017",
      "name": "Pranav Desai",
      "email": "pranav.desai@example.com",
      "phone": "+919000000017",
      "applied_job_id": "JOB017",
      "experience": 2,
      "skills": ["Java", "Android Studio", "Kotlin"]
    },
    {
      "candidate_id": "CAND018",
      "name": "Simran Ahuja",
      "email": "simran.ahuja@example.com",
      "phone": "+919000000018",
      "applied_job_id": "JOB018",
      "experience": 3,
      "skills": ["SEO", "Google Analytics", "On-page Optimization"]
    },
    {
      "candidate_id": "CAND019",
      "name": "Harsh Vardhan",
      "email": "harsh.vardhan@example.com",
      "phone": "+919000000019",
      "applied_job_id": "JOB019",
      "experience": 4,
      "skills": ["Financial Modeling", "MS Excel", "Valuation"]
    },
    {
      "candidate_id": "CAND020",
      "name": "Kriti Chauhan",
      "email": "kriti.chauhan@example.com",
      "phone": "+919000000020",
      "applied_job_id": "JOB016",
      "experience": 1,
      "skills": ["Swift", "UIKit", "Xcode"]
    },
    {
      "candidate_id": "CAND021",
      "name": "Suresh Babu",
      "email": "suresh.babu@example.com",
      "phone": "+919000000021",
      "applied_job_id": "JOB001",
      "experience": 2,
      "skills": ["Python", "Flask", "SQL"]
    },
    {
      "candidate_id": "CAND022",
      "name": "Nidhi Arora",
      "email": "nidhi.arora@example.com",
      "phone": "+919000000022",
      "applied_job_id": "JOB020",
      "experience": 4,
      "skills": ["Documentation", "API Manuals", "Technical Writing"]
    },
    {
      "candidate_id": "CAND023",
      "name": "Aniket Bhatt",
      "email": "aniket.bhatt@example.com",
      "phone": "+919000000023",
      "applied_job_id": "JOB005",
      "experience": 3,
      "skills": ["Docker", "Ansible", "Linux"]
    },
    {
      "candidate_id": "CAND024",
      "name": "Fatima Sheikh",
      "email": "fatima.sheikh@example.com",
      "phone": "+919000000024",
      "applied_job_id": "JOB008",
      "experience": 2,
      "skills": ["Manual Testing", "Regression Testing"]
    },
    {
      "candidate_id": "CAND025",
      "name": "Omkar Rane",
      "email": "omkar.rane@example.com",
      "phone": "+919000000025",
      "applied_job_id": "JOB006",
      "experience": 1,
      "skills": ["Python", "FastAPI", "PostgreSQL"]
    }
  ]
  