import os
# from dotenv import load_dotenv

from snowflake import connector
from snowflake.snowpark import Session
from snowflake.cortex import Summarize, Complete, ExtractAnswer, Sentiment, Translate

# Load environment variables from .env
# load_dotenv()

connection_params = {
    "account": "sibsego-vub12130",
    "user": "mrinalsnow2",
    "password": "passSNOW@1234"
}

# Create a Snowflake session
snowflake_session = Session.builder.configs(connection_params).create()


# Define the LLM functions
def summarize(user_text):
    summary = Summarize(text=user_text, session=snowflake_session)
    return summary


def complete(user_text):
    completion = Complete(
        model="snowflake-arctic",
        prompt=f"Provide 5 keywords from the following text: {user_text}",
        session=snowflake_session,
    )
    return completion


def extract_answer(user_text):
    answer = ExtractAnswer(
        from_text=user_text,
        question="What is the Importance of Pupil-Teacher Ratios",
        session=snowflake_session,
    )
    return answer


def sentiment(user_text):
    sentiment = Sentiment(text=user_text, session=snowflake_session)
    return sentiment


# def translate(user_text):
#     translation = Translate(
#         text=user_text, from_language="en", to_language="de", session=snowflake_session
#     )
#     return translation


# Define the main function
def main():
    user_text = """
        Analysis of Pupil-Teacher Ratios in India by Level of Education: A State-wise Examination based on UDISEPlus 2021-22 Data

Significance of PTR at School Level in India
Proper pupil-teacher-ratio in schools at different levels of education plays a vital role in ensuring meaningful and effective teaching-learning processes in schools. However, maintaining valid PTR doesn’t guarantee that school transaction is smooth and as envisaged. Also, there is no guarantee that all schools have adequate teachers. The proper pupil-teacher ratio in schools in India holds significant importance for several reasons:

Quality of Education: A proper pupil-teacher ratio ensures teachers can give individual attention to each student by identifing their strengths and weaknesses, and provide personalized instruction. This customized attention enhances the quality of education and improves learning outcomes.
Student Engagement: With a lower pupil-teacher ratio, students have more opportunities to actively participate in class activities, ask questions, and engage in discussions. Increased engagement fosters a positive learning environment to develop critical thinking and problem-solving skills.
Effective Classroom Management: A balanced pupil-teacher ratio helps maintain discipline and manage classrooms effectively. Teachers can better monitor student behavior, address individual needs, and provide timely feedback.
Support for Special Needs: Proper pupil-teacher ratios are crucial for students with special needs or diverse learning abilities. Students requiring additional support can receive personalized attention and specialized instruction to meet their unique learning requirements.
Increased Teacher Effectiveness: Lower pupil-teacher ratios allow teachers to dedicate more time to planning lessons, designing activities, and providing constructive feedback; this enables teachers to be more effective in their teaching strategies and adapt their methods to address the diverse needs of students.
Building Strong Teacher-Student Relationships: A lower pupil-teacher ratio facilitates strong relationships between teachers and students. Teachers have the opportunity to understand each student’s strengths, weaknesses, and interests, fostering trust and better communication between them.
Improved Overall School Environment: A well-balanced pupil-teacher ratio contributes to a positive school environment. Students feel supported, valued, and more motivated to excel academically and participate in extracurricular activities.
It is important to note that while maintaining an ideal pupil-teacher ratio is vital, it should be accompanied by other educational reforms, such as practical teacher training, infrastructure development, and curriculum enhancement, to ensure comprehensive quality education for all students.

Historical Perspective of PTR in India
 The pupil-teacher ratio in India’s school education system has significantly changed. Here is a historical perspective:

Earlier Years: In the early years of India’s education system, pupil-teacher ratios were generally higher due to limited infrastructure, resources, and many students; this resulted in overcrowded classrooms and challenges in providing individual attention to students.
Post-Independence: Following India’s independence in 1947, concerted efforts were made to expand educational access and reduce pupil-teacher ratios. The government established more schools and recruited additional teachers to cater to the growing student population. However, the ratios remained relatively high, particularly in rural and remote areas.
Education Reforms: In subsequent years, various education reforms were implemented to improve access and quality; this included recruiting more teachers, enhancing teacher training, and providing adequate infrastructure efforts aimed at lowering the pupil-teacher ratio and improving learning outcomes.
The Right to Education Act (2009): The implementation of the Right to Education Act in 2009 further emphasized the importance of pupil-teacher ratios. It mandated specific norms for pupil-teacher ratios at different levels of education. As per the Act, the prescribed pupil-teacher ratio for primary schools is 30:1, and for upper primary and secondary schools, it is 35:1.
Current Status: The pupil-teacher ratio in India varies across states and regions. While progress has been made in reducing ratios, challenges such as teacher shortages, uneven distribution of resources, and urban-rural gaps persist. Efforts are being made to address these issues and improve the pupil-teacher balance to ensure quality education for all.
It is important to note that the pupil-teacher ratio is dynamic and can vary based on demographic changes, government policies, and resource allocations.

 PTR Norms  in Samagra Shiksha
The Samagra Shiksha is a centrally-sponsored scheme the Government of India implements for school education from pre-school to higher secondary levels. It aims to provide inclusive and equitable quality education for all. Regarding pupil-teacher ratio, the scheme does not specify specific provisions for each level of education. However, it emphasizes maintaining an optimal Pupil-Teacher Ratio (PTR) to ensure quality education. The exact PTR may vary between states and regions. Claiming a lower pupil-teacher ratio at the primary level is generally recommended compared to the upper primary, secondary, and higher secondary levels; this allows for better individual attention and effective student learning outcomes. State government education departments or governing bodies may outline the specific guidelines for pupil-teacher ratio.

In particular, the Samagra Shiksha has specified the following Pupil-Teacher Ratio (PTR) for different levels of education in India:

Primary Level: 20:1
Upper Primary Level: 30:1; and
Secondary Level: 30: 1
The Samagra Shiksha scheme also aims to achieve a PTR of 20:1 at all levels of education by 2025; this will require hiring additional teachers and the more effective deployment of existing teachers. It is important to note that the PTR norms are just a guideline, and there may be some variation depending on the specific needs of a state or district. For example, a remote or underserved area may have a higher PTR than a more urban area. However, the Samagra Shiksha scheme ensures that all children can access a qualified teacher, regardless of where they live.

UDISEPlus PTR 2021-22: All India Level
Analyzing the data provided for the Pupil-Teacher Ratio (PTR) by levels of education at the All India level, as well as at the State/UT level, we can observe the following trends and critical points:

 All India Level

Primary (I-V): The pupil-teacher ratio is 26:1, indicating that, on average, there is one teacher for every 26 students.
Upper Primary (VI-VIII): The PTR is 19:1, which shows a relatively lower ratio compared to the primary level, suggesting a slightly better teacher-student ratio at this level.
Secondary (IX-X): The PTR is 17:1, indicating a further reduction in the ratio, potentially indicating a greater allocation of resources and teachers at the secondary level compared to primary and upper primary levels and
Higher Secondary (XI-XII): The PTR is 27:1, slightly higher than the secondary level, suggesting a slight increase in the pupil-teacher ratio at this level.
 UDISEPlus PTR 2021-22: State/UT Level

There are variations in the pupil-teacher ratio across different States/UTs for each level of education. Some states/UTs, like Bihar, Jharkhand, and Rajasthan, exhibit higher PTRs across all levels, indicating a potential need for more teachers and resources to provide optimal learning environments. On the other hand, states/UTs like Sikkim, Lakshadweep, and Ladakh have relatively lower PTRs, suggesting a comparatively better teacher-student ratio.
It’s important to note that the optimal PTR vary depending on various factors, such as the teaching methodology, infrastructure, and resources available in each state/UT. Overall, the data highlights the need for attention to improve the pupil-teacher ratio in certain states/UTs, especially at the primary and upper primary levels; this can help facilitate better individual attention and enhance the overall quality of education. Additionally, efforts to maintain or lower the pupil-teacher ratio in all states/UTs would contribute to better learning outcomes and provide a conducive learning environment for students.

The Samagra Shiksha scheme has several provisions to improve the pupil-teacher ratio (PTR) in India. These include:

Hiring more teachers:The scheme allows additional teachers to reduce the PTR to 20:1 at the elementary (primary and upper primary) level and 30:1 at the secondary level.
Deploying teachers more effectively:The scheme also aims to deploy teachers more effectively by rationalizing the distribution of teachers across schools and ensuring that teachers are posted in schools where they are most needed.
Improving the quality of teachers:The Samagra Shiksha scheme also includes provisions for improving the quality of teachers through pre-service and in-service training; this is important because high-quality teachers are more likely to be effective in the classroom and help to improve student learning outcomes.
In addition to these provisions, the Samagra Shiksha scheme also includes several other measures to improve the quality of education in India. These include:

Providing more resources to schools:The scheme provides increased funding for schools to improve infrastructure, teaching materials, and other resources.
Focusing on early childhood education:The scheme also strongly emphasizes early childhood education (ECE), essential for laying the foundation for lifelong learning.
Promoting inclusive education: The Samagra Shiksha scheme ensures that all children have access to quality education, regardless of their background or circumstances; this includes children with disabilities, children from disadvantaged groups, and children in remote and underserved areas.
The Samagra Shiksha scheme is a comprehensive and ambitious program that aims to improve the quality of education for all children in India. The provisions of PTR are an essential part of this program and are designed to ensure that every child has access to a qualified teacher.

Despite significant improvement in PTR across the Country, as specified above, all schools still may not have the adequate number of teachers to function effectively, which is also reflected in UDISEPlus data. Below, we briefly view the existing number of single-teacher schools in India.

Single-Teacher Schools
Single-teacher schools, or one-teacher schools, are educational institutions in India where a single teacher is responsible for teaching students across various grade levels. These schools are primarily found in remote rural areas with limited resources and infrastructure. Consequences of Single-Teacher Schools are many, a few of which are listed below:

Limited Attention: With just one teacher, providing individual attention to all students becomes challenging; this can affect the quality of education and hinder the overall learning experience.
Multigrade Teaching: In single-teacher schools, students from different grade levels are taught together in a single classroom. The teacher needs to manage multiple subjects and grade-level curricula simultaneously, which can be overwhelming and may compromise the depth of education.
Lack of Specialization: Due to the limited number of teachers, subjects that require specialized knowledge may not be adequately covered. Students in single-teacher schools may miss out on specific subjects like science, mathematics, or languages.
Teaching Quality: In some cases, the teacher in a single-teacher school may lack proper qualifications or training.; this can impact the quality of teaching and limit access to up-to-date knowledge and teaching methodologies.
Infrastructure Challenges: Single-teacher schools often face infrastructure challenges, such as inadequate classrooms, lack of teaching materials, and limited access to technology. These limitations can further hamper the students’ learning experience.
Limited Extracurricular Activities: Due to limited resources and staff, single-teacher schools may struggle to provide various extracurricular activities, depriving students of holistic development opportunities.
The government, NGOs, and other organizations are making efforts to address these consequences. Initiatives include recruiting more teachers, improving infrastructure, providing teacher training programs, and integrating technology into the learning process.

According to the UDISE+ 2021-22 Flash Statistics Report, there are 14.89 lakh schools in India, out of which 10.22 lakhs are government schools. The total number of students in India is 26.52 crores, and the total number of teachers is 95 lakhs. According to the UDISE+ 2021-22 Flash Statistics Report, there are 56,056 single-teacher schools in India. Andhra Pradesh 882, Arunachal Pradesh 1188,  Assam 675, Bihar 17359, Chhattisgarh 1293, Himachal Pradesh 257, Jharkhand 1876, Karnataka 1262, Madhya Pradesh 2424, Odisha 1524, Telangana 513, Uttar Pradesh 10922  and West Bengal 2290 are states which have significant number of single-teacher schools. Using the Samagra Shiksha funding, all schools must be provided with an adequate number of teachers without delay.

Frequently Asked Questions (FAQs)
1: What is the pupil-teacher ratio (PTR), and why is it important in India’s education context?
Answer: The pupil-teacher ratio (PTR) is a measure that indicates the number of students per teacher in a school or educational institution. A lower PTR generally means that each student receives more individual attention and personalized instruction, which can enhance the quality of education and improve learning outcomes. PTR is important in India to ensure that students can engage in meaningful and effective learning experiences.

2: How has the pupil-teacher ratio in India evolved over the years?
Answer: The pupil-teacher ratio in India has evolved significantly. In the early years of the Indian education system, PTRs were generally high due to limited infrastructure and resources. Efforts were made post-independence to expand access to education and reduce PTRs. Education reforms and the Right to Education Act (2009) mandated specific PTR norms, leading to improvements. However, teacher shortages and regional disparities persist, and efforts are ongoing to improve the PTR.

3: What does the Samagra Shiksha scheme in India specify the PTR norms?
Answer: The Samagra Shiksha scheme aims to achieve an optimal Pupil-Teacher Ratio (PTR) to ensure quality education in India. The specific PTR norms for different levels of education are as follows:

Primary Level (I-V): 20:1
Upper Primary Level (VI-VIII): 30:1
Secondary Level (IX-X): 30:1 The scheme also aims to achieve a PTR of 20:1 at all levels of education by 2025. These norms may vary slightly based on the specific needs of a state or district.
4: What does the latest UDISEPlus 2021-22 data reveal about the pupil-teacher ratio in India?
Answer: According to the UDISEPlus 2021-22 data, the pupil-teacher ratio varies across different states and regions in India. On average, at the All India level, the PTR is 26:1 for primary, 19:1 for upper primary, 17:1 for secondary, and 27:1 for higher secondary. However, states have variations, with some exhibiting higher PTRs across all levels. Addressing these disparities is essential to ensure quality education for all.

5: What are the consequences of single-teacher schools in India, and how are they being addressed?
Answer: Single-teacher schools, where one teacher is responsible for multiple grade levels, face challenges like limited attention, multigrade teaching, lack of specialization, and infrastructure issues. Efforts are being made by the government, NGOs, and organizations to address these consequences. Initiatives include recruiting more teachers, improving infrastructure, providing teacher training programs, and integrating technology into the learning process.

6: What can be done to further improve the pupil-teacher ratio in India?
Answer: To improve the pupil-teacher ratio in India, various measures can be taken, including hiring more teachers, deploying teachers more effectively, improving the quality of teachers through training, and providing more resources to schools. Additionally, there should be a focus on early childhood education, promoting inclusive education, and addressing regional disparities in teacher distribution.

7: How can parents and communities contribute to improving the quality of education in India?
Answer: Parents and communities can also improve education by actively engaging with schools and teachers. They can also advocate for adequate infrastructure, resources, and qualified teachers in their local schools to enhance the quality of education.

8: Are there specific government programs and policies to improve the pupil-teacher ratio in India?
Answer: Yes, the Samagra Shiksha scheme is a significant government program in India aimed at improving the pupil-teacher ratio by providing funding, hiring more teachers, and enhancing the quality of education. The Right to Education Act (2009) also mandates specific PTR norms for different levels of education.

9: How can technology be leveraged to improve education and mitigate the challenges of single-teacher schools?
Answer: Technology can play a vital role in improving education by providing online resources, virtual classrooms, and interactive learning materials. In single-teacher schools, technology can help deliver a more comprehensive curriculum, even in the absence of specialized teachers, and facilitate remote learning and teacher training.

10: How can individuals and organizations contribute to addressing the challenges of single-teacher schools in India?
Answer: Individuals and organizations can contribute by supporting initiatives to recruit more teachers, improve infrastructure, and provide teacher training in remote areas. Donations, volunteer teaching programs, and partnerships with local schools can also help address the challenges of single-teacher schools.

    """

    user_text1 = """
        Keep up the good Work. Loved the information
    """


    try:
        summary_result = summarize(user_text)
        print(
            f"Summarize() Snowflake Cortex LLM function result:\n{summary_result.strip()}\n"
        )

        # completion_result = complete(user_text)
        # print(
        #     f"Complete() Snowflake Cortex LLM function result:\n{completion_result.strip()}\n"
        # )

        # answer_result = extract_answer(user_text)
        # print(
        #     f"ExtractAnswer() Snowflake Cortex LLM function result:\n{answer_result}\n"
        # )

        # sentiment_result = sentiment(user_text1)
        # print(
        #     f"Sentiment() Snowflake Cortex LLM function result:\n{sentiment_result}\n"
        # )

        # translation_result = translate(user_text)
        # print(
        #     f"Translate() Snowflake Cortex LLM function result:\n{translation_result.strip()}\n"
        # )

    finally:
        if snowflake_session:
            # Close the Snowflake session
            snowflake_session.close()


if __name__ == "__main__":
    # Run the main function
    main()