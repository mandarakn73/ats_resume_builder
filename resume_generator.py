def generate_resume(profile):
    return f"""
{profile['name']}
{profile['email']} | {profile['phone']}

SUMMARY
{profile['summary']}

SKILLS
{profile['skills']}

EXPERIENCE
{profile['experience']}

PROJECTS
{profile['projects']}

EDUCATION
{profile['education']}
"""
