import argparse
import urllib2

# Base Url
URL_SERIE_360 = "http://sc.cuevana.tv/files/s/sub/ID_ES.srt"
URL_SERIE_720 = "http://sc.cuevana.tv/files/s/sub/ID_ES_720.srt"
URL_PELICULA_360 = "http://sc.cuevana.tv/files/sub/ID_ES.srt"
URL_PELICULA_720 = "http://sc.cuevana.tv/files/sub/ID_ES_720.srt"
# URL_BASE = "http://sc.cuevana.tv/files[/s]/files/sub/{ID}_ES[_720].srt"

# Config Parser
parser = argparse.ArgumentParser(
								add_help=True,
								description="Download subtitles from cuevana",
								prog='subCuevana.py',
								)
groupType = parser.add_mutually_exclusive_group(required=True)
groupType.add_argument('-s',
						'--serie',
						action='store_true',
						dest='serie',
						help='Select Serie')
groupType.add_argument('-m',
						'--movie',
						action='store_true',
						dest='movie',
						help='Select Movie')
parser.add_argument('-q',
					'--quality',
					action='store',
					choices=('360', '720'),
					dest='quality',
					help='Select Quality',
					required=True)

parser.add_argument('num', help='Num of the Serie or Movie')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
args = parser.parse_args()
# print args

def openUrl(url):
	"""Return Request from url"""
	return urllib2.urlopen(url)

def save(text, fn):
	"""Save text in file"""
	f = open(fn, 'w')
	f.write(text)
	f.close()


if args.serie:
	if args.quality == 360:
		req = openUrl(URL_SERIE_360.replace('ID', args.num))
	else:
		req = openUrl(URL_SERIE_720.replace('ID', args.num))
else:
	if args.quality == 360:
		req = openUrl(URL_PELICULA_360.replace('ID', args.num))
	else:
		req = openUrl(URL_PELICULA_720.replace('ID', args.num))

save(req.read(), args.num+'.srt')