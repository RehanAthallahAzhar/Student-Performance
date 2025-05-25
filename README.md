# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Institut, berdiri sejak tahun 2000, Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun belakangan ini institusi menghadapi tantangan serius: tingginya angka siswa yang tidak menyelesaikan pendidikan (dropout).

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Isu dropout sangat krusial karena berpengaruh langsung pada citra institusi.  Setiap siswa yang berhenti sebelum lulus menimbulkan reputasi yang buruk di mata calon mahasiswa baru.Oleh karena itu, Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Dengan menganalisis prediktor-prediktor risiko dropout menggunakan dataset [students_performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md), Jaya Institut dapat:

1. Mendeteksi dini -> mengidentifikasi siswa berisiko tinggi sebelum keputusan berhenti diambil.

2. Intervensi terfokus -> memberikan bimbingan akademik maupun psikologis sesuai kebutuhan individu sehingga mencegah mahasiswa dropout

3. Mengurangi dropout -> menurunkan angka putus studi, meningkatkan pendapatan dan reputasi, serta memenuhi target kualitas pendidikan.

Dengan demikian, proyek ini tidak hanya memperkuat daya saing dan keberlanjutan institusi, tetapi juga meningkatkan kualitas pengalaman belajar bagi seluruh siswa.




### Permasalahan Bisnis
1. Jaya Institut mengalami kesulitan dalam mengenali faktor-faktor kunci yang memicu siswa dropout.
2. Institusi pendidikan belum ada mekanisme pemantauan yang andal untuk menemukan indikasi siswa berisiko putus sekolah secara langsung
3. Belum adanya alat prediktif untuk mengambil keputusan strategis dalam upaya menurunkan angka dropout.

### Persiapan

Setup environment: 

1. Clone repository
2. Download dataset pada link berikut [student dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)
3. Jalankan perintah dibawah 
    ```
        conda activate student-performance
        pip install -r requirements.txt
        jupyter notebook .
    ```

atau bisa jalankan pada environment google collab

## Business Dashboard
Dashboard ini berisi parameter parameter penting yang dapat digunakan untuk memantau sebaran data mahasiswa yang dropout dan juga memonitor mahasiswa agar institusi dapat mendeteksi dan mengambil tindakan dini untuk mencegah mahasiswa dropout. 

Berikut link Dashboard yang bisa anda buka
[Student Performance Dashboard](https://public.tableau.com/app/profile/rehan.azhar/viz/studentperformancedashboard_17467815293880/Dashboard1)

## Menjalankan Sistem Machine Learning
Model Random Forest ini dapat digunakan untuk membantu sekolah mengidentifikasi lebih awal mana siswa yang berisiko tidak lulus . Berikut cara menjalankan model yg telah dibuat.
1. Buka terminal di folder student performance
2. Jalankan perintah dibawah
    ```
    streamlit run app.py
    ```
3. Jika berhasil dijalankan, isi data sesuai format yg ditetapkan dan klik tombol predict

Atau bisa mencoba model melalui link berikut [Student Performance Model](https://student-performance-oz2dqvdju8lxbstt8swapi.streamlit.app/)

## Conclusion
1. Secara keseluruhan, tingkat dropout mahasiswa, baik internasional maupun domestik, cukup tinggi, dan status kelulusan sangat dipengaruhi oleh berbagai faktor.
2. Faktor-faktor yg menjadi pemicu mahasiswa dropout dapat dilihat melalui hasil analisis PCA yang meliputi
    - Perbandingan mahasiswa yg tidak menerima beasiswa cenderung memiliki tingkat dropout lebih tinggi daripada yg tidak meneirma beasiswa
    - Mahasiswa yg terlantar cenderung memiliki tingkat dropout lebih tinggi
    - Mahasiswa laki-laki cenderung memiliki tingkat dropout lebih tinggi dibanding perempuan.
    - Keluarga mahasiswa yang memiliki pinjaman cenderung memiliki tingkat dropout yang tinggi
    - Masalah biaya pendidikan menunggak juga menjadi salah satu faktor penting

3. Pipeline data preprocessing dan model prediktif menggunakan Random Forest yang dapat memungkinkan integrasi ke dalam sistem operasional institusi untuk memantau status setiap siswa secara langsung dan mengeluarkan peringatan dini bila probabilitas dropout melewati ambang batas.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
1. **Perkuat dukungan akademik di semester awal**
Banyak mahasiswa gagal di semester awal. Fokuskan bimbingan dan monitoring intensif pada semester 1 dan 2.

2. **Bantu mahasiswa dengan kesulitan keuangan**
Fitur Debtor dan Tuition_fees_up_to_date sangat memengaruhi kelulusan. Tawarkan program bantuan keuangan atau beasiswa.

3. **Pantau dan evaluasi mahasiswa dengan latar belakang kurang mampu**
Mahasiswa dengan orang tua dengan pendidikan rendah atau pendapatan rendah memerlukan perhatian tambahan.

4. **Fasilitasi pembelajaran yang mendukung penyelesaian mata kuliah**
Mahasiswa yang menyelesaikan lebih banyak mata kuliah punya peluang lulus lebih besar. Dorong partisipasi dan hindari "tidak hadir ujian".
