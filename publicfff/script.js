window.onload = function(){
    const apiUrl = "https://coconutopenclass.pythonanywhere.com/api/getdata";
    fetch(apiUrl)
    .then(response => {
      if (!response.ok){
        throw new Error("Gagal mengambil data");
      }
      return response.json();
    })
    .then(data => {
        document.getElementById("nama").innerText = data.nama;
        document.getElementById("usia").innerText = data.usia;
      console.log(data);
    })
    .catch(error => {
      console.error("Terjadi kesalahan baru");
    })
  }