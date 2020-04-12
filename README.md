<<<<<<< HEAD
# QASystemOnHepatopathyKG
基于neo4j知识图谱和规则匹配的肝病问答系统  
项目介绍详见：  
基于医疗知识图谱的问答系统源码详解 https://blog.csdn.net/vivian_ll/article/details/89840281  
和  
基于医疗知识图谱的问答实践中遇到的问题 https://blog.csdn.net/vivian_ll/article/details/89337931
=======
源自中科院软件所刘焕勇老师在github上的开源项目，地址：https://github.com/liuhuanyong/QASystemOnMedicalKG
更新点如下：
1.当检索结果为空时会报错，该问题我已经修复，在answer_search.py增加结果判断，如检索结果为空则返回未检索到结果；
2.当检索内容与肝病无关时只能返回初始化答案，需要增加相似性判断，然后找到相似度最高的内容，检索答案返回给用户；该问题还在修复；
>>>>>>> 9be699cfddf2ab649b07a6b1871b87ca34f9d61f
