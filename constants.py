import os
print(os.getcwd())
questions = {
    1: "What is your ideal way to spend a weekend?",
    2: "How important is financial stability to you in a relationship?",
    3: "Do you want children in the future?",
    4: "How do you typically handle conflicts in a relationship?",
    5: "What role does religion or spirituality play in your life?",
    6: "How do you feel about maintaining individual friendships and hobbies in a relationship?",
    7: "What's your approach to household chores and responsibilities?",
    8: "How important is physical intimacy to you in a relationship?",
    9: "What are your long-term career goals and how might they affect a relationship?",
    10: "How do you prefer to communicate your feelings and needs in a relationship?"
}

options = {
    1: [
        "Relaxing at home with movies, books, or hobbies",
        "Engaging in outdoor activities like hiking, biking, or picnicking",
        "Socializing with friends, attending events, or exploring new places",
        "Focusing on productive tasks, personal projects, or self-improvement"
    ],
    2: [
        "Very important - I prioritize financial planning and security in a relationship",
        "Somewhat important - I value financial stability but it's not the top priority",
        "Not very important - I'm more focused on emotional connection than finances",
        "Not important at all - I believe love conquers all, including financial challenges"
    ],
    3: [
        "Yes, definitely - Having children is a crucial part of my life plan",
        "Maybe in the future - I'm open to the idea but not certain yet",
        "No, I don't want children - I prefer a child-free lifestyle",
        "Unsure - I haven't made a decision about having children"
    ],
    4: [
        "Discuss immediately - I prefer addressing issues as soon as they arise",
        "Take time to cool off - I need some space before discussing conflicts",
        "Seek compromise - I focus on finding middle ground and resolving issues together",
        "Avoid conflict - I tend to sidestep confrontations and hope issues resolve themselves"
    ],
    5: [
        "Very important - My faith/spirituality guides most aspects of my life",
        "Somewhat important - I value spirituality but it doesn't dictate all my decisions",
        "Not very important - I'm open to spiritual ideas but they don't play a major role",
        "Not important at all - I'm not religious or spiritual"
    ],
    6: [
        "Essential - I believe maintaining individual identities is crucial for a healthy relationship",
        "Important - I value personal space and interests alongside the relationship",
        "Somewhat important - I enjoy shared activities more but appreciate some individuality",
        "Not important - I prefer spending most of my time and sharing all interests with my partner"
    ],
    7: [
        "Equal distribution - I believe in splitting chores 50/50 regardless of other factors",
        "Based on preferences and schedules - I prefer dividing tasks according to individual strengths and availability",
        "One person does more - I'm comfortable with an uneven split if it makes sense for the relationship",
        "Hire help - I prefer outsourcing household chores when possible to reduce potential conflicts"
    ],
    8: [
        "Very important - Physical intimacy is a key factor in my relationship satisfaction",
        "Somewhat important - I value physical intimacy but it's not the most crucial aspect",
        "Not very important - Emotional connection matters more to me than physical intimacy",
        "Not important at all - Physical intimacy is not a priority in my relationships"
    ],
    9: [
        "Ambitious career goals - I'm focused on advancement, even if it requires sacrifices",
        "Balanced work-life approach - I aim for career growth while maintaining personal life",
        "Stable job - I prefer job security and consistency over career advancement",
        "Uncertain - I'm still figuring out my long-term career path"
    ],
    10: [
        "Open and direct - I express my feelings and needs clearly and immediately",
        "Actions over words - I prefer showing my feelings through gestures and behavior",
        "Need time to process - I take time to understand my emotions before discussing them",
        "Struggle to express - I find it challenging to communicate my feelings and needs"
    ]
}