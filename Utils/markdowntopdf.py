import pdfkit

def markdown_to_pdf(markdown_text, output_filename="output.pdf"):
    """
    Converts Markdown text to a PDF file.
    """
    try:
        # Convert Markdown to HTML
        import markdown
        html_content = markdown.markdown(markdown_text)

        # Specify the path to wkhtmltopdf
        config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  # Update this path

        # Convert HTML to PDF
        pdfkit.from_string(html_content, output_filename, configuration=config)

        print(f"PDF saved as {output_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    markdown_content = """
    Preparing for a **Google Data Engineer** interview requires a combination of technical expertise, problem-solving skills, and a deep understanding of data engineering concepts. Google looks for candidates who can design scalable data systems, optimize data pipelines, and work with large datasets. Here's a comprehensive guide to help you prepare:

---

### **1. Understand the Role and Responsibilities**
Google Data Engineers are responsible for:
- Designing and building scalable data pipelines.
- Working with large-scale distributed systems.
- Optimizing data storage and retrieval.
- Collaborating with data scientists, analysts, and software engineers.
- Ensuring data quality, reliability, and efficiency.

Review the job description for the specific role you're targeting to understand the expectations.

---

### **2. Master Core Data Engineering Concepts**
Focus on the following key areas:
- **Data Modeling**: Understand relational and non-relational data models, normalization, and denormalization.
- **ETL/ELT Processes**: Learn how to extract, transform, and load data.
- **Distributed Systems**: Study concepts like sharding, replication, and partitioning.
- **Big Data Technologies**: Gain expertise in tools like Hadoop, Spark, and Hive.
- **Data Warehousing**: Learn about data warehouses (e.g., BigQuery, Snowflake, Redshift) and data lakes.
- **Streaming Data**: Understand real-time data processing with tools like Kafka, Flink, or Spark Streaming.

---

### **3. Learn Google's Data Ecosystem**
Google has its own suite of data tools and technologies. Familiarize yourself with:
- **BigQuery**: A serverless, highly scalable data warehouse.
- **Cloud Dataflow**: A fully managed stream and batch data processing service.
- **Cloud Pub/Sub**: A messaging service for event-driven systems.
- **Cloud Storage**: A scalable object storage service.
- **Dataproc**: A managed Hadoop and Spark service.
- **Data Studio**: A tool for data visualization and reporting.

---

### **4. Master Key Programming Languages and Tools**
Google Data Engineers often use:
- **SQL**: Advanced SQL skills are a must (e.g., window functions, joins, subqueries).
- **Python**: Learn Python for scripting and data processing.
- **Java/Scala**: These are commonly used for big data processing frameworks like Spark.
- **Bash/Shell Scripting**: Useful for automation and pipeline management.

---

### **5. Practice System Design**
Google places a strong emphasis on system design. Be prepared to design scalable and efficient data systems. Focus on:
- **Data Pipeline Design**: How to ingest, process, and store data at scale.
- **Data Storage Solutions**: When to use relational databases, NoSQL, or distributed file systems.
- **Scalability and Performance**: How to handle large volumes of data and optimize queries.
- **Fault Tolerance and Reliability**: Ensure systems are robust and can handle failures.

Practice designing systems like:
- A real-time analytics pipeline.
- A recommendation system.
- A log processing system.

---

### **6. Prepare for Coding Interviews**
Google's interview process includes coding challenges. Focus on:
- **Data Structures and Algorithms**: Practice problems on arrays, strings, trees, graphs, and dynamic programming.
- **SQL Challenges**: Solve complex SQL problems on platforms like LeetCode, HackerRank, or StrataScratch.
- **Python/Java Coding**: Practice writing efficient and clean code.

Use platforms like:
- LeetCode
- HackerRank
- CodeSignal
- Kaggle (for SQL and data processing challenges)

---

### **7. Prepare for Behavioral Interviews**
Google evaluates cultural fit and collaboration skills. Be ready to answer questions like:
- Tell me about a time you solved a challenging data engineering problem.
- How do you handle conflicting priorities?
- Describe a project where you collaborated with cross-functional teams.

Use the **STAR method** (Situation, Task, Action, Result) to structure your answers.

---

### **8. Work on Real-World Projects**
Build a portfolio of data engineering projects to showcase your skills. Examples include:
- Building an ETL pipeline to process and analyze large datasets.
- Designing a real-time data streaming system.
- Creating a data warehouse for a mock business.
- Optimizing a slow-running SQL query or data pipeline.

Use tools like:
- Apache Airflow
- Apache Spark
- Google Cloud Platform (BigQuery, Dataflow, etc.)
- Docker and Kubernetes (for containerization and orchestration)

---

### **9. Study Google's Interview Process**
Google's interview process typically includes:
1. **Phone Screen**: Coding and SQL challenges.
2. **Technical Interviews**: Coding, SQL, and system design.
3. **Onsite Interviews**: Coding, system design, and behavioral questions.

Practice mock interviews to simulate the real experience.

---

### **10. Stay Updated on Industry Trends**
Google values candidates who are aware of the latest trends in data engineering. Stay updated on:
- Cloud-based data solutions (GCP, AWS, Azure).
- Data mesh and data lakehouse architectures.
- Real-time data processing and analytics.
- Machine learning and AI integration with data pipelines.

---

### **Recommended Resources**
- **Books**:
  - *Designing Data-Intensive Applications* by Martin Kleppmann.
  - *Big Data: Principles and Best Practices* by Nathan Marz.
- **Online Courses**:
  - Data Engineering on Google Cloud (Coursera).
  - Apache Spark and Python for Big Data (Udemy).
  - DataCamp (for SQL and Python).
- **Practice Platforms**:
  - LeetCode (coding and SQL).
  - StrataScratch (SQL and data engineering problems).
  - HackerRank (coding challenges).

---

### **Final Tips**
- Network with current or former Google employees to gain insights into the role and interview process.
- Tailor your resume to highlight relevant data engineering experience.
- Be prepared to discuss your projects in detail during interviews.

By focusing on these areas, you'll be well-prepared to tackle the Google Data Engineer interview and demonstrate your expertise in building scalable, efficient data systems. Good luck!
    """
    markdown_to_pdf(markdown_content, "markdown_output.pdf")