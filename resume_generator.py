def professional_template(profile):
    return f"""
{profile['name']}
{profile['email']} | {profile['phone']}

SUMMARY
{profile['summary']}

SKILLS
{profile['skills']}

EDUCATION
{profile['degree']} – {profile['college']} ({profile['degree_year']}) | {profile['cgpa']}
Class XII – {profile['board_12']} | {profile['percent_12']}
Class X – {profile['board_10']} | {profile['percent_10']}
"""

def minimal_template(profile):
    return f"""
{profile['name']}
{profile['email']} | {profile['phone']}

PROFILE
{profile['summary']}

CORE SKILLS
{profile['skills']}

EDUCATION
{profile['degree']} | {profile['degree_year']}
12th – {profile['percent_12']}
10th – {profile['percent_10']}
"""

def fresher_template(profile):
    return f"""
{profile['name']}
{profile['email']} | {profile['phone']}

CAREER OBJECTIVE
{profile['summary']}

SKILLS
{profile['skills']}

EDUCATION
{profile['degree']} (Ongoing)
12th – {profile['percent_12']}
10th – {profile['percent_10']}
"""
