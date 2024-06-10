from flask import Flask, jsonify, request
from db_connections.connections import session
from model.table import Indian_colleges_table

app = Flask(__name__)


# Give all colleges
@app.route('/get_all_colleges_list', methods=['GET'])
def get_all_colleges_list():
    colleges = session.query(Indian_colleges_table).all()
    colleges_list = [
        {'id': college.id, 'name': college.name, 'city': college.city, 'state': college.state,
         'rank': college.rank, 'fees': college.fees, 'courses': college.courses} for college in colleges]
    return jsonify({'data': colleges_list})


# Get a specific college
@app.route('/get_particular_colleges', methods=['GET'])
def get_particular_colleges():
    data = []
    result = request.args.get('id')
    colleges = session.query(Indian_colleges_table).filter(Indian_colleges_table.id == result).all()
    if colleges:
        colleges_list = [
            {'id': college.id, 'name': college.name, 'city': college.city, 'state': college.state,
             'rank': college.rank, 'fees': college.fees, 'courses': college.courses} for college in colleges]
        return jsonify({'data': colleges_list})
    else:
        return jsonify({'message': 'College not found'}), 404


# Insert a new College
@app.route('/add_college', methods=['POST'])
def add_college():
    new_college_data = request.get_json()
    new_college = Indian_colleges_table(
        id=new_college_data['id'],
        name=new_college_data['name'],
        city=new_college_data['city'],
        state=new_college_data['state'],
        rank=new_college_data['rank'],
        fees=new_college_data['fees'],
        courses=new_college_data['courses']
    )
    session.add(new_college)
    session.commit()
    return jsonify({'message': 'New College added successfully'})


# Update an existing college
@app.route('/update_college', methods=['PATCH'])
def update_college():
    user_data = request.get_json()
    session.query(Indian_colleges_table).filter(Indian_colleges_table.id == user_data.get('id')).update(user_data)

    session.commit()
    return jsonify({'message': 'College details updated successfully'})


# Delete a college
@app.route('/delete_college', methods=['DELETE'])
def delete_college():
    data = request.get_json()
    college = session.query(Indian_colleges_table).filter(Indian_colleges_table.id == data.get('id')).delete()
    session.commit()
    return jsonify({'message': 'College deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
