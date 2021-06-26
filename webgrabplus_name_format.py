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
        self.create_widgets()

    def create_widgets(self):
        myFont = font.Font(family="Terminal", size=22)

        canvas.pack()

        label = tk.Label(root, text='Create alternative channel names for Webgrab+ config file')
        label.config(font=('Helvetica', 16))
        canvas.create_window(200, 0, window=label)
        canvas.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')
        
        start = tk.Button(self, height=3, width=15, text="Create", fg="blue", command=self.run)
        start.grid(row=0, column=1, padx=50, pady=300)
        start['font'] = myFont

        ex = tk.Button(self, height=3, width=15, text="Exit", fg="red", command=self.master.destroy)
        ex.grid(row=0, column=2, padx=50, pady=300)
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
        channList = re.findall('\s<chann.*site_channel=".*" xmltv_id="(.*?)">.*<\/channel>', webConfig)
        channNonHDList = re.findall('\s<chann.*site_channel=".*" xmltv_id="(.*?)\sHD.*">.*<\/channel>', webConfig)

        # Find country code prefix
        try:
            ccList = re.findall('\s<chann.*site_channel=".*" xmltv_id=".*\w{2,3}">.*<\/channel>', webConfig)
            cc = ccList[0]
        except:
            cc = ''

        # Non HD chann list
        channChList = list()

        for chann_hd in channNonHDList:
            chann_hd = str(chann_hd + ' ' + cc)
            channChList.append(chann_hd)

        with open(dest+'output.xml', 'wb') as subChann:
            for chann_id in channList:
                try:
                    getPrefix = re.findall(r'\w{2,3}$', chann_id)
                    cc = getPrefix[0]
                    if cc != cc.upper():
                        cc = 'XX'
                except:
                    cc = ''
                    
                for item in tempList:
                    chann = re.sub('\s*{cc}$'.format(cc=cc), '', chann_id)
                    norm = unidecode(chann)

                    sd = ' SD'
                    hd = ' HD'
                    fhd = ' FHD'
                    ww = ' VIP'

                    if chann_id in channChList:
                        sd = ''
                        hd = ''
                        fhd = ''

                    if chann + ' HD' + cc in channList:
                        sd = ''
                        hd = ''
                        fhd = ''

                    if chann_id not in channChList:
                        sd = ' SD'
                        hd = ' HD'
                        fhd = ' FHD'

                    if 'HD' in chann_id:
                        sd = ''
                        hd = ''
                        fhd = ''

                    if 'UHD' in chann_id:
                        sd = ''
                        hd = ''
                        fhd = ''

                    if '4K' in chann_id:
                        sd = ''
                        hd = ''
                        fhd = ''

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
