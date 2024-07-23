from app import db

class Pendaftar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(64))
    email = db.Column(db.String(64))
    no_telp = db.Column(db.String(64))
    bukti_transfer = db.Column(db.String(64))
    def __repr__(self):
        return f"<Pendaftar {self.nama_lengkap}>"