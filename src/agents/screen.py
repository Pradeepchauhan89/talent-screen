import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

def screen_resume(text_content):
  try:
    response = ""
    job_detail = "Jr Prompt Engineer Company Overview: Activate Intelligence is a new agency offering design and development services to medium and large businesses. Leveraging generative AI agents, we redefine productivity and efficiency. Based in London, we are looking to add a like-minded Junior Developer to our innovative team. Role Overview: The Junior Developer role is an opportunity for an individual who thrives in a fast-paced, ever-changing tech landscape. We're not just looking for a coder; we are looking for a problem-solver who is keen to learn and passionate about technology. Key Responsibilities: Develop and maintain software solutions, primarily in Python. Work closely with data analysis libraries and AI APIs. Engage in projects involving vector databases and graph databases. Collaborate with cross-functional teams to define, design, and ship new features. Commit to improving code quality through writing unit tests, automation, and performing code reviews. Qualifications: Basic understanding of any programming language, with a willingness to learn Python quickly. Familiarity with data analysis tools is a plus, but not a requirement. Curiosity and aptitude for learning new technologies and methodologies. Strong problem-solving skills. Personal Qualities: A tech enthusiast who keeps up with the latest trends. Passionate about coding—whether it is our software or your own personal projects. Excellent communication skills and a team player. Opportunities for Growth: Regular in-house hackathons and coding sessions. Opportunities for mentorship from leading experts in the field. Access to online learning platforms and e-courses. Technology Stack: Primary: Python (Good to have) Libraries: Various Data Analysis Libraries Databases: Vector Databases, Graph Databases APIs: Various AI APIs Benefits: Competitive salary and performance bonuses. Flexible tech budget for devices Flexible, potentially remote work environment. Tech-specific perks such as conference tickets, e-learning subscriptions. Call to Action: If you are a passionate tech lover who wants to be at the forefront of innovation from the comfort of your own space, we would love to hear from you. Apply now and let us push the boundaries of what is possible together!"
    prompt = f'''
    Carefully analyze this resume content <<<{text_content}>>> against the provided job details {job_detail}. Identify and list the skills from the resume that directly match the job requirements. Also, note any key skills or qualifications that are missing. If the resume includes any professional certifications, especially those relevant to the job, highlight them. If the job description mentions a specific location requirement and the candidate cv mentions a location that is not in the same country that candidate should not be considered. The output should include the candidate's name, email, contact number, location, detailed skill match analysis, a list of any missing skills pertinent to the job, and relevant certifications. Your goal is to ensure a thorough and precise match to select the most qualified candidate.
    '''
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
  except Exception as e:
    print('error in gpt==')
    print(e)

  print(response.choices[0].text)