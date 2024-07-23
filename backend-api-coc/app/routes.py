from flask import request, jsonify

from app.models import Pendaftar
from app import app, db
import os

@app.route("/api/add", methods=["POST","GET"])
def add():
    allData = Pendaftar.query.all()
    allEmail = []
    for isi in allData:
        allEmail.append(isi.email)

 
    try:
        data = request.form
        print("Tes1")
        if len(data['nama_lengkap']) < 2:
            print(f"Data nama {data['nama_lengkap']} < 2")
            return jsonify({"message":"nama"})
        print("Tes2")
        
        if len(data['email']) < 2 or "@" not in data['email']:
            print(f"Data email {data['email']} < 2")
            return jsonify({"message":"email"})
        print("Tes3")
        
        if len(data['telepon']) < 2:
            print(f"Data telepon {data['telepon']} < 2")
            return jsonify({"message":"telepon"})
        print("Tes4")
        
        if data['email'] in allEmail:
            return jsonify({"message":"emailtrue"})
        print("Tes5")
        
        photo = request.files['file']

        print(data['nama_lengkap'])
        orangDaftar = Pendaftar(nama_lengkap=data['nama_lengkap'], email=data['email'], no_telp=data['telepon'], bukti_transfer=f'bukti_tf{data["email"]}.jpg')
        print(os.getcwd())
        photo_path = os.path.join(os.getcwd(), f'app/static/bukti_tf{data["email"]}.jpg')
        print(photo_path.join)
        photo.save(photo_path)
        db.session.add(orangDaftar)
        db.session.commit()
        print(orangDaftar)
        return jsonify({"message":"success","nama":"t"})
    except:
        db.session.rollback()
        return jsonify({"message":"error"})
        

@app.route("/api/<pendaftar>", methods=["GET","POST"])
def orang(pendaftar):
    data = Pendaftar.query.filter_by(email=pendaftar).first()
    print(bool(data))
    if data:
        newData = {
            "nama_lengkap":data.nama_lengkap,
            "email":data.email,
            "telepon":data.no_telp,
            "bukti_tf":data.bukti_transfer,
            "status":"Berhasil Mendaftar"
        }
        return jsonify(newData)
    else:
        newData = {
            "nama_lengkap":pendaftar,
            "email":"Tidak ada",
            "telepon":"Tidak ada",
            "bukti_tf":"Tidak ada",
            "status":"Tidak Terdaftar"
        }
        return jsonify(newData)


@app.route("/api/get/<nama>/<kunci>", methods=["GET","POST"])
def ambil(nama, kunci):
    print(nama, kunci)
    if nama == "coc02" and kunci == "coconut@013":
        print("True")
        data = Pendaftar.query.all()
        newData = {}
        for isi in data:
            newData[str(isi.id)] = {}
            newData[str(isi.id)]['nama_lengkap'] = isi.nama_lengkap
            newData[str(isi.id)]['email'] = isi.email
            newData[str(isi.id)]['telepon'] = isi.no_telp
            newData[str(isi.id)]['bukti_transfer'] = f"/static/{isi.bukti_transfer}"
        return jsonify({"message":"success","data":newData})
    return jsonify({"message":"Tidak memiliki akses!"})
