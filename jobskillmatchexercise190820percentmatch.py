#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[47]:


#Job vs Skill match in % match
def jobSkillMatch(list1,list2):
    lowerlist2=[x.lower() for x in list2]
    lowerlist1=[x.lower() for x in list1]
    result= len(list(set(lowerlist2) & set(lowerlist1)))
    totchar = (len(lowerlist1))
    return (int((result / totchar)*100))
#jobchar=input("Enter Job Character: ")
#indSkill=input("Enter Individual Skill: ")
jobchar=["Onsite", "SQL", "Analytical", "Garduate"]
indSkill=["Remote", "SQL", "Business", "Masters"]
print(jobSkillMatch(jobchar, indSkill))
#returns in % match


# In[ ]:





# In[ ]:




