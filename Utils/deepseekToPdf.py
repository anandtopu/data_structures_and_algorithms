from fpdf import FPDF

def text_to_pdf(text, output_filename="output.pdf"):
    """
    Converts a given text into a PDF file.

    :param text: The text content to be converted to PDF.
    :param output_filename: The name of the output PDF file.
    """
    # Create an instance of FPDF
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font for the text
    pdf.set_font("Arial", size=12)

    # Add the text to the PDF
    pdf.multi_cell(0, 10, txt=text)

    # Save the PDF to a file
    pdf.output(output_filename)

    print(f"PDF saved as {output_filename}")

# Example usage
if __name__ == "__main__":
    # Example DeepSeek response
    deepseek_response = """
    Preparing for a **Meta (Facebook) Data Engineer** role requires a combination of technical skills, problem-solving abilities, and a deep understanding of data engineering concepts. Meta looks for candidates who can design, build, and optimize scalable data pipelines, work with large datasets, and collaborate with cross-functional teams. Here's a step-by-step guide to help you prepare:

---

### **1. Understand the Role and Responsibilities**
Meta Data Engineers are responsible for:
- Designing and building scalable data pipelines.
- Working with large-scale distributed systems.
- Optimizing data storage and retrieval.
- Collaborating with data scientists, analysts, and software engineers.
- Ensuring data quality, reliability, and efficiency.

Familiarize yourself with the job description for the specific role you're targeting.

---

### **2. Build a Strong Foundation in Data Engineering Concepts**
Master the following core concepts:
- **Data Modeling**: Understand relational and non-relational data models, normalization, and denormalization.
- **ETL/ELT Processes**: Learn how to extract, transform, and load data.
- **Distributed Systems**: Study concepts like sharding, replication, and partitioning.
- **Big Data Technologies**: Gain expertise in tools like Hadoop, Spark, and Hive.
- **Data Warehousing**: Learn about data warehouses (e.g., Snowflake, Redshift) and data lakes.
- **Streaming Data**: Understand real-time data processing with tools like Kafka, Flink, or Spark Streaming.

---

### **3. Master Key Programming Languages and Tools**
Meta Data Engineers often use:
- **SQL**: Advanced SQL skills are a must (e.g., window functions, joins, subqueries).
- **Python**: Learn Python for scripting and data processing.
- **Java/Scala**: These are commonly used for big data processing frameworks like Spark.
- **Bash/Shell Scripting**: Useful for automation and pipeline management.

Familiarize yourself with Meta's tech stack, which may include:
- **Presto/Trino**: Distributed SQL query engine.
- **Spark**: For large-scale data processing.
- **Hive**: Data warehouse infrastructure.
- **Airflow**: Workflow orchestration.

---

### **4. Practice System Design**
Meta places a strong emphasis on system design. Be prepared to design scalable and efficient data systems. Focus on:
- **Data Pipeline Design**: How to ingest, process, and store data at scale.
- **Data Storage Solutions**: When to use relational databases, NoSQL, or distributed file systems.
- **Scalability and Performance**: How to handle large volumes of data and optimize queries.
- **Fault Tolerance and Reliability**: Ensure systems are robust and can handle failures.

Practice designing systems like:
- A real-time analytics pipeline.
- A recommendation system.
- A log processing system.

---

### **5. Learn Meta's Data Infrastructure**
Meta has a unique data infrastructure. Research and understand:
- **Scuba**: Real-time data analysis system.
- **TAO**: Distributed data store for social graph data.
- **ZuckDB**: Meta's internal data warehouse.
- **FBData**: Meta's data processing framework.

While you may not have direct experience with these tools, understanding their purpose and how they fit into Meta's ecosystem will help you during interviews.

---

### **6. Practice Coding and Problem-Solving**
Meta's interview process includes coding challenges. Focus on:
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
Meta evaluates cultural fit and collaboration skills. Be ready to answer questions like:
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
- AWS/GCP/Azure (for cloud-based data solutions)
- Docker and Kubernetes (for containerization and orchestration)

---

### **9. Study Meta's Interview Process**
Meta's interview process typically includes:
1. **Phone Screen**: Coding and SQL challenges.
2. **Technical Interviews**: Coding, SQL, and system design.
3. **Onsite Interviews**: Coding, system design, and behavioral questions.

Practice mock interviews to simulate the real experience.

---

### **10. Stay Updated on Industry Trends**
Meta values candidates who are aware of the latest trends in data engineering. Stay updated on:
- Cloud-based data solutions (AWS, GCP, Azure).
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
- Network with current or former Meta employees to gain insights into the role and interview process.
- Tailor your resume to highlight relevant data engineering experience.
- Be prepared to discuss your projects in detail during interviews.

By focusing on these areas, you'll be well-prepared to tackle the Meta Data Engineer interview and demonstrate your expertise in building scalable, efficient data systems. Good luck!
    """

    # Convert the response to a PDF
    text_to_pdf(deepseek_response, "meta_data_engineer.pdf")