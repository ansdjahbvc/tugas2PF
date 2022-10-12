from cmath import tan
from collections import namedtuple

tanggal = namedtuple('tanggal', ['hari', 'bulan', 'tahun'])

hari_ini = tanggal(12, 10, 2022)
kemarin = tanggal(11, 10, 2022)
besok = tanggal(13, 10, 2022)
print(hari_ini)
print(kemarin)
print(besok)
