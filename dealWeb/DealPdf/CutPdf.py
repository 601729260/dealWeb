from PyPDF2 import PdfFileReader, PdfFileWriter


def addBlankpage():
    readFile = '/Users/wangguannan/Downloads/gddsbd_veryhuo.com/高等代数高等教育出版社第三版.pdf'
    outFile = '/Users/wangguannan/Downloads/gddsbd_veryhuo.com/高等代数高等教育出版社第三版out.pdf'
    pdfFileWriter = PdfFileWriter()

    # 获取 PdfFileReader 对象
    pdfFileReader = PdfFileReader(readFile)  # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    numPages = pdfFileReader.getNumPages()

    for index in range(0, numPages):
        print("处理第"+str(index)+"页")
        pageObj = pdfFileReader.getPage(index)
        #print(pageObj.mediaBox.getUpperLeft_x(),pageObj.mediaBox.getUpperLeft_y())
        #print(pageObj.mediaBox.getUpperRight_x(),pageObj.mediaBox.getUpperRight_y())
        #print(pageObj.mediaBox.getLowerLeft_x(),pageObj.mediaBox.getLowerLeft_y())
        #print(pageObj.mediaBox.getLowerRight_x(),pageObj.mediaBox.getLowerRight_y())
        if(index>5 or index==0):
            pageObj.mediaBox.upperLeft=(130,670)
            pageObj.mediaBox.upperRight=(470,670)
            pageObj.mediaBox.lowerLeft=(130,170)
            pageObj.mediaBox.lowerRight=(470,170)

        pdfFileWriter.addPage(pageObj)  # 根据每页返回的 PageObject,写入到文件
        pdfFileWriter.write(open(outFile, 'wb'))

addBlankpage()
