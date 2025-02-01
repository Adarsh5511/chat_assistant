import sqlite3
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


DB_PATH = "company.db"


class ChatAssistant:
    def __init__(self, db_path):
        self.db_path = db_path

    def execute_query(self, query):
        """Execute a SQL query and return the results."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results

    def handle_query(self, user_input):
        """Process user input and generate a response."""
        user_input = user_input.lower()

    
        if "show me all employees in the" in user_input:
            department = user_input.split("department")[0].split("the")[-1].strip()
            department = department.capitalize()  
            query = f"SELECT Name FROM Employees WHERE Department = '{department}'"
            results = self.execute_query(query)
            if results:
                return f"Employees in {department}: {', '.join([row[0] for row in results])}"
            else:
                return f"No employees found in the {department} department."

        elif "who is the manager of the" in user_input:
            department = user_input.split("department")[0].split("the")[-1].strip()
            department = department.capitalize()  
            query = f"SELECT Manager FROM Departments WHERE Name = '{department}'"
            results = self.execute_query(query)
            if results:
                return f"The manager of {department} is {results[0][0]}."
            else:
                return f"No manager found for the {department} department."

        elif "list all employees hired after" in user_input:
            date = user_input.split("after")[-1].strip()
            query = f"SELECT Name FROM Employees WHERE Hire_Date > '{date}'"
            results = self.execute_query(query)
            if results:
                return f"Employees hired after {date}: {', '.join([row[0] for row in results])}"
            else:
                return f"No employees hired after {date}."

        elif "what is the total salary expense for the" in user_input:
            department = user_input.split("department")[0].split("the")[-1].strip()
            department = department.capitalize()  
            query = f"SELECT SUM(Salary) FROM Employees WHERE Department = '{department}'"
            results = self.execute_query(query)
            if results and results[0][0]:
                return f"Total salary expense for {department}: ₹{results[0][0]}"
            else:
                return f"No salary data found for the {department} department."

        else:
            return "Sorry, I couldn't understand your query. Please try again."



assistant = ChatAssistant(DB_PATH)



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('query')
    if not user_input:
        return jsonify({"error": "No query provided"}), 400

 
    response = assistant.handle_query(user_input)
    return jsonify({"response": response})



if __name__ == '__main__':
    app.run(debug=True)
