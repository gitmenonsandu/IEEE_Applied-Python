import re
string="Vision - To facilitate transformation of students into good human beings, responsible citizens and competent professionals, focusing on assimilation, generation and dissemination of knowledge. Mission - Impart quality education to meet the needs of profession and society, and achieve excellence in teaching-learning and research. Attract and develop talented and committed human resource, and provide an environment conducive to innovation, creativity, team-spirit and entrepreneurial leadership. Facilitate effective interactions among faculty and students, and foster networking with alumni, industries, institutions and other stake-holders.Practice and promote high standards of professional ethics, transparency and accountability."
list=re.findall(r"and (.+?) and",string)
for i in range(len(list)):
	print list[i]
	