

import xml.etree.ElementTree as ET, json

def xml_clean(read_path, save_path):
    tree = ET.parse(read_path)
    elements = tree.getroot().findall('Review')
    # print(len(elements))
    for e in elements:
        for sentences in e.findall("sentences"):
            for s in sentences.findall("sentence"):
                try:
                    if s.attrib['OutOfScope'] == 'TRUE':
                        sentences.remove(s)
                        continue
                except:
                    pass
                for eterms in s.findall('Opinions'):
                    if eterms is not None:
                        for a in eterms.findall('Opinion'):
                            if a.attrib['target'] == 'NULL':
                                eterms.remove(a)
                                continue
                            elif a.attrib['polarity'] == 'conflict':
                                eterms.remove(a)
                                continue
                            # # If there are uppercase characters, they are converted to lowercase
                            # elif not a.attrib['target'].islower():
                            #     a.attrib['target'] = a.attrib['target'].casefold()
                    if len(eterms) == 0:
                        s.remove(eterms)
                if s.findall('Opinions') == []:
                    sentences.remove(s)
            if len(sentences) == 0:
                e.remove(sentences)
    tree.write(save_path)

def xml_clean_14(read_path, save_path):
    tree = ET.parse(read_path)
    elements = tree.getroot()
    print(len(elements))
    for s in elements.findall('sentence'):
        if s.findall('aspectTerms') == []:
            elements.remove(s)
        else:
            for aspectTerms in s.findall('aspectTerms'):
                for a in aspectTerms.findall('aspectTerm'):
                    if a.attrib['polarity'] == 'conflict':
                        aspectTerms.remove(a)
                    # elif not a.attrib['term'].islower():
                    #     a.attrib['term'] = a.attrib['term'].casefold()
                if len(aspectTerms) == 0:
                    s.remove(aspectTerms)
            if s.findall('aspectTerms') == []:
                elements.remove(s)
    print(len(elements))
    tree.write(save_path)

if __name__=='__main__':
    # 'ABSA15_Restaurants_Test.xml'
    # 'ABSA-15_Restaurants_Train_Final.xml'
    # 'ABSA16_Restaurants_Train_SB1_v2.xml'
    # 'EN_REST_SB1_TEST.xml.gold'

    # 'Laptop_Train_v2.xml'
    # 'Restaurants_Test_Gold.xml'
    # 'Restaurants_Train_v2.xml'
    # 'Laptops_Test_Gold.xml'
    read_path = r'C:\Users\pc\Desktop\Laptops_Test_Gold.xml'
    save_path = r'C:\Users\pc\Desktop\Laptops_Test_Gold_clean.xml'
    # xml_clean(read_path, save_path)
    xml_clean_14(read_path, save_path)


