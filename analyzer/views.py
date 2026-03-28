from django.shortcuts import render, redirect
from .services import simulate_job_listings, analyze_with_ai, build_learning_roadmap, compare_skills

def home_view(request):
    """
    Renders the homepage with a skill input form.
    """
    return render(request, 'analyzer/home.html')

def analyze_view(request):
    """
    Handles form submission, calls AI for analysis, and displays results.
    Supports single skill analysis and dual skill comparison.
    """
    if request.method == 'POST':
        skill_one = request.POST.get('skill', '').strip()
        skill_two = request.POST.get('skill_two', '').strip()
        
        if not skill_one:
            return redirect('home')
        
        # Comparison Mode
        if skill_two:
            comparison_results = compare_skills(skill_one, skill_two)
            context = {
                'mode': 'comparison',
                'skill_one': comparison_results['skill_one'],
                'skill_two': comparison_results['skill_two'],
                'comparison': comparison_results['comparison']
            }
        else:
            # Single Skill Mode
            job_listings = simulate_job_listings(skill_one)
            analysis_results = analyze_with_ai(skill_one, job_listings)
            roadmap = build_learning_roadmap(analysis_results.get('skill_gaps', []))
            
            context = {
                'mode': 'single',
                'skill': skill_one,
                'top_skills': analysis_results.get('top_skills', []),
                'skill_gaps': analysis_results.get('skill_gaps', []),
                'market_summary': analysis_results.get('market_summary', 'No summary available.'),
                'roadmap': roadmap,
                'job_listings': job_listings[:5] # Show 5 listings
            }
        
        return render(request, 'analyzer/results.html', context)
    
    return redirect('home')
