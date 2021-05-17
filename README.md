# chatbot
一个可以使用自己语料进行训练的中文聊天机器人，目前包含seq2seq tf1.x和tf.2x版本，seqGan版本为tf1.x版本，pytorch版本，欢迎大家实践交流。

# 关于语料的说明
大家可以使用小黄鸡的预料，地址https://github.com/zhaoyingjun/chatbot/blob/master/chineseChatbotWeb-tf2.0/seq2seqChatbot/train_data/xiaohuangji50w_nofenci.conv

# seq2seq版本代码执行顺序

1、在下载好代码和语料之后，将语料文件放入data目录下。

2、按照 数据预处理器（data_utls.py)-->execute.py(执行器)-->app.py（可视化对话模块）的顺序执行就可以了。

3、超参配置在seq2seq.ini和seq2seq_sever.ini文件中配置。

# seqGAN版本代码执行顺序
1 、在下载好代码和语料之后，将语料文件放入source_data目录下。
2、按照 数据预处理器（source_data_utls.py)-->execute.py(执行器)-->app.py（可视化模块）的顺序执行就可以了

# 参考代码和文献

http://blog.topspeedsnail.com/archives/10735/comment-page-1#comment-1161。

http://www.easyapple.net/?p=1384&from=singlemessage&isappinstalled=0。

https://github.com/zpppy/seqGan_chatbot

# 建议环境

ubuntu14.04  
python3.5  
TF1.X:
tensorflow==1.10.1或者tensorflow-gpu==1.10.1  
flask==0.11.1

TF2.X:
tensorflow==2.0.0
flask==0.11.1

pytorch:
torch==2.0.0
flask==0.11.1


# 已更新功能清单:

V1.1:已经增加中文分词，效果是变得更好了。注意在使用分词后，需要增加词典的大小，否则的话会导致词典无法覆盖训练集，导致出现很多的UNK。直接在seq2seq.ini中修改超参数enc_vocab_size和dec_vocab_size的值即可。  

V2.0:增加一个基于SeqGan的版本，以增加训练的效果。  

V3.0：增加TensorFlow2.0版，训练效果见文件夹内图片，训练数据已经准备好，直接执行python3 execute即可进行训练。 PS:预训练好了一个模型，链接:https://pan.baidu.com/s/1zcrBn8dpOhtBZu_T7TOO9w  密码:s7sq，可以下载使用，模型的效果见效果图，在使用预训练模型前需要先执行data_utl.py文件更新字典。 

V4.0:a、seq2seq模型增加pytorch版本，seqGAN模型pytorch版本稍后更新；b、对当前的工程结构进行调整。
# 版本路线图:
V4.1:seqGAN模型增加tf2.0和pytorch版本，敬请期待。


