import json
import random

def simulate_job_listings(skill):
    """
    Simulates fetching real job listings related to the given skill.
    Returns a list of mock job dictionaries.
    """
    companies = ["TechNova", "CloudScale", "DataFlow", "AI Frontiers", "NexGen Solutions", "DevStream", "SkyNet Systems"]
    titles = [
        f"Senior {skill} Engineer",
        f"Junior {skill} Developer",
        f"Lead {skill} Specialist",
        f"Full Stack Developer ({skill} Focused)",
        f"{skill} Consultant",
        f"Software Engineer - {skill} Ecosystem"
    ]
    locations = ["Remote", "New York, NY", "San Francisco, CA", "Austin, TX", "London, UK", "Berlin, DE"]
    
    jobs = []
    # Generate 5-8 random job listings
    for _ in range(random.randint(5, 8)):
        job = {
            "title": random.choice(titles),
            "company": random.choice(companies),
            "location": random.choice(locations),
            "description": f"We are looking for a highly skilled professional with expertise in {skill}. The ideal candidate will have 3+ years of experience and a strong background in modern software development practices. Proficiency in related technologies is a plus."
        }
        jobs.append(job)
    
    return jobs

def build_prompt(skill, job_listings):
    """
    Constructs the AI prompt based on current skill and simulated job listings.
    """
    listings_text = ""
    for idx, job in enumerate(job_listings, 1):
        listings_text += f"\n{idx}. {job['title']} at {job['company']} ({job['location']})\n   Description: {job['description']}\n"

    prompt = f"""
    Analyze the job market for a developer with the skill: '{skill}'.
    
    Here are some recent job listings found:
    {listings_text}
    
    Please provide a detailed analysis in a STRICT JSON format with the following structure:
    {{
        "top_skills": [
            {{
                "skill": "Name of skill",
                "demand_level": "High/Medium/Low",
                "explanation": "Why this skill is in demand",
                "job_titles": ["Title 1", "Title 2"]
            }}
        ],
        "skill_gaps": [
            {{
                "missing_skill": "Name of missing skill",
                "why_needed": "How it complements {skill}",
                "how_to_learn": "Recommended resource or path"
            }}
        ],
        "market_summary": "A 2-3 sentence paragraph summarizing the current market landscape for '{skill}'."
    }}
    
    Return ONLY the JSON object.
    """
    return prompt

def analyze_with_ai(skill, job_listings):
    """
    Simulates calling the Anthropic API and returning parsed JSON.
    For this prototype, it returns realistic mock data.
    """
    # This is where we would normally use 'requests' to call Anthropic
    # Since this is a prototype, we return a simulated AI response
    
    # Simulate some processing delay
    import time
    time.sleep(1)

    # Realistic mock response based on common tech trends
    mock_response = {
        "top_skills": [
            {
                "skill": f"Advanced {skill} Concepts",
                "demand_level": "High",
                "explanation": "Companies are looking for deep architectural knowledge, not just syntax.",
                "job_titles": [f"Senior {skill} Architect", f"Lead {skill} Engineer"]
            },
            {
                "skill": "Edge Computing & Cloud Native",
                "demand_level": "High",
                "explanation": "Integration with AWS/Azure/GCP is now a baseline requirement for modern applications.",
                "job_titles": ["Cloud Engineer", "DevOps Specialist"]
            },
            {
                "skill": "System Design & Scalability",
                "demand_level": "Medium",
                "explanation": "Understanding how systems scale horizontally is critical for high-traffic platforms.",
                "job_titles": ["Backend Engineer", "Infrastructure Expert"]
            }
        ],
        "skill_gaps": [
            {
                "missing_skill": "Unit Testing & TDD",
                "why_needed": f"Crucial for maintaining large-scale {skill} codebases without regressions.",
                "how_to_learn": "Explore PyTest (if Python) or Jest (if JS) documentation and build a test-driven project."
            },
            {
                "missing_skill": "CI/CD Pipeline Integration",
                "why_needed": "Automating deployments is essential in agile environments.",
                "how_to_learn": "Learn GitHub Actions or GitLab CI basics via online labs."
            }
        ],
        "market_summary": f"The market for developers with '{skill}' is robust, but shifting towards a requirement for cross-functional knowledge in cloud infrastructure and automated testing. While {skill} remains a core asset, candidates who bridge the gap between development and operations are seeing significantly higher salary offers."
    }
    
    return mock_response
