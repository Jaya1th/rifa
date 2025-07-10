import mysql.connector
import pandas as pd

def fetch_course_progress_summary():
    try:
        # Connect to the MySQL database
        mydb = mysql.connector.connect(
            host="kpitacademysql.kpit.com",
            database="openedx_prd",
            user="openedxprduser",
            password="OpEn5DxP@dU5ER",
            port=3309
        )
        cursor = mydb.cursor(dictionary=True)

        # Dictionary of course names and their corresponding IDs
        course_dict = {
            "Gen AI to Agentic AI": "course-v1:KPIT+LMSAGAI0223+2025",
            "Basics of Prompt Engineering": "course-v1:KPIT+LMSBPE2605+2025",
            "KGPT Code Assist Plugin": "course-v1:KPIT+LMSGPT0220+2025",
            "Introduction to Gen AI": "course-v1:KPIT+LMSIAI+2025",
            "Introduction to KGPT File Hub": "course-v1:KPIT+LMSIFH0106+2025"
        }

        # Query to fetch course progress data for specific courses
        query = f"""
        SELECT course_id, user_id, course_progress
        FROM openedx_prd.student_courseenrollment
        WHERE course_id IN ({','.join(['%s'] * len(course_dict))})
        """
        cursor.execute(query, list(course_dict.values()))
        rows = cursor.fetchall()

        # Convert to DataFrame
        df = pd.DataFrame(rows)
        if df.empty:
            print("No course enrollment data found for the specified courses.")
            return

        # Group and summarize data
        grouped = df.groupby('course_id')

        for course_name, course_id in course_dict.items():
            if course_id in grouped.groups:
                group = grouped.get_group(course_id)
                total_enrolled = group['user_id'].nunique()
                total_completed = (group['course_progress'] == 100).sum()
                total_not_completed = total_enrolled - total_completed
                course_status = 'Completed' if total_enrolled == total_completed else 'Not Completed'

                print(f"Course Name: {course_name}")
                print(f"Total Enrolled: {total_enrolled}")
                print(f"Total Completed: {total_completed}")
                print(f"Total Not Completed: {total_not_completed}")
                print(f"Course Status: {course_status}")
                print("-" * 50)
            else:
                print(f"Course Name: {course_name}")
                print("Total Enrolled: 0")
                print("Total Completed: 0")
                print("Total Not Completed: 0")
                print("Course Status: No Enrollment")
                print("-" * 50)

        cursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")

# Example usage
if __name__ == "__main__":
    fetch_course_progress_summary()
