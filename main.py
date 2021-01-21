import sys
import pywikibot
from pywikibot import pagegenerators
from gps_dsc import get_exif_dsc
siteC = pywikibot.Site(u'commons', u'commons')
siteC.login()

category = pywikibot.Category(siteC, u'Uploaded with PyCommonist')
print("this category is analysed...")

gen = pagegenerators.CategorizedPageGenerator(category)

'''
https://commons.wikimedia.org/w/api.php?action=help&modules=query%20imageinfo
'''
for page in gen:
    print (page.title())
    imageInfo = siteC.loadimageinfo(page, history=False)
    exifData = imageInfo['metadata']
    heading = get_exif_dsc(exifData)
    print(heading)
    if heading != 0:

        index = 0
        for (template, params) in page.templatesWithParams():
            #print(template.title())
            if template.title() == 'Template:Location dec':
                if (len(params) == 2): #no heading
                    newParam = 'heading:' + str(heading)
                    params = page.templatesWithParams()[index][1]
                    paramOut = params.copy()
                    paramOut.append(newParam)

                    paramsText = params[0] + '|' + params[1]
                    paramOutText = paramOut[0] + '|' + paramOut[1] + '|' + paramOut[2]

                    page.text = page.text.replace(paramsText, paramOutText)
                    page.save(u"Add missing parameter heading into Template:Location dec")

            index = index + 1