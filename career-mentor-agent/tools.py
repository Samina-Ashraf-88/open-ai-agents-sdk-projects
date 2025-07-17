from agents import function_tool

@function_tool
def get_career_roadmap(field: str) -> str:
    """
    Provide a learning roadmap for a given career field.
    """
    roadmaps = {
        "Data Science": "Learn Python, Pandas, Machine Learning, SQL, Deep Learning.",
        "Web Development": "HTML, CSS, JavaScript, React, Node.js.",
        "Cybersecurity": "Networking, Linux, Cryptography, Ethical Hacking."
    }
    return roadmaps.get(field, "No roadmap available for this field.")

@function_tool
def get_real_world_jobs(field: str) -> str:
    """
    Provide real-world job roles in a specific field.
    """
    jobs = {
        "Data Science": "Data Analyst, ML Engineer, Data Scientist.",
        "Web Development": "Frontend Developer, Backend Developer, Full Stack Engineer.",
        "Cybersecurity": "Security Analyst, SOC Analyst, Penetration Tester."
    }
    return jobs.get(field, "No jobs found for this field.")
