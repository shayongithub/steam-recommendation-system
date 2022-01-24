# Steam Recommendation System
Suggest relevent games based on Item based Collaborative Filtering

<br>
<p align="center">
    <img src="https://zok-blog.oss-cn-hangzhou.aliyuncs.com/pythonlg.jpg" 
        alt="python3 spider">
</p>
<br />

## Installing: 
To use the project, first clone the repo on your device using the command below: 
```conda
git init
```
```cd
git clone https://github.com/shayongithub/stream-recommendation-system
```
As we mentioned above, we use Pycharm as an IDE for this project, you can also you other IDE or run it directly from your terminal. If you want to download Pycharm, you can find it here: ```cd
https://www.jetbrains.com/pycharm/download/#section=windows
```
Scrapy works best with python 3.6 – 3.7, so we recommend you create an environment with this version inside, we have undergone some troubles with later version like 3.9. Anaconda supports very well in managing your environment, so you may want to install it here: ```cd
https://www.anaconda.com/products/individual
```
Then, you can create an environment with specific version with this command (run on your Anaconda terminal): 
```cd
conda create -n myenv python=3.6
```
Install libraries Scrapy and Selenium, as well as some supported library like Loguru and Json:
```cd
pip install scrapy
```
```cd
pip install selenium
```
```cd
pip install loguru
```
```cd
pip install json
```
We use FireFox as a web browser for this project, so you have to install Geckodriver to support for it: 
https://github.com/mozilla/geckodriver/releases .<br />

### Note:  
The main problem can happen is that you don’t get the right path for your directory. So, pay attention to it, especially the path link to your Firefox browser and where you put Geckodriver.<br />
Besides, we use relative path to ensure the users can run it easily without changing all the path, so make sure you set your terminal path to some things like this:
F:\...\...\...\steamcrawl>.<br />

## Crawling data
```
First move to file steamcrawl
```cd
cd /steamcrawl
```
Then run the spider by command:
```cd
scrapy crawl steam
```

After running, you will receivei a file `products.csv`, which is our result data.

# Recommendation System
