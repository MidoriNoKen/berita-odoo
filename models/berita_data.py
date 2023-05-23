from odoo import models, fields, api


class berita_data(models.Model):
    _name = 'berita.beritadata'
    _description = 'berita.beritadata'

    name = fields.Char(String='ID Berita', required=True)
    proyek = fields.Many2one("project.project", String='Nama Proyek', required=True)
    judul = fields.Char(String='Judul', required=True)
    penulis = fields.Char(String='Penulis', required=True)
    tanggal = fields.Date(String='Tanggal Posting', required=True)
    kategori = fields.Text(String='Kategori', required=True)
    teks = fields.Text(String='Teks Berita', required=True)
    tl_bukti_file = fields.Binary(String='File Bukti', attachment=True, required=True)

