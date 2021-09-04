import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import tkinter.font as font

from unidecode import unidecode

import re
import os

user = os.getlogin()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.gui()

    def gui(self):
        myFont = font.Font(family="Terminal", size=22)

        canvas.pack()

        label = tk.Label(self, text='Create alternative channel names for Webgrab+ config file')
        label.config(font=('Helvetica', 16))
        label.grid(row=0, column=2, padx=0, pady=100)
        
        start = tk.Button(self, height=3, width=15, text="Create", fg="blue", command=self.run)
        start.grid(row=1, column=1, padx=50, pady=300)
        start['font'] = myFont

        ex = tk.Button(self, height=3, width=15, text="Exit", fg="red", command=self.master.destroy)
        ex.grid(row=1, column=3, padx=50, pady=300)
        ex['font'] = myFont


    def run(self):
        ret = messagebox.askquestion(title='Alternative channels', message='Would you like to generate alternative channel names?')
        if ret == 'yes':
            messagebox.showinfo(title='File selection', message='Select a WebGrab++.config file.')
            org_dest = filedialog.askopenfilename(filetypes=(("XML Files", "*.xml"),))
            print(org_dest)

        else:
            return
        
        # Desktop
        dest = 'C:\\Users\\'+user+'\\Desktop\\'

        # Open file
        f = open (org_dest, 'r', encoding='utf-8')#, errors='ignore') #, encoding='utf-8')

        # Read lines
        webConfig = f.read()
        tempList = ['\t<channel same_as="{chann_id}" xmltv_id="{chann}{sd} {cc}">{chann}{sd} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{chann}{fhd} {cc}">{chann}{fhd} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{chann}{ww} {cc}">{chann}{ww} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{chann}{sd}{ww} {cc}">{chann}{sd}{ww} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{chann}{hd}{ww} {cc}">{chann}{hd}{ww} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{chann}{fhd}{ww} {cc}">{chann}{fhd}{ww} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc} {chann}">{cc} {chann}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc} {chann}{sd}">{cc} {chann}{sd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc} {chann}{hd}">{cc} {chann}{hd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc} {chann}{fhd}">{cc} {chann}{fhd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}: {chann}">{cc}: {chann}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}: {chann}{sd}">{cc}: {chann}{sd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}: {chann}{hd}">{cc}: {chann}{hd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}: {chann}{fhd}">{cc}: {chann}{fhd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}| {chann}">{cc}| {chann}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}| {chann}{sd}">{cc}| {chann}{sd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}| {chann}{hd}">{cc}| {chann}{hd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}| {chann}{fhd}">{cc}| {chann}{fhd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="|{cc}| {chann}">|{cc}| {chann}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="|{cc}| {chann}{sd}">|{cc}| {chann}{sd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="|{cc}| {chann}{hd}">|{cc}| {chann}{hd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="|{cc}| {chann}{fhd}">|{cc}| {chann}{fhd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{chann}">{chann}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{chann}{sd}">{chann}{sd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{chann}{hd}">{chann}{hd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{chann}{fhd}">{chann}{fhd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{norm}{sd} {cc}">{norm}{sd} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{norm}{fhd} {cc}">{norm}{fhd} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{norm}{ww} {cc}">{norm}{ww} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{norm}{sd}{ww} {cc}">{norm}{sd}{ww} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{norm}{hd}{ww} {cc}">{norm}{hd}{ww} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{norm}{fhd}{ww} {cc}">{norm}{fhd}{ww} {cc}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc} {norm}">{cc} {norm}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc} {norm}{sd}">{cc} {norm}{sd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc} {norm}{hd}">{cc} {norm}{hd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc} {norm}{fhd}">{cc} {norm}{fhd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}: {norm}">{cc}: {norm}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}: {norm}{sd}">{cc}: {norm}{sd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}: {norm}{hd}">{cc}: {norm}{hd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}: {norm}{fhd}">{cc}: {norm}{fhd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}| {norm}">{cc}| {norm}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}| {norm}{sd}">{cc}| {norm}{sd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}| {norm}{hd}">{cc}| {norm}{hd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{cc}| {norm}{fhd}">{cc}| {norm}{fhd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="|{cc}| {norm}">|{cc}| {norm}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="|{cc}| {norm}{sd}">|{cc}| {norm}{sd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="|{cc}| {norm}{hd}">|{cc}| {norm}{hd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="|{cc}| {norm}{fhd}">|{cc}| {norm}{fhd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{norm}">{norm}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{norm}{sd}">{norm}{sd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{norm}{hd}">{norm}{hd}</channel>\n', 
                    '\t<channel same_as="{chann_id}" xmltv_id="{norm}{fhd}">{norm}{fhd}</channel>\n']
        
        # Find channels in Webgrab config
        channList = re.findall('\s*<chann.*site_channel=".*" xmltv_id="(.*?)">.*<\/channel>', webConfig)

        # Find country code prefix
        try:
            ccList = re.findall('\s*<chann.*site_channel=".*" xmltv_id=".*\s\w{2,3}">.*<\/channel>', webConfig)
            cc = ccList[0]
        except:
            cc = 'XX'
     
        with open(dest+'output.xml', 'wb') as subChann:
            for chann_id in channList:
                try:
                    getPrefix = re.findall(r'\s(\w{2,3})$', chann_id)
                    cc = getPrefix[0]
                    if cc != cc.upper():
                        cc = 'XX'
                except:
                    cc = 'XX'
                    
                for item in tempList:
                    chann = re.sub('\s*{cc}$'.format(cc=cc), '', chann_id)
                    norm = unidecode(chann)

                    sd = ' SD'
                    hd = ' HD'
                    fhd = ' FHD'
                    ww = ' VIP'

                    nonList = ['SD', 'HD', 'FHD']

                    if '4K' in chann_id or 'UHD' in chann_id:
                        sd = ''
                        hd = ''
                        fhd = ''

                    if any(x in chann_id for x in nonList):
                        for x in nonList:
                            chann_id = re.sub(' ' + x, '', chann_id)
                            chann = re.sub(' ' + x, '', chann)

                    result = ''

                    prefList_a = ['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BH', 'BS', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'UG', 'UA', 'AE', 'GB', 'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW']

                    prefList_b = ['ABW', 'AFG', 'AGO', 'AIA', 'ALA', 'ALB', 'AND', 'ANT', 'ARE', 'ARG', 'ARM', 'ASM', 'ATA', 'ATF', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLM', 'BLR', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'BVT', 'BWA', 'CAF', 'CAN', 'CCK', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COK', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CXR', 'CYM', 'CYP', 'CZE', 'DEU', 'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESH', 'ESP', 'EST', 'ETH', 'FIN', 'FJI', 'FLK', 'FRA', 'FRO', 'FSM', 'GAB', 'GBR', 'GEO', 'GGY', 'GHA', 'GIB', 'GIN', 'GLP', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GRL', 'GTM', 'GUF', 'GUM', 'GUY', 'HKG', 'HMD', 'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IMN', 'IND', 'IOT', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JEY', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LIE', 'LKA', 'LSO', 'LTU', 'LUX', 'LVA', 'MAC', 'MAF', 'MAR', 'MCO', 'MDA', 'MDG', 'MDV', 'MEX', 'MHL', 'MKD', 'MLI', 'MLT', 'MMR', 'MNE', 'MNG', 'MNP', 'MOZ', 'MRT', 'MSR', 'MTQ', 'MUS', 'MWI', 'MYS', 'MYT', 'NAM', 'NCL', 'NER', 'NFK', 'NGA', 'NIC', 'NIU', 'NLD', 'NOR', 'NPL', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PCN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRI', 'PRK', 'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'REU', 'ROU', 'RUS', 'RWA', 'SAU', 'SDN', 'SEN', 'SGP', 'SGS', 'SHN', 'SJM', 'SLB', 'SLE', 'SLV', 'SMR', 'SOM', 'SPM', 'SRB', 'STP', 'SUR', 'SVK', 'SVN', 'SWE', 'SWZ', 'SYC', 'SYR', 'TCA', 'TCD', 'TGO', 'THA', 'TJK', 'TKL', 'TKM', 'TLS', 'TON', 'TTO', 'TUN', 'TUR', 'TUV', 'TWN', 'TZA', 'UGA', 'UKR', 'UMI', 'URY', 'USA', 'UZB', 'VAT', 'VCT', 'VEN', 'VGB', 'VIR', 'VNM', 'VUT', 'WLF', 'WSM', 'YEM', 'ZAF', 'ZMB', 'ZWE']
                    
                    if cc not in prefList_a and cc not in prefList_b:
                        if '{ww}' in item and not '{norm}' in item and not '{cc}' in item:
                            result = item.format(chann_id=chann_id, chann=chann, sd=sd, hd=hd, fhd=fhd, ww=ww)#.replace('\n', '')#.encode('utf-8')

                        elif '{norm}' in item and '{ww}' in item and not '{cc}' in item:
                            result = item.format(chann_id=chann_id, norm=norm, sd=sd, hd=hd, fhd=fhd, ww=ww)#.replace('\n', '')#.encode('utf-8')
                            
                        elif '{norm}' in item and not '{cc}' in item:
                            result = item.format(chann_id=chann_id, norm=norm, sd=sd, hd=hd, fhd=fhd)#.replace('\n', '')#.encode('utf-8')
                            
                        elif not '{cc}' in item:
                            result = item.format(chann_id=chann_id, chann=chann, sd=sd, hd=hd, fhd=fhd)#.replace('\n', '')#.encode('utf-8')
                    else:
                        if '{ww}' in item and not '{norm}' in item:
                            result = item.format(chann_id=chann_id, cc=cc, chann=chann, sd=sd, hd=hd, fhd=fhd, ww=ww)#.replace('\n', '')#.encode('utf-8')

                        elif '{norm}' in item and '{ww}' in item:
                            result = item.format(chann_id=chann_id, cc=cc, norm=norm, sd=sd, hd=hd, fhd=fhd, ww=ww)#.replace('\n', '')#.encode('utf-8')
                            
                        elif '{norm}' in item:
                            result = item.format(chann_id=chann_id, cc=cc, norm=norm, sd=sd, hd=hd, fhd=fhd)#.replace('\n', '')#.encode('utf-8')
                            
                        else:
                            result = item.format(chann_id=chann_id, cc=cc, chann=chann, sd=sd, hd=hd, fhd=fhd)#.replace('\n', '')#.encode('utf-8')
                    same = re.findall('same_as="(.*?)"', str(result))
                    xmltv = re.findall('xmltv_id="(.*?)"', str(result))
                    if same != xmltv:
                        subChann.write(bytearray(result, 'utf-8'))

        # Read output
        lines = open(dest+'output.xml', 'rb').readlines()

        # Remove duplicates
        lines_set = set(lines)

        with open(dest+'output.xml', 'wb') as out:

            newList = list()

            # Sort list lexicographically ascending
            for line in lines_set:
                newList.append(line)

            result = sorted(newList)

            # Write result to file
            for line in result:
                out.write(line)

        messagebox.showinfo(title='Finished', message='Channels have been generated')
        path = os.path.realpath(dest+'output.xml')
        os.startfile(dest+'output.xml')

root = tk.Tk()
root.resizable(True, True)
root.state('zoomed')
canvas = tk.Canvas(root, width=400, height=300)
app = Application(master=root)
app.master.title('Webgrab+ Generate alternative channel names')
app.mainloop()
