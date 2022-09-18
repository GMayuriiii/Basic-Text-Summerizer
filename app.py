import nltk
nltk.download('punkt')
import re
from nltk.corpus import stopwords
import streamlit as st

def main():
    st.subheader("Paste/type text here:")
    input_text=st.text_area("",)
    
    input_text=input_text.lower()
    if input_text is not None:
        input_text=re.sub('[^.a-zA-Z]'," ",input_text)
        input_text=re.sub('\s+'," ",input_text)
        sent_list=nltk.sent_tokenize(input_text)
        if len(sent_list)>=1:
            number=st.number_input("Select size of text summary",min_value=1,max_value=(len(sent_list)-1),step=1)
            stopwords=nltk.corpus.stopwords.words("english")
            
            word_freq={}
            for word in nltk.word_tokenize(input_text):
                if word not in stopwords:
                    if word not in word_freq:
                        word_freq[word]=1
                    else:
                         word_freq[word]+=1
                         
            max_freq=max(word_freq.values())
            for word in word_freq:
                word_freq[word]=word_freq[word]/max_freq
                
            sent_score={}
            for sent in sent_list:
                for word in nltk.word_tokenize(sent):
                     if word in word_freq and len(sent.split(' ')) < 30:
                            if sent not in sent_score:
                                sent_score[sent]=word_freq[word]
                            else:
                                sent_score[sent]+=word_freq[word]
            
            ranked_sentences=dict(sorted(sent_score.items(),key=lambda item:item[1],reverse=True))
            top_sentence=list(ranked_sentences)
            summerize_text=' '
            for i in range(number):
                summerize_text=summerize_text + top_sentence[i][0].upper()+top_sentence[i][1:]
            submit=st.button("Summerize Text")
            if submit:
                st.text_area("",value=summerize_text,height=10)
        
if __name__=='__main__':
    main()
    
