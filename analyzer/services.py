import json
import random
import time

def simulate_job_listings(skill):
    """
    Simulates fetching real job listings related to the given skill.
    Returns a list of mock job dictionaries with expanded data.
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
    locations = ["Remote", "New York, NY", "San Francisco, CA", "Austin, TX", "London, UK", "Berlin, DE", "Lagos, Nigeria"]
    all_tags = ["Agile", "TDD", "REST API", "Microservices", "Docker", "Kubernetes", "GraphQL", "CI/CD", "Cloud Native", "System Design"]
    
    jobs = []
    # Generate 5-8 random job listings
    for _ in range(random.randint(5, 8)):
        job = {
            "title": random.choice(titles),
            "company": random.choice(companies),
            "location": random.choice(locations),
            "salary_range": f"${random.randint(30, 60)*100}–${random.randint(70, 120)*100}/year",
            "required_skills": random.sample(all_tags, 3),
            "description": f"We are looking for a highly skilled professional with expertise in {skill}. The ideal candidate will have 3+ years of experience and a strong background in modern software development practices."
        }
        jobs.append(job)
    
    return jobs

def build_learning_roadmap(skill_gaps):
    """
    Returns a 3-step learning path for each missing skill.
    """
    roadmap = []
    resources = ["freeCodeCamp", "CS50", "Real Python", "MDN Web Docs", "Coursera", "Udemy", "LinkedIn Learning"]
    
    for gap in skill_gaps:
        missing = gap.get('missing_skill', 'Unknown Skill')
        steps = [
            {
                "step": 1,
                "action": f"Master the fundamentals of {missing}.",
                "time": "1 week",
                "resource": random.choice(resources)
            },
            {
                "step": 2,
                "action": f"Build a mini-project focused on {missing}.",
                "time": "2 weeks",
                "resource": "GitHub Portfolio"
            },
            {
                "step": 3,
                "action": f"Complete an advanced certification in {missing}.",
                "time": "1 month",
                "resource": random.choice(resources)
            }
        ]
        roadmap.append({"skill": missing, "steps": steps})
    return roadmap

def analyze_with_ai(skill, job_listings):
    """
    Simulates calling the Anthropic API and returning parsed JSON.
    Detailed mock data with demand scores.
    """
    time.sleep(0.5) # Slight delay for realism

    # Mock scores and levels
    # We assign random but realistic scores
    demand_scores = [random.randint(85, 98), random.randint(60, 84), random.randint(40, 59)]
    
    def get_level(score):
        if score >= 80: return "High"
        if score >= 50: return "Medium"
        return "Low"

    mock_response = {
        "top_skills": [
            {
                "skill": f"Advanced {skill} Architecture",
                "demand_score": demand_scores[0],
                "demand_level": get_level(demand_scores[0]),
                "explanation": "Modern enterprises are moving towards scalable architectural patterns where deep expertise is a premium.",
                "job_titles": [f"Senior {skill} Architect", "Staff Engineer"]
            },
            {
                "skill": "Cloud-Native Infrastructure",
                "demand_score": demand_scores[1],
                "demand_level": get_level(demand_scores[1]),
                "explanation": "Deployment and orchestration skills are becoming inseparable from core development tasks.",
                "job_titles": ["DevOps Engineer", "Backend Developer"]
            },
            {
                "skill": "Performance Optimization",
                "demand_score": demand_scores[2],
                "demand_level": get_level(demand_scores[2]),
                "explanation": "With the rise of high-traffic apps, efficiency and resource management are key differentiators.",
                "job_titles": ["Reliability Engineer", "Senior Developer"]
            }
        ],
        "skill_gaps": [
            {
                "missing_skill": "Automated Testing",
                "why_needed": f"Crucial for ensuring reliability in complex {skill} environments.",
                "how_to_learn": "Focus on integration and end-to-end testing frameworks."
            },
            {
                "missing_skill": "API Security Best Practices",
                "why_needed": "Essential for protecting sensitive data in modern distributed systems.",
                "how_to_learn": "Explore OWASP Top 10 for API security."
            }
        ],
        "market_summary": f"The market for {skill} is currently evolving. While baseline knowledge is common, there is a significant shortage of developers who understand security and performance at scale. Transitioning from a generalist to a specialist in these sub-domains can yield 30-40% higher compensation."
    }
    
    return mock_response

def compare_skills(skill_one, skill_two):
    """
    Performs dual analysis and determines a market winner.
    """
    # Analyze Skill One
    listings_one = simulate_job_listings(skill_one)
    analysis_one = analyze_with_ai(skill_one, listings_one)
    roadmap_one = build_learning_roadmap(analysis_one['skill_gaps'])
    
    # Analyze Skill Two
    listings_two = simulate_job_listings(skill_two)
    analysis_two = analyze_with_ai(skill_two, listings_two)
    roadmap_two = build_learning_roadmap(analysis_two['skill_gaps'])
    
    # Calculate Winner (Average Demand Score)
    avg_score_one = sum(s['demand_score'] for s in analysis_one['top_skills']) / len(analysis_one['top_skills'])
    avg_score_two = sum(s['demand_score'] for s in analysis_two['top_skills']) / len(analysis_two['top_skills'])
    
    if avg_score_one > avg_score_two:
        winner = skill_one
        summary = f"{skill_one} shows a slightly higher market demand based on average score."
    elif avg_score_two > avg_score_one:
        winner = skill_two
        summary = f"{skill_two} currently leads in overall demand score."
    else:
        winner = "Tie"
        summary = "Both skills are equally in demand right now."
        
    return {
        "skill_one": {
            "name": skill_one,
            "analysis": analysis_one,
            "roadmap": roadmap_one,
            "jobs": listings_one[:5],
            "avg_score": round(avg_score_one, 1)
        },
        "skill_two": {
            "name": skill_two,
            "analysis": analysis_two,
            "roadmap": roadmap_two,
            "jobs": listings_two[:5],
            "avg_score": round(avg_score_two, 1)
        },
        "comparison": {
            "winner": winner,
            "summary": summary
        }
    }
