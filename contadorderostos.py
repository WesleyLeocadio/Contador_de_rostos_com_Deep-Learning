#!/usr/bin/env python
# coding: utf-8

# In[2]:


from mtcnn import MTCNN


# In[3]:


detector = MTCNN ()


# In[4]:


from matplotlib import pyplot


# In[5]:


img =pyplot.imread('pessoas.jpeg')


# In[7]:


faces = detector.detect_faces(img)


# In[8]:


len(faces)


# In[ ]:



pyplot.imshow(img)
pyplot.show()


# In[10]:


faces


# In[12]:


from matplotlib.patches import Rectangle


# In[16]:


def caixas(imagem, faces):
    ax = pyplot.gca()
    for face in faces:
        x, y, width, height =  face['box']
        #criando o retangulo
        rect = Rectangle((x,y), width, height, color='green', fill=False)
        ax.add_patch(rect)
        
    pyplot.imshow(imagem)
    pyplot.savefig('contagem.png')
    pyplot.show()
    
        


# In[ ]:


caixas(img,faces)


# In[ ]:




