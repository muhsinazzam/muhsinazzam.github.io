from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
app.template_folder = 'templates'

# Database sederhana untuk menyimpan data pasien
patients = []

@app.route('/')
def home():
    return ("Home")
# Rute untuk menampilkan formulir tambah pasien (GET) dan menambahkan pasien (POST)
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'GET':
        # Tampilkan formulir tambah pasien
        print("GET request received")  # Tambahkan pernyataan ini
        return render_template('')

    elif request.method == 'POST':
        data = request.form
        print("POST request received")  # Tambahkan pernyataan ini
        print(data)  # Tambahkan pernyataan ini untuk melihat data formulir yang diterima
        if 'name' in data and 'age' in data and 'gender' in data:
            name = data['name']
            age = data['age']
            gender = data['gender']

            patient = {
                'name': name,
                'age': age,
                'gender': gender
            }

            patients.append(patient)
            return jsonify({'message': 'Pasien berhasil ditambahkan'}), 201
        else:
            return jsonify({'error': 'Data pasien tidak lengkap'}), 400

# Rute untuk mendapatkan daftar semua pasien
@app.route('/get_patients', methods=['GET'])
def get_patients():
    return jsonify({'patients': patients})

if __name__ == '__main__':
    app.run(debug=True)
