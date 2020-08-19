#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[29]:


#Job vs Skill match
def jobSkillMatch(list1,list2):
    lowerlist2=[x.lower() for x in list2]
    lowerlist1=[x.lower() for x in list1]
    return len(list(set(lowerlist2) & set(lowerlist1)))
#jobchar=input("Enter Job Character: ")
#indSkill=input("Enter Individual Skill: ")
jobchar=["Onsite", "SQL", "Analytical", "Graduate"]
indSkill=["Remote", "SQL", "Business", "Masters"]

print(jobSkillMatch(jobchar, indSkill))
#returns count/number of matches


# In[ ]:





# In[ ]:




