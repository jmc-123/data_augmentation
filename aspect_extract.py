

import xml.etree.ElementTree as ET, json
import pandas as pd


def aspect_extract(read_path, dataset):
    tree = ET.parse(read_path)
    elements = tree.getroot().findall('Review')
    dataset_list = []
    sentenceid_list = []
    sentence_list = []
    category_list = []
    sub_cat_list = []
    polarity_list = []
    aspect_term_list = []
    for e in elements:
        for sentences in e.findall("sentences"):
            for s in sentences.findall("sentence"):
                for eterms in s.findall('Opinions'):
                    for a in eterms.findall('Opinion'):
                        dataset_list.append(dataset)
                        sentenceid_list.append(s.attrib['id'])
                        sentence_list.append(s.findall('text')[0].text)
                        category_list.append(a.attrib['category'].split('#')[0])
                        sub_cat_list.append(a.attrib['category'].split('#')[1])
                        polarity_list.append(a.attrib['polarity'])
                        aspect_term_list.append(a.attrib['target'])
    df = pd.DataFrame({'dataset': dataset_list, 'sentenceid': sentenceid_list, 'sentence': sentence_list,
                       'category': category_list, 'sub_cat': sub_cat_list, 'polarity': polarity_list, 'aspect_term': aspect_term_list})
    return df
    # print((dataset_list))
    # print((sentenceid_list))
    # print((sentence_list))
    # print((category_list))
    # print((sub_cat_list))
    # print((polarity_list))
    # print(aspect_term_list)

def aspect_extract_14(read_path, dataset):
    tree = ET.parse(read_path)
    elements = tree.getroot()
    dataset_list = []
    sentenceid_list = []
    sentence_list = []
    polarity_list = []
    aspect_term_list = []
    for s in elements.findall('sentence'):
        for aspectTerms in s.findall('aspectTerms'):
            for a in aspectTerms.findall('aspectTerm'):
                dataset_list.append(dataset)
                sentenceid_list.append(s.attrib['id'])
                sentence_list.append(s.findall('text')[0].text)
                polarity_list.append(a.attrib['polarity'])
                aspect_term_list.append(a.attrib['term'])
    df = pd.DataFrame({'dataset': dataset_list, 'sentenceid': sentenceid_list, 'sentence': sentence_list,
                    'polarity': polarity_list,
                       'aspect_term': aspect_term_list})
    return df

def merge_df(df1, df2, df3, df4, save_path):
    all_df = pd.concat([df1, df2, df3, df4], ignore_index=True)
    all_df.to_csv(save_path, index=False)

if __name__=='__main__':
    # df1 = aspect_extract(r'C:\Users\pc\Desktop\ABSA15_Restaurants_Test_clean.xml', '15_rest_test')
    # df2 = aspect_extract(r'C:\Users\pc\Desktop\ABSA-15_Restaurants_Train_Final_clean.xml', '15_rest_train')
    # df3 = aspect_extract(r'C:\Users\pc\Desktop\ABSA16_Restaurants_Train_SB1_v2_clean.xml', '16_rest_train')
    # df4 = aspect_extract(r'C:\Users\pc\Desktop\EN_REST_SB1_TEST_clean.xml.gold', '16_rest_test')
    # save_path = r'C:\Users\pc\Desktop\all_data.csv'
    # merge_df(df1, df2, df3, df4, save_path)
    # df1 = aspect_extract_14(r'C:\Users\pc\Desktop\Laptop_Train_v2_clean.xml', '14_laptop_train')
    # df2 = aspect_extract_14(r'C:\Users\pc\Desktop\Laptops_Test_Gold_clean.xml', '14_laptop_test')
    # df3 = aspect_extract_14(r'C:\Users\pc\Desktop\Restaurants_Test_Gold_clean.xml', '14_rest_test')
    # df4 = aspect_extract_14(r'C:\Users\pc\Desktop\Restaurants_Train_v2_clean.xml', '14_rest_train')
    # df = pd.read_csv(r'C:\Users\pc\Desktop\all_data.csv', low_memory=False)
    # # df.loc[df['dataset']=='en_rest_sb1_test', 'dataset'] = '16_rest_test'
    # new_df = pd.concat([df, df1, df2, df3, df4], ignore_index=True)
    # new_df.to_csv(r'C:\Users\pc\Desktop\new_all_data.csv', index=False)

    df = pd.read_csv(r'C:\Users\pc\Desktop\new_all_data.csv', low_memory=False)
    df.sort_values(by='dataset', inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(df)
    df.to_csv(r'C:\Users\pc\Desktop\new_all_data.csv', index=False)

