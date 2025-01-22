from faker import Faker
from app import app
from models import db,Story

fake = Faker()

with app.app_context():
    print('Deleting all records ...')
    Story.query.delete()

    print('Creating Items ....')

    stories = []

    stories.append(
        Story (
                id = 1,
                title = "The Future of AI in Everyday Life",
                subtitle = "Exploring how artificial intelligence is shaping our world.",
                contentparagraph1 = "Artificial intelligence is no longer a futuristic concept; it is already a part of our daily lives. From voice assistants to recommendation systems, AI is streamlining tasks and making our lives easier. Businesses are increasingly leveraging AI to analyze data and improve decision-making. This growing reliance on AI raises questions about privacy and ethics.",
                contentparagraph2 = "One of the most visible applications of AI is in smart home devices. These devices learn user preferences and adapt accordingly, providing personalized experiences. Voice-activated assistants like Alexa and Google Home are becoming household staples. Their ability to understand and respond to natural language continues to improve.",
                contentparagraph3 = "Healthcare is another area where AI is making significant strides. From diagnosing diseases to predicting patient outcomes, AI algorithms are revolutionizing the field. Medical imaging powered by AI helps doctors detect anomalies with greater accuracy. AI-driven chatbots also provide 24/7 health advice to users.",
                contentparagraph4 = "AI is also transforming the way businesses operate. Predictive analytics help companies forecast trends and optimize their supply chains. Customer service chatbots improve response times and enhance customer satisfaction. Automation powered by AI reduces operational costs and increases efficiency.",
                contentparagraph5 = "Despite the benefits, AI comes with its challenges. Ethical concerns regarding data privacy and bias in algorithms are widely discussed. Ensuring fairness and transparency in AI systems is a growing area of research. Governments are introducing regulations to address these challenges.",
                contentparagraph6 = "Education is another sector being transformed by AI. Personalized learning platforms tailor lessons to individual students' needs. AI-driven tutoring systems provide instant feedback and recommendations. This helps educators focus on more strategic teaching approaches.",
                contentparagraph7 = "The job market is experiencing a shift due to AI-driven automation. While AI creates new job opportunities, it also renders some roles obsolete. Workers must reskill and adapt to stay relevant in an AI-driven world. Governments and organizations are investing in retraining programs.",
                contentparagraph8 = "AI in entertainment is revolutionizing content creation and consumption. Streaming platforms use AI to recommend content based on viewing habits. Video games leverage AI to create dynamic and adaptive gameplay experiences. The creative industry is also experimenting with AI-generated art and music.",
                contentparagraph9 = "Transportation is another industry benefiting from AI advancements. Self-driving cars powered by AI are being tested worldwide. AI traffic management systems help reduce congestion in urban areas. Predictive maintenance powered by AI enhances vehicle safety and performance.",
                contentparagraph10 = "In conclusion, AI is becoming an integral part of our lives, offering numerous benefits across various sectors. However, it is crucial to address ethical concerns and ensure responsible AI development. As AI continues to evolve, society must adapt to its rapid advancements. The future of AI holds exciting possibilities and challenges.",
                author = "Jane Smith",
                date = "2025/01/20",
                category = "Technology",
                image = "AI.jpeg"
        )
    )

    stories.append(
        Story (
                id = 2,
                title = "The Rise of Remote Work Culture",
                subtitle = "How remote work is changing the way we do business.",
                contentparagraph1 = "The COVID-19 pandemic accelerated the shift to remote work for many industries. Companies were forced to adopt digital tools to enable employees to work from home. This change has shown that remote work is not only possible but also efficient. Employees now enjoy greater flexibility and work-life balance.",
                contentparagraph2 = "Remote work has led to an increase in productivity for many professionals. Without the daily commute, employees have more time to focus on tasks. Virtual meetings have replaced in-person interactions, making collaboration easier. Companies are investing in remote work infrastructure to support their teams.",
                contentparagraph3 = "However, remote work comes with its challenges. Many employees struggle with isolation and lack of social interaction. Companies are finding ways to maintain a sense of community through virtual team-building activities. Maintaining a work-life balance can also be difficult for remote workers.",
                contentparagraph4 = "The gig economy has benefited greatly from the rise of remote work. Freelancers and independent contractors now have more opportunities to work with global clients. Online platforms have made it easier to find remote gigs across various industries. This has democratized job opportunities for skilled professionals worldwide.",
                contentparagraph5 = "Technology plays a crucial role in enabling remote work. Collaboration tools like Slack, Zoom, and Trello have become essential for remote teams. Cloud storage solutions allow employees to access files from anywhere. Security measures are also being enhanced to protect remote work environments.",
                contentparagraph6 = "Companies are rethinking their office space needs due to the rise of remote work. Many organizations are adopting hybrid work models, combining office and remote work. This allows employees to choose their preferred work environment. Real estate costs are being reevaluated as a result.",
                contentparagraph7 = "Work-from-home policies are evolving to accommodate long-term remote work. Organizations are focusing on employee well-being and mental health. Offering flexibility and support helps retain talent and improve job satisfaction. Policies are being tailored to meet the unique needs of remote workers.",
                contentparagraph8 = "Remote work has also impacted the hiring process. Companies are now hiring talent from different geographical locations. This has led to more diverse teams and global collaboration. Hiring managers are adjusting their strategies to screen and onboard remote employees.",
                contentparagraph9 = "As remote work becomes more common, companies must address cybersecurity risks. Protecting sensitive company data from cyber threats is a top priority. Employees are being trained to recognize and prevent security breaches. Secure remote access solutions are being implemented.",
                contentparagraph10 = "In conclusion, remote work is here to stay and continues to evolve. While it offers numerous benefits, organizations must address its challenges. Adopting the right strategies and tools can ensure success in a remote work environment. The future of work will likely be a blend of remote and in-office work.",
                author = "Alex Johnson",
                date = "2025/01/21",
                category = "Business",
                image = "Remote.jpeg"
        )
    )

    stories.append(
        Story (
                 id = 3,
                title = "The Benefits of Mindful Meditation",
                subtitle = "How mindfulness can improve your mental well-being.",
                contentparagraph1 = "Mindfulness meditation is gaining popularity as people seek ways to manage stress. It involves focusing on the present moment without judgment. This practice has been shown to reduce anxiety and increase emotional resilience. Many individuals find it helpful for dealing with daily pressures.",
                contentparagraph2 = "Studies suggest that practicing mindfulness can enhance overall mental health. Regular meditation helps regulate emotions and reduce negative thought patterns. People who practice mindfulness report feeling more present and aware in their daily lives. It fosters a greater sense of inner peace and balance.",
                contentparagraph3 = "Incorporating mindfulness into daily routines can be simple and effective. Breathing exercises, mindful walking, and body scans are common techniques. These practices can be done anywhere, making them accessible to everyone. Even a few minutes of mindfulness each day can have a profound impact.",
                contentparagraph4 = "Mindfulness can also improve focus and concentration. By training the mind to stay present, individuals can enhance their productivity. This is particularly useful for students and professionals who need to stay focused. Mindfulness techniques can be used to manage distractions and maintain attention.",
                contentparagraph5 = "Aside from mental benefits, mindfulness has physical health advantages. It can lower blood pressure and improve sleep quality. Chronic pain sufferers often report relief through consistent meditation. The mind-body connection plays a crucial role in overall well-being.",
                contentparagraph6 = "Mindfulness practices can be adapted to suit different lifestyles. Whether through guided meditation apps or attending in-person sessions, there are many options available. Finding a method that works best is key to sustaining the practice. Experimenting with different approaches can help individuals stay committed.",
                contentparagraph7 = "Companies are recognizing the benefits of mindfulness in the workplace. Corporate mindfulness programs help employees manage stress and boost productivity. Encouraging a mindful culture fosters a positive work environment. Employers see improvements in employee engagement and overall job satisfaction.",
                contentparagraph8 = "Mindfulness can also enhance relationships and social connections. By being fully present during interactions, individuals can improve communication. Active listening and empathy are key components of mindful relationships. Strengthening these skills leads to deeper and more meaningful connections.",
                contentparagraph9 = "Children and teens can benefit from mindfulness as well. Schools are incorporating mindfulness techniques to help students manage stress. These practices teach young people how to handle emotions and build resilience. Introducing mindfulness at an early age sets the foundation for lifelong well-being.",
                contentparagraph10 = "In conclusion, mindfulness meditation offers numerous benefits for mental and physical health. Incorporating mindfulness into daily life can lead to increased happiness and reduced stress. With practice and commitment, anyone can experience the positive effects of mindfulness. The journey to mindfulness is a rewarding one.",
                author = "Emily Davis",
                date = "2025/01/22",
                category = "Health",
                image = "1.jpeg"
        )
    )

    stories.append(
        Story (
                id = 4,
                title = "Exploring Sustainable Travel Options",
                subtitle = "How to travel responsibly and reduce your carbon footprint.",
                contentparagraph1 = "Sustainable travel is becoming more important as travelers seek eco-friendly options. Reducing carbon footprints and supporting local communities are key priorities. Choosing sustainable travel options helps preserve the environment for future generations. Travelers are now more conscious of their impact.",
                contentparagraph2 = "One way to travel sustainably is by choosing eco-friendly accommodations. Many hotels and resorts are adopting green practices such as solar energy. Staying at eco-conscious properties can contribute to conservation efforts. These accommodations often use sustainable materials and practices.",
                contentparagraph3 = "Using public transportation instead of rental cars can significantly reduce emissions. Trains, buses, and bicycles are great alternatives for getting around. Walking tours are another sustainable option that allows travelers to explore more intimately. Public transport also provides an opportunity to experience local culture.",
                contentparagraph4 = "Travelers can support local economies by shopping and dining at local businesses. Buying handmade crafts and eating at family-owned restaurants contribute to the community. This practice ensures that tourism benefits the local population. It also provides an authentic travel experience.",
                contentparagraph5 = "Reducing plastic waste while traveling is another important consideration. Carrying reusable water bottles, bags, and utensils can help minimize single-use plastics. Many destinations now offer refill stations and encourage travelers to go plastic-free. Being mindful of waste helps protect the environment.",
                contentparagraph6 = "Volunteering while traveling is a great way to give back. Many travelers participate in conservation projects and community service initiatives. These experiences can be rewarding and help travelers connect with locals. Choosing reputable organizations ensures meaningful contributions.",
                contentparagraph7 = "Carbon offset programs allow travelers to neutralize their emissions. Many airlines and travel companies offer carbon offset options for flights. Investing in reforestation and renewable energy projects can make travel more sustainable. Travelers should research and choose reliable programs.",
                contentparagraph8 = "Exploring destinations during off-peak seasons can reduce overcrowding. Over-tourism can strain resources and harm local communities. Traveling during quieter periods allows for a more enjoyable experience. It also helps spread tourism income throughout the year.",
                contentparagraph9 = "Engaging with local culture and respecting traditions is crucial. Learning about the customs and language shows respect for the local people. Responsible travelers seek cultural experiences that are ethical and sustainable. Being open-minded and respectful enhances the travel experience.",
                contentparagraph10 = "In conclusion, sustainable travel is a responsibility that every traveler should embrace. By making conscious choices, travelers can reduce their impact on the environment. Supporting local communities and minimizing waste are essential steps. Sustainable travel ensures that future generations can enjoy the beauty of our planet.",
                author = "Michael Brown",
                date = "2025/01/23",
                category = "Travel",
                image = "Eco.jpeg"
        )
    )
            
            

    db.session.add_all(stories)
    db.session.commit()

    print("Items created successfully!")